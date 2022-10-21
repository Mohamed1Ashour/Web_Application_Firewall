# --------------TASK1----------------------------------------
name = "'Mohamed Ashour'"
age = ' "23 years old"" '
country = "zhraa"
print('"Hello' + " " + name + " " + "How you Doing" +
      " " + "\\" + '"""' + " Your Age Is:" + age + "+" + "And Your Country is: " + country)
print("------------------------------------------------------------------------------------")
# --------------TASK2-----------------------------------------
namee = "'Mohamed Ashour'"
agee = ' "23 years old"" '
countryy = "zhraa"
print('"Hello' + " " + name + " " + "How you Doing" + " " + "\\" + "\n" +
      '"""' + " Your Age Is:" + age + "+" + "\n" + "And Your Country is: " + country)
print("------------------------------------------------------------------------------------")
# ---------------TASK3-----------------------------------------------
nameee = "ELZERO"
print("secound letter is:", nameee[1])
print("third letter is:", nameee[2])
print("last letter is:", nameee[5])
print("--------------------------------------------------------------------------------------")
# ---------------TASK4-----------------------------------------------
nameeee = "ELZERO"
print(nameeee[1] + nameeee[2] + nameeee[3])
print(nameeee[0] + nameeee[2] + nameeee[4])
print(nameeee[4] + nameeee[2] + nameeee[0])
print("--------------------------------------------------------------------------------------")
# ---------------TASK5-----------------------------------------------
namez = "#@#@Elzero#@#@"
print(namez.strip("#@"))
print("----------------------------------------------------------------")
# ---------------TASK6-----------------------------------------------
a = "9"
b = "15"
c = "130"
d = "950"
x = "1500"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))
print(x.zfill(4))
print("----------------------------------------------------------------")
# ---------------TASK7-----------------------------------------------
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
print("-----------------------------------------------------------------------")
# -----------------TASK8--------------------------------------------------------
name_1one = "OSamA"
name_2two = "osaMA"
print(name_1one.swapcase())
print(name_2two.swapcase())
print("-----------------------------------------------------------------------")
# -----------------TASK9--------------------------------------------------------
msg = "I Love Python And Although Love Elzero Web School"
print(msg.index("L"))
print("-----------------------------------------------------------------------")
# -----------------TASK10--------------------------------------------------------
nnname = "Elzero"
print(nnname.index("z"))
print("-----------------------------------------------------------------------")
# -----------------TASK11--------------------------------------------------------
mmsg = "I <3 Python And Although <3 Elzero Web School"
print(mmsg. replace("<3", "Love", 1))
print("-----------------------------------------------------------------------")
# -----------------TASK12--------------------------------------------------------
mssg = "I <3 Python And Although <3 Elzero Web School"
print(mssg. replace("<3", "Love", 2))
print("-----------------------------------------------------------------------")
# -----------------TASK13--------------------------------------------------------
na_me = "Mohamed Ashour"
a_ge = 23
cou_ntry = "Egypt"
print("my name is: {:s}, and my age is {:.2} and my country is {:s}".
      format(na_me, a_ge, cou_ntry))
print("-----------------------------------------------------------------------")
