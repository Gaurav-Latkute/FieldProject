# 7. Write a program to input a number and display the same number in hexadecimal and binary format.

# Input from user
num = int(input("Enter Any Number: "))

# Calculations:- Convert to Hecadecimal and Binary
hexadecimal = hex(num) [2:] .upper()
binary = bin(num) [2:]

# Display the Result
print(f"Hexadecimal No.= {hexadecimal} \nBinary No.= {binary}")