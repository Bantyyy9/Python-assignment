bill= str(input("Thanks for using our resturant, your bill is #150,000 which includes a 5% tip\n Type Yes to continue\n>>"))

if bill=="Yes":
    response=str(input("How would you like to pay?\n1. Pay Full Once +5% tip\n2. Split the bill into 3 places\n>>")).lower()
    if response=="1" or response=="Pay Once":
        mode_of_payment=str(input("Mode of payment\n1. By Transfer\n2. By Card\n>>"))

        if response=="1" or response=="transfer":
            account_number=str(input("Input your account number\n>>"))
            amount=str(input("Enter the amount to transfer\n>>"))
            if account_number and len(account_number)==10:
                print(f"Payment successful. Amount paid: {amount} to Account Number: {account_number}")
            else:
                print("Invalid account number")
        elif response=="2" or response == "card":
            card_number =str(input("Type your card number\n>>"))
            cvv=str(input("Type your CVV\n>>"))
            if card_number and len(card_number)==16:
                print(f"Payment successful. Card details: Card Number:{card_number}, CVV:{cvv}")
            else:
                print("Invalid card details")
    if response=="2" or response=="split":
        split_bill=int(input("Split the bill into how many parts?\n>>")) 
        if split_bill>1:
            amount_per_person=int(150000/split_bill)
            print(f"Payment successful. Each person will pay: {amount_per_person}")
        else:
            print("Invalid number of parts")
    

else:
    print("Invalid Command")
