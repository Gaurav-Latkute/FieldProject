# 6. Write a program to input the principal, rate, and time, and display the simple interest.

# Take Inpute from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter rate of Interest (in %): "))
time = float(input("Enter Time (in Years): "))

# Calculations
si = (principal * rate * time)/100

# Display Result
print(f"\nSimple Interest is: ", si)
