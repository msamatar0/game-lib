import random

def number_guess(scores):
    n = random.randint(0, 20)
    for i in range(5):
        guess = int(input("Guess the number: "))
        
        #End guessing game if equal
        if(n == guess):
            print("Guessed correct, congratulations!")
            scores[0] += 1
            break
        
        print("Incorrect! " +  
              ("Too high" if n < guess else "Too low") +
              (", but close..." if abs(n - guess) < 5 else "") +
              (f"\n{5 - (i + 1)} guesses remain.." if i < 4 else
               f"\nNo guesses remain\nCorrect answer was {n}")
              )
        
    return scores
    
#number_guess()