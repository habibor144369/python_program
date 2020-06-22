#  Login Form program with database connection.........

print("******Welcome to Sk Data System******")
get = int(input("What do you want!!? for SinUp Press 1 or Login press 0: "))
database = {}
c = {}

def update_database():
    # Create text File in same Directory as Name of data.txt
    with open("data.txt") as ref:
        for line in ref:
            key, value = line.strip().split(",")
            c[key] = int(value)
            database.update(c)


def singUp(user_name, password, database):
    update_database()

    for i in database.keys():

        if (i == user_name):
            print(user_name, "not valuable Please try with other User Name")
            sing_input()
            break
    else:
        newdata = open("data.txt", "a")
        newdata.write('%s , %d \n' % (user_name, password))
        print("singUp successfully ")
        newdata.close()
        update_database()
        login_input()


def login(user_name, password, database):
    update_database()
    for i in database.keys():
        if (i == user_name):
            if (password == database[i]):
                print("login Successfully")
                break
            else:
                print("Password is incorrect & Please try again")
                login_input()
                break

    if (user_name in database.keys()):
        pass

    else:
        print("User Name is incorrect & Please try again")
        login_input()


def sing_input():
    print("please input your Data for SinUp")
    user_name = input("Please input User Name: ")
    password = int(input("Please input Password: "))
    singUp(user_name, password, database)


def login_input():
    print("please input your Data for Login")
    user_name = input("Please input User Name: ")
    password = int(input("Please input Password: "))
    login(user_name, password, database)

if (get == 1):
    sing_input()

elif (get == 0):
    login_input()


