class Bank:
    balance=1000
    def __debit(self,amt):
        self.balance-amt

    def __creadit(self,amt):
        self.balance=amt
    def __checkbbalance(self):
        print("total balance is")+str(self.balance)
    def login(self,pin):
        if pin==1234:
            self__debit(int(input("enter amt")))
            self__chackbalance()
obj=Bank
obj.login(1234)
obj.display()
