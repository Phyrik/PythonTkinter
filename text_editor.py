from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog

openFileName = None
textToEdit = None
textBoxToEditIn = None

def exitApp():
    root.quit()

'''
def doNothing():
    print("Doing nothing...")
'''

def newFile():
    global openFileName
    openFileName = simpledialog.askstring(title="New File", prompt="What do you want to call your new file?")
    textBoxToEditIn.delete(0.0, END)

def openFile():
    global openFileName
    global textToEdit
    global textBoxToEditIn
    root.fileName = filedialog.askopenfilename(initialdir = "Documents", title="Select file to open")
    root.title("Tkinter Text Editor - " + root.fileName)
    openFileName = root.fileName
    textToEdit = open(root.fileName).read()
    textBoxToEditIn.insert(END, textToEdit)

def saveFile():
    global openFileName
    global textToEdit
    global textBoxToEditIn
    textToEdit = textBoxToEditIn.get(0.0, END)
    openedFile = open(openFileName, "w")
    openedFile.write(textToEdit)
    openedFile.close()

'''
def saveFileAs():
    openedFile = asksaveasfilename(defaultextension=".txt")
    textToEdit = textBoxToEditIn.get(0.0, END)
    try:
        openedFile.write(textToEdit.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")
'''

root = Tk()
root.title("Tkinter Text Editor")
root.state("zoomed")

# *** Text Box ***

textBoxToEditIn = Text(root)
textBoxToEditIn.pack(fill=BOTH, expand=1)

# *** Main Menu ***

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=fileMenu)
# fileMenu.add_command(label="New Project...", command=doNothing)
fileMenu.add_command(label="New File", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
# fileMenu.add_command(label="Save As", command=saveFileAs)

fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitApp)

editMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Redo", command=doNothing)

# *** Toolbar ***
'''
toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=5, pady=5)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=5, pady=5)

toolbar.pack(side=TOP, fill=X)
'''
# *** Status Bar ***

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
