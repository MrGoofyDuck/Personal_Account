from ppacc  import personal_account

account = personal_account(123456789, "Jane Doe", 500.0, [])

account.deposit(100.0)
account.withdraw(1000000.0)
account.print_transaction_history()

print(account)