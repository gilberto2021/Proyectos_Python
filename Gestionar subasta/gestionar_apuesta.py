import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def calcular_ganador(apuestas):
    apuesta_maxima = 0
    ganador = ""
    for clave in apuestas:
        precio_apuestas = apuestas[clave]
        if precio_apuestas > apuesta_maxima:
            apuesta_maxima = precio_apuestas
            ganador = clave
    print(f"El ganador es {ganador} con un precio de apuesta de {apuesta_maxima}")


print("Bienvenidos a la subasta")

apuestas = {}

mas_apuestas = True

while mas_apuestas:
    nombre =input("Nombre del apostador")
    precio =float(input("Precio de la apuesta"))
    apuestas[nombre] = precio

    pregunta = input("¿Hay mas personas que quieran hacer apuestas?. Escribe 'si' o 'no'")
    if pregunta == 'si':
        clearConsole()
    elif pregunta == 'no':
        mas_apuestas = False

clearConsole()    
calcular_ganador(apuestas)

