import random

def rps(p2control, scores):
    print("Welcome to rock, paper, scissors: " +
          ("Multiplayer Edition..." if p2control else "Singleplayer Edition...") + "\n")
    print(scores)
    valid = True
    result = None
    playing = True

    while playing == True:
        player1 = input("Player 1, choose: ").lower()
        if(player1 == "r" or player1 == "p" or player1 == "s"):
            pass
        else:
            valid = False
        
        #p2control decides if p2 is another player or random
        if(p2control):
            player2 = input("Player 2, choose: ").lower()
            if(player2 == "r" or player2 == "p" or player2 == "s"):
                pass
            else:
                valid = False
        else:
            player2 = random.choice(("r", "p", "s"))
            print("Player 2 chose " + player2)

        if(valid):
            if((player1 == "r" and player2 == "s") or (player1 == "s" and player2 == "p") or (player1 == "p" and player2 == "r")):
                result = "Player 1 wins!"
                scores[0] += 1
            elif(player1 == player2):
                result = "Draw."
            else:
                result = "Player 2 wins!"
                if p2control:
                    scores[1] += 1
        else:
            result = "Invalid input, no contest.."
            
        print(result)
        retry = input("Continue playing? y/n: ").lower()
        if(retry == "y" or retry == "n"):
            if(retry == "y"):
                playing = True
                valid = True
            else: break
        else:
            print("Invalid input")
            break
        
    return scores
                
#rps()