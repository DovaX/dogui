import kivy
from kivy.app import App
from kivy.uix.label import Label as Lbl
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button as Btn
from kivy.uix.image import Image
from kivy.core.window import Window


class GUI(App):
    def __init__(self,title="GUI",size=[800,400],rows=5,cols=5):
        super().__init__()
        self.title=title
        self.size=size     
        self.no_rows=rows
        self.no_cols=cols
        self.window=None #proxy
        self.layout_list=None

    #    self.build()
        
    def build(self):
        self.page=Page(self,self.no_rows,self.no_cols)
        Window.size = tuple(self.size)
        return(self.page)
    
    def build_gui(self):    
        self.run()
        
    
class Page(GridLayout):
    def __init__(self,app,rows,cols,**kwargs):
        self.clear_widgets()
        self.cols=cols
        self.rows=rows
        print(self.cols)
        print(self.rows)
        print(app.layout_list)
        super().__init__(**kwargs)
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                chosen_item=None
                for item in app.layout_list:
                    #print(item.row_index,item.column_index)
                    if item.row_index==i and item.column_index==j:
                        chosen_item=item
           
                if chosen_item is not None:
                    if isinstance(chosen_item,Label):
                        self.add_widget(Lbl(text=chosen_item.text.get()))
                    if isinstance(chosen_item,Entry):
                        self.add_widget(TextInput(text=chosen_item.text_input,multiline=False))
                    if isinstance(chosen_item,Button):
                        btn=Btn(text=chosen_item.text_input)
                        btn.bind(on_press=chosen_item.function)
                        self.add_widget(btn)
                    if isinstance(chosen_item,PictureBox):
                        print(chosen_item.image_path)
                        self.add_widget(Image(source=chosen_item.image_path))
                else:          
                    self.add_widget(Lbl(text="_"))
                
                

class Label:
    def __init__(self,window,text_input,row_index,column_index,width=10):
        self.row_index=row_index
        self.column_index = column_index
        self.text_input=text_input
        self.text=Text(text_input)
        
        
class Entry:
    def __init__(self,window,row_index,column_index,text_input=None,width=10):
        self.row_index=row_index
        self.column_index = column_index
        self.text_input=text_input
        self.text=Text(text_input)
        
class Text:
    def __init__(self,text):
        self.text=text
        
    def set(self,new_text):
        self.text=new_text
        
    def get(self):
        return(self.text)
        
class PictureBox:
    def __init__(self,window,image_path,row_index,column_index,width=10):
        self.row_index=row_index
        self.column_index = column_index
        self.image_path=image_path
        
class Button():
    def __init__(self, window, text_input, function ,row_index, column_index):
        self.row_index=row_index
        self.column_index = column_index
        self.text_input=text_input
        self.function=function
        #self.b = tkinter.Button(window, text =text_input, command = lambda:function())
        #self.b.grid(row=row_index,column=column_index)   

def donothing(*_):
    print("ahoj")


"""
gui1=GUI()

label1=Label(gui1.window,"ahoj",1,1)
label2=Label(gui1.window,"cau",2,2)
label3=Label(gui1.window,"aj",1,3)
btn1=Button(gui1.window,"aj",donothing,4,3)
entry1=Entry(gui1.window,"blabla",3,3)
img1=PictureBox(gui1.window,"bla.jpg",4,4)
gui1.layout_list=[label1,label2,label3,btn1,entry1,img1]
gui1.build_gui()

"""