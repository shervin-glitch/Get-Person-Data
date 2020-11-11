from tkinter import *
master=Tk()
master.title("Login Page")
master.geometry("250x155")
master.resizable(0 , 0)
master["bg"]="tomato"

Label(master, text = "Name:" , bg = "yellow").grid(row = 0 , column = 0 , sticky = W)
sv_name=StringVar()
Entry(master, textvariable = sv_name).grid(row = 0 , column = 1)

Label(master, text = "Family:" , bg = "yellow").grid(row = 1, column = 0, sticky = W)
sv_family=StringVar()
Entry(master, textvariable= sv_family).grid(row = 1 , column =1)

Label(master, text = "ID:" , bg = "yellow").grid(row = 2 , column = 0 , sticky = W)
sv_id=StringVar()
Entry(master, textvariable= sv_id).grid(row = 2 , column = 1)

Label(master, text = "Tel:" , bg = "yellow").grid(row = 3 , column = 0 , sticky = W)
sv_tel=StringVar()
Entry(master, textvariable = sv_tel).grid(row = 3 , column = 1)

Label(master, text = "Gmail:" , bg = "yellow").grid(row = 4 , column = 0 , sticky =W)
sv_gmail=StringVar()
Entry(master, textvariable = sv_gmail).grid(row = 4 , column = 1)

Label(master, text = "Password:" , bg = "yellow").grid(row = 5 , column = 0 , sticky =W)
sv_password=StringVar()
Entry(master, textvariable = sv_password).grid(row = 5 , column = 1)


def press(e):
    if e=="snd":
        master.destroy()
        name=sv_name.get()
        family=sv_family.get()
        id=sv_id.get()
        tel=sv_tel.get()
        gmail=sv_gmail.get()
        password=sv_password.get()

        file=open("Person.txt", "a")
        file.write("Personal Information:"+'\n'+"Name:"+name+'\n'+"Family:"+family+'\n'+"ID:"+id+'\n'+"Tel:"+tel+'\n'+"Gmail:"+gmail
        +'\n'+"Password:"+password+'\n'+'\n')
        file.close()

Button(master, text = "Send", command = lambda :press("snd") , bg ="purple").grid(row = 6 , column = 0 , sticky =W)
btn02=Button(master, text = "Exit" , command = master.destroy, bg = "Red")
btn02.grid (row = 6 , column = 1 , columnspan = 2)
btn02.config(height = 1 , width = 8)

master.mainloop()
