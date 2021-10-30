from tkinter import *
from PIL import ImageTk,Image #PIL -> Pil
#from tkinter import messageb
from tkinter.filedialog import askopenfilename
from tkinter import filedialog


def browseFiles():
    global root
    Newwindow=Toplevel(root)
    Newwindow.title("disease identify")
    Newwindow.minsize(width=100,height=50)
    Newwindow.geometry("1000x500")
    Canvas1 = Canvas(Newwindow, width = 300, height = 300) 
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)     
    #headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    #headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    #headingLabel = Label(headingFrame1, text="LEAF DISEASE DETECTION", bg='black', fg='white', font = ('Courier',15))
    #headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(Newwindow,bg='white')
    labelFrame.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.8)
    filesetter=askopenfilename(initialdir ="/",title="select a file",filetypes=(("Template files",".tplate"),("images files",".jpg"),("HTML files", "*.html;*.htm"),("all files","*.*")))
    #img = PhotoImage(file=filesetter)          
    #imge = PhotoImage(file=filesetter,master=Newwindow)
    #load= Image.open(filesetter)
    #print(filesetter)
    #render = ImageTk.PhotoImage(load)
    #img = Label(Newwindow, image=render)
    #img.place(x=100, y=100)
    img = PhotoImage(file=filesetter,master=Newwindow)
    print(filesetter)
    Canvas1.create_image(20,20, anchor=NW, image=img)
    print(filesetter)

    
    #Canvas1.create_image(10,10, anchor=NW, image=imge)
    
root=Tk()
root.title("image view")
root.minsize(width=500,height=500)
root.geometry("600x600")
Canvas1 = Canvas(root) 
Canvas1.config(bg="#12a4d9")
Canvas1.pack(expand=True,fill=BOTH)
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
headingLabel = Label(headingFrame1, text="LEAF DISEASE DETECTION", bg='black', fg='white', font = ('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
labelFrame = Frame(root,bg='black')
labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
buttonof=Button(root, text=" UPLOAD IMAGE ",bg='black',fg='white',font=('Courier',10),command=browseFiles)
buttonof.place(relx=0.40,rely=0.55)



root.mainloop()
