import cppyy
cppyy.load_reflection_info("libMyClassDict.so")
myinst = cppyy.gbl.MyClass(42)
print myinst.GetMyInt()
myinst.SetMyInt(33)
print myinst.m_myint
myinst.m_myint = 77
print myinst.GetMyInt()
help(cppyy.gbl.MyClass)   # shows that normal python introspection works
