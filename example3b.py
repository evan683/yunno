# example if an if else with conditionals

print("Notice there is going to be a problem if the number is 20. Why? Check the code!")
number = input("Enter a number that is an integer (no decimals)")
number = int(number)

if number < 0:
    print(f"{number} is negative")
elif number < 10:
    print(f"{number} is less than 10")
elif number == 10:
    print(f"{number} is 10")
elif number < 20:
    print(f"{number} is less than 20")
else:
    print("this is a catchall. The number is > 20")