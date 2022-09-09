def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Si es año biciesto")
            else:
                print('No es año biciesto')
        else:
            print("Si es año biciesto")
    else:
        print("No es año biciesto")


is_leap_year(2000)
