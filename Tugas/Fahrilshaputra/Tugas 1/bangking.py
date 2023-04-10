from admin import users,current_users, add_users, show_users, delete_users,transactions, show_transactions, accounts
from user import check_balance, transaction, withdraw, deposit, view_transaction

def login(email, password, current_users):
    for user in users:
        if user['email'] == email and user['password'] == password:
            current_users.update(user)
            return True
    return False
    
def login_action(current_users):
    while  True:
        print("===========================================")
        print("               Form Login                  ")
        email = input("\nEnter Email: ")
        password = input("Enter Password: ")
        if login(email, password, current_users):
            print("\n            Login successfully!            ")
            print("===========================================")
            break
        else:
            print("Login failed, please check username and password!")

def choice_menu(current_users):
    if current_users['role'] == 'admin':
        while True:
            # print(current_users)
            # print(transactions)
            # print(accounts)
            print("Menu :")
            print("1. Add User")
            print("2. Delete User")
            print("3. Show Users")
            print("4. Show Transaction")
            print("5. Logout")
            print("-------------------------------------------")
            choice = int(input("Select menu: "))
            if choice == 1:
                add_users(users, current_users)
                # print(users)
            elif choice == 2:
                delete_users(users)
                pass
            elif choice == 3:
                show_users(users)
                pass
            elif choice == 4:
                show_transactions()
                pass
            elif choice == 5:
                current_users.clear()
                break
            else:
                print("sorry not in the options")
    elif current_users['role'] == 'user':
         while True:
            print("Menu:")
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Transaction history")
            print("6. Logout")
            choice = int(input("Select menu: "))
            if choice == 1:
                check_balance(accounts, current_users['email'])
                pass
            elif choice == 2:
                withdraw(accounts, transactions, current_users['email'])
            elif choice == 3:
                deposit(accounts, transactions, current_users['email'])
            elif choice == 4:
                transaction(accounts, transactions, current_users['email'])
            elif choice == 5:
                view_transaction(transactions, current_users['email'])
            elif choice == 6:
                current_users.clear()
                break
            else:
                print("sorry not in the options")

def main():
    while True:
        print("1.Login")
        print("2.Exit")
        main_input = int(input("Select menu: "))
        if main_input == 1:
            login_action(current_users)
            choice_menu(current_users)
        elif main_input == 2:
            break
        else:
            print("Sorry not in the option!")
        print('\033c', end='')
        
main()