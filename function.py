from database import create_database
from savings import Savings
from current import Current
from trust import Trust

def open_account_type(acc_dict):
    type = input('which account you want to open (S)avings, (C)urrent, (T)rust: ').upper()
    match type:
        case 'S':
            saving = Savings.create_account()
            print(saving)
            acc_dict['Savings'][saving.account_number] = saving

            conn = create_database()
            cur = conn.cursor()
            query = ("INSERT INTO Accounts(Account_number,Name,Age,Account_type,PAN_number,Balance) VALUES(%s,%s,%s,%s,%s,%s)")
            values = (saving.account_number,saving.name,saving.age,'Savings',saving.pan,saving.balance)

            cur.execute(query,values)
            conn.commit()

            cur.close()
            conn.close()

        case 'C':
            current = Current.create_account()
            print(current)
            acc_dict['Current'][current.account_number] = current

            conn = create_database()
            cur = conn.cursor()
            query = (
                "INSERT INTO Accounts(Account_number,Name,Age,Account_type,PAN_number,Balance) VALUES(%s,%s,%s,%s,%s,%s)")
            values = (current.account_number, current.name, current.age, 'Current', current.pan, current.balance)

            cur.execute(query, values)
            conn.commit()

            cur.close()
            conn.close()

        case 'T':
            trust = Trust.create_account()
            print(trust)
            acc_dict['Trust'][trust.account_number] = trust

            conn = create_database()
            cur = conn.cursor()
            query = (
                "INSERT INTO Accounts(Account_number,Name,Age,Account_type,PAN_number,Balance) VALUES(%s,%s,%s,%s,%s,%s)")
            values = (trust.account_number, trust.name, trust.age, 'Trust', trust.pan, trust.balance)

            cur.execute(query, values)
            conn.commit()

            cur.close()
            conn.close()

        case _:
            print('Enter a valid choice')




def look_up(acc_dict):
    acc_type = ''
    try:
        acc_type = input('Enter the type of account you want to see: ')
    except KeyError:
        print('Account number doesnt match!')

    for key , value in acc_dict[acc_type].items():
        print(key,value)

def deposit_amount(acc_dict):
    acc_type = input('Enter the type of account you want to deposit: ')
    acc_number = 0

    while True:
        try:
            acc_number = int(input('Enter the account number of that account: '))
        except ValueError:
            print('Account number should be in digits!')
            continue
        else:
            break

    if acc_dict[acc_type][acc_number].deposit():
        print('Money deposited successfully!')

    else:
        print('Failed to deposit money')

def withdraw_amount(acc_dict):
    acc_type = input('Enter the type of account you want to deposit: ')
    acc_number = 0

    while True:
        try:
            acc_number = int(input('Enter the account number of that account: '))
        except ValueError:
            print('Account number should be in digits!')
            continue
        else:
            break

    if acc_dict[acc_type][acc_number].withdraw():
        print('Money withdrawn successfully!')

    else:
        print('Failed to withdraw money')

def transaction_history():
    acc_number = 0

    while True:
        try:
            acc_number = int(input('Enter the account number: '))
        except ValueError:
            print('Account number should be in digits!')
            continue
        else:
            break

    conn = create_database()
    cur = conn.cursor()

    query = ("""SELECT * FROM Transactions WHERE Account_number = %s""")
    values = (acc_number,)

    cur.execute(query, values)

    columns = [col[0] for col in cur.description]

    for row in cur.fetchall():
        record = dict(zip(columns, row))
        print(record)

    cur.close()
    conn.close()
