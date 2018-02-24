########################################
# ATM Withdraw
########################################

# Allowed papers: 100, 50, 10, 5, and rest of request

from enum import Enum

class Reason(Enum):
    Insufficient = 1
    Negative = 2

class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    @staticmethod
    def give(c):
        print('give : ' + str(c))
        return

    @staticmethod
    def accept(balance, request, cash = [100, 50, 10, 5]):
        reminder = balance - request
        for c in cash:
            while request >= c:
                ATM.give(c)
                request -= c
        return reminder

    @staticmethod
    def finish(request, reminder):
        print('')
        print(' >>> Request for ' + str(request) + ' is done ')
        print(' >>> Current balance is : ' + str(reminder))
        return

    @staticmethod
    def refuse(balance,reason):
        if reason == Reason.Insufficient:
            print('Request refused - Account balance is ' + str(balance) + ' please use less amount')
            return
        elif reason == Reason.Negative:
            print('Request refused, please enter a postive amount')
            return
        else:
            print('Request refused')

    def withdraw(self, request):
        cash = [100, 50, 10, 5]
        result = self.balance

        print('===========================================')
        print(' Welcome to Bank    : ', self.bank_name)
        print(' Account balance    : ', self.balance)
        print(' Withdraw Request   : ', request)
        print('===========================================')
        
        # Check Requested Amount - Enough Balance
        if (request > self.balance):
            ATM.refuse(self.balance,Reason.Insufficient)
        
        # Check Requested Amount - Negative Request
        elif (request <= 0):
            ATM.refuse(Reason.Negative)
        
        # Valid Request
        else:
            reminder = self.accept(self.balance,request,cash)
            ATM.finish(request, reminder)
            # Return balance after withdraw
            result = reminder
            self.withdrawals_list.append(request)

        return result
        
    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)

# Testing 1
# balance  = 500
# requests = [300, 800, 150, 5, -20, 0, 40]

# for t in requests:
    # balance = withdraw(balance, t)
    # print('')

# Testing 2
balance1 = 500
balance2 = 1000

bank1    ='Smart Bank'
bank2    ='Faisl Bank'

atm1 = ATM(balance1,bank1)
atm2 = ATM(balance2,bank2)

atm1.withdraw(200)
atm1.withdraw(800)
print('Withdrawals : ')
atm1.show_withdrawals()

atm2.withdraw(500)
atm2.withdraw(300)
atm2.withdraw(1200)
print('Withdrawals : ')
atm2.show_withdrawals()
