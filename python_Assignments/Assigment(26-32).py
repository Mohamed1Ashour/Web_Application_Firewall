# ------------------------TASK1------------------------
mylist = [1, 2, 3, 3, 4, 5, 1]
unique_list = [5, 4, 2]
print(unique_list)
print(type(unique_list))
print(unique_list[0:2:1])
print("-" * 60)
# ------------------------TASK2------------------------
myset = {1, 2, 3}
myset1 = {"A", "b", "C"}
first = (myset | myset1)
myset.update(myset1)
third = myset.union(myset1)
print(first, "\n", myset, "\n", third)
print("-" * 60)
# ------------------------TASK3------------------------
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.update("A", "B")
print(my_set)
print("-" * 60)
# ------------------------TASK4------------------------
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("-" * 60)
# ------------------------TASK5------------------------
mohamed = {
    "HTML": "progress is 90%",
    "Python": "progress is 20%",
    "c++": "progress is 25%"
}
mohamed.update({"CCNA": "progress is 60%"})
print("HTMAL", mohamed["HTML"])
print("Python", mohamed["Python"])
print("c++", mohamed["c++"])
print("CCNA", mohamed["CCNA"])
