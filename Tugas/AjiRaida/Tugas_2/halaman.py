from admin import AddUser, DeleteUser, ShowUser, ShowTransaksi
from customer import CekSaldo, TarikSaldo, setorTunai, transfer, lihatTransaksi
from berkas import  read_file

users = read_file('user.txt')
cUser = {}
transaksi = read_file('transaksi.txt')
account = read_file('account.txt')

def infoLogin(user, password, cUser):
    for u in users:
        if u['user'] == user and u['password'] == password:
            cUser.update(u)
            return True
    return False


def login(cUser):
    while True:
        user = input('Username : ')
        passsword = input('Password : ')
        if infoLogin(user, passsword, cUser):
            print('Login Berhasil')
            break
        else:
            print('Login Gagal')
#Menu Admin
def menu(cUser):
    if cUser['role'] == 'admin':
        while True:
            print('-------Admin-------')
            print('1. AddUser')
            print('2. DeleteUser')
            print('3. ShowUser')
            print('4. ShowTransaksi')
            print('5. Logout')
            pilihan = input('Pilih menu : ')
            if pilihan == '1':
                AddUser(users, account)
            elif pilihan == '2':
                DeleteUser(users, account, transaksi)
            elif pilihan == '3':
                ShowUser(users)
            elif pilihan == '4':
                ShowTransaksi(transaksi)
            elif pilihan == '5':
                cUser.clear()
                break
# Menu customer
    elif cUser['role'] == 'customer':
        while True:
            print('-------Custumer-------')
            print('1. Lihat Saldo')
            print('2. Tarik Saldo')
            print('3. Setor Tunai')
            print('4. Transfer')
            print('5. Lihat Transaksi')
            print('6. Logout')
            pilihan = input('Pilih Menu : ')
            if pilihan == '1':
                CekSaldo(account, cUser['user'])
            elif pilihan == '2':
                TarikSaldo(account, transaksi, cUser['user'])
            elif pilihan == '3':
                setorTunai(account, transaksi, cUser['user'])
            elif pilihan == '4':
                transfer(account, transaksi, cUser['user'])
            elif pilihan == '5':
                lihatTransaksi(transaksi, cUser['user'])
            elif pilihan == '6':
                cUser.clear()
                break

# Menu login
def main():
    while True:
        print('1. Login')
        print('2. Exit')
        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            login(cUser)
            menu(cUser)
        elif pilihan == '2':
            break
        print('\033c', end='')

main()
