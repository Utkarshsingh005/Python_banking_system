from database import create_database
import function

my_account_dict = {'Savings':{},
                   'Current':{},
                   'Trust':{}
                   }

while True:
    print('\nO: Open an account')
    print('P: Print a specific account' )
    print('D: Deposit money')
    print('W: Withdraw money')
    print('T: See transaction history')
    print('Q: Quit')

    choice = input('\nEnter you choice: ').upper()

    match choice:
        case 'O':
            function.open_account_type(my_account_dict)

        case 'P':
            function.look_up(my_account_dict)

        case 'D':
            function.deposit_amount(my_account_dict)

        case 'W':
            function.withdraw_amount(my_account_dict)

        case 'T':
            function.transaction_history()

        case 'Q':
            choice = input('Do you want to delete all accounts[Y/N]').upper()
            if choice == 'Y':
                conn = create_database()
                cur = conn.cursor()

                cur.execute("DELETE FROM Transactions")
                cur.execute("DELETE FROM Accounts")

                conn.commit()
                cur.close()
                conn.close()

                print('Accounts deleted Successfully')
                break

            elif choice == 'N':
                print('Closing App...')

            else:
                print('Enter a valid choice!')

        case _:
            print('Enter a valid choice')

