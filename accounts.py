import csv

def saving_accounts_and_pass(dictionary):
    with open('accounts.csv', 'w') as infile:
        w = csv.writer(infile)
        for key, val in dictionary.items():
            w.writerow([key, val])
        
def load_accounts_and_pass():
    with open('accounts.csv', 'r') as infile:
        reader = csv.reader(infile)
        accounts = {rows[0]:rows[1] for rows in reader}
    return accounts


def create_acc():
    original = True
    accounts = load_accounts_and_pass()
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