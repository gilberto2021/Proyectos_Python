from tkinter import * 
import operaciones

#Funciones para los botones (del fichero operaciones)

def comando_visualizar():
    lista.delete(0,END)
    lista_libros = operaciones.visualizar()
    for libro in lista_libros:
        lista.insert(END, libro)

def comando_buscar():
    lista.delete(0,END)
    lista_libros = operaciones.buscar(titulo.get(), autor.get(), year.get(), editorial.get())
    for libro in lista_libros():
        lista.insert(END, libro)

def comando_insertar():
    operaciones.insertar(titulo.get(), autor.get(), year.get(), editorial.get())
    lista.delete(0,END)
    lista.insert(END, (titulo.get(), autor.get(), year.get(), editorial.get()))

def recojer_fila_seleccionada(event):
    try: 
        global libro_seleccionado
        indice = lista.curselection()[0]
        libro_seleccionado = lista.get(indice)

        entrada1.delete(0,END)
        entrada1.insert(END, libro_seleccionado[1])

        entrada2.delete(0,END)
        entrada2.insert(END, libro_seleccionado[2])

        entrada3.delete(0,END)
        entrada3.insert(END, libro_seleccionado[3])

        entrada4.delete(0,END)
        entrada4.insert(END, libro_seleccionado[4])

    except IndexError:
        pass

def comando_actualizar():
    operaciones.actualizar(titulo.get(), autor.get(), year.get(), editorial.get(), libro_seleccionado[0])
    lista.delete(0,END)
    lista.insert(END, "Libro actualizado correctamente")

def comando_borrar():
    operaciones.borrar(libro_seleccionado[0])
    lista.delete(0,END)
    lista.insert(END, "Libro borrado correctamente")

def comando_cerrar():
    ventana.destroy()
    

#Creamos parte grafica visual de la aplicación
ventana = Tk()

etiqueta1 = Label(ventana, text="Título")
etiqueta1.grid(row=0, column=0)

etiqueta2 = Label(ventana, text="Autor")
etiqueta2.grid(row=0, column=2)

etiqueta3 = Label(ventana, text="Año")
etiqueta3.grid(row=1, column=0)

etiqueta4 = Label(ventana, text="Editorial")
etiqueta4.grid(row=1, column=2)

titulo = StringVar()
entrada1 = Entry(ventana, textvariable=titulo)
entrada1.grid(row=0, column=1)

autor = StringVar()
entrada2 = Entry(ventana, textvariable=autor)
entrada2.grid(row=0, column=3)

year = StringVar()
entrada3 = Entry(ventana, textvariable=year)
entrada3.grid(row=1, column=1)

editorial = StringVar()
entrada4 = Entry(ventana, textvariable=editorial)
entrada4.grid(row=1, column=3)

lista = Listbox(ventana, height=8, width=25)
lista.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(ventana)
scrollbar.grid(row=2, column=2, rowspan=6)

lista.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista.yview)

#Evento de la lista
lista.bind("<<ListboxSelect>>", recojer_fila_seleccionada)

#Botones
boton1 = Button(ventana, text="Visualizar", width=12, command=comando_visualizar)
boton1.grid(row=2, column=3)

boton2 = Button(ventana, text="Buscar", width=12, command=comando_buscar)
boton2.grid(row=3, column=3)

boton3 = Button(ventana, text="Añadir", width=12, command=comando_insertar)
boton3.grid(row=4, column=3)

boton4 = Button(ventana, text="Actualizar", width=12, command=comando_actualizar)
boton4.grid(row=5, column=3)

boton5 = Button(ventana, text="Borrar", width=12, command=comando_borrar)
boton5.grid(row=6, column=3)

boton6 = Button(ventana, text="Cerrar", width=12, command=comando_cerrar)
boton6.grid(row=7, column=3)


operaciones.conectar()
ventana.title("Libros")
ventana.mainloop()

