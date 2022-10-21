# -------------------------------------------------TASK1--------------------------------------------
# values = (0, 1, 2)

# if any(values):  # law fe haga wa7da bas aw akter true fe (values) khosh----fe hagtan true fa hykhosh

#     my_var = 0

# # list feha shwayt arkam we feha list tany we feha zero bta3 my_var
# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# # 1) law fe (my_list) mn index 0-4 true khosh(true)
# # 2) law fe (my_list) mn index 0-6 true khosh (false)
# # 3) law fe (my_list) mn awel-akher true khosh (false)
# # bas hwa haykhosh 3ashan ahna 3amlnha or(law feh shart wa7et true khosh we dh rakm 1)
# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

#     print("Good")  # run

# else:

#     print("Bad")
# -------------------------------------------------TASK2--------------------------------------------
# v = 40
# my_range = list(range(v))
# print(sum(my_range, v) + pow(v, v, v))  # 820
# # sum batgm3 kull al iteration aly gwa fa lazem yakon masln list aw touple
# # al v haykon rakm,,,my range howa mahtot ano list we al v deh hatkon (end) l2no egbary taktbha we zero haya start
# # khaly balk ((v**v)%v) =0 "grbtha" kda goz2 tany mn conc hayter
# # fe sum lma bygy yagm3 list m3 rakm ,,,bayd8l al rakm dh gwa al list we bygm3 kolo m3 ba3do
# # kda 2der 22ol an magmo3 mn zero le had al (V-1) + v = 820 y3ny mn al akher kda 0+1+2+3....+(v-1)+v=820
# # aw bardo 22dr aa'ol 0+1+2+3+4....+v=820
# # ya3ny ana b7awel adwer 3la equation law adetha rakm,,,trg3ly mgmo3 al arkam mn zero le had al rakm aly adetholha
# # equation deh haya ((v(v+1))/2) = 820 ===> "google"
# #  v = +40 aw bardp v = -41(refused)
# -------------------------------------------------TASK3--------------------------------------------
# n = 21

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):  # max = 10

#     print("Good")  # Output => Good

# awel haga 3and varible l baysawy list mn 0-(n-1)
# 3and condation bay2ol law 3amlt gam3 ll list deh (0+1+2+3+...(n-1)/n) == 10
# -1 hyter m3 1 fa hatkon (2+3+4+----n) ===> dawr 3la function bat3ml kda
# round hat2rb al rakm fa kda al max l2ma 9.>5  l2ma  11.<5
# kda ana badwr 3la equation adeha rakm tdeny 0+1+2+3+4....(rakm dh - 1) we ba3deha 22smha 3la al rakm dh tdeny rakm 2oryab mn al 10
# equation:: ((n(n-1))/2/n) = 10 law tal3 rakm we nta 3wat tany fe al equation we tl3lk haga 2otyba mn 10 haykon sa7 l2n hwa 3aml fo2 round
# -------------------------------------------------TASK4--------------------------------------------
# def my_all(all):
#     sum = 0
#     for x in all:
#         if bool(x):
#             sum += 1
#     if sum == len(all):
#         return (True)
#     else:
#         return (False)


# print(my_all([1, 2, 3]))  # True
# print(my_all([1, 2, 3, []]))  # False
# ................................................
# def my_any(any):
#     summ = 0
#     for x in any:
#         if bool(x):
#             summ += 1
#     if summ >= 1:
#         return (True)
#     else:
#         return (False)


# print(my_any([0, 1, [], False]))  # True
# print(my_any([(), 0, False]))  # False
# ................................................
# def my_min(min):
#     cun = 0
#     for m in min:
#         if cun > m:
#             cun = m
#         else:
#             continue
#     return (cun)


# print(my_min([10, 100, -20, -100, 50]))  # -100
# print(my_min((10, 100, -20, -100, 50)))  # -100
# ................................................
# def my_max(max):
#     cunn = 0
#     for ma in max:
#         if cunn < ma:
#             cunn = ma
#         else:
#             continue
#     return (cunn)


# print(my_max([10, 100, -20, -100, 50, 700]))  # 700
# print(my_max((10, 100, -20, -100, 50, 700)))  # 700
