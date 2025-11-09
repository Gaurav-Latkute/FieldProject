# Que4. Write a program to input marks and display grade according to the following rules: Marks >= 90:
#  A, Marks >= 80: B, Marks >= 70: C, Marks >= 60: D, else: Fail. (if-else ladder)

# Input
marks = int(input("Enter the Marks: "))

# Calculation and Result
if marks >= 90:
    print("'A' Grade")
elif marks >= 80:
    print("'B' Grade")
elif marks >= 70:
    print("'C' grade")
elif marks >= 60:
    print("'D' Grade")
else:
    print("You are Failed.....")