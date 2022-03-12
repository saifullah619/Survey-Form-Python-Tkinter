from tkinter import *
from PIL import Image, ImageTk

def on_resize(event):
    # resize the background image to the size of label
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    # update the image of the label
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)
    
def saveToFile():
    saveFirstName = firstNameEntry.get()
    saveGender = gender.get()
    saveage = age.get()
    
    file = open("data.txt","a+")
    file.write(saveFirstName)
    file.write(',')
    if saveGender==1:
        file.write('M')
    elif saveGender==2:
        file.write('F')
    else:
        pass
    file.write(',')
    file.write(saveage)
    file.write('\n')
    file.close()

    firstNameEntry.delete(0,END)
    male.deselect()
    female.deselect()
    age.delete(0,END)
    
class NewWindow(Toplevel):
    def __init__(self, master = None):         
        super().__init__(master = master)
        self.title("New Window")
        self.geometry("500x500")
        Label(self, text ="username : ").pack()
        uname = Entry(self,width=20,bd=2,foreground=  'black',font=("times",12,"bold")).pack()
        Label(self,text="password : ").pack()
        pas = Entry(self,width=20,bd=2,foreground=  'black',font=("times",12,"bold"),show='*').pack()
        if uname == 'admin' and pas == '1234':
            Label(self, text ="Average age of users is 22").pack()
            Label(self, text ="").pack()
            Label(self, text ="username : ").pack()

root = Tk()

if __name__ == "__main__":    
    root.geometry("1000x1000")
    # canvas = Canvas(root, width = 1000, height = 800)
    # img1 = PhotoImage(file="d.jpeg")
    # canvas.pack()      
    # #img = PhotoImage(file="ball.ppm")      
    # canvas.create_image(0,0, anchor=NW, image=img1)   
    bgimg = Image.open('D2.jpg') # load the background image
    l = Label(root)
    l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
    l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized

    # Label(root, text='Some File').grid(row=0)
    # e1 = Entry(root)
    # e1.grid(row=0, column=1)



    i = 0
    firstName = Label(root, text='Name: ', fg='black',font=("times",16))
    firstName.grid(row=i+0)
    age = Label(root, text='Age: ', fg='black',font=("times",16))
    age.grid(row=i+1)
    sex = Label(root,text='Sex: ',fg='black',font=("times",16))
    sex.grid(row=i+2)

    firstNameEntry = Entry(root,width=20,bd=2,foreground=  'black',font=("times",16,"bold"))
    age = Entry(root,width=20,bd=2,foreground=  'black',font=("times",16,"bold"))
    firstNameEntry.grid(row=i+0,column=1)
    age.grid(row=i+1,column=1)
    gender = IntVar()
    male = Radiobutton(root, text='Male', variable=gender,value=1)
    female = Radiobutton(root, text='Female', variable=gender,value=2)
    other = Radiobutton(root, text="Other",variable=gender,value=3)

    male.grid(row=i+2 , column = 2)
    female.grid(row=i+2,column=1)
    other.grid(row=i+2,column=3)
    
    Ethnecity = Label(root, text='Ethnicity: ', fg='black',font=("times",16))
    Ethnecity.grid(row=i+3)
    
    ethnecity = IntVar()
    asian = Radiobutton(root, text='Asian', variable=ethnecity,value=1)
    asian.grid(row=i+3,column=1)
    white=Radiobutton(root, text='White', variable=ethnecity,value=2)
    white.grid(row=i+3,column=2)
    black=Radiobutton(root, text='Black', variable=ethnecity,value=3)
    black.grid(row=i+3,column=3)
    chinese = Radiobutton(root, text='Chinese', variable=ethnecity,value=4)
    chinese.grid(row=i+3,column=4)
    other = Radiobutton(root, text='Other', variable=ethnecity,value=5)
    other.grid(row=i+3,column=5)
    
    disabilty = Label(root, text='Disability: ', fg='black',font=("times",16))
    disabilty.grid(row=i+4)
    
    disabilty = IntVar()
    disabilty_y = Radiobutton(root, text='YES', variable=disabilty,value=1)
    disabilty_n = Radiobutton(root, text='NO', variable=disabilty,value=2)
    
    disabilty_y.grid(row=i+4 , column = 1)
    disabilty_n.grid(row=i+4,column=2)
    
    
    enjoymennt = Label(root, text='Are you curiois : ', fg='black',font=("times",16))
    enjoymennt.grid(row=i+6)
    
    enjoymennt = IntVar()
    enjoyment_y = Radiobutton(root, text='YES', variable=enjoymennt,value=1)
    enjoyment_n = Radiobutton(root, text='NO', variable=enjoymennt,value=2)
    
    enjoyment_y.grid(row=i+6 , column = 1)
    enjoyment_n.grid(row=i+6,column=2)

    enj = Label(root, text='Have you enjoyed the sculpture: ', fg='black',font=("times",16))
    enj.grid(row=i+5)
    
    enj = IntVar()
    enj1 = Radiobutton(root, text='Strongly Agree', variable=enj,value=1)
    enj1.grid(row=i+5,column=1)
    enj2=Radiobutton(root, text='Agree', variable=enj,value=2)
    enj2.grid(row=i+5,column=2)
    enj3=Radiobutton(root, text='Neither Agree', variable=enj,value=3)
    enj3.grid(row=i+5,column=3)
    enj4= Radiobutton(root, text='Disagree', variable=enj,value=4)
    enj4.grid(row=i+5,column=4)
    enj5 = Radiobutton(root, text='Strongly disagree', variable=enj,value=5)
    enj5.grid(row=i+5,column=5)
    
    
    learning = Label(root, text='Do you want to learn more about science : ', fg='black',font=("times",16))
    learning.grid(row=i+7)
    
    learning = IntVar()
    learning_y = Radiobutton(root, text='YES', variable=learning,value=1)
    learning_n = Radiobutton(root, text='NO', variable=learning,value=2)
    
    learning_y.grid(row=i+7 , column = 1)
    learning_n.grid(row=i+7,column=2)
    
    submitButton = Button(root,text='Submit ',command=saveToFile,bg='orange',fg='black')
    submitButton.place(x=60,y=220,width=150)
    
    # quitButton = Button(root, text='Quit',bg='orange',fg='black' ,command=root.quit)
    # quitButton.place(x=60,y=260,width=150)
    
    btn = Button(root,text ="Login as host")
    
    # Following line will bind click event
    # On any click left / right button
    # of mouse a new window will be opened
    btn.bind("<Button>",
            lambda e: NewWindow(root))
    btn.place(x=60,y=260,width=150)
    


    root.mainloop()