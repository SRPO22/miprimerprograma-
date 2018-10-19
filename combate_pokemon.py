
print("¿Como se llama tu pokemon?") #Con estas lineas conseguimos que el usuario pueda  elegir su nombre
nombre_elegido_usuario = input() #Aqui el usuario introduce su nombre
print("bienvenido {}".format(nombre_elegido_usuario))

pokemon_elegido = input("¿contra que pokemon quieres combatir? (agua / fuego/ verde): ")

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "agua":
    vida_enemigo = 90
    nombre_pokemon = "agua"
    ataque_pokemon = 9

elif pokemon_elegido == "fuego": #Se pone elif en vez de if,para que no tenga que mirar todas las lineas.
    vida_enemigo = 80
    nombre_pokemon = "fuego"
    ataque_pokemon = 10

elif pokemon_elegido =="verde":
    vida_enemigo = 100
    nombre_pokemon = "verde"
    ataque_pokemon = 11

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elejido = input("¿Que ataque quieres usar? buco / patada / insulto")

    if ataque_elejido == "buco":
        vida_enemigo -= 4
    elif ataque_elejido == "patada": #Se pone elif en vez de if,para que no tenga que mirar todas las lineas.
        vida_enemigo -= 5
    elif ataque_elejido == "insulto":
        vida_enemigo -= 15
    print("La vida del pokemon {} es de {} ".format(nombre_pokemon, vida_enemigo))


    if pokemon_elegido == nombre_pokemon:
       print("El Pokemon {} te acaba de quitar 9".format(nombre_pokemon))
       vida_pikachu -= ataque_pokemon

    print("La vida de tu pokmon {} es de {}".format(nombre_elegido_usuario, vida_pikachu))

if vida_enemigo <= 70:
    print("casi lo matas")
if vida_enemigo <= 0:
    print("has ganado!!! {} ha sido derrotado".format(nombre_pokemon))
if vida_pikachu <= 0:
    print("perdiste")

print("El combate termina")
