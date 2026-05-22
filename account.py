import random
from database import create_database


def user_input():
    acc_age = 0
    acc_balance = 0
    acc_pan = ''
    acc_name = input('Enter the name: ')
    while True:
        try:
            acc_age = int(input('Enter you age: '))
        except ValueError:
            print('\nAge must be in digits!')
            continue
        if acc_age < 18:
            print('\nYou must be above 18 to open an account!')
            continue
        else:
            break
    while True:
        temp = input('Do you have a PAN card[Y/N]').upper()
        if temp == 'N':
            print('\nYou need PAN card in order to open an account!')
            continue
        elif temp == 'Y':
            acc_pan = input('Enter you PAN number: ')
            break
        else:
            print('\nYou must type [Y/N]!')
            continue
    while True:
        print('You need deposit atleast 500$ to open an account')
        try:
            acc_balance = int(input('Enter the amount to open an account: '))
        except ValueError:
            print('\nThe amount must in digits!')
            continue
        if acc_balance < 500:
            print('\nDeposit atleast 500!')
            continue
        else:
            break
    account_number = random.randint(1000, 100000)
    print('\nYour account has been opened successfully!')
    return acc_name, acc_age, account_number, acc_balance, acc_pan


class Account:
    def __init__(self,name,age,account_number,balance,pan):
        self.name = name
        self.age = age
        self.account_number = account_number
        self.balance = balance
        self.pan = pan

    @classmethod
    def create_account(cls):
        name,age,acc,bal,pan = user_input()
        return cls(name,age,acc,bal,pan)



    def __str__(self):
        return f'[Name: {self.name},Age: {self.age},Account number: {self.account_number},Balance: {self.balance}$,PAN number: {self.pan}]'

    def deposit(self):
        amount = 0
        while True:
            try:
                amount = int(input('Enter the amount to deposit money: '))
            except ValueError:
                print('\nAmount should be in digits!')
                continue
            else:
                break

        if amount <= 0:
            return False

        else:
            self.balance += amount
            conn = create_database()
            cur = conn.cursor()

            query1 = ("UPDATE Accounts SET Balance = %s WHERE Account_number = %s")
            value1 = (self.balance,self.account_number)
            cur.execute(query1,value1)

            query2 = """
                     INSERT INTO Transactions(Account_number,Amount_Credited,Total_balance)
                     VALUES (%s, %s,%s) \
                     """
            value2 = (self.account_number,amount,self.balance)
            cur.execute(query2,value2)
            conn.commit()

            cur.close()
            conn.close()
            return True

    def withdraw(self):
        amount = 0
        while True:
            try:
                amount = int(input('Enter the amount to withdraw money: '))
            except ValueError:
                print('\nAmount should be in digits!')
                continue
            else:
                break

        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            conn = create_database()
            cur = conn.cursor()

            query1 = ("UPDATE Accounts SET Balance = %s WHERE Account_number = %s")
            value1 = (self.balance, self.account_number)
            cur.execute(query1, value1)

            query2 = """
                     INSERT INTO Transactions(Account_number, Amount_Debited, Total_balance)
                     VALUES (%s, %s, %s) \
                     """
            value2 = (self.account_number, amount, self.balance)
            cur.execute(query2, value2)
            conn.commit()

            cur.close()
            conn.close()
            return True










