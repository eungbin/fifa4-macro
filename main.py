import tkinter

window = tkinter.Tk()

# get window screen size
monitor_height = window.winfo_screenheight()
monitor_width = window.winfo_screenwidth()

# macro window size
gui_width = 480
gui_height = 300

# macro window init position
gui_init_position = str(int(monitor_width/2 - gui_width/2)) + '+' + str(int(monitor_height/2 - gui_height/2 - 100))

window.title("FIFA4 MACRO")
window.geometry(str(gui_width)+'x'+str(gui_height)+'+'+gui_init_position)
window.resizable(False, False)

window.mainloop()