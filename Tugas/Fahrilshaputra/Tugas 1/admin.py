users = [{'email': 'f','password': '123','role': 'admin'},{'email': 'c', 'password' : '321', 'role' : 'user'}] 

current_users = {}
accounts = [{'email' : 'f','amount' : 0},{'email' : 'c','amount' : 0},]
transactions = []
def check_user(users, email):
    for user in users:
        if user['email'] == email:
            return False
    return True
def add_users(users, current_users):
    print("===========================================")
    print("                  Add Users                ")
    email = input("\nAdd Email: ")
    password = input("Add password: ")
    print("1. Admin or 2. User")
    role = input("Enter Role: ")
    for user in users:
        if user['email'] == email:
            print("Email already exists")
            return True
        else:
            if role == '1':
                role = 'admin'
                break
            elif role == '2':
                role = 'user'
                break
        print("Enter role 1 or 2!")
    if check_user(users, email):
        accounts.append({
            'email' : email,
            'amount' : 0
        })  
        users.append({
            'email': email,
            'password': password,
            'role': role
            })
        print("\n        User added successfully          ")
        print("===========================================")
        return True
    print("===========================================")

def delete_users(users):
    print("===========================================")
    print("                Data Users                 ")
    for user in users:
        print("\nEmail", user["email"], "    ||    ", "Role", user['role'])
    print("===========================================")
    
    while True:
        choice_del = input("Enter the email to delete: ")
        for i, user in enumerate(users):
            if user['email'] == choice_del:
                del users[i]
                print("             Delete successfully!          ")
                print("===========================================")
                return True
        print("Email not found!")
        print("===========================================")


def show_users(users):
    print("===========================================")
    print("                Data Users                 ")
    for user in users:
        print("\nEmail", user["email"], "    ||    ", "Role", user['role'])
    print("===========================================")

def show_transactions():
    print("===========================================")
    print("            Transaction data               ")
    for trans in range(len(transactions)):
        print(trans+1,"\nEmail: " , transactions[trans]['email'])
        print("","Destination: " , transactions[trans]['destination'])
        print("","Amount: " , transactions[trans]['amount'])
        print("","Type: " , transactions[trans]['type'])
        print("-------------------------------------------")
    print("\n          No transactions yet!")
    print("===========================================")
    