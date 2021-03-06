import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className="Python Text editor")
textPad = ScrolledText(root, width=100, height=100)

## add functionality

## Open file command
def open_command():
    file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()

## save function
def save_command(self):
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = self.textPad.get('1.0', END+'1-c')
        file.write(data)
        file.close()

## exit function
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit"):
        root.destroy()


##info function, add info
def about_command():
    label = tkMessageBox.showinfo("About", "Basic textpad")


def dummy():
    print "I am a dummy command"

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label = "New", command=dummy)
filemenu.add_command(label = "Open", command=open_command)
filemenu.add_command(label = "Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

##run the app##
textPad.pack()
root.mainloop()