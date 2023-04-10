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



def cekSaldo(account, user):
    for a in account:
        if a['user'] == user:
            print('Saldo kamu : Rp. ', str(a['amount']))

def tarikTunai(account, transaksi, user):
    amount = input('Masukkan nominal penarikan : ')
    for a in range(len(account)):
        if account[a]['user'] == user:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                transaksi.append(
                    {
                        'user':user,
                        'to': 'self',
                        'amount': int(amount),
                        'type': 'withdraw',
                    }
                )
                print('Tarik tunai berhasil!')
            else:
                print('Maaf, Saldo kamu tidak cukup!')

def setorTunai(account, transaksi, user):
    amount = input('Masukkan nominal setor : ')
    for a in range(len(account)):
        if account[a]['user'] == user:
            account[a]['amount'] += int(amount)
            transaksi.append(
                {
                    'user':user,
                    'to': 'self',
                    'amount': int(amount),
                    'type': 'deposit',
                }
            )
            print('Saldo berhasil di tambahkan!')

def transfer(account, transaction, user):
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
                                transaction.append(
                                    {
                                        'user':user,
                                        'to': tujuan,
                                        'amount': int(amount),
                                        'type': 'transfer',
                                    }
                                )
                                print('Transfer berhasil!')
                                return True
                    else:
                        print('Saldo kamu tidak cukup!')
                        return False
        else:
            print('Nama tujuan tidak tersedia!')
                

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
    print('Kamu belum melakukan transaksi apapun!')