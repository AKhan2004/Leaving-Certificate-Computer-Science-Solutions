# Question 16(a)
# Examination Number:

def display_intro():
    print("Welcome to my BMI calculator!")

display_intro() # (v)
weight = int(input("Enter weight (in kilograms): ")) # Read weight (i)
height = int(input("Enter height (in centimetres): ")) # (ii)

bmi = weight / (pow(height, 2)) * 10000 # (iv)

print("BMI is: ", round(bmi, 1)) # (iii)

if bmi < 18.5: # (vi)
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obese")
