# ------------------------TASK1---------------------
print(bool(100 == 100))
print(bool(100 == 100.00))
print(bool(200 > 100))
print(bool(100 < 300))
print(not bool(100 != 100))
print(bool(100 == 200))
print(bool(100 == 110.00))
print(bool(200 > 400))
print(bool(100 < 50))
print(not bool(100 == 100))
print("-" * 60)
# ------------------------TASK2---------------------
html = 80
css = 60
javascript = 70
print(bool(html > 50 and css > 50 and javascript > 50))
print("-" * 60)
# ------------------------TASK3---------------------
numone = 10
numtwo = 20
num = 20
print(bool(num > numtwo or num > numone))
print(bool(num > numtwo and num > numone))
print("-" * 60)
# ------------------------TASK4---------------------
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
print(result ** 3)
print((result ** 3) % 26000)
print(((result ** 3) % 26000)/5)
print(type(str(result)))
