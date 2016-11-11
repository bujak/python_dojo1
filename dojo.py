import random
import sys
import time

name = input('What is your name?' )
input_num = int(sys.argv[1])
def game():
    print('Well, %s, I\'m thinking of a number between 1 and %i.' %(name, input_num))
    number = random.randrange(1,input_num)
    #print(number)
    count = 1
    while True:
        start_time = time.time()
        guess = int(input("What is your # " + str(count) + " guess?"))
        if guess > number:
            print(guess, "is too high")
            count += 1
        elif guess < number:
            print(guess, "is too low")
            count += 1
        elif guess == number:
            elapsed = time.time() - start_time
            print(elapsed)
            print("YES!!!", number, "is my secret number! Congratulations!!! You guessed my number in ", count, "guess")
            again = input("Do you want to play again?")
            if again == 'yes':
                game()
            else:
                sys.exit()

game()
