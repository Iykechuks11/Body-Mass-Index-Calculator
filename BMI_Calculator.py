# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's
# weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
#
# The BMI is calculated by dividing a person's weight (in kg)
# by the square of their height (in m):

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

bmi_calc = round(weight / (height ** 2))

if bmi_calc <= 18.5:
    print(f"Your BMI is {bmi_calc}, you are underweight.")
elif (bmi_calc > 18.5) and (bmi_calc <= 25):
    print(f"Your BMI is {bmi_calc}, you have a normal weight.")
elif (bmi_calc > 25) and (bmi_calc <= 30):
    print(f"Your BMI is {bmi_calc}, you are slightly overweight.")
elif (bmi_calc > 30) and (bmi_calc <= 35):
    print(f"Your BMI is {bmi_calc}, you are obese.")
elif bmi_calc > 35:
    print(f"Your BMI is {bmi_calc}, you are clinically obese.")
