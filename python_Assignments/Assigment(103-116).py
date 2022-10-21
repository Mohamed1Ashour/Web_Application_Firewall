# -----------------------------------TASK1-------------------------------------
# class Game:
#     def __init__(self, game_name, game_developer, price_in_pounds, game_year):
#         self.gamename = game_name
#         self.gamedeveloper = game_developer
#         self.price = price_in_pounds
#         self.year = game_year

#     def info_game(self):
#         print(f"Game Name Is \"{self.gamename}\", ", end=" ")
#         print(f"Developer Is \"{self.gamedeveloper}\", ", end=" ")
#         print(f"Release Date Is \"{self.year}\", ")
#         print(f"Price In Egypt Is {self.price}", end=" ")


# games = Game("Ys", "Falcom", 50, 2010)
# print(games.info_game())
# -----------------------------------TASK2-------------------------------------
# class User:
#     def __init__(self, name, namee, agee, gender):
#         self.fname = name
#         self.sname = namee
#         self.age = agee
#         self.gender = gender

#     def hello(self):
#         years = 40-self.age
#         x = str(years)
#         y = x.zfill(2)
#         if self.gender == "Male":
#             print(
#                 f"hello Mr: {self.fname} {self.sname:.1s}. [{y}] Years To Reach 40")

#         elif self.gender == "Female":
#             print(
#                 f"hello Ms: {self.fname} {self.sname:.1s}. [{y}] Years To Reach 40")

#         else:
#             print(
#                 f"hello : {self.fname} {self.sname:.1s}. [{y}] Years To Reach 40")


# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.hello())
# print(user_two.hello())
# -----------------------------------TASK3-------------------------------------
# class Message:
#     def __init__():
#         print("Hello From Class Message")


# print(Message.__init__())
# -----------------------------------TASK4-------------------------------------
# class Games:
#     def __init__(self, g1):
#         self.g1 = g1

#     def game(self):
#         print(f"I Have One Game Called {self.g1}")


# class Gamess:
#     def __init__(self, g1, g2, g3):
#         self.g1 = g1
#         self.g2 = g2
#         self.g3 = g3

#     def games(self):
#         print("I have many games")
#         print(f"{self.g1}\n{self.g2}\n{self.g3}")


# class counttt:
#     def __init__(self, count):
#         self.Count = count

#     def count_game(self):
#         print(f"I Have {self.Count} Game")


# user_one = Games("Shadow Of Mordor")
# print(user_one.game())
# print("-" * 20)
# user_two = Gamess("Ys II", "Ys Oath In Felghana", "YS Origin")
# print(user_two.games())
# print("-" * 20)
# user_games_count = counttt("80")
# print(user_games_count.count_game())
# -----------------------------------TASK5-------------------------------------
