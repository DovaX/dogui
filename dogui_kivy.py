import kivy
from kivy.app import App
from kivy.uix.label import Label as Lbl
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button as Btn
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.carousel import Carousel

class GUI(App):
    def __init__(self,title="GUI",size=[800,400],rows=5,cols=5):
        super().__init__()
        self.title=title
        self.size=size     
        self.no_rows=rows
        self.no_cols=cols
        self.window=None #proxy
        self.layout_list=None
        self.heights=[1]*self.no_rows #list of relative heights of rows
        self.widths=[1]*self.no_cols #list of relative widths of columns
        
    def custom_screens(self):
        pass #not implemented - free to modify
       
    def prepare_screens(self,is_one_screen=True):
        self.page = Page(self)
        screen1 = Screen(name="Page")
        screen1.add_widget(self.page)
        if is_one_screen:
            self.screen_manager.add_widget(screen1)
        else:
            print("Implement custom solution")
            self.custom_screens()
        #####
        #gui2=GUI()
        
        #self.page = Page(self)
        #screen2 = Screen(name="Page2")
        #screen2.add_widget(self.page)
        #self.screen_manager.add_widget(screen2)
        

        #carousel = Carousel(direction='right', id='carousel')
        #carousel.add_widget(screen1)
        #carousel.add_widget(screen2)
        
        #screen3 = Screen(name="Page3")
        #screen3.add_widget(carousel)

        #self.screen_manager.add_widget(screen1) 

        
        
    def build(self):
        #####
        self.screen_manager = ScreenManager()
        self.prepare_screens()
        
    
        #self.page=Page(self)
        Window.size = tuple(self.size)
        return(self.screen_manager)
    
    def build_gui(self):    
        self.run()
        
    
class Page(GridLayout):
    def __init__(self,app,**kwargs):
        self.clear_widgets()
        self.cols=app.no_cols
        self.rows=app.no_rows
        self.buttons=[]
        print(self.cols)
        print(self.rows)
        print(app.layout_list)
        super().__init__(**kwargs)
        for i in range(1,self.rows+1):
            for j in range(1,self.cols+1):
                chosen_item=None
                for item in app.layout_list:
                    if item.row_index==i and item.column_index==j:
                        chosen_item=item
           
                if chosen_item is not None:
                    if isinstance(chosen_item,Label):
                        kivy_widget=Lbl(text=chosen_item.text.get(),width=app.widths[j-1]/sum(app.widths)*Window.size[0],height=app.heights[i-1]/sum(app.heights)*Window.size[1],size_hint_x=None,size_hint_y=None)
                        chosen_item.kivy_widget=kivy_widget
                        self.add_widget(kivy_widget)
                    if isinstance(chosen_item,Entry):
                        kivy_widget=TextInput(text=chosen_item.text.get(),multiline=False,width=app.widths[j-1]/sum(app.widths)*Window.size[0],height=app.heights[i-1]/sum(app.heights)*Window.size[1],size_hint_x=None,size_hint_y=None)
                        chosen_item.kivy_widget=kivy_widget
                        self.add_widget(kivy_widget)
                    if isinstance(chosen_item,Button):
                        btn=Btn(text=chosen_item.text_input,width=app.widths[j-1]/sum(app.widths)*Window.size[0],height=app.heights[i-1]/sum(app.heights)*Window.size[1],size_hint_x=None,size_hint_y=None)                        
                        chosen_item.btn=btn
                        self.buttons.append(chosen_item)
                        index=self.buttons.index(chosen_item)
                        chosen_item.btn.bind(on_press=self.click_button)
                        self.add_widget(btn)
                    if isinstance(chosen_item,PictureBox):
                        chosen_item.kivy_image=Image(source=chosen_item.image_path,width=app.widths[j-1]/sum(app.widths)*Window.size[0],height=app.heights[i-1]/sum(app.heights)*Window.size[1],size_hint_x=None,size_hint_y=None)
                        self.add_widget(chosen_item.kivy_image)
                else:          
                    self.add_widget(Lbl()) #Lbl(text="_")

    def click_button(self,instance):
        button_widgets=[x.btn for x in self.buttons]
        index=button_widgets.index(instance)
        button=self.buttons[index]
        button.function()

        


class Label:
    def __init__(self,window,text_input,row_index,column_index,width=10):
        self.row_index=row_index
        self.column_index = column_index
        self.text_input=text_input
        self.kivy_widget=None
        self.text=Text(text_input,widget=self)
        
        
class Entry:
    def __init__(self,window,row_index,column_index,text_input="",width=10):
        self.row_index=row_index
        self.column_index = column_index
        self.text=Text(text_input,widget=self)
        self.kivy_widget=None
        
class Text:
    def __init__(self,text,widget=None):
        self.text=text
        self.widget=widget
        
    def set(self,new_text):
        if self.widget is None:
            self.text=new_text
        elif isinstance(self.widget,Entry): #Handling Entry for text.set("") option
            self.text=new_text
            self.widget.kivy_widget.text=new_text
        elif isinstance(self.widget,Label): #Handling Entry for text.set("") option
            self.text=new_text
            if self.widget.kivy_widget is not None:
                self.widget.kivy_widget.text=new_text
        
    def get(self):
        return(self.text)
        
class PictureBox:
    def __init__(self,window,image_path,row_index,column_index,width=10):
        self.row_index=row_index
        self.column_index = column_index
        self.image_path=image_path
        self.kivy_image=None
        
    def load_picture(self,image_path=None):
        print(self.kivy_image)
        if self.kivy_image is not None:
            self.kivy_image.source = './image.png'
            self.kivy_image.reload()
        
        
class Button():
    def __init__(self, window, text_input, function ,row_index, column_index):
        self.row_index=row_index
        self.column_index = column_index
        self.text_input=text_input
        self.function=function

def donothing(*_):
    print("ahoj")




"""
gui1=GUI()

label1=Label(gui1.window,"ahoj",1,1)
label2=Label(gui1.window,"cau",2,2)
label3=Label(gui1.window,"aj",1,3)
btn1=Button(gui1.window,"aj",donothing,4,3)
entry1=Entry(gui1.window,3,3,"blabla")
img1=PictureBox(gui1.window,"bla.jpg",4,4)
gui1.layout_list=[label1,label2,label3,btn1,entry1,img1]
gui1.build_gui()
"""
