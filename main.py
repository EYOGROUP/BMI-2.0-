# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)

bmi_round = int(round(bmi))

if bmi < 18.5:
    print(f"Your BMI is {bmi_round}, you are underweight.")

elif  18 < bmi <25:
    print(f"Your BMI is {bmi_round}, you have a normal weight.")

elif 25 < bmi <30:
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")

elif 30 < bmi < 35:
    print(f"Your BMI is {bmi_round}, you are obese.")

else:
     print(f"Your BMI is {bmi_round}, you are clinically obese.")

