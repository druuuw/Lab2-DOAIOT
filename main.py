print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print(bmi)
    if bmi < 18.5:
        print("Underweight")
    elif bmi > 25:
        print("Obese")
    else:
        print("Normal")


calculate_bmi(height=1.73,weight=57)
