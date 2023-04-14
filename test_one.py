# Write a logic to implement a simple calculator
# capable of computing two numbers entered by the user
# as input
# Make sure the program can compute with either of
# the four mathematical operations
first_no = input("Enter the first number\n")
second_no = input("Enter the second number\n")
operation = input("Enter the operation\n")

first_no = int(first_no)
second_no = int(second_no)

if operation =="+":
    print(first_no + second_no)
elif operation == "-":
    print(first_no - second_no)
elif operation == "*":
    print(first_no * second_no)
elif operation == "/":
    print(first_no / second_no)
else:
    print("Enter any of these operations -+/*")






















