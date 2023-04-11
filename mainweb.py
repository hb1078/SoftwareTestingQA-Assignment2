from flask import Flask, render_template, request
app = Flask(__name__)

#gets user input for feet part of height
def h_feet_input():
    h_feet = float(request.form['h_feet'])
    return (h_feet)

#gets user input for inches part of height
def h_inches_input():
    h_inches = float(request.form['h_inches'])
    return (h_inches)

#gets user input for weight in pounds
def p_weight_input():
    p_weight = float(request.form['p_weight'])
    return (p_weight)

#large function that calculates bmi
def bmi_calc(h_feet, h_inches, p_weight):

    status = None

    #calculations for converting measurements into metric/usable numbers for bmi calculation
    k_weight = p_weight * 0.45

    total_inches_height = (h_feet*12 + h_inches)

    h_meters = total_inches_height * 0.025

    h_meters_squared = h_meters*h_meters

    bmi = k_weight / h_meters_squared

    #if/elif statements to print results depending on inputs
    if round(bmi, 1) < 18.5:
        status = "Underweight"

    elif round(bmi, 1) >= 18.5 and round(bmi, 1) < 25:
        status = "Normal"

    elif round(bmi, 1) >= 25 and round(bmi, 1) < 30:
        status = "Overweight"

    elif round(bmi, 1) >=30:
        status = "Obese"

    return status

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        h_feet = h_feet_input()
        h_inches = h_inches_input()
        p_weight = p_weight_input()
        status = bmi_calc(h_feet, h_inches, p_weight)
        k_weight = p_weight * 0.45
        total_inches_height = (h_feet*12 + h_inches)
        h_meters = total_inches_height * 0.025
        h_meters_squared = h_meters * h_meters
        bmi = k_weight / h_meters_squared
        return render_template('bmi_result.html', status=status, bmi=round(bmi, 1))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
