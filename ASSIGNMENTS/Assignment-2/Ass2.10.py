# Que 10. Write a program to reverse a given number using a loop

num = int(input("Enter the Number"))
reverse = 0
# Condition
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10
print("The Reverse No. is: ", reverse)