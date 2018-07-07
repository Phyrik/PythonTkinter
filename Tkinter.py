import tkinter as tk

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

subMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label)

root.mainloop()