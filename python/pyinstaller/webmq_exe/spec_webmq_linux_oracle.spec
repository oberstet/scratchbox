######################################################################
##
##   Copyright (c) 2013 Tavendo GmbH. All rights reserved.
##   Author(s): Tobias Oberstein
##
######################################################################

a = Analysis(['exe_webmqora.py'],
             pathex = ['/home/webmq/scm/WebMQ/appliance/exe'],
             hiddenimports = [],
             hookspath = None)

a.binaries.append(('libociicus.so', '/home/webmq/drivers/oracle/instantclient_11_2/libociicus.so', 'BINARY'))
a.binaries.append(('libclntsh.so.11.1', '/home/webmq/drivers/oracle/instantclient_11_2/libclntsh.so.11.1', 'BINARY'))
a.binaries.append(('libnnz11.so', '/home/webmq/drivers/oracle/instantclient_11_2/libnnz11.so', 'BINARY'))

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name = os.path.join('dist', 'webmqora'),
          debug = False,
          strip = None,
          upx = True,
          console = True ,
          icon = 'tavendo.ico')
