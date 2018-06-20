high = int(100)
low = int(0)
ans = 50

print("Please think of a number between {} and {}!".format(low, high))
print("Is your secret number {}?".format(ans))
answer = input(
    "Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ")

while True:
    if answer.lower() == "c":
        break
    if answer.lower() == "h":
        high = ans
        ans = int(high + low) / 2.0
        print("Is your secret number {}?".format(ans))
        answer = input(
            "Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ")
    elif answer.lower() == "l":
        low = ans
        ans = int(high + low) / 2.0
        print("Is your secret number {}?".format(ans))
        answer = input(
            "Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ")
    else:
        print("You have indicated a wrong letter")
        exit()
print("Game over. Your secret number was:{}".format(ans))
