# Python_banking_system

🏦 Banking System
A command-line Banking System built in Python using Object-Oriented Programming and MySQL for persistent storage.

📌 Features
Open Savings, Current, and Trust accounts
Deposit and Withdraw money
View Transaction History
Nested dictionary for O(1) fast lookups using account number as authentication
MySQL database for persistent storage
Secure credentials via environment variables

🏗️ Project Structure
banking_system/
├── main.py          # Entry point & menu
├── account.py       # Base Account class
├── savings.py       # Savings account (6% interest on deposit)
├── current.py       # Current account (10 withdrawal limit)
├── trust.py         # Trust account (8% tax on withdrawal)
├── function.py      # Helper functions
├── database.py      # MySQL connection
├── .env             # Secret credentials (not pushed to GitHub)
└── .gitignore

⚙️ Account Types
<table>
<td>Account</td>
<td>Special Rule</td>
<tr>Savings</tr>
<tr>6% interest added on every deposit<tr><br>
<tr>Current</tr>
<tr>Max 10 withdrawals per session</tr><br>
<tr>Trust</tr>
<tr>8% tax deducted on every withdrawal</tr>
</table>
