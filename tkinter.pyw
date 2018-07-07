import tkinter as tk
import tkinter.messagebox

def doNothing():
    print("Doing nothing...")

def exit():
    wantsToExit = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if wantsToExit == True:
        root.quit()

root = tk.Tk()
root.title("Tkinter Application")
root.geometry("1920x1080")

# *** Main Menu ***

menu = tk.Menu(root)
root.config(menu=menu)

subMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(labe="New Project...", command=doNothing)
subMenu.add_command(labe="New", command=doNothing)

subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

editMenu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# *** Toolbar ***

toolbar = tk.Frame(root, bg="blue")

insertButton = tk.Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=tk.LEFT, padx=5, pady=5)
printButton = tk.Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=tk.LEFT, padx=5, pady=5)

toolbar.pack(side=tk.TOP, fill=tk.X)

# *** Status Bar ***

status = tk.Label(root, text="Preparing to do nothing...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()