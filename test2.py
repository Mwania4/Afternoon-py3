# Create a function to ascertain that the user has "eMobilis" as
# username and "eMobilis@123" as password. Henceforth, proceed
# to calculate the BMI Of the user and display the results of the
# BMI as either 1. Underweight, 2. normal weight, 3. overweight or 4. Obese
# NOTE: All the data should be provided by the user as input.
# use the scale below for the BMI:
#     0-----------------18----------UNDERWEIGHT
#     18.1----------29-------NORMAL WEIGHT
#       29.1--------34-------OVERWEIGHT
#         34.1 ----AND ABOVE ----OBESE

username = input("Enter the username\n")
password = input("Enter the password\n")
weight = input("Enter the weight\n")
height = input("Enter the height\n")

weight = int(weight)
height = int(height)

if username == "eMobilis" and password == "eMobilis@123":
        bmi =weight/(height*height)
        if bmi <= 18:
            print("underweight")
        elif bmi <= 29:
            print("Normalweight")
        elif bmi <= 34:
            print("overweight")
        else:
            print("obese")

else:
    print("enter correct details")