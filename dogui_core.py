import tkinter
import tkinter.ttk

class Combobox():
    def __init__(self, window, inputlist, row_index, column_index,width=10):
        self.cb=tkinter.ttk.Combobox(window,values=inputlist, width=width)
        self.cb.set(inputlist[0])
        self.cb.grid(row=row_index,column=column_index, padx=4, pady=4)

class Button():
    def __init__(self, window, text_input, function ,row_index, column_index):
        self.b = tkinter.Button(window, text =text_input, command = lambda:function())
        self.b.grid(row=row_index,column=column_index)        

class Label():
    def __init__(self, window,text_input,row_index,column_index):
        self.label=tkinter.Label(window, text=text_input)
        self.label.grid(row=row_index,column=column_index)

class Entry():
    def __init__(self, window,row_index,column_index,width=10):
        self.entry=tkinter.Entry(window,width=width)
        self.entry.grid(row=row_index,column=column_index)

class GUI:
    def __init__(self,title="GUI",size=[600,400]):
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.minsize(width=size[0], height=size[1])
        self.menu_list=[]
        
        
        
        #self.window.bind_all('<Control-Key-w>', do_nothing)
    def build_gui(self):
        if len(self.menu_list)>0:    
            self.window.config(menu=self.menu_bar)
        self.window.mainloop()

    def add_menu(self,label,list_of_labels,list_of_commands):
        self.menu_list.append([label,list_of_labels,list_of_commands])
        if len(self.menu_list)==1:  
            self.menu_bar = tkinter.Menu(self.window)
        menu1=self.add_list_of_commands(self.menu_bar,list_of_labels,list_of_commands)
        self.menu_bar.add_cascade(label=label, menu=menu1)

            
        
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
    

    
    
################### SPECIAL FUNCTIONS ######################
    
def do_nothing():
    pass

def do_nothing_window():
   filewin = tkinter.Toplevel(self.window)
   button = tkinter.Button(filewin, text="Do nothing button")
   button.grid(row=1,column=1)
    
        
      
       