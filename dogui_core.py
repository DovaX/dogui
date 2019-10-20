import tkinter
import tkinter.ttk

root = tkinter.Tk()
root.title("GUI")
root.minsize(width=666, height=366)


class Combobox():
    def __init__(self, inputlist, rowindex, columnindex):
        self.cb=tkinter.ttk.Combobox(root,values=inputlist, width=50)
        self.cb.set(inputlist[0])
        self.cb.grid(row=rowindex,column=columnindex, padx=4, pady=4)

class Button():
    def __init__(self, textinput, function ,rowindex, columnindex):
        self.b = tkinter.Button(root, text =textinput, command = lambda:function())
        self.b.grid(row=rowindex,column=columnindex)        



def do_nothing():
   filewin = tkinter.Toplevel(root)
   button = tkinter.Button(filewin, text="Do nothing button")
   button.grid(row=1,column=1)




menubar = tkinter.Menu(root)

jobmenu = tkinter.Menu(menubar, tearoff=0)
jobmenu.add_command(label="Do nothing #1", command=do_nothing, accelerator='ctrl+w')
jobmenu.add_separator()
jobmenu.add_command(label="Do nothing #2", command=do_nothing)

menubar.add_cascade(label="Menu", menu=jobmenu)


root.bind_all('<Control-Key-w>', do_nothing)

root.config(menu=menubar)
root.mainloop()
