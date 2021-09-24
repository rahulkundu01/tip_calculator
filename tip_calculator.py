#Tip Calculator
print("Welcome to Tip Calculator")
bill = float(input("What is your total bill? "))
tip = int(input("How much Tip you like to give? 10, 15, 20? "))
people = int(input("How may people to split the bill? "))

tip_as_percent = tip * 100
total_tip_amount = bill + tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = bill / people

final_amount = round(bill_per_person,2)
print("Each person shold pay: ",final_amount)