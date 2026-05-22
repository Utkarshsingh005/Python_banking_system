
from database import create_database
from account import Account

class Current(Account):
    def __init__(self, name, age, account_number, balance, pan, limit=0):
        super().__init__(name, age, account_number, balance, pan)
        self.limit = limit

    def __str__(self):
        return f'[Name: {self.name},Age: {self.age},Account number: {self.account_number},Balance: {self.balance}$,Withdrawal limit: {self.limit},PAN number: {self.pan}]'

    def withdraw(self):
        amount = 0
        while self.limit < 10:
            try:
                amount = int(input('Enter the amount to withdraw money: '))
            except ValueError:
                print('Amount Should be in digits!')

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

                self.limit += 1
                return True
        else:
            print('You cannot exceed the withdrawal limit')

