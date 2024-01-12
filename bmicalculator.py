#Beginner level BMI Calculator project

def BMI_calculator(weight, height):
    
    calculator = (weight/height**2)
    if calculator  < 18.5:
        return "OH No! You are Underweight, Go to gym and become healthy"
    elif calculator >= 18.5 and calculator  < 25:
        return "You Are Healthy, Normal"
    elif calculator >= 25 and calculator  < 30:
        return "OH.. You are Overweight"
    elif calculator >= 30:
        return "OH.. Noo.. You are Obesity"
    else:
        return "The Weight Must Be An Integer And Height In Decimal"
    
if __name__ == '__main__':
    weight = int(input("Enter Your Weight in KiloGrams: "))
    height = float(input("Enter Your Height in Meters: "))
    result = BMI_calculator(weight,height)
    print(result)