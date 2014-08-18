######################################################################
##
##   Copyright (c) 2013 Tavendo GmbH. All rights reserved.
##   Author(s): Tobias Oberstein
##
######################################################################

a = Analysis(['exe_webmqora.py'],
#             pathex = ['f:\\scm\\WebMQ\\appliance\\exe'],
             hiddenimports = [],
             hookspath = None)

a.binaries.append(('oraociicus11.dll',
                   r'C:\instantclient_11_2\oraociicus11.dll',
#                   r'C:\oracle\product\11.2.0\client_1\instantclient\light\oraociicus11.dll',
                   'BINARY'))

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name = os.path.join('dist', 'Tavendo WebMQ for Oracle.exe'),
          debug = False,
          strip = None,
          upx = True,
          console = True ,
          icon = 'tavendo.ico')
