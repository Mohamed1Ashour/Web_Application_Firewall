# ------------------------TASK1---------------------------
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secound number: "))
operator = input(
    "enter your operarot (\'+\' \'-\' \'*\' \'/\' \'%\') ").strip()
if operator == "+":
    print(f"result = {num1 + num2}")
elif operator == "-":
    print(f"result = {num1 - num2}")
elif operator == "*":
    print(f"result = {num1 * num2}")
elif operator == "/":
    print(f"result = {num1 / num2}")
elif operator == "%":
    print(f"result = {num1 % num2}")
else:
    print("undefined operator ")
print("-" * 60)
# ------------------------TASK2---------------------------
age = int(input("what\'s your age:: "))
print('"App Is Suitable For You"') if age >= 16 else print(
    '"App Is Not Suitable For You"')
print("-" * 60)
# ------------------------TASK3---------------------------
agee = int(input("enter your age: "))
if agee > 10 and agee < 100:
    month = agee*12
    week = month*4
    day = week*7
    hours = day*24
    min = hours*60
    sec = min*60
    print(f"your age in month is: {month:,}")
    print(f"your age in week is: {week:,}")
    print(f"your age in day is: {day:,}")
    print(f"your age in hours is: {hours:,}")
    print(f"your age in min is: {min:,}")
    print(f"your age in sec is: {sec:,}")
else:
    print("oPP\'s your age out of rang")
print("-" * 60)
# ------------------------TASK4---------------------------
country = input("Enter Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA",
             "USA", "Bahrain", "England"]
price = 100
discount = 0.30
if country in countries:
    print(
        f"Because you are from {country} you have 30% discount, so the price is ${int(price * discount)} ")
else:
    print("we don\'t dilever to this area")
print("-" * 60)
