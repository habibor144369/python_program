user_name = str(input("Enter the value of name: "))
Password = int(input("Please press your password: "))
user = {'Thomas': 144369, 'Alva': 137022}

for i in user.keys():
    if (i == user_name):
        for x in user.values():
            if (Password == user[i]):
                print("login successfully")
                break
            else:
                print("password is incorrect, please try again")
                break
if (user_name in user.keys()):
    pass
else:
    print("user name is incorrect please correct name press please:")
