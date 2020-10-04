import random
randno=random.randint(1,100)
userguess=None
guesses=0
while userguess!=randno:
    userguess=int(input("enter the number: "))
    if userguess==randno:
        print("You entered the right number")
    else:
        if userguess<randno:
            print("You enterd wrong No.! enter bigger no")
        else:
            print("You enterd wrong No.! enter smaller no")
    guesses+=1        
print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
     hiscore = int(f.read())
if guesses<hiscore:
    print("You have just broken the high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))