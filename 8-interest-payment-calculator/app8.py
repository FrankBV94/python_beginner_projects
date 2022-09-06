# collect the necesary inputs: principal, apr, years
# calculate the monthly payment
# show to the user

def main():
    print("This is a monthly payment loan calculater")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_inteteres_rate = apr / 1200
    amount_of_month = years * 12
    monthly_payment = principal * monthly_inteteres_rate / \
        (1 - (1 + monthly_inteteres_rate) ** (-amount_of_month))
    # %.2f imprime el numero con 2 cifras decimales
    print("the monthly payment for this loan is: %.2f" % monthly_payment)


main()
