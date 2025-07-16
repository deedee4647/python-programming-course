print("BMI Calculator")

weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = weight / height ** 2

if bmi < 18.5:
    print("Underweight")

if bmi >= 18.5 and bmi <= 24.9:
    print("Normal weight")

if bmi >= 24.9 and bmi <= 30:
    print("Overweight")

if bmi > 30:
    print("Obese")
