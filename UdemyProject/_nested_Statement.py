input("Welcome to Rollercoster !")
Height = int(input("Wht is your height in cm ?"))

if Height == 120:
    print("You can ride the Rollercoster")
    age = int(input("what is your Age ?"))
    if age <= 12:
        print("Please pay 5$")
    elif age <= 18:
        print("Please pay 7$.")
    else:
        print("Please pay 12$.")
else:
    print("Sorry you can to grow taller before you can ride.")
