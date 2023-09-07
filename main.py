import Tkinter

window = Tkinter.Tk()

monitor_height = window.winfo_screenheight()
monitor_width = window.winfo_screenwidth()
gui_width = 480
gui_height = 300
gui_init_position = str(monitor_width/2 - gui_width/2) + '+' + str(monitor_height/2 - gui_height/2 - 100)

window.title("FIFA4 MACRO")
window.geometry(str(gui_width)+'x'+str(gui_height)+'+'+gui_init_position)
window.resizable(False, False)

window.mainloop()