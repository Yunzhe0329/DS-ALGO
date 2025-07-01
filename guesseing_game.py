
import random
def guessing_game():
    goal = random.randint(1, 99)
    while True:
        num = input("請輸入一個數字: ")
        if num.isdigit():
            user_guess = int(num)
            if user_guess == goal:
                print("恭喜你猜對了～")
                break
            elif user_guess < goal:
                print("猜太低了")
            else:
                print("猜太高了")
        else:
            print("請輸入數值:")

guessing_game()