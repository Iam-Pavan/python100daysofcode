print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        # print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        # print("Youth tickets are $7.")
        bill = 7
    else:
        # print("Adult tickets are $12.")
        bill = 12
    wants_photos = input('Do you want to have photo take? type y for yes and n for no.')
    if wants_photos == 'y':
        # bill = bill + 3
        bill += 3
    print(f'Your final bill is ${bill}')
else:
    print("Sorry you have to grow taller before you can ride.")
