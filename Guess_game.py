secrect_number=95
guess_limit=5
guess_count=0
while guess_count < guess_limit:
    guess=int(input(">Guess :"))
    guess_count += 1
    if(guess == secrect_number):
        print("You Won ! ")
        break
else :
    print("Sorry you failed !")