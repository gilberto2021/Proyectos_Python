import random

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['1','2','3','4','5','6','7','8','9','0']
simbolos = ['!','"','#','$','%','&','/','(',')','=','?','¿','¡','+','}','{','-','*','[',']','_',',','.',':',';','>','<']

print("Bienvenidos al generador de contraseñas")

cantidad_letras = int(input("\n ¿Cuantas letras quieres?"))
cantidad_numeros = int(input("\n ¿Cuantos numeros quieres?"))
cantidad_simbolos = int(input("\n ¿Cuantos símbolos quieres?"))

lista = []

for letra in range (1, cantidad_letras + 1):
    valor = random.choice(letras)
    lista.append(valor)

for numero in range (1, cantidad_numeros + 1):
    valor = random.choice(numeros)
    lista.append(valor)

for simbolo in range (1, cantidad_simbolos + 1):
    valor = random.choice(simbolos)
    lista.append(valor)

random.shuffle(lista)

password = ""

for caracter in lista:
    password = password + caracter

print("Su contraseña es " + password)