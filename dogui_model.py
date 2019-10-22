
from dogui_core import * 



gui1=GUI()
gui1.add_menu("Menu",['Function1','Function2'],[do_nothing,do_nothing])

gui1.add_menu("Menu2",['Function3','Function4'],[do_nothing,do_nothing])
gui1.build_gui()

