# File ini berisi segala sesuatu mengenai transaksi

# Import

# Variable
transaction = []

# Function
def showTransaction(username = "admin"):
    if username == "admin":
        for i in range(len(transaction)):
            print(transaction[i]["user"], transaction[i]["to"], transaction[i]["jumlah transfer"], transaction[i]["tipe transfer"])
    else:
        for i in range(len(transaction)):
            if transaction[i]["user"] == username:
                print("-------------------")
                print(transaction[i]["user"])
                print(transaction[i]["to"])
                print(transaction[i]["jumlah transfer"])
                print(transaction[i]["tipe transfer"])

def transfer(username, to, uang):
    transaction.append(
        {
            "user": username,
            "to": to,
            "jumlah transfer": uang,
            "tipe transfer": "Transfer"
        }
    )

def deposit(username, uang):
    transaction.append(
        {
            "user" : username,
            "to" : "self",
            "jumlah transfer" : uang,
            "tipe transfer" : "Deposito"
        }
    )

def tarikTunai(username, uang):
    transaction.append(
        {
            "user": username,
            "to": "self",
            "jumlah transfer": uang,
            "tipe transfer": "Tarik Tunai"
        }
    )