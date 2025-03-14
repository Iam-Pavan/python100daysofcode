# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount= round(bill_per_person,2)
# print(f" Each person should pay: ${final_amount}")

print("welcome to the tip calculator")
bill = float(input("Enter your total Bill: $"))
tip = int(input('what percentage tip would you like to give? 10 12 15: $ '))
people = int(input("How many people to split the bill? "))
tip_as_percentage = bill / 100 * tip
total_percentage_bill = bill + tip_as_percentage
total_split = total_percentage_bill / people
final_bill = round(total_split,2)
print(f"you payable bill per person is: ${final_bill}")