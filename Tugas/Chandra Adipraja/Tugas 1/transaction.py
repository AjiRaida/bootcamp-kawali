#mengenai transaksi

transaction = []

def showTransaction(username = 'admin'):
    if username == 'admin':
        print(transaction)
    else:
        for i  in range(len(transaction)):
            if transaction[i - 1]['user'] == username:
                print(transaction[i - 1])

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