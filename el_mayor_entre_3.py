number_to_guess = 2

user_number = int(input("adivina un numero: "))

if number_to_guess == user_number:
    print("bien,era ese")
else:
    print("no,vuelve a intentarlo")

number_to_guess = 2
user_number = int(input("intentalo de nuevo,¿cual es el numero?: "))
if number_to_guess == user_number:
    print("has ganado")
else:
    print("has perdido")
    breakpoint = input ("fin de la partida1")
    exit()



 