

https://github.com/postgresxl


FDW:
projection pushdown
predicate pushdown
join pushdown
aggregate pushdown

http://www.pgcon.org/2014/schedule/attachments/334_PGCon2014Gaia.pdf



http://sourceforge.net/p/postgres-xl/mailman/message/34296320/


http://postgres-x2.github.io/presentation_docs/2014-07-PGXC-Implementation/pgxc.pdf



http://sourceforge.net/p/postgres-xl/mailman/message/34218006/


pgxc_clean


pgloader
pg_bulkload
http://sourceforge.net/p/postgres-xl/mailman/message/33626317/



Corosync/Pacemaker: http://clusterlabs.org/


http://sourceforge.net/p/postgres-xl/mailman/message/32838036/

"you may want to hire someone from one of the
Postgres-XL/PostgreSQL consulting companies to investigate if it is urgent."

---

The background that views are defined only at coordinator is views may
not be pushable to datanodes.    For safety, views are not allowed to
propagate to datanodes.

Regards;
---
Koichi Suzuki

http://sourceforge.net/p/postgres-xl/mailman/message/32949027/


---

Both the coordinator and datanode use the same binary, but they run in
different modes, either as a coordinator, or a datanode.  The coordinator
just has a copy of the catalog info, but no user data. The coordinator
maintains session state, and parses and plans queries and sends subplans
down to the datanodes. It gets these connections from a pooler process that
it is forked off of the main process. Also, the coordinator interacts with
GTM to obtain transaction identifiers (XIDs) and snapshots.

http://sourceforge.net/p/postgres-xl/mailman/message/32742199/

---

DML in plpgsql
"ERROR:  Postgres-XL does not support DML queries in PL/pgSQL"

Yes, your observation is correct.    In XL (and in XC as well), only
one DML may be allowed.    We need to support SAVEPOINT and
surrounding features to allow DMLs in plpgsql.
---
Koichi Suzuki
http://sourceforge.net/p/postgres-xl/mailman/message/32843601/

http://sourceforge.net/p/postgres-xl/mailman/message/32829103/
http://sourceforge.net/p/postgres-xl/mailman/message/32763404/

---

Koichi Suzuki
https://www.linkedin.com/in/koichidbms

Nikhil Sontakke
https://www.linkedin.com/in/nikhilsontakke

Pavan Deolasee
https://www.linkedin.com/in/pavandeolasee

Masons Sharp
https://www.linkedin.com/in/masonsharp
https://twitter.com/mason_db

https://github.com/mason-sharp/postgres-xl

https://www.youtube.com/watch?v=ixOO-Yv5its
http://de.slideshare.net/mason_s/postgres-xl-scaling



- Postgres-XL Director (XLD)
- Postgres-XL Agent (XLA)

- systemd service starts "Postgres-XL Director" (XLD) under user "postgres"
- XLD is a Python/WAMP app component


http://sourceforge.net/p/postgres-xl/mailman/message/32763404/


http://sourceforge.net/p/postgres-xl/tickets/search/?q=!status%3Awont-fix+%26%26+!status%3Aclosed



replace pgxc_ctl with fabric (http://www.fabfile.org/)

http://sourceforge.net/p/postgres-xl/mailman/message/34399361/

SELECT pgxc_pool_reload();



temp tables testen

GTM proxy
pg-xl shared_queue



http://blog.jelly-king.com/prog/2015/03/22/Install%20pgxl%20on%20cluster.html

