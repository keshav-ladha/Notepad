from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documemts","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Unititled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documemts","*.txt")])
        if file=="":
            file=None
        else:
            #Save As New File
            f = open(file,"w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+ " - Notepad")
            print("File Saved")
    else:
        #Save The Current File
        f = open(file,"w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    pass
def contact():
    tmsg.showinfo("Contact US","Email:keshavladha22@gmail.com")

if __name__ == "__main__":
    #Basic Python Syntax
    root =Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("icon.ico")
    root.geometry("788x644")


    #Adding Text Area
    TextArea = Text(root, font="lucida 13")
    TextArea.pack(fill=BOTH,expand=TRUE)
    file = None

    #Creating a Menu Bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar,tearoff=0)


    '''File Menu'''
    #To Open A New File
    FileMenu.add_command(label="New",command=newFile)

    #To Open A New File
    FileMenu.add_command(label="Open File", command=openFile)

    #To Save A New File
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()

    #Exit Command
    FileMenu.add_command(label="Exit", command = quitApp)

    MenuBar.add_cascade(label="File",menu=FileMenu)


    '''File Menu Ends'''

    '''Edit Menu'''
    EditMenu = Menu(MenuBar, tearoff=0)

    #Cut Feature
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    '''Edit Menu Ends'''

    '''Help Menu'''
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label = "About",command=about)
    HelpMenu.add_command(label="Contact Us",command=contact)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    '''Help Menu Ends'''

    root.config(menu=MenuBar)

    #Adding ScrollBar

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)

    root.mainloop()