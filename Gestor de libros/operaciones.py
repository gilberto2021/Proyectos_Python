import re
import sqlite3

def conectar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, year INTEGER, editorial TEXT)")
    conexion.commit()
    conexion.close()

def insertar(titulo, autor, year, editorial):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros VALUES(NULL,?,?,?,?)",(titulo, autor, year, editorial))
    conexion.commit()
    conexion.close()

def visualizar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def buscar(titulo="", autor="", year=0, editorial=""):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR year=? OR editorial=?", (titulo,autor,year,editorial))
    resultado = cursor.fetchall
    return resultado

def borrar (id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?", (id,))
    conexion.commit()
    conexion.close()
    
def actualizar (titulo, autor, year, editorial, id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?, autor=?, year=?, editorial=? WHERE id=?", (titulo,autor,year,editorial, id))
    conexion.commit()
    conexion.close()

#conectar()
#insertar()
#resultados = buscar(autor="Pedro")
#for resultado in resultados():
#    print(resultado)

#borrar(7)
#resultados = visualizar()
#for resultado in resultados:
#    print(resultado)   

#actualizar(titulo="Libro4", autor="Juana" , year=2011, editorial="Santillana", id=4)
#resultados = visualizar()
#for resultado in resultados:
#    print(resultado)