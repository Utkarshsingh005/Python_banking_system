
from database import create_database
from account import Account

class Savings(Account):
    interest_rate = 0.06
    def __str__(self):
        return f'[Name: {self.name},Age: {self.age},Account number: {self.account_number},Balance: {self.balance}$,Interest rate: {Savings.interest_rate},PAN number: {self.pan}]'

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
            interest = amount * Savings.interest_rate
            self.balance += (amount + interest)
            conn = create_database()
            cur = conn.cursor()
            query1 = ("UPDATE Accounts SET Balance = %s WHERE Account_number = %s")
            value1 = (self.balance, self.account_number)
            cur.execute(query1, value1)

            query2 = """
                     INSERT INTO Transactions(Account_number, Amount_Credited, Total_balance)
                     VALUES (%s, %s, %s) \
                     """
            value2 = (self.account_number, amount, self.balance)
            cur.execute(query2, value2)
            conn.commit()

            cur.close()
            conn.close()
            return True
