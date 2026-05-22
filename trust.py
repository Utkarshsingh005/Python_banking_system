from database import create_database
from account import Account

class Trust(Account):
    tax_deduction = 0.08

    def __str__(self):
        return f'[Name: {self.name},Age: {self.age},Account number: {self.account_number},Balance: {self.balance}$,Tax Deduction: {Trust.tax_deduction},PAN number: {self.pan}]'

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
            tax = amount * Trust.tax_deduction
            self.balance -= (amount + tax)
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
