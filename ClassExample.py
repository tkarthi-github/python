class Bank:
    def __init__(self):
        print("method Called")

    def __init__(self,acc_name, acc_address, acc_mobile, acc_emailid,acc_pan):
        self.acc_name = acc_name
        self.acc_address = acc_address
        self.acc_mobile = acc_mobile
        self.acc_emailid = acc_emailid
        self.acc_pan = acc_pan
        self.acc_balance = 1000.00

    def show_account_details(self):
        print(f"Account Name is : {self.acc_name}, Address is {self.acc_address}, Contact Number is {self.acc_mobile} and EmailID is {self.acc_emailid} ")
    
    def check_balance(self):
        print(f"Current Balance is {self.acc_balance}")
    
    def deposit_amount(self,amount):
        self.acc_balance += amount
        print(f"Current Balance is {self.acc_balance}")
    
    def widthdrawal_amount(self, amount):
        if self.acc_balance <= 0:
            print("No Balance. Please deposit and then widthdraw the amount")
            return
        
        if amount > self.acc_balance:
            print(f"Account Balance is low. Current balance is {self.acc_balance}. Please try with some other amount")
            return
        else:
            print("Please Wait for the Cash..!")
            self.acc_balance -= amount
            print(f"Please take the cash.! Current Balance is {self.acc_balance}")

        



