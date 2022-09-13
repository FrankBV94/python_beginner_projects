import random
from tkinter import E

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ['piedra', 'papel', 'tijeras']
    user_input = input("Selecione piedra, papel o tijeras o exit:")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print("Puntos usuario " + str(user_points))
        print("Puntos pc " + str(computer_points))
        exit = True

    if user_input == "piedra":
        if computer_input == "piedra":
            print("Seleccionaste Piedra")
            print("Pc selecciono Piedra")
            print("Empate")
        elif computer_input == "papel":
            print("Seleccionaste Piedra")
            print("Pc selecciono papel")
            print("Pc gana")
            computer_points += 1
        elif computer_input == "tijeras":
            print("Seleccionaste Piedra")
            print("Pc selecciono Tijeras")
            print("Tu ganas")
            user_points += 1
    elif user_input == "papel":
        if computer_input == "piedra":
            print("Seleccionaste Papel")
            print("Pc selecciono Piedra")
            print("tu ganas")
            user_points += 1
        elif computer_input == "papel":
            print("Seleccionaste Papel")
            print("Pc selecciono Papel")
            print("Empate")
        elif computer_input == "tijeras":
            print("Seleccionaste Papel")
            print("Pc selecciono Tijeras")
            print("Pc gana")
            computer_points += 1
    elif user_input == "tijeras":
        if computer_input == "piedra":
            print("Seleccionaste Tijeras")
            print("Pc selecciono Piedra")
            print("Pc gana")
            computer_points += 1
        elif computer_input == "papel":
            print("Seleccionaste Tijeras")
            print("Pc selecciono Papel")
            print("Tu ganas")
            user_points += 1
        elif computer_input == "tijeras":
            print("Seleccionaste Tijeras")
            print("Pc selecciono Tijeras")
            print("Empate")

    elif user_input != "piedra" or user_input != "papel" or user_input != "tijeras":
        print("Entrada incorrecta")
