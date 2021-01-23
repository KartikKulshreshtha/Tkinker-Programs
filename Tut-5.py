


from tkinter import *

def Subbmited():
    print(f"The name of student is: {nameval.get()}")
    print(f"The age of student is: {ageval.get()}")
    print(f"The address of student is: {addressval.get()}")

root = Tk()
root.geometry("400x400")




name = Label(root,text="What's your name buddy??",font=10,pady=10)
age = Label(root,text="What's your age buddy??",font=10,pady=10)
address = Label(root,text="What's your address buddy??",font=10,pady=10)

name.grid()
age.grid(row=1)
address.grid(row=2)

nameval = StringVar()
ageval = StringVar()
addressval = StringVar()


Entry(root,textvariable=nameval).grid(row=0,column=1)
Entry(root,textvariable=ageval).grid(row=1,column=1)
Entry(root,textvariable=addressval).grid(row=2,column=2)

Button(root,text="Submit",borderwidth=5,font=10,command=Subbmited,padx=10).grid()


root.mainloop()
