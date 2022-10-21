# -------------------------TASK1---------------------------------------
# num1 = int(input("first number: "))
# num2 = int(input("secound number: "))
# operation = input("Add, Subtract, Multiply: ").strip().capitalize()


# def calcoulator(n1, n2, op="A"):
#     if op == "Add" or op == "A":
#         print(f"result = {n1 + n2}")
#     elif op == "Subtract" or op == "S":
#         print(f"result = {n1 - n2}")
#     elif op == "Multiply" or op == "M":
#         print(f"result = {n1 * n2}")
#     else:
#         print("undefine operation")


# if operation == "":
#     calcoulator(num1, num2)
# else:
#     calcoulator(num1, num2, operation)
# print("-" * 20)
# -------------------------TASK2---------------------------------------
# num = []
# a = 0
# c = 1
# while a < 5:
#     numms = int(input(f"{c} numbrs: " if c < 5 else "enter the last number: "))
#     num.append(numms)
#     a += 1
#     c += 1
# else:
#     print("-" * 20)
#     print("thank you")
#     print("-" * 20)
# print(num)
# print("-" * 20)


# def addition(*numbers):
#     total = 0
#     for nnum in numbers:
#         if nnum == 10:
#             continue
#         elif nnum == 5:
#             total -= nnum
#         else:
#             total += nnum
#     return (total)


# for x in num:
#     addition(x)
# print(addition)
# print("-" * 20)
# -------------------------TASK3---------------------------------------
# def skill(name, *skills):
#     if len(skills) == 0:
#         print(f"you don\'t have skills {name}")
#     else:
#         print(f"hello {name} your skills is")
#         for x in skills:
#             print(x)
# skill("Osama")
# print("-" * 20)
# -------------------------TASK3---------------------------------------
# def hello(name="unkown", age="unkown", country="unkown"):
#     print(f"hello {name} your age is {age} you are from {country}")
# print("-" * 20)
# -------------------------TASK3---------------------------------------
