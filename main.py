user_pass = {"Vuyani": "Vuya@2021", "Atheelah": "maroon17", "Ikraam": "carsthemovie", "Nathan": "blue1",
             "Amanda": "@amanda28"}

user = input("enter your username")
password = input("enter your password")


def user_pass_search(username, _password, _dict):
    if username in _dict:
        if _password == _dict[username]:
            return 1
        else:
            return 0
    else:
        return -1


x = int(user_pass_search(user, password, user_pass))
print(" ")
if x == 1:
    print("Your details are Correct")
elif x == 0:
    print("Incorrect Password")
elif x == -1:
    print("Username Dousn't Exist")
