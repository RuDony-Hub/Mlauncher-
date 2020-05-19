from tkinter import *
from PIL import ImageTk, Image


def open_menu_download():
	root_load = Tk()
	root_load.title("Download")
	root_load.geometry("200x600")
	root_load.resizable(False, False)
	root_load.mainloop()
	pass


root = Tk()
root.title("Mlauncher")
root.geometry("1200x700")
root.resizable(False, False)

path = "pictures/logo.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image=img)
panel.place(x=200, y=30)

button_Download = Button(text="Скачать", command=open_menu_download)
button_Mods = Button(text="Моды")
button_Settings = Button(text="Настройки")
button_Help = Button(text="Помощ")

button_Download.place(x=400, y=150)
button_Mods.place(x=490, y=150)
button_Settings.place(x=565, y=150)
button_Help.place(x=675, y=150)

root.mainloop()