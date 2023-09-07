import tkinter
import tkinter.font

window = tkinter.Tk()

# get window screen size
monitor_height = window.winfo_screenheight()
monitor_width = window.winfo_screenwidth()

# macro window size
gui_width = 330
gui_height = 200

# macro window init position
gui_init_position = str(int(monitor_width/2 - gui_width/2)) + '+' + str(int(monitor_height/2 - gui_height/2 - 100))

window.title("FIFA4 MACRO")
window.geometry(str(gui_width)+'x'+str(gui_height)+'+'+gui_init_position)
window.resizable(False, False)

status_text = 'STOPPING'
status_font = tkinter.font.Font(family="맑은 고딕", size=16, weight='bold')
status_color = 'red'

# generate widget
start_button = tkinter.Button(window, text='START', width=10, height=3)
stop_button = tkinter.Button(window, text='STOP', width=10, height=3)
status_label = tkinter.Label(window, text=status_text, font=status_font, foreground=status_color)
footer = tkinter.Label(window, text='Made by covy kim (programmer97@naver.com)', anchor='e')

# widget position
start_button.grid(row=0, column=0, padx=30, pady=30)
stop_button.grid(row=0, column=1, padx=30)
status_label.grid(row=1, column=0, columnspan=2, padx=30)
footer.grid(row=2, column=0, columnspan=2, padx=30, pady=20)

window.mainloop()