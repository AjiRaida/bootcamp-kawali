from data_store import write_file

def cekUser(users, user):
    for u in users:
        if u['user'] == user :
            return False
    return True
        
def tambahUser(users, account):
    while True:
        user = input('User : ')
        if len(user) > 0 :
            if cekUser(users, user):
                while True:
                    password = input('Password : ')
                    if len(password) > 0 :
                        while True:
                            role = input('Role (1: admin, 2: customer) :')
                            if role == '1':
                                role = 'admin'
                                break
                            elif role == '2':
                                role = 'customer'
                                break
                            print('Masukkan role yang sesuai!')
                        users.append({
                            'user' : user,
                            'password' : password,
                            'role' : role
                        }),
                        write_file('user.txt', users)
                        account.append({
                            'user' : user,
                            'amount' : 0,
                        })
                        write_file('account.txt', account)
                        print('User berhasil di tambahkan!')
                        return True
                    else:
                        print('Harap masukan password!')
            else:
                print('Nama user sudah digunakan!')
        else:
            print('Harap masukan nama user!')

def hapusTransaksi(transaksi, user):
    import copy
    b = copy.copy(transaksi)
    for item in b:
        if item['user'] == user:
            print(item)
            transaksi.remove(item)
    write_file('transaksi.txt', transaksi)
    return True

def hapusUser(users, account, transaksi):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['user'], ' (',users[u]['role'],')')
    
    while True:
        user = input('Masukan nama user yang mau di hapus : ')
        for u in range(len(users)):
            if users[u]['user'] == user:
                if hapusTransaksi(transaksi, user):
                    users.pop(u)
                    account.pop(u)
                    write_file('user.txt', users)
                    write_file('account.txt', account)
                    print('User berhasil dihapus!')
                    return True
        print('Pilih user yang ada!')

def lihatUser(users):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['user'], ' (',users[u]['role'],')')

def lihatSemuaTransaksi(transaksi):
    if len(transaksi) > 0:
        for t in range(len(transaksi)):
            print(str(t+1), '. ','user : ', transaksi[t]['user'])
            print('   ', 'to : ', transaksi[t]['to'])
            print('   ', 'amount : ', transaksi[t]['amount'])
            print('   ', 'type : ', transaksi[t]['type'])
    else:
        print('Belum ada transaksi yang di lakukan')



