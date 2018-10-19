

apetece_helado = input("te apetece un helado (Si/No):").upper()


if
     apetece_helado == "SI":
    apetece_helado = True

elif
    apetece_helado == "NO":
    apetece_helado == False
    print("pues nada,no te lo comas")
    exit()

else:
    print("No entiendo lo que dices")
    exit()




tiene_dinero = input("tienes dinero para un helado? (Si/No):")
esta_el_senor = input("esta el señor de los helados? (Si/No):")
esta_tu_tia = input("esta tu tia (Si/No):")


if apetece_helado == "Si"  and tiene_dinero == "Si" or esta_tu_tia == "Si" and esta_el_senor == "Si":
    print("comete un helado")
else:

    print("pues nada")
    print("te quedas sin helado")
#Aqui se enseña a usar el "if" "and" "or" "==" y mas cosas.
#El ejemplo de arriba se puede hacer de la siguiente manera

#apetece_helado_input = input("te apetece un helado (Si/No):")
#tiene_dineo_input = input("tienes dinero para un helado? (Si/No):")
#esta_el_senor_input = input("esta el señor de los helados? (Si/No):")
#esta_tu_tia_input = input("esta tu tia (Si/No):")

#SE ESCRIBE INPUT EN LA VARIABLE
#apetece_helado = apetece_helado_input == "Si"
#tiene_dineo = tiene_dinero_input == "Si"

#asi con todos. Luego solo tendremos que poner
#apetrce_helado = apetece_helado_input == "Si"
#etc etc

#LUEGO:

# if apetece_helado and tiene_dinero and esta_el_senor:
# print("comete el helado")

#En la parte que pone ((tiene_dineo == "Si" or esta_tu_tia == "Si")) tiene puesto un "or", eso significa que
#una es "false" y la otra "true", el resultado sera "true"

#que es .upper() esto hace que #TODO ESTE EN MAYUSCULAS

# que es "alif". Lo usamos para que,si el usuario no pone la respuesta correcta,la compare con otra y mire si esa es correcta