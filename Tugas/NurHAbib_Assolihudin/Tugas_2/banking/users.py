# Di dalam file ini terdapat system penambahan dan pengambilan user
import json

# Import

# Variable
data_users = open("data/users.txt")
users = data_users.read()
users = json.loads(users)
data_users.close()

current_user = {}

# Function
def login(**data_user):
    for i in range(len(users)):
        if data_user["username"] == users[i]["username"]:
            if data_user["password"] == users[i]["password"]:
                for i in range(len(users)):
                    if data_user["username"] == users[i]["username"]:
                        current_user.update(
                            {
                                "id": i,
                                "username": users[i]["username"],
                                "password": users[i]["password"],
                                "role": users[i]["role"]
                            }
                        )
                        role = users[i]["role"]
                        if role == "admin":
                            return "lamanAdmin"
                        elif role == "customor":
                            return "lamanCustomor"


def addUser(**data_user):
    username_users = []
    for i in range(len(users)):
        username_users.append(users[i]["username"])

    if data_user["username"] in username_users:
        print("Maaf data telah ada di database")
    else:
        users.append(
            {
                "username" : data_user["username"],
                "password" : data_user["password"],
                "role" : data_user["role"],
                "saldo" : 0
            }
        )
        json_users = json.dumps(users)
        data_users = open("data/users.txt", "w")
        data_users.write(json_users)
        data_users.close()
        print("Data Berhasil Ditambahkan")


def deleteUser(username):
    for i in range(len(users)):
        if username == "nurhabib@gmail.com":
            print("Maaf tidak bisa menghapus user default")
        elif users[i]["username"] == username:
            id_user = i
            users.pop(id_user)
            json_users = json.dumps(users)
            data_users = open("data/users.txt", "w")
            data_users.write(json_users)
            data_users.close()
            print("User behasil dihapus")

def showUsers():
    for i in range(len(users)):
        print("--------------")
        print(users[i]["username"])
        print(users[i]["password"])
        print(users[i]["role"])
        print(users[i]["saldo"])

def lihatSaldo(username):
    for i in range(len(users)):
        if users[i]["username"] == username:
            print(users[i]["saldo"])