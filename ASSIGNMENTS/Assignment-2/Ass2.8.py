# Que8. Write a program to find the factorial of a number using a loop.

# Input from user
num = int(input("Enter a number: "))
fact = 1
# Condition and Result
i = 1
while i <= num:
    fact *= i
    i += 1

print("The factorial of", num, "is", fact)
