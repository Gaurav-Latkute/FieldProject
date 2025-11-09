#  Que7. Write a program to print the multiplication table of a number using a loop.

# Input form user
num = int(input("Enter the Number: "))

# For Loop Statement
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
    
print()


# While Loop Statement 
n = 1
while n <=10:
    print(f"{num} * {n} = {num*n}")
    n += 1

