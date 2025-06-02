units = {
    1: 'Underweight',
    2: 'Normal',
    3: 'Overweight',
    4: 'Obesity'
}
print('')
print('==============')
print('BMI CALCULATOR')
print('==============')
print('')
weight = float(input('Input your weight in kg: '))
heightcm = float(input('Input your height in cm: '))
heightm = heightcm/100
formula = round((weight/(heightm**2)),2)

if formula < 18.5:
    print('')
    print(f"Your BMI is {formula}\
          You are classified as {units[1]}")
elif formula >= 18.5 and formula <= 24.9:
    print('')
    print(f"Your BMI is {formula}\
          You are classified as {units[2]}")
elif formula >= 25 and formula <= 29.9:
    print('')
    print(f"Your BMI is {formula}\
          You are classified as {units[3]}")
else:
    print('')
    print(f"Your BMI is {formula}\
          You are classified in {units[4]}")
print('')