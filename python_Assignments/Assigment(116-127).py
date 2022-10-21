# # --------------------------------TASK1--------------------------------
# import sqlite3
# Data = """
# 1)text
# 2)Integer
# 3)Data/Time
# 4)Byte
# 5)Hyperlink
# """
# # --------------------------------TASK(2,3)--------------------------------
# db = sqlite3.connect("Ashour.db")
# cr = db.cursor()
# # creat table with 4 row
# cr.execute("create table if not exists Users (user_id integer unique, name text unique, user_Birthday integer unique, user_mail text unique)")
# db.commit()  # to save all changes
# index_numbers = [0, 1, 2, 3, 4]
# ids = [1, 2, 3, 4, 5]
# names = ["Ahmed", "Sayed", "Gamal", "Mahmoud", "Sameh"]
# brithday = ["20/10/1980", "20/10/1990", "5/10/1951", "9/10/1987", "8/11/2000"]
# mail = ["Ahmed@Elzero.org", "Sayed@Elzero.org",
#         "Gamal@Elzero.org", "Mahmoud@Elzero.org", "Sameh@Elzero.org"]
# for NUM in index_numbers:
#     try:
#         cr.execute(
#             f"insert into Users(user_id,name,user_Birthday, user_mail) values ('{ids[NUM]}','{names[NUM]}','{brithday[NUM]}','{mail[NUM]}')")
#     except:
#         print("its aready exists")
# db.commit()
# print("-" * 20)
# # --------------------------------TASK4--------------------------------
# # cr.execute("select * from Users")
# # # result is touple used index to find the last
# # result = cr.fetchall()
# # print(result[4])
# # --------------------------------TASK5--------------------------------
# userr_id = int(input("Enter the ID: "))
# if userr_id in ids:
#     cr.execute(f"delete from Users where user_id = {userr_id}")
#     cr.execute("select * from Users")
#     resultt = cr.fetchall()
#     for one_row in resultt:
#         print(
#             f"ID ==> {one_row[0]}, Name ==> {one_row[1]}, Date of Birthday ==> {one_row[2]}, Email ==> {one_row[3]}")
# else:
#     print("User Not Found")
