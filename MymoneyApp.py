import datetime as dt
account_details = {"Card" : 0}
incoming_mode = {"Salary","Rent","Dept"}
expense_details = {}

def update_incoming_details(mode,amount,date):
    if mode in incoming_mode:
        account_details.update({"Card": account_details["Card"] + amount})
        print(f"Amount added Successfully.! on {date}")
    else:
        print(f"Amount of Rs {amount} is failure in Addition due to given mode not in list of Incoming")
        
def expense_update(category,amount):
    if category in expense_details:
        expense_details.update({category:expense_details[category] + amount})
        account_details.update({"Card": account_details["Card"] - amount})
        print("Expenses added successfully.!")
    else:
        expense_details.update({category:amount})
        account_details.update({"Card": account_details["Card"] - amount})
        print("Expenses added successfully.!")


update_incoming_details("Salary",30000,dt.datetime.now())
expense_update("Tea", 500);
expense_update("Load", 1000);
update_incoming_details("Rent",5000,dt.datetime.now())
expense_update("Food", 700);
expense_update("Snacks", 800);
expense_update("Tea", 500);

print(account_details)
expense_amount = 0
for expense,amount in expense_details.items():
    print(f"Spend {expense} for {amount} Rs.")
    expense_amount +=  amount

print(f"Total Expense Amount is {expense_amount}")
