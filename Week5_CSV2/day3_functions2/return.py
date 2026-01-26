# The retrun keyword can be used only within a function


sales = [261.96, 731.94, 14.62, 957.5, 1706.18, 95, 43, 17, 48, 71, 54, 63]

def calcualte_average(values):
    sales_count = len(values)
    total_sales = sum(values)

    average = total_sales / sales_count

    print("\nWhat is average?", average)

    return average

result = calcualte_average(sales)
print("The avearage value of sales for the month of December 2025 was {result}")

print("*************************************************************")
# Muliple Returns
# A function can have muliple return statements
print("*************************************************************")

def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index (BMI)"""
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_catgeory(bmi):
    """Get BMI category as a string"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
height = 1.75
weight = 70


bmi_value = calculate_bmi(weight, height)
category = get_bmi_catgeory(bmi_value)

print(f"\nHeight: {height}")
print(f"\nWeight: {weight}")
print(f"\nBMI: {bmi_value:.1f}")
print(f"Category: {category}")
