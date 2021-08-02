
import dogui.dogui_core as dg


def do_nothing():
    pass


gui1=dg.GUI()
gui1.add_menu("Menu",['Function1','Function2'],[do_nothing,do_nothing])

gui1.add_menu("Menu2",['Function3','Function4'],[do_nothing,do_nothing])
gui1.build_gui()

