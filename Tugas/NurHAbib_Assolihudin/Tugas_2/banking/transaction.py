# File ini berisi segala sesuatu mengenai transaksi
import json

# Import

# Variable
data_transaction = open("data/transactions.txt")
transaction = data_transaction.read()
transaction = json.loads(transaction)
data_transaction.close()

# Function
def showTransaction(username = "admin"):
    jml_transaksion = 0
    if transaction == []:
        print("Maaf belum terdapat transaksi")
    else:
        if username == "admin":
            for i in range(len(transaction)):
                print(transaction[i]["user"], transaction[i]["to"], transaction[i]["jumlah transfer"], transaction[i]["tipe transfer"])
        else:
            for i in range(len(transaction)):
                if transaction[i]["user"] == username:
                    jml_transaksion += 1
                    print("-------------------")
                    print(transaction[i]["user"])
                    print(transaction[i]["to"])
                    print(transaction[i]["jumlah transfer"])
                    print(transaction[i]["tipe transfer"])
            if jml_transaksion == 0:
                print("Maaf anda belum memiliki histori transaksi")

def transfer(username, to, uang):
    transaction.append(
        {
            "user": username,
            "to": to,
            "jumlah transfer": uang,
            "tipe transfer": "Transfer"
        }
    )
    json_transaction = json.dumps(transaction)
    data_transaction = open("data/transactions.txt", "w")
    data_transaction.write(json_transaction)
    data_transaction.close()

def deposit(username, uang):
    transaction.append(
        {
            "user" : username,
            "to" : "self",
            "jumlah transfer" : uang,
            "tipe transfer" : "Deposito"
        }
    )
    json_transaction = json.dumps(transaction)
    data_transaction = open("data/transactions.txt", "w")
    data_transaction.write(json_transaction)
    data_transaction.close()

def tarikTunai(username, uang):
    transaction.append(
        {
            "user": username,
            "to": "self",
            "jumlah transfer": uang,
            "tipe transfer": "Tarik Tunai"
        }
    )
    json_transaction = json.dumps(transaction)
    data_transaction = open("data/transactions.txt", "w")
    data_transaction.write(json_transaction)
    data_transaction.close()

def deletTransaction(username):
    for t in transaction:
        if t["user"] == username:
            transaction.remove(username)
    json_transaction = json.dumps(transaction)
    data_transaction = open("data/transactions.txt", "w")
    data_transaction.write(json_transaction)
    data_transaction.close()