from file_ops import write_to_file,read_file
import copy
_USER_FILE = ('users.txt')
_ACCOUNT_FILE = ('accounts.txt')
_TRANSAKSI_ = ('transaksi.txt')


users = read_file(_USER_FILE)
accounts = read_file(_ACCOUNT_FILE)
transaction = read_file(_TRANSAKSI_)
cUser = {}

def cekUser(users, username):
    for u in users:
        if u['username'] == username:
            return True
    return False
    
def cekTo(accounts, to):
    for a in range(len(accounts)):
        if accounts[a]['username'] == to:
            return True
    return False
    
def add_user(users, accounts):
    while True:
        username = input('Username : ')
        password = input('Password : ')
        while True:
            role = input('Role (1: admin, 2:customer) : ')
            if role == '1':
                role = 'admin'
                break
            elif role == '2':
                role = 'customer'
                break
        print("Masukan Role Yang Sesuai!")
        
        if cekUser(users, username) == False:
            users.append({
                'username' : username,
                'password' : password,
                'role' : role
            }),
            write_to_file(_USER_FILE,users)
            accounts.append({
                'username' : username,
                'amount' : 0,
            })
            write_to_file(_ACCOUNT_FILE, accounts)
            print('User berhasil di tambahkan!')
            return True
        else:
            print('Username sudah digunakan!')

def delete_user(users,transaction,accounts):
    for u in users:
        print(u['username'])

    while True:
        choice = input('Masukan username user : ')
        for u in users:
            if u['username'] == choice:
                users.remove(u)
                write_to_file(_USER_FILE,users)
                for a in accounts:
                    if a['username'] == choice:
                        accounts.remove(a)
                        write_to_file(_ACCOUNT_FILE,accounts)
                b = copy.copy(transaction)
                for t in b:
                    if t['username'] == choice:
                        transaction.remove(t)
                        write_to_file(_TRANSAKSI_,transaction)
                print('Remove Succes')
                return True
            
# def delete_trx(users,transaction):
#     for t in range(len(transaction)):
#         if transaction[t]['username'] == users:
#             transaction.pop(t)
#             write_to_file('transaction.txt', transaction)

def show_users(users):
    for u in users:
        print(u['username'])

def admin():
    pass

def show_balance(accounts, username):
    for u in accounts:
        if u['username'] == username:
            print("Your Balance : ", int(u['amount']))

def withdraw(accounts, transaction, username):
    amount = input('Masukkan jumlah withdraw : ')
    for a in range(len(accounts)):
        if accounts[a]['username'] == username:
            if accounts[a]['amount'] - int(amount) >= 0:
                accounts[a]['amount'] -= int(amount)
                write_to_file(_ACCOUNT_FILE,accounts)
                transaction.append(
                    {
                        'username':username,
                        'to': 'self',
                        'amount': int(amount),
                        'type': 'deposit',
                    }
                )
                write_to_file(_TRANSAKSI_, transaction)
                print("Penarikan Berhasil")
            else:
                print('Maaf, Saldo kamu tidak cukup!')

def deposit(accounts, transaction, username):
    amount = input('Masukkan jumlah deposit : ')
    for a in range(len(accounts)):
        if accounts[a]['username'] == username:
            accounts[a]['amount'] += int(amount)
            write_to_file(_ACCOUNT_FILE,accounts)
            transaction.append(
                {
                    'username':username,
                    'to': 'self',
                    'amount': int(amount),
                    'type': 'deposit',
                }
            )
            print('Saldo berhasil di tambahkan!')
            write_to_file(_TRANSAKSI_, transaction)

def transfer(accounts, transaction, username):
    amount = input('Masukkan jumlah transfer : ')
    while True:
        to = input('Masukkan nama tujuan : ')
        if cekTo(accounts, to):
            for a in range(len(accounts)):
                if accounts[a]['username'] == username:
                    if accounts[a]['amount'] - int(amount) >= 0:
                        accounts[a]['amount'] -= int(amount)
                        for a in range(len(accounts)):
                            if accounts[a]['username'] == to:
                                accounts[a]['amount'] += int(amount)
                                transaction.append(
                                    {
                                        'username':username,
                                        'to': to,
                                        'amount': int(amount),
                                        'type': 'transfer',
                                    }
                                )
                                print('Transfer berhasil!')
                                write_to_file(_TRANSAKSI_, transaction)
                                write_to_file(_ACCOUNT_FILE, accounts)
                                return True
                    else:
                        print('Saldo kamu tidak cukup!')
                        return False
        else:
            print('Nama tujuan tidak tersedia!')

def showTransaction(transaction, username):
    for t in range(len(transaction)):
        if transaction[t]['username'] == username:
            print('username : ', transaction[t]['username'])
            print('to : ', transaction[t]['to'])
            print('amount : ', transaction[t]['amount'])
            print('type : ', transaction[t]['type'])
            print('')

def showAllTransaction(transaction):
    for t in range(len(transaction)):
        print(str(t+1), '. ','username : ', transaction[t]['username'])
        print('   ', 'to : ', transaction[t]['to'])
        print('   ', 'amount : ', transaction[t]['amount'])
        print('   ', 'typr : ', transaction[t]['type'])