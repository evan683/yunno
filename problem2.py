#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

a = float(input("enter a number "))
if a.is_integer():
    print("its an integer")
else:
    print("it's not an integer")