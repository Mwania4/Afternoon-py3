# necessary to calculate both simple interest of a loan borrowed
# and volume of any cylinder.
# Implement the respective functions to calculate the volume of a
# cylinder and the SI of a loan borrowed.
#NOTE: All data should come from the use as input

from database import Hesabu
try:
    Hesabu.create()
    rate = input("Enter the rate\n")
    principal = input("Enter the principal\n")
    time = input("Enter the time\n")

    rate = float(rate)
    principal = float(principal)
    time = float(time)

    interest = (principal * rate * time) / 100
    print(interest)

    width = input("Enter the width\n")
    height = input("Enter the height\n")
    length = input("Enter the length\n")

    width = float(width)
    height = float(height)
    length = float(length)

    volume = width * length * height
    print(volume)

except:
    print("try again")