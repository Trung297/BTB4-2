import random

def game_engine():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    #dice1 = 2
    #dice2 = 3
    #print(dice1)
    #print(dice2)
    is_win = False
    result = "Tai"
    while True:
        player_guess = input("guess Tai, Xiu or 5: ").lower()
        if player_guess == "tai" or player_guess == "xiu" or player_guess == "5":
            break
    if dice1 + dice2 > 5:
        print(f"the result is: {result}")
    elif dice1 + dice2 < 5:
        result = "Xiu"
        print(f"the result is: {result}")
    else:
        result = "5"
        print(f"the result is {result}")
    if result.lower() == player_guess.lower():
        print("you won. congrats!")
        is_win = True
    else:
        print("good luck next time!")
    return is_win, result

if __name__ == '__main__':
    no_win = 0
    moneyAmmount = 100000
    while True:
        moneyBet = int(input("enter the ammount of money you want to bet: "))
        if moneyBet > moneyAmmount:
            moneyBet = int(input("you don't have enough to bet that much, please bet again: "))
        is_win, result = game_engine()
        if is_win:
            no_win += 1
            if result == "5":
                moneyAmmount += moneyBet * 3
                print("you earned triple the money you've bet")
            else:
                moneyAmmount += moneyBet
        else:
            moneyAmmount -= moneyBet
        respond = input("do you want to continue: <n/N> to stop: ").lower()
        if respond == "n" or moneyAmmount == 0:
            break
    print(f"money player have left: {moneyAmmount}")
    print(f"win count: {no_win}")
