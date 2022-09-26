import random 

ordenador = random.randint(0,2)

print ("Bienvenidos al juago")
usuario = int(input("¿Que opción quieres?. Escribe '0' para piedra, '1' para papel y '2' para tijeras"))

print("Usuario = " + str(usuario))
print(f"Ordenador = {ordenador}")

if usuario == 0 and ordenador == 2:
    print("Ha ganado el usuario")
elif usuario == 1 and ordenador == 0:
    print("Ha ganado el usuario")
elif usuario == 2 and ordenador == 1:
    print("Ha ganado el usuario")
elif usuario == ordenador:
    print("Es un empate, vuelve a intentar")
else:
    print("Ha ganado el ordenador")
