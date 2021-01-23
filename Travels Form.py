from tkinter import *

root = Tk()
root.geometry("700x400")

#Heading
Label(root,text="Welcome to Kartik Travels",font='sans 20 bold',pady=10).grid(row=0,column=3)

#Text Boxes
Label(root,text="Name",font='sans 10 bold',pady=10).grid(row=1,column=2)
Label(root,text="Phone",font='sans 10 bold',pady=10).grid(row=2,column=2)
Label(root,text="Gender",font='sans 10 bold',pady=10).grid(row=3,column=2)
Label(root,text="Emergency Contact Number",font='sans 10 bold',pady=10).grid(row=4,column=2)
Label(root,text="Email",font='sans 10 bold',pady=10).grid(row=5,column=2)

#String Variables
Nameval = StringVar()
Phoneval = StringVar()
Genderval = StringVar()
Emergencyval = StringVar()
Emailval = StringVar()

#Blank Box for String entry
Entry(root,textvariable=Nameval).grid(row=1,column=3)
Entry(root,textvariable=Phoneval).grid(row=2,column=3)
Entry(root,textvariable=Genderval).grid(row=3,column=3)
Entry(root,textvariable=Emergencyval).grid(row=4,column=3)
Entry(root,textvariable=Emailval).grid(row=5,column=3)

#Submit Button
button = Button(root,text="Submit",borderwidth=5,padx=10,font='sans 10 bold').grid(column=2)


root.mainloop()