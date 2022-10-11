from tkinter import *
from tkinter import ttk

def validateLogin(): 
    global e_email
    e_email = email_empresa.get()
    print("email_empresa entered :", e_email)
    global e_senha
    e_senha = password.get()
    print("password entered :", e_senha)
    global e_maquina
    e_maquina = maquina_cb.get()
    print("idMaquina entered :", e_maquina) 
    tkWindow.after(1000,lambda:tkWindow.quit())
    return 



#window
global tkWindow
tkWindow = Tk()  
tkWindow.geometry('450x250')
tkWindow.resizable(False, False)  
tkWindow.title('Green Light || Login Empresa')

#username label and text entry box
header = Label(tkWindow, text="Login Green Light", font=("Arial", 15),height=3).grid(row=0, column=2)
usernameLabel = Label(tkWindow, text="Email empresa: ", font=("Arial", 12)).grid(row=2, column=1)
global email_empresa
email_empresa = StringVar()
usernameEntry = Entry(tkWindow, textvariable=email_empresa, width=25).grid(row=2, column=2)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Senha :", font=("Arial", 12)).grid(row=5, column=1)  
global password
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', width=25).grid(row=5, column=2) 

#
label = Label(tkWindow, text="Selecione qual é essa maquina:", font=("Arial", 12)).grid(row=7, column=2)
listaIdMaquina = [101,102,103,104,105]
maquina_cb = ttk.Combobox(tkWindow, values=listaIdMaquina, width=22, state="readonly")
maquina_cb.grid(row=8, column=2)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin, font=("Arial", 11), ).grid(row=10, column=2) 
tkWindow.mainloop()

