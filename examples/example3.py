
import dogui.dogui_core as dg


def click_button():
    print("Your name is:",entry1.text.get())

gui1=dg.GUI()

label1=dg.Label(gui1.window,"What is your name?",1,1)
entry1=dg.Entry(gui1.window,1,2)
button1=dg.Button(gui1.window,"Submit",click_button,2,1)


gui1.build_gui()

