# ------------------------TASK1-------------------------------------
name = input("whats your name:")
print(f"hello {name.strip().capitalize()} , Happy to see you")
print("-" * 60)
# ------------------------TASK2-------------------------------------
age = float(input("enter your age: "))
if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
print("-" * 60)
# ------------------------TASK3-------------------------------------
firstname = input("whats your first name:") .strip().capitalize()
secoundnamed = input("whats your secound name:") .strip().capitalize()
thirdnamed = input("whats your third name:") .strip().capitalize()
print(f"Hello {firstname} {secoundnamed:.1s}.{thirdnamed}")
print("-" * 60)
# ------------------------TASK3-------------------------------------
email = (input("write your email: ")).strip().lower()
namee = email[:email.index("@")].capitalize()
Service_Provider = email[email.index("@")+1:email.index(".")]
Domain = email[email.index(".")+1:]
print(
    f"your user name is:: {namee} \nyour service provider is:: {Service_Provider} \n your domain is:: {Domain}")
print("-" * 60)
