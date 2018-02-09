########################################
# ATM Withdraw
########################################

# Allowed papers: 100, 50, 10, 5, and rest of request

from enum import Enum

class Reason(Enum):
    Insufficient = 1
    Negative = 2

def withdraw(balance, request):
    cash = [100, 50, 10, 5]
    request_orig = request
    result       = balance

    print('===========================================')
    print(' Account balance   : ', balance)
    print(' Withdraw Request  : ', request)
    print('===========================================')

    # Check Requested Amount - Enough Balance
    if (request > balance):
        refuse(Reason.Insufficient)

    # Check Requested Amount - Negative Request
    elif (request <= 0):
        refuse(Reason.Negative)

    # Valid Request
    else:
        reminder = balance - request
        for c in cash:
            while request >= c:
                give(c)
                request -= c
        finish(request_orig, reminder)
        # Return balance after withdraw
        result = reminder

    return result

def give(c):
    print('give : ' + str(c))
    return


def finish(request, reminder):
    print('')
    print(' >>> Request for ' + str(request) + ' is done ')
    print(' >>> Current balance is : ' + str(reminder))
    return


def refuse(reason):
    if reason == Reason.Insufficient:
        print('Request refused - Account balance is ' + str(balance) + ' please use less amount')
        return
    elif reason == Reason.Negative:
        print('Request refused, please enter a postive amount')
        return
    else:
        print('Request refused')


# Testing
balance  = 500
requests = [300, 800, 150, 5, -20, 0, 40]

for t in requests:
    balance = withdraw(balance, t)
    print('')