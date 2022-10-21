# ----------------------------------------TASK1-----------------
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# x = 1
# for num in my_nums:
#     if num % 5 == 0:
#         print(f"{x} ===> {num}")
#         x += 1
#     else:
#         continue
# print("ALL LOOP IS DONE")
# print("-"*20)
# ----------------------------------------TASK2-----------------
# mylist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
#           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
# for nums in mylist:
#     if nums == "6" or nums == "8" or nums == "12":
#         continue
#     else:
#         print(nums.zfill(2))
# ----------------------------------------TASK3-----------------
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# for grade in my_ranks:
#     if my_ranks[grade] == "A":
#         print(
#             f"My Grade in \'{grade}\' is {my_ranks[grade]} This Equal 100 Points")
#         print("-" * 20)
#     elif my_ranks[grade] == "B":
#         print(
#             f"My Grade in \'{grade}\' is {my_ranks[grade]} This Equal 80 Points")
#         print("-" * 20)
#     else:
#         print(
#             f"My Grade in \'{grade}\' is {my_ranks[grade]}This Equal 40 Points")
#         print("-" * 20)
# ----------------------------------------TASK4-----------------
# students = {
#     "Ahmed": {
#         "Math": "A",
#         "Science": "D",
#         "Draw": "B",
#         "Sports": "C",
#         "Thinking": "A"
#     },
#     "Sayed": {
#         "Math": "B",
#         "Science": "B",
#         "Draw": "B",
#         "Sports": "D",
#         "Thinking": "A"
#     },
#     "Mahmoud": {
#         "Math": "D",
#         "Science": "A",
#         "Draw": "A",
#         "Sports": "B",
#         "Thinking": "B"
#     }
# }

# for names in students:
#     print("-" * 20)
#     print(f"student name ==> {names}")
#     print("-" * 20)
#     for subject in students[names]:
#         if students[names][subject] == "A":
#             print(f"{subject} ==> {students[names][subject]} = 100 points")
#         elif students[names][subject] == "B":
#             print(f"{subject} ==> {students[names][subject]} = 80 points")
#         elif students[names][subject] == "c":
#             print(f"{subject} ==> {students[names][subject]} = 40 points")
#         else:
#             print(f"{subject} ==> {students[names][subject]} = 20 points")
