from Tkinter import *

import Tkinter

tk = Tkinter.Tk()
frame = Tkinter.Frame(tk, relief="ridge", borderwidth=2)
frame.pack(fill="both",expand=1)
label = Tkinter.Label(frame, text="Hallo Welt!")
label.pack(expand=1)
button = Tkinter.Button(frame,text="OK",command=tk.destroy)
button.pack(side="bottom")

if True:
    tk.mainloop()
else:
    from twisted.internet import tksupport, reactor

    # Install the Reactor support
    tksupport.install(tk)

    # at this point build Tk app as usual using the root object,
    # and start the program with "reactor.run()", and stop it
    # with "reactor.stop()".
    reactor.run()
