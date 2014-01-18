DART = __get__(dict, "__call__")([], {"js_object": [{"key": "time", "value": __get__(dict, "__call__")([], {"js_object": [{"key": "time", "value": "time() { return new DateTime.now().millisecondsSinceEpoch / 1000.0; }"}]})}]});
JS = __get__(dict, "__call__")([], {"js_object": [{"key": "time", "value": __get__(dict, "__call__")([], {"js_object": [{"key": "time", "value": "function time() { return new Date().getTime() / 1000.0; }"}, {"key": "clock", "value": "function clock() { return new Date().getTime() / 1000.0; }"}]})}, {"key": "random", "value": __get__(dict, "__call__")([], {"js_object": [{"key": "random", "value": "var random = Math.random"}]})}, {"key": "bisect", "value": __get__(dict, "__call__")([], {"js_object": [{"key": "bisect", "value": "/*bisect from fake bisect module*/"}]})}, {"key": "math", "value": __get__(dict, "__call__")([], {"js_object": [{"key": "sin", "value": "var sin = Math.sin"}, {"key": "cos", "value": "var cos = Math.cos"}, {"key": "sqrt", "value": "var sqrt = Math.sqrt"}]})}, {"key": "os.path", "value": __get__(dict, "__call__")([], {"js_object": [{"key": "dirname", "value": "function dirname(s) { return s.slice(0, s.lastIndexOf('/')+1)}; var os = {'path':{'dirname':dirname}}"}]})}]});
add2 = function(args, kwargs) {
  if (args instanceof Array && {}.toString.call(kwargs) === '[object Object]' && ( arguments.length ) == 2) {
    /*pass*/
  } else {
    args = Array.prototype.slice.call(arguments);
    kwargs = Object();
  }
  var signature, arguments;
  signature = {"kwargs": Object(), "args": __create_array__("a", "b")};
  arguments = get_arguments(signature, args, kwargs);
  var a = arguments['a'];
  var b = arguments['b'];
  if (( b ) < 0) {
    throw __get__(Exception, "__call__")(["2nd number is negative"], __NULL_OBJECT__);
  } else {
    return (a + b);
  }
}

add2.NAME = "add2";
add2.args_signature = ["a", "b"];
add2.kwargs_signature = {  };
add2.types_signature = {  };
add2.pythonscript_function = true;
var Foo, __Foo_attrs, __Foo_parents;
__Foo_attrs = Object();
__Foo_parents = [];
__Foo_properties = Object();
__Foo___init__ = function(args, kwargs) {
  if (args instanceof Array && {}.toString.call(kwargs) === '[object Object]' && ( arguments.length ) == 2) {
    /*pass*/
  } else {
    args = Array.prototype.slice.call(arguments);
    kwargs = Object();
  }
  var signature, arguments;
  signature = {"kwargs": Object(), "args": __create_array__("self", "title")};
  arguments = get_arguments(signature, args, kwargs);
  var self = arguments['self'];
  var title = arguments['title'];
  self.title = title;
}

__Foo___init__.NAME = "__Foo___init__";
__Foo___init__.args_signature = ["self", "title"];
__Foo___init__.kwargs_signature = {  };
__Foo___init__.types_signature = {  };
__Foo___init__.pythonscript_function = true;
__Foo_attrs["__init__"] = __Foo___init__;
__Foo_hello1 = function(args, kwargs) {
  if (args instanceof Array && {}.toString.call(kwargs) === '[object Object]' && ( arguments.length ) == 2) {
    /*pass*/
  } else {
    args = Array.prototype.slice.call(arguments);
    kwargs = Object();
  }
  var signature, arguments;
  signature = {"kwargs": Object(), "args": __create_array__("self", "msg")};
  arguments = get_arguments(signature, args, kwargs);
  var self = arguments['self'];
  var msg = arguments['msg'];
  return __sprintf("%s: %s", [self.title, msg]);
}

__Foo_hello1.NAME = "__Foo_hello1";
__Foo_hello1.args_signature = ["self", "msg"];
__Foo_hello1.kwargs_signature = {  };
__Foo_hello1.types_signature = {  };
__Foo_hello1.pythonscript_function = true;
__Foo_attrs["hello1"] = __Foo_hello1;
__Foo_hello2 = function(args, kwargs) {
  if (args instanceof Array && {}.toString.call(kwargs) === '[object Object]' && ( arguments.length ) == 2) {
    /*pass*/
  } else {
    args = Array.prototype.slice.call(arguments);
    kwargs = Object();
  }
  var signature, arguments;
  signature = {"kwargs": Object(), "args": __create_array__("self", "msg")};
  arguments = get_arguments(signature, args, kwargs);
  var self = arguments['self'];
  var msg = arguments['msg'];
  return __get__(__get__("{}: {}", "format"), "__call__")([self.title, msg], __NULL_OBJECT__);
}

__Foo_hello2.NAME = "__Foo_hello2";
__Foo_hello2.args_signature = ["self", "msg"];
__Foo_hello2.kwargs_signature = {  };
__Foo_hello2.types_signature = {  };
__Foo_hello2.pythonscript_function = true;
__Foo_attrs["hello2"] = __Foo_hello2;
Foo = create_class("Foo", __Foo_parents, __Foo_attrs, __Foo_properties);
main = function(args, kwargs) {
  var res, foo, m;
  __get__(__get__(console, "log"), "__call__")(["Sum: ", add2([2, 3], __NULL_OBJECT__)], __NULL_OBJECT__);
  __get__(__get__(console, "log"), "__call__")([__get__(range, "__call__")([5], __NULL_OBJECT__)], __NULL_OBJECT__);
  var __comprehension0;
  __comprehension0 = [];
  var idx0;
  var iter0;
  var get0;
  idx0 = 0;
  iter0 = 10;
  while(( idx0 ) < iter0) {
    var x;
    x = idx0;
    __comprehension0.push((3 * x));
    idx0 += 1;
  }
  __get__(__get__(console, "log"), "__call__")([__comprehension0], __NULL_OBJECT__);
  foo = __get__(Foo, "__call__")(["Meister Eder"], __NULL_OBJECT__);
    try {
m = __get__(__get__(foo, "hello1"), "__call__")(["Pumuckel"], __NULL_OBJECT__);
__get__(__get__(console, "log"), "__call__")([m], __NULL_OBJECT__);
  } catch(__exception__) {
if (__exception__ == Exception || isinstance([__exception__, Exception], Object())) {
var e = __exception__;
__get__(__get__(console, "log"), "__call__")([__get__(str, "__call__")([e], __NULL_OBJECT__)], __NULL_OBJECT__);
}

}
    try {
m = __get__(__get__(foo, "hello2"), "__call__")(["Pumuckel"], __NULL_OBJECT__);
__get__(__get__(console, "log"), "__call__")([m], __NULL_OBJECT__);
  } catch(__exception__) {
if (__exception__ == Exception || isinstance([__exception__, Exception], Object())) {
var e = __exception__;
__get__(__get__(console, "log"), "__call__")([__get__(str, "__call__")([e], __NULL_OBJECT__)], __NULL_OBJECT__);
}

}
    try {
res = add2([2, -1], __NULL_OBJECT__);
__get__(__get__(console, "log"), "__call__")([res], __NULL_OBJECT__);
  } catch(__exception__) {
if (__exception__ == Exception || isinstance([__exception__, Exception], Object())) {
var e = __exception__;
__get__(__get__(console, "log"), "__call__")([__get__(str, "__call__")([e], __NULL_OBJECT__)], __NULL_OBJECT__);
}

}
}

main.NAME = "main";
main.args_signature = [];
main.kwargs_signature = {  };
main.types_signature = {  };
main.pythonscript_function = true;
