from tkinter import *

root=Tk()
root.geometry("600x500")
root.title("Entry box")




nOmbre=StringVar()
aPellido=StringVar()

def saludar(): print(f'hola{nOmbre.get()} {aPellido.get()}')

framePrincipal = Frame(root,bg="#FFFACD")
framePrincipal.pack(fill="both",expand=1)


titulo=Label(framePrincipal, text = "Registro",bg="#FFFACD",font=("Roboto",20,"bold")).pack()
nombre=Label(framePrincipal,text="Nombre: ").place(x=10,y=100)


Apellido=Label(framePrincipal,text="Apellido: ").place(x=10,y=150)

nombreTexto=Entry(framePrincipal,textvariable=nOmbre).place(x=100, y=100)
apellidoTexto=Entry(framePrincipal,textvariable=aPellido).place(x=100, y=150)

botonSaludar=Button(framePrincipal,text="Saludar", bg="#000000",fg="#FFFACD",font=("Comic Sans Ms",12,"bold"),width=12,height=1,command=saludar)
botonSaludar.place(x=100,y=200)



root.mainloop() 
