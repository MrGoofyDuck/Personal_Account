# Assignment-3: Personal Account

In this assignment we need to creat a program on python for the to manage a personal bank account using object-oriented programming (OOP).

In the repository you will see three files the first one is a first chapter **Amount Class** and the second one **Personal_Account** the third one is a test of the program, you can see how it works, copy it and check it yourself

In this program we used **attributes** such as:

amount- sum of transaction

timestamp - date and time of transaction

transaction_type - such as ("DEPOSIT and "WITHDRAWAL")

**Methods:**

A constructor (__init __) to initialize the amount, timestamp and transaction_type.

__str __: Provides a string representation of the object for easier readability when printed or converted to a string.

**Personal_Account Class**

Create a class called PersonalAccount to represent a personal bank account. This class should include:

**Attributes:**

account_number (int): A unique identifier for the account.

account_holder (str): The name of the account holder.

balance (float): The current balance in the account.

transactions (list): A list to store Amount objects representing deposit and withdrawal transactions.

**Methods:**

A constructor (__init __) to initialize account_number, account_holder, and set the initial balance to 0.0.

deposit(self, amount): A method to deposit money into the account. This method should:

Create an Amount object with the 'DEPOSIT' type.

Add the transaction to the transactions list.

Update the balance.

withdraw(self, amount): A method to withdraw money from the account. This method should:

Create an Amount object with the 'WITHDRAWAL' type.

Add the transaction to the transactions list.

Update the balance. Ensure that the withdrawal amount does not exceed the current balance.

print_transaction_history(self): A method to print the transaction history of the account. Iterate through the transactions list and display each transaction, including the transaction_type and amount.

get_balance(self): A method to retrieve the current balance of the account.

get_account_number(self): A method to retrieve the account number.

set_account_number(self, account_number): A method to set the account number.

get_account_holder(self): A method to retrieve the account holder's name.

set_account_holder(self, account_holder): A method to set the account holder's name.

__str __(self) : Provides a string representation of the object for easier readability when printed or converted to a string.

__add __(self, amount): Performs the same operation as the deposit(self, amount) method, allowing for addition of the specified amount to the object.

__sub __(self, amount): Performs the same operation as the withdraw(self, amount) method, allowing for subtraction of the specified amount to the object.
