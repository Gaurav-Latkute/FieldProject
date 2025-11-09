# Que3. Write a program to input a year and check whether it is a leap year or not. (if-else)

#Input
year = int(input("Enter the Year: "))

# Conditions and Result
if year % 4 == 0:
    print(f"{year} is leaf Year")
else:
    print(f"{year} is not leaf year")