from user import users, cUser, accounts,transaction,add_user, show_users, delete_user, show_balance,deposit,showAllTransaction,transfer,withdraw, showTransaction
from file_ops import write_to_file,read_file


def login(username, password, cUser):
    for u in users:
        if u['username'] == username and u['password'] == password:
            cUser.update(u)
            return True
    return False
  

def login_process(cUser):
    while True:
        username = input('Username : ')
        password = input('Password : ')
        if login(username, password, cUser):
            print('Login Succes')
            break
        else:
            print('Login Failed')

def menu(cUser):
    if cUser['role'] == 'admin':
        while True:
            print()
            print('------------------------------')
            print('1. Add User')
            print('2. Delete user')
            print('3. Show User')
            print('4. Show Transaction')
            print('5. Logout')
            print('------------------------------')
            print()
            choice = input('Choice : ')
            if choice == '1':
                add_user(users, accounts)
            elif choice == '2':
                delete_user(users,transaction,accounts)
            elif choice == '3':
                show_users(users)
            elif choice == '4':
                showAllTransaction(transaction)
            elif choice == '5':
                cUser.clear()
                break
    elif cUser['role'] == 'customer':
        while True:
            print('------------------------------')
            print('1. Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transfer')
            print('5. Transaction')
            print('6. Logout')
            print('------------------------------')
            choice = input('Choice : ')
            if choice == '1':
                show_balance(accounts,cUser['username'])
            elif choice == '2':
                withdraw(accounts, transaction, cUser['username'])
            elif choice == '3':
                deposit(accounts, transaction, cUser['username'])
            elif choice == '4':
                 transfer(accounts, transaction, cUser['username'])
            elif choice == '5':
                showTransaction(transaction,cUser['username'])
            elif choice == '6':
                cUser.clear()
                break
def main():
    while True:
        print('-----------MENU------------')
        print('1. Login')
        print('2. Exit')
        print('---------------------------')
        choice = input('Choice : ')
        if choice == '1':
            login_process(cUser)
            menu(cUser)
        elif choice == '2':
            break
        print('\033c', end='')

main()