import psycopg2
import re as regex

from psycopg2.extras import _solve_conn_curs

from psycopg2.extensions import register_type, new_type, new_array_type, STATUS_IN_TRANSACTION

from psycopg2.extensions import adapt, register_adapter, AsIs


class CompositeDictCaster(object):
    """Helps conversion of a PostgreSQL composite type into a Python object.

    The class is usually created by the `register_composite()` function.
    You may want to create and register manually instances of the class if
    querying the database at registration time is not desirable (such as when
    using an :ref:`asynchronous connections <async-support>`).

    .. attribute:: name

        The name of the PostgreSQL type.

    .. attribute:: oid

        The oid of the PostgreSQL type.

    .. attribute:: array_oid

        The oid of the PostgreSQL array type, if available.

    .. attribute:: type

        The type of the Python objects returned. If :py:func:`collections.namedtuple()`
        is available, it is a named tuple with attributes equal to the type
        components. Otherwise it is just the `!tuple` object.

    .. attribute:: attnames

        List of component names of the type to be casted.

    .. attribute:: atttypes

        List of component type oids of the type to be casted.

    """
    def __init__(self, name, oid, attrs, array_oid=None):
        self.name = name
        self.oid = oid
        self.array_oid = array_oid

        self.attnames = [ a[0] for a in attrs ]
        self.atttypes = [ a[1] for a in attrs ]
        self._create_type(name, self.attnames)
        self.typecaster = new_type((oid,), name, self.parse)
        if array_oid:
            self.array_typecaster = new_array_type(
                (array_oid,), "%sARRAY" % name, self.typecaster)
        else:
            self.array_typecaster = None

    def totuple(self, value):
       r = []
       for i in xrange(len(self.attnames)):
          k = self.attnames[i]
          if value.has_key(k):
             valoid = self.atttypes[i]
             if self.casters.has_key(valoid):
                r.append(self.casters[valoid].totuple(value[k]))
             elif self.acasters.has_key(valoid):
                p1 = self.acasters[valoid]
                p2 = self.casters[p1.oid]
                l = []
                for v in value[k]:
                    l.append(p2.totuple(v))
                r.append(l)
             else:
                r.append(value[k])
          else:
             r.append(None)
       return tuple(r)
       
    def getAdapter(self):
       class A:
           def __init__(self, adapted):
              self.adapted = adapted
           def getquoted(self):
               r = []
               for k in self.attnames:
                  if self.adapted.has_key(k):
                     r.append(adapt(self.adapted[k]))
                  else:
                     r.append(None)
               return adapt(r)
       return A
              

    def parse(self, s, curs):
        if s is None:
            return None

        tokens = self.tokenize(s)
        if len(tokens) != len(self.atttypes):
            raise psycopg2.DataError(
                "expecting %d components for the type %s, %d found instead" %
                (len(self.atttypes), self.name, len(tokens)))

        attrs = [ curs.cast(oid, token)
            for oid, token in zip(self.atttypes, tokens) ]
        
        o = {}
        for i in xrange(len(self.atttypes)):
            if attrs[i] is not None:
                o[self.attnames[i]] = attrs[i]
        o['record'] = self.name
        return o
        #return self._ctor(*attrs)

    _re_tokenize = regex.compile(r"""
  \(? ([,)])                        # an empty token, representing NULL
| \(? " ((?: [^"] | "")*) " [,)]    # or a quoted string
| \(? ([^",)]+) [,)]                # or an unquoted string
    """, regex.VERBOSE)

    _re_undouble = regex.compile(r'(["\\])\1')

    @classmethod
    def tokenize(self, s):
        rv = []
        for m in self._re_tokenize.finditer(s):
            if m is None:
                raise psycopg2.InterfaceError("can't parse type: %r" % s)
            if m.group(1):
                rv.append(None)
            elif m.group(2):
                rv.append(self._re_undouble.sub(r"\1", m.group(2)))
            else:
                rv.append(m.group(3))

        return rv

    def _create_type(self, name, attnames):
        try:
            from collections import namedtuple
        except ImportError:
            self.type = tuple
            self._ctor = lambda *args: tuple(args)
        else:
            self.type = namedtuple(name, attnames)
            self._ctor = self.type

    @classmethod
    def _from_db(self, name, conn_or_curs):
        """Return a `CompositeCaster` instance for the type *name*.

        Raise `ProgrammingError` if the type is not found.
        """
        conn, curs = _solve_conn_curs(conn_or_curs)

        # Store the transaction status of the connection to revert it after use
        conn_status = conn.status

        # Use the correct schema
        if '.' in name:
            schema, tname = name.split('.', 1)
        else:
            tname = name
            schema = 'public'

        # column typarray not available before PG 8.3
        typarray = conn.server_version >= 80300 and "typarray" or "NULL"

        # get the type oid and attributes
        curs.execute("""\
SELECT t.oid, %s, attname, atttypid
FROM pg_type t
JOIN pg_namespace ns ON typnamespace = ns.oid
JOIN pg_attribute a ON attrelid = typrelid
WHERE typname = %%s AND nspname = %%s
    AND attnum > 0 AND NOT attisdropped
ORDER BY attnum;
""" % typarray, (tname, schema))

        recs = curs.fetchall()

        # revert the status of the connection as before the command
        if (conn_status != STATUS_IN_TRANSACTION
        and not conn.autocommit):
            conn.rollback()

        if not recs:
            raise psycopg2.ProgrammingError(
                "PostgreSQL type '%s' not found" % name)

        type_oid = recs[0][0]
        array_oid = recs[0][1]
        type_attrs = [ (r[2], r[3]) for r in recs ]

        return CompositeDictCaster(tname, type_oid, type_attrs,
            array_oid=array_oid)

def register_composite_as_dict(name, conn_or_curs, globally=False):
    """Register a typecaster to convert a composite type into a tuple.

    :param name: the name of a PostgreSQL composite type, e.g. created using
        the |CREATE TYPE|_ command
    :param conn_or_curs: a connection or cursor used to find the type oid and
        components; the typecaster is registered in a scope limited to this
        object, unless *globally* is set to `!True`
    :param globally: if `!False` (default) register the typecaster only on
        *conn_or_curs*, otherwise register it globally
    :return: the registered `CompositeCaster` instance responsible for the
        conversion

    .. versionchanged:: 2.4.3
        added support for array of composite types

    """
    caster = CompositeDictCaster._from_db(name, conn_or_curs)
    register_type(caster.typecaster, not globally and conn_or_curs or None)

    if caster.array_typecaster is not None:
        register_type(caster.array_typecaster, not globally and conn_or_curs or None)

    return caster
