import tkinter
import sqlite3

# Setting up tkinter
window = tkinter.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

width = 900
height = 500

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

window_config = {"title": window.title("Pomodoro"),
                 "geometry": window.geometry(f"{width}x{height}+{int(x)}+{int(y)}"),
                 "bgcolor": window.configure(bg="darkcyan"),
                 "icon": window.iconbitmap("images/icon1.ico")}

# Setting up sqlite3
database = sqlite3.connect("database.db")
cursor = database.cursor()

window.mainloop()
