print("=== BMI CALCULATOR ===")
weight=float(input("Enter the weight (kg)"))
height=float(input("Enter the height (m)"))
bmi= weight/(height*height)
print(f"Your BMI is {bmi:.2f}")
if bmi<18.5 :
    print("Category : Underweight")
elif bmi>18.5 and bmi<24.9 :
    print("Category : Normal")
elif bmi>24.9 and bmi<29.9 :
    print("Category : Overweight")
else:
    print("Category : Obese")
