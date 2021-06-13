print("Enter your name:\n")
n = str(input())
print("Enter your weight (in pounds):\n")
w = float(input())
print("Enter your heigh:\n")
h = float(input())
BMI = w/(h**2)*703

print(str(n) + ", your BMI is:" + str(BMI))
