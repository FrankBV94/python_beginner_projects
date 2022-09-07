def main():
    print("This program converts US Dollars to Cuban Peso")

    dollars = eval(input("Enter amount in dollar: "))

    peso = convert_to_peso(dollars)

    print("That is", peso, "pesos.")


def convert_to_peso(dollars): return dollars * 24


main()
