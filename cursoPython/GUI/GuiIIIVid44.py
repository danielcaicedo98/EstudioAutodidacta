from tkinter import *

root=Tk()

miMarco=Frame(root, width=1200, height=600)

miMarco.pack()

txtTexto=Entry(miMarco)

#txtTexto.place(x=100,y=100)

lblNombre=Label(miMarco, text="Nombre: ")

#lblNombre.place(x=100,y=100)

lblApellido=Label(miMarco, text="Apellido: ")

txtApellido=Entry(miMarco)

lblDireccion=Label(miMarco, text="Direccion Casa: ")

txtDireccion=Entry(miMarco)

txtTexto.config(fg="blue", justify="right")

txtDireccion.config(show="*")

lblNombre.grid(row=0,column=0, sticky="e",pady=10,padx=10)

txtTexto.grid(row=0,column=1,pady=10,padx=10)

lblApellido.grid(row=1,column=0, sticky="e",pady=10,padx=10)

txtApellido.grid(row=1,column=1,pady=10,padx=10)

lblDireccion.grid(row=2,column=0, sticky="e",pady=10,padx=10)

txtDireccion.grid(row=2,column=1,pady=10,padx=10)

root.mainloop()