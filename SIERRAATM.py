import datetime
user1 = {
    "Username": ["Hellen Obwaya", "Eugene Gwara", "Victor Owino", "Esther Love", \
                 "Sylvia Chacha", "Sharon Wangila", "Mohamed Musitsu"],
    "PIN": [0000, 1234, 7896, 5234, 7421, 6321, 9251],
    "balance": [50000, 60000, 25000, 90000, 50000, 30000, 20000]
         }
trials = 3


def withdrawing():
    user1["balance"][x] -= withdraw
    print("Your balance is Ksh", user1["balance"][x])


def receipt():
    option1 = input("Would you like a receipt for your transaction?y/n:\n ")
    if option1 == "y":
        print(name)
        print("Your account balance is Ksh", user1["balance"][x])
        print(datetime.datetime.now())
        print("Thank you for using Sierra Bank")
    else:
        print("Thank you for using Sierra Bank")


def authenticate():
    if pin != user1["PIN"][x]:
        print('Wrong username or password\nAccess denied')


print("Welcome to Sierra Bank!")
while trials != 0:
    name = input("Enter your username:\n ")
    if name in user1["Username"]:
        x = (user1["Username"].index(name))
        pin = int(input('Enter your pin number:\n '))
        if pin != user1["PIN"][x]:
            print('Wrong username or password\nAccess denied')
            trials -= 1
            print("You have ", trials, "trials remaining")
            if trials == 0:
                print('Your account has been temporarily locked, please visit your branch')
        else:
            option2 = input("Enter w to withdraw or b for balance:\n ")
            if option2 == "w":
                withdraw = int(input('Enter the amount you wish to withdraw:\n '))
                if withdraw >= user1["balance"][x]:
                    print("You have insufficient balance.Try again")
                    withdraw = int(input('Enter the amount you wish to withdraw:\n '))
                    withdrawing()
                else:
                    withdrawing()
                option = input("Would you wish to withdraw again?y/n:\n ")
                if option == "y":
                    withdraw = int(input('Enter the amount you wish to withdraw:\n '))
                    withdrawing()
                    receipt()
                    break
                else:
                    receipt()
                    break
            else:
                print("Your account balance is ", user1["balance"][x])
                receipt()
                break
    else:
        pin = int(input('Enter your pin number:\n '))
        if pin:
            print("Wrong username or password \n Access denied ")
        else:
            print("Wrong username or password \n Access denied ")
        trials -= 1
        print("You have ", trials, "trials remaining")
        if trials == 0:
            print('Your account has been temporarily locked, please visit your branch')