# Que 2. Write a program to input three numbers and find the greatest among them. (if-else)

# Input Three Numbers
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))

# Cinditions and Result
if num1 > num2:
    print(f"The Greater No. is: {num1}")
elif num2 > num3:
    print(f"The Greater No. is: {num2}")
else:
    print(f"The Greater No. is: {num3}")


