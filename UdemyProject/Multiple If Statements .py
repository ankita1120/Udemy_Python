input("Welcome to the Rollercoster !")
Height = int(input("What is your height in cm ? "))
bill = 0
if Height >= 120:
    print("You can ride the rollercoster.")
    age = int(input("What is your age ?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age and age <= 55:
        print("Everthing is going to be ok . Have a free ride on us !")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo =input("Do you want to have a photo take ? Type  y for Yes  n for No.")
    if want_photo == "y":
     # Add $3 to their  bill
      bill += 3
    print(f"Your final bill is{bill} ")

else:
    print("Sorry you can to grow taller before you can ride.")


