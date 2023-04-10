from berkas import write_file

def cekUser(users, user):
    for u in users:
        if u['user'] == user :
            return False
    return True

def cekTujuan(account, tujuan):
    for a in range(len(account)):
        if account[a]['user'] == tujuan:
            return True
    return False



def CekSaldo(account, user):
    for a in account:
        if a['user'] == user:
            print(' Sisa saldo kamu : Rp. ', str(a['amount']))
            print('----------------------')

def TarikSaldo(account, transaksi, user):
    amount = input('Masukkan nominal penarikan : ')
    for a in range(len(account)):
        if account[a]['user'] == user:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                write_file('account.txt', account)
                transaksi.append(
                    {
                        'user':user,
                        'to': 'self',
                        'amount': int(amount),
                        'type': 'withdraw',
                    }
                )
                write_file('transaksi.txt', transaksi)
                print('Tarik saldo berhasil!')
            else:
                print('Maaf Saldo kamu tidak cukup!')

def setorTunai(account, transaksi, user):
    amount = input('Masukkan nominal : ')
    for a in range(len(account)):
        if account[a]['user'] == user:
            account[a]['amount'] += int(amount)
            write_file('account.txt', account)
            transaksi.append(
                {
                    'user':user,
                    'to': 'self',
                    'amount': int(amount),
                    'type': 'deposit',
                }
            )
            print('Saldo berhasil di tambahkan!')
            write_file('transaksi.txt', transaksi)

def transfer(account, transaksi, user):
    amount = input('Masukkan jumlah transfer : ')
    while True:
        tujuan = input('Masukkan nama tujuan : ')
        if cekTujuan(account, tujuan):
            for a in range(len(account)):
                if account[a]['user'] == user:
                    if account[a]['amount'] - int(amount) >= 0:
                        account[a]['amount'] -= int(amount)
                        for a in range(len(account)):
                            if account[a]['user'] == tujuan:
                                account[a]['amount'] += int(amount)
                                write_file('account.txt', account)
                                transaksi.append(
                                    {
                                        'user':user,
                                        'to': tujuan,
                                        'amount': int(amount),
                                        'type': 'transfer',
                                    }
                                )
                                write_file('transaksi.txt', transaksi)
                                print('Transfer berhasil!')
                                return True
                    else:
                        print('Saldo kamu tidak cukup!')
                        return False
        else:
            print('Maaf nama tujuan tidak tersedia!')
                

def lihatTransaksi(transaksi, user):
    for t in range(len(transaksi)):
        if transaksi[t]['user'] == user:
            i = 1
            for t in range(len(transaksi)):
                if transaksi[t]['user'] == user:
                    print('')
                    print('=== Transaksi ', str(i), '===')
                    print('user : ', transaksi[t]['user'])
                    print('to : ', transaksi[t]['to'])
                    print('amount : ', transaksi[t]['amount'])
                    print('type : ', transaksi[t]['type'])
                    print('')
                i += 1
            return True
    print('Kamu belum melakukan transaksi !')