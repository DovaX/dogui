# dogui
A lightweight wrapper around Tkinter library enabling easy GUI creation for general applications in just few lines of code.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dogui.

```
pip install dogui
```

## Usage
It is very simple, just remember all GUI widgets need to be declared between GUI initialization and build_gui() method.

```
import dogui.dogui_core as dg

def click_button():
    print("Your name is:",entry1.text.get())

gui1=dg.GUI()

label1=dg.Label(gui1.window,"What is your name?",1,1)
entry1=dg.Entry(gui1.window,1,2)
button1=dg.Button(gui1.window,"Submit",click_button,2,1)


gui1.build_gui()
```
![obrazek](https://user-images.githubusercontent.com/29150831/127937395-d5120570-233f-46bb-b0df-2ede28884aff.png)

Widgets:
Label
Entry
Button
Combobox
Picturebox
For more information about their parameters, please look into the dogui_core.py file.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
