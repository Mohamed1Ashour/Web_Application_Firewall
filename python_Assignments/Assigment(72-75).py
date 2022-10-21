# --------------------------------TASK1------------------------
# def remove_chars(remove):
#     return (remove[1:-1])


# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# for names in map(remove_chars, friends_map):
#     print(names)

# print("-" * 20)

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# for names in map((lambda remove: (remove[1:-1])), friends_map):
#     print(names)
# --------------------------------TASK2------------------------
# def get_names(names):
#     if names[-1] == "m":
#         return names


# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
# myp = filter(get_names, friends_filter)
# for n in myp:
#     print(n)
# --------------------------------TASK3------------------------
# from functools import reduce


# def multiply(num1, num2):
#     return (num1*num2)


# nums = [2, 4, 6, 2]
# cic = reduce(multiply, nums)
# print(cic)
# --------------------------------TASK4------------------------
# skills = reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript"))
# word_with_count = enumerate(skills, 50)
# for count, stringg in word_with_count:
#     if type(stringg) == int:
#         continue
#     else:
#         print(f"{count} - {stringg}")
