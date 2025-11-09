# Que3. Write a program to input the marks of 5 subjects and display the total and average marks.

# Message
print("Enter the marks of Subject")

# Inpute 5 Subjects
sub1 = int(input("\nEnter English subject Mark:- "))
sub2 = int(input("Enter Maths subject Mark:- "))
sub3 = int(input("Enter Physics subject Mark:- "))
sub4 = int(input("Enter Chemistry subject Mark:- "))
sub5 = int(input("Enter Biology subject Mark:- "))

# Calculation
total = sub1 + sub2 + sub3 + sub4 + sub5
average = (sub1 + sub2 + sub3 + sub4 + sub5)/5

# Display Result
print(f"\nTotal Marks of 5 Subject is:- {total} \nAverage of 5 Subject is:- {average}")
# print("Total Marks of 5 Subject is:- ", total)
# print("Average of 5 Subject is:- ", average)