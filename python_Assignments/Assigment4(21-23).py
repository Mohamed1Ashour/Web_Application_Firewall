# -----------------TASK1--------------------------
frind = ["Osama", "Mohamed", "Ashour", "Ayman", "Mahmoud"]
print(frind[0])
print(frind.pop(0))
print(frind[3])
print(frind.pop(3))
print("----------------------------------------------------")
# -----------------TASK2----------------------------
frinds = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(frinds[0::2])
print(frinds[1:4:2])
print("----------------------------------------------------")
# -----------------TASK3----------------------------
friendss = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friendss[1:4:1])
print(friendss[3:5])
print("----------------------------------------------------")
# -----------------TASK4----------------------------
friendsss = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friendsss[3:5] = ["ELZERO", "ELZERO"]
print(friendsss)
print("----------------------------------------------------")
# -----------------TASK5----------------------------
frieends = ["Osama", "Ahmed", "Sayed"]
frieends.insert(0, "Nasser")
print(frieends)
frieends.insert(4, "Salem")
print(frieends)
print("----------------------------------------------------")
# -----------------TASK6----------------------------
frriends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
frriends.remove("Nasser")
frriends.remove("Osama")
print(frriends)
frriends.remove("Salem")
print(frriends)
print("----------------------------------------------------")
# -----------------TASK7----------------------------
ffriends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
ffriends.extend(employees)
print(ffriends)
ffriends.extend(school)
print(ffriends)
print("----------------------------------------------------")
# -----------------TASK8----------------------------
friiends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friiends.sort()
print(friiends)
friiends.sort(reverse=True)
print(friiends)
print("----------------------------------------------------")
# -----------------TASK9----------------------------
fffriends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(fffriends))
print("----------------------------------------------------")
# -----------------TASK10----------------------------
mylist = ["Html", "CSS", "JS", "Python"]
list = ["Django", "Flask", "Web"]
mylist.append(list)
print(mylist)
print(mylist[4][0])
print(mylist[4][2])
print("----------------------------------------------------")
