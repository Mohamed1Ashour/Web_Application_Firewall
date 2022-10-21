# ------------------TASK1---------------------
tupleee = ("osama", )
print(tupleee)
print(type(tupleee))
print("----------------------------------------------------------------")
# ------------------TASK2---------------------
friends = ("Osama", "Ahmed", "Sayed", )
y = list(friends)
y[0] = "ELZERO"
friends = tuple(y)
print(friends)
print(type(friends))
print(len(friends), "Elements")
print("----------------------------------------------------------------")
# ------------------TASK3---------------------
nums = (1, 2, 3)
letters = ("A", "B", "C")
sum = nums + letters
print(sum)
print(len(sum), "Elemmnts")
print("----------------------------------------------------------------")
# ------------------TASK4---------------------
my_tuple = (1, 2, 3, 4)
A, B, _, C = my_tuple
print(A)
print(B)
print(C)
print("----------------------------------------------------------------")
