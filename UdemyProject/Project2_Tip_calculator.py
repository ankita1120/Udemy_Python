print("Welcome to tip Calculator.")

bill =float(input("What was the total bill? $ " ))

tip =int(input("What percentage tip would you like to give?  10 12 15 "))

people = int(input("How many people split the bill ? " ))

tip_of_percent =tip /100
total_tip_amount = bill * tip_of_percent
total_bill = bill + total_tip_amount
bill_per_person  =  total_bill /people
final_amount = round(bill_per_person ,2)
print(f"Each person should pay: ${final_amount}")
