from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

#Create GUI Window
window = Tk()

#Function for insert image when clik the button
def InsertImage():
    #Take Image from file
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    img = ImageTk.PhotoImage(Image.open(window.filename))
    
    #Delete image from previous canvas (if available), then add the new image
    C.delete("all")
    C.create_image(0,0,anchor=NW, image = img)
    window.mainloop()

#Create Canvas with button inside GUI WIndow
C = Canvas(window, width = 1366, height = 768)
C.pack()
B = Button(window, text ="Insert Image Here", command = InsertImage)
B.pack()

window.mainloop()