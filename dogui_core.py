import tkinter
import tkinter.ttk

class Combobox():
    def __init__(self, window, inputlist, rowindex, columnindex):
        self.cb=tkinter.ttk.Combobox(window,values=inputlist, width=50)
        self.cb.set(inputlist[0])
        self.cb.grid(row=rowindex,column=columnindex, padx=4, pady=4)

class Button():
    def __init__(self, window, textinput, function ,rowindex, columnindex):
        self.b = tkinter.Button(window, text =textinput, command = lambda:function())
        self.b.grid(row=rowindex,column=columnindex)        


class GUI:
    def __init__(self,title="GUI",size=[600,400]):
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.minsize(width=size[0], height=size[1])
        
        menu_bar=self.generate_menu_bar()
        
        #self.window.bind_all('<Control-Key-w>', do_nothing)
        self.window.config(menu=menu_bar)
        self.window.mainloop()

    def generate_menu_bar(self,label="Menu"):
        menu_bar = tkinter.Menu(self.window)
        menu1=self.add_list_of_commands(menu_bar,["choice #1","choice #2","","choice #3"],[self.do_nothing,self.do_nothing,self.do_nothing,self.do_nothing])
        menu_bar.add_cascade(label=label, menu=menu1)
        return(menu_bar)
        
        
    def add_list_of_commands(self,menu_bar,list_of_labels,list_of_commands):
        menu = tkinter.Menu(menu_bar, tearoff=0)
        for i,label in enumerate(list_of_labels):
            if label=="":
                menu.add_separator()
            else:
                #TODO: add accelerator possibility
                #menu.add_command(label="Do nothing #1", command=do_nothing, accelerator='ctrl+w')
                menu.add_command(label=list_of_labels[i],command=list_of_commands[i]) 
        return(menu)
     
    def do_nothing(self):
       filewin = tkinter.Toplevel(self.window)
       button = tkinter.Button(filewin, text="Do nothing button")
       button.grid(row=1,column=1)
        
        
gui1=GUI()     
        
        
        
