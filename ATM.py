import sys
lst = sys.argv

acc_balance=10000

if lst[1]=="Balance enquiry":
    print("Balance is :",acc_balance)
elif lst[1]=="Withdraw":
    x = int(input("Enter amount to withdraw :"))
    print("Balance is :",acc_balance-x)
elif lst[1]=="Deposit":
    x = int(input("Enter amount to deposit :"))
    print("Balance is :", acc_balance + x)
else:pass
