# Que4. Write a program to input the radius of a circle and display its area and circumference.

# Input Radius of circle
radius = float(input("Enter the Radius of Circle:- "))

# Calculations
area = 3.14 * radius * radius

cir = 2 * 3.14 * radius

# Display Results
print(f"\nThe Area of Circle is:- {area:.2f} \nThe Circumference of Circle is:- {cir:.2f}")