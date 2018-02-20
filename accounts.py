import csv

def saving_accounts_and_pass(dictionary):
    w = csv.writer(open("accounts.csv", "w"))
    for key, val in dictionary.items():
        w.writerow([key, val])
        

def create_acc():
    original = True

    with open('accounts.csv', mode='r') as infile:
        reader = csv.reader(infile)
        accounts = {rows[0]:rows[1] for rows in reader}
        
    print(accounts)

    while original:

        login = input('Choose your login: ')
        
        if login not in accounts:
            password = input('choose you password: ')
            accounts[login] = password
            print('Account created!')
            original = False
        else:
            print('Login taken, try again')

    print(accounts)
    return accounts