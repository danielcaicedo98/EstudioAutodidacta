from tkinter import *
import tkinter.scrolledtext as scrolledtext
root=Tk()

minombre = StringVar()

miMarco=Frame(root, width=1200, height=600)

miMarco.pack()

txtTexto=Entry(miMarco, textvariable=minombre)

#txtTexto.place(x=100,y=100)

lblNombre=Label(miMarco, text="Nombre: ")

#lblNombre.place(x=100,y=100)

lblApellido=Label(miMarco, text="Apellido: ")

lblComentario=Label(miMarco, text="Comentario: ")

txtApellido=Entry(miMarco)

lblDireccion=Label(miMarco, text="Direccion Casa: ")

txtDireccion=Entry(miMarco)

txaComentario=scrolledtext.ScrolledText(miMarco, width=16,height=5)

sclComentario=Scrollbar(miMarco, command=txaComentario.yview)

#sclComentario.grid(row=3,column=2)

txtTexto.config(fg="blue", justify="right")

txtDireccion.config(show="*")

lblNombre.grid(row=0,column=0, sticky="e",pady=10,padx=10)

txtTexto.grid(row=0,column=1,pady=10,padx=10)

lblApellido.grid(row=1,column=0, sticky="e",pady=10,padx=10)

txtApellido.grid(row=1,column=1,pady=10,padx=10)

lblDireccion.grid(row=2,column=0, sticky="e",pady=10,padx=10)

txtDireccion.grid(row=2,column=1,pady=10,padx=10)

lblComentario.grid(row=3,column=0, sticky="e",pady=10,padx=10)

txaComentario.grid(row=3,column=1, sticky="e",pady=10,padx=10)

def codigoBoton():
	minombre.set("Daniel")

btnEnvio=Button(root,text="Enviar", command=codigoBoton)


btnEnvio.pack()


root.mainloop()