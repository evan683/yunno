#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

a = float(input("enter a number "))
E = a % 2
if E == 1:
    print("its an odd number")
if E == 0:
    print("its an even number")