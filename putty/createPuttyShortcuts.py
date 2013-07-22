# http://www.blog.pythonlibrary.org/2010/01/23/using-python-to-create-shortcuts/
# https://pypi.python.org/pypi/winshell
# http://support.microsoft.com/kb/242297
# http://msdn.microsoft.com/en-us/library/xsy6k3ys%28v=vs.84%29.aspx

import os, winshell
from win32com.client import Dispatch


def createShortcut(path, target, wdir = None, icon = None, args = None):
   """
   Creates a Windows shortcut.

   :param path: Fully qualified path for the link to be created.
   :type path: str
   :param target: 
   """
   ext = path[-3:]
   if ext == 'url':
      shortcut = file(path, 'w')
      shortcut.write('[InternetShortcut]\n')
      shortcut.write('URL=%s' % target)
      shortcut.close()
   elif ext == 'lnk':
      shell = Dispatch('WScript.Shell')
      shortcut = shell.CreateShortCut(path)
      shortcut.Targetpath = target
      if args:
         shortcut.Arguments = args
      if wdir:
         shortcut.WorkingDirectory = wdir
      else:         
         shortcut.WorkingDirectory = os.path.dirname(target)
      if icon:
         shortcut.IconLocation = icon
      shortcut.save()
   else:
      raise Exception("invalid extension '%s' - allowed values: url | lnk" % ext)


def getPuttyConnections():
   """
   Get all Putty connections from registry.
   """
   psessions = []
   os.system(r'regedit /a /e "%userprofile%\desktop\putty-registry.reg" HKEY_CURRENT_USER\Software\Simontatham')
   pdef = os.path.join(winshell.desktop(), "putty-registry.reg")
   r = open(pdef, 'r').read().splitlines()
   prefix = "[HKEY_CURRENT_USER\Software\Simontatham\PuTTY\Sessions"
   for l in r:
      if l.startswith(prefix):
         psessions.append(l[len(prefix) + 1:-1])
   return psessions


def createPuttyShortcuts(folder = "Putty Connections"):
   """
   Create shortcuts to Putty connections.
   """
   desktop = winshell.desktop()
   cpath = os.path.join(desktop, folder)

   if not os.path.exists(cpath):
      os.mkdir(cpath)
   
   for c in getPuttyConnections():
      if c.strip() != "":
         path = os.path.join(cpath, c + ".lnk")
         target = "C:\\Program Files (x86)\\PuTTY\\putty.exe"
         args = "-load " + c
         wdir = "C:\\Program Files (x86)\PuTTY\\"
         try:
            createShortcut(path, target, wdir = wdir, args = args)
         except Exception, e:
            print "could not create shortcut for " + c


def test_createShortcut():
   desktop = winshell.desktop()

   ## create Web shortcut
   ##
   path = os.path.join(desktop, "Tavendo.url")
   target = "http://www.tavendo.de/"
   createShortcut(path, target)

   ## create program shortcut
   ##
   path = os.path.join(desktop, "oberstet@scm.tavendo.de.lnk")
   target = "C:\\Program Files (x86)\\PuTTY\\putty.exe"
   args = "-load oberstet@scm.tavendo.de"
   wdir = "C:\\Program Files (x86)\PuTTY\\"
   createShortcut(path, target, wdir = wdir, args = args)


if __name__ == '__main__':
   createPuttyShortcuts()
