# Main file ini bersisi sesuatu yang ditampilkan kepada user

# Import File
import json
from users import users, login, addUser, deleteUser, showUsers, lihatSaldo, current_user
from transaction import showTransaction, deposit, transfer, tarikTunai

# Halaman
def lamanLogin():
    print("Laman Login")
    username = input("Username : ")
    password = input("Password : ")
    hasil_login = login(username = username, password = password)
    if hasil_login == "lamanAdmin":
        lamanAdmin()
    if hasil_login == "lamanCustomor":
        lamanCustomor()

def lamanAddUser():
    kondisi = 0
    while kondisi == 0:
        print("Add User")
        username = input("Username : ")
        password = input("Password : ")
        role = input("Role (1: admin, 2: customor) : ")
        if role == "1":
            role = "admin"
        elif role == "2":
            role = "customor"

        if role == "admin" or role == "customor":
            addUser(username = username, password = password, role = role)
            kondisi = 1
        else:
            print("Maaf hanya masukan nomor 1 / 2")

def lamanAwal():
    exit = 0
    while exit == 0:
        input_nomor_tampilan_awal = input("""SISTEM BANKING
        1. Login
        2. Exit
        Masukan Nomor : """)

        if input_nomor_tampilan_awal == "1":
            lamanLogin()
        elif input_nomor_tampilan_awal == "2":
            exit = 1

def lamanAdmin():
    current_id = current_user["id"]
    current_username = current_user["username"]
    current_password = current_user["password"]
    current_role = current_user["role"]
    logout = 0
    while logout == 0:
        input_laman_admin = input("""WELCOME BACK ADMIN
        1. Add User
        2. Delete User
        3. Show Users
        4. Show Transaction
        5. Logout
        Masukan Nomor : """)
        if input_laman_admin == "1":
            lamanAddUser()
        elif input_laman_admin == "2":
            username = input("Masukan Username : ")
            deleteUser(username)
        elif input_laman_admin == "3":
            showUsers()
        elif input_laman_admin == "4":
            showTransaction()
        elif input_laman_admin == "5":
            logout = 1
        else:
            print("Maaf Nomor Yang Diinputkan Tidak Falid!!")

def lamanCustomor():
    current_id = current_user["id"]
    current_username = current_user["username"]
    current_password = current_user["password"]
    current_role = current_user["role"]
    logout = 0
    while logout == 0:
        input_laman_customor = input("""WELCOME BACK
        1. Lihat Saldo
        2. Tarik Tunai
        3. Deposit
        4. Transfer Uang
        5. Lihat History Transaksi
        6. Logout
        Masukan Nomor : """)
        if input_laman_customor == "1":
            lihatSaldo(current_username)
        elif input_laman_customor == "2":
            tarik = int(input("Masukan Jumlah Penarikan : "))
            tarikTunai(current_username, tarik)
            for i in range(len(users)):
                if users[i]["username"] == current_username:
                    if 0 < users[i]["saldo"] - tarik:
                        users[i]["saldo"] = users[i]["saldo"] - tarik
                        json_users = json.dumps(users)
                        data_users = open("data/users.txt", "w")
                        data_users.write(json_users)
                        data_users.close()
                    else:
                        print("Maaf Saldo Tidak Mencukupi")
        elif input_laman_customor == "3":
            depo = int(input("Masukan Jumlah Deposit : "))
            deposit(current_username, depo)
            for i in range(len(users)):
                if users[i]["username"] == current_username:
                    users[i]["saldo"] = users[i]["saldo"] + depo
                    json_users = json.dumps(users)
                    data_users = open("data/users.txt", "w")
                    data_users.write(json_users)
                    data_users.close()
        elif input_laman_customor == "4":
            user_tujuan = input("Masukan Username Tujuan : ")
            uang = int(input("Masukan Jumlah Uang : "))
            ckp = 0
            for j in range(len(users)):
                if users[j]["username"] == current_username:
                    if users[j]["saldo"] - uang > 0:
                        for i in range(len(users)):
                            if users[i]["username"] == current_username:
                                users[i]["saldo"] = users[i]["saldo"] - uang
                        for i in range(len(users)):
                            if users[i]["username"] == user_tujuan:
                                users[i]["saldo"] = users[i]["saldo"] + uang
                        transfer(current_username, user_tujuan, uang)
                        ckp = 1
                        json_users = json.dumps(users)
                        data_users = open("data/users.txt", "w")
                        data_users.write(json_users)
                        data_users.close()
            if ckp == 0:
                print("Maaf Saldo Tidak Mencukupi")
        elif input_laman_customor == "5":
            showTransaction(current_username)
        elif input_laman_customor == "6":
            logout = 1
        else:
            print("Maaf Nomor Yang Diinputkan Tidak Falid!!")