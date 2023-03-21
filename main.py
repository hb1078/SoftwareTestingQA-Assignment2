
def h_feet_input():
    h_feet = float(input("What is the feet part of your height? (example, if you're 5'10\", put 5\n"))
    return (h_feet)


def h_inches_input():
    h_inches = float(input("What is the inches part of your height? (example, if you're 5'10\", put 10\n"))
    return (h_inches)


def p_weight_input():
    p_weight = float(input("What is your weight in pounds?\n"))
    return (p_weight)


def bmi_calc(h_feet, h_inches, p_weight):
    k_weight = p_weight * 0.45

    total_inches_height = (h_feet*12 + h_inches)

    h_meters = total_inches_height * 0.025

    h_meters_squared = h_meters*h_meters

    bmi = k_weight / h_meters_squared

    if bmi < 18.5:
        print("You are underweight.")
        print("Your BMI is:", bmi)

    elif bmi >= 18.5 and bmi <= 24.9:
        print("You are normal weight.")
        print("Your BMI is:", bmi)

    elif bmi >= 25 and bmi <= 29.9:
        print ("You are overweight.")
        print("Your BMI is:", bmi)

    elif bmi >=30:
        print("You are obese.")
        print("Your BMI is:", bmi)


    return(bmi)

def main():
    h_feet = h_feet_input()
    h_inches = h_inches_input()
    p_weight = p_weight_input()

    bmi_calc(h_feet, h_inches, p_weight)

if __name__ == "__main__":
    main()