number_to_guess: int = 23
user_number = int(input("adivina un numero"))

if number_to_guess == user_number:
     print("ganas")

else:
     print("has perdido")
     print("intentalo otra vez")
     user_number = int(input("adivina un numero"))
     if number_to_guess == user_number:
         print("ganas")
     else: print("pierdes otra vez,muy mal")

print("otro intento mas")

user_number = int(input("adivina el dichoso numero"))
if number_to_guess == user_number:
     print("bien,a la segunda va la vencida")
else:
     print("has vuelto a perder,eres un perdedor xDD")
print("voy a ser bueno")
print("te dare otra oportunidad")
print("¿preparado?")
primero_si = input("di S (si) o N (no)")
if primero_si == "S":
    print("Genial")
else:
    print("¿porque?")






