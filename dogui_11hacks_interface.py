#Dominik's Graphical User Interface

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



""" COMBOBOX DIRECTORY MANAGEMENT
def move():
    file=combobox1.cb.get()
    newdir=combobox2.cb.get()
    if "//" in file:
        prefix=file.split("//")[1]
        directory=file.split("//")[0]
    else:
        prefix=file
        directory="."
    if directory=="Done":
        olddir=".//Metadata//Automated//Matches//Done"
    elif directory=="Todo":
        olddir=".//Metadata//Automated//Matches//Todo"
    else:
        olddir=".//Metadata//Automated//Matches"
    newdir=".//Metadata//Automated//Matches//"+newdir
    helper.move_file(prefix,".txt",olddir,newdir,0)    
    new_files=get_files()
    combobox1.cb['values']=new_files



def get_files():    
    list_of_directories=[".//Metadata//Automated//Matches",".//Metadata//Automated//Matches//Todo",".//Metadata//Automated//Matches//Done"]
    files=helper.get_all_files_from_list_of_directories(list_of_directories,".txt")
    new_files=[]
    for file in files:
        new_files.append(file.replace("\\","//").split("Matches//")[-1])
    return(new_files)
     
def ComboBoxUpdate(event):
    new_files=get_files()
    combobox1.cb['values']=new_files
  
    
new_files=get_files()
#files=["Ahoj","Ahoj2"]
directories=[".","Done","Todo","Backup"]  
     

"""
    
list1=['hello','world']
combobox1=Combobox(list1,1,1)
combobox2=Combobox(list1,2,1)
button1=Button("Move",do_nothing,3,1)
button2=Button("Move with XML",do_nothing,4,1)


"""All buttons below this need league instatid in the combobox 3"""
files=list(range(1000))
combobox3=Combobox(files,1,2)
button3=Button("Get matchxml metadata",do_nothing,2,2)
button4=Button("Prepare clusters of matches to matches_*.txt",do_nothing,3,2)
button5=Button("Complete season in dbo.match for given league",do_nothing,4,2)
button6=Button("Get team metadata",do_nothing,5,2)


var1 = tkinter.IntVar()
tkinter.Checkbutton(root, text="Online Interface", variable=var1).grid(row=5, sticky="w")
var2 = tkinter.IntVar()
tkinter.Checkbutton(root, text="Directory Interface", variable=var2).grid(row=6, sticky="w")
var2.set(1)

def use_interface():
    return(var1.get(),var2.get())


"""##########################  MENU  ###########################""" 

menubar = tkinter.Menu(root)

jobmenu = tkinter.Menu(menubar, tearoff=0)
jobmenu.add_command(label="Run job_maker.py", command=do_nothing, accelerator='ctrl+w')
jobmenu.add_command(label="Create new job download_xml.py", command=do_nothing)
jobmenu.add_command(label="Create new job player.py", command=do_nothing)
jobmenu.add_command(label="Create new job match_stats.py", command=do_nothing)
jobmenu.add_command(label="Create new job match.py", command=do_nothing)
jobmenu.add_command(label="Create new job test", command=do_nothing)
jobmenu.add_separator()
jobmenu.add_command(label="Archive all jobs", command=do_nothing)
jobmenu.add_command(label="Archive next job", command=do_nothing)
jobmenu.add_separator()
jobmenu.add_command(label="Get player metadata", command=do_nothing)


menubar.add_cascade(label="Job Maker", menu=jobmenu)


metadatamenu = tkinter.Menu(menubar, tearoff=0)
metadatamenu.add_command(label="Transform metadata league", command=do_nothing)
metadatamenu.add_command(label="Transform metadata matches", command=do_nothing)
metadatamenu.add_command(label="Transform metadata matchxml", command=do_nothing)
metadatamenu.add_command(label="Transform metadata player", command=do_nothing)
metadatamenu.add_separator()
menubar.add_cascade(label="Metadata", menu=metadatamenu)

sql_menu = tkinter.Menu(menubar, tearoff=0)
sql_menu.add_command(label="Update dbo.match guest+home teams, league_instatid (Necessary to run after match.py)", command=do_nothing)
sql_menu.add_command(label="Update dbo.match match_player_stats_true count (Necessary to run after match.py)", command=do_nothing)
menubar.add_cascade(label="SQL", menu=sql_menu)



tm_menu = tkinter.Menu(menubar, tearoff=0)
tm_menu.add_command(label="Transform metadata tmteam", command=do_nothing)
tm_menu.add_command(label="Transform metadata tmplayer", command=do_nothing)
tm_menu.add_separator()
menubar.add_cascade(label="Transfermarkt", menu=tm_menu)




helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=do_nothing)
helpmenu.add_command(label="About...", command=do_nothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.bind_all('<Control-Key-w>', do_nothing)

root.config(menu=menubar)
root.mainloop()
