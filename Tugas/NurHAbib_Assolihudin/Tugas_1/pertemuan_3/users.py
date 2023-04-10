# Di dalam file ini terdapat system penambahan dan pengambilan user

# Import

# Variable
users = [
    {
        "username" : "nurhabib@gmail.com",
        "password" : "1234",
        "role" : "admin",
        "saldo" : 0
    }
]

current_user = {}

# Function
def login(**data_user):
    for i in range(len(users)):
        if data_user["username"] == users[i - 1]["username"]:
            if data_user["password"] == users[i - 1]["password"]:
                role = users[i - 1]["role"]
                if role == "admin":
                    return "lamanAdmin"
                elif role == "customor":
                    return "lamanCustomor"

def addUser(**data_user):
    username_users = []
    for i in range(len(users)):
        username_users.append(users[i-1]["username"])

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
        print("Data Berhasil Ditambahkan")


def deleteUser(username):
    for i in range(len(users)):
        if username == "nurhabib@gmail.com":
            print("Maaf tidak bisa menghapus user default")
        elif users[i]["username"] == username:
            id_user = i
            users.remove(id_user)
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