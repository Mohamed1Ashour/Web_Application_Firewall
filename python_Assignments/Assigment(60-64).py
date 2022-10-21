# --------------------------------------TASK1-----------------------------
# def iget_score(**score):
#     for x, y in score.items():
#         print(f"{x} ==> {y}")


# iget_score(Math=90, Science=80, Language=70)
# print("-" * 20)


# def get_score(**scores):
#     for z in scores:
#         print(f"{z} ==> {scores[z]}")


# get_score(Logic=70, Problems=60)
# print("-" * 20)
# --------------------------------------TASK2-----------------------------
# def test1(name="", **skills1):
#     if len(name) == 0:
#         for s1 in skills1:
#             print(f"-{s1} ==> {skills1[s1]}")
#     elif len(skills1) == 0:
#         print(f"hello {name} your skills is")
#         print("no skills yet!")
#     else:
#         print(f"hello {name} your skills is")
#         for s1 in skills1:
#             print(f"-{s1} ==> {skills1[s1]}")


# test1("Ashour", Math=90, Science=80, Language=70)
# print("-"*20)


# def test2(names="", **skills2):
#     if len(names) == 0:
#         for s2 in skills2:
#             print(f"-{s2} ==> {skills2[s2]}")
#     elif len(skills2) == 0:
#         print(f"hello {names} your skills is")
#         print("no skills yet!")
#     else:
#         print(f"hello {names} your skills is")
#         for s2 in skills2:
#             print(f"-{s2} ==> {skills2[s2]}")


# test2(Logic=70, Problems=60)
# print("-"*20)


# def test3(**skills3):
#     if len(skills3) == 0:
#         print("No skills yet!")
#     else:
#         c = 1
#         for s3 in skills3:
#             print(f"({c}) {s3} ==> {skills3[s3]}")
#             c += 1


# test3(Logic=70, Problems=60)
# print("-"*20)


# def test4(namme=""):
#     if namme == 0:
#         print("unkown person")
#     else:
#         print(f"Hello {namme}")


# test4("Ahmed")
# print("-"*20)
# --------------------------------------TASK3-----------------------------
# mydic = {
#     "Math": "90",
#     "Science": "80",
#     "language": "70"
# }


# def my_function(nname="", **cv):
#     c = 1                                         # local varible
#     if nname == 0:
#         for o in cv:
#             print("your skills is")
#             print(f"{(c)} {o} ==> {cv[o]} ")
#             c += 1
#     elif cv == 0:
#         print(f"hello {nname} no skills yet!")
#     else:
#         print(f"hello {nname} your skills is")
#         for l in cv:
#             print(f"{(c)} {l} ==> {cv[l]} ")
#             c += 1


# my_function(**mydic)
