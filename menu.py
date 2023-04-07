import guess, rps, tictactoe, save
FILE_NAME = "log.txt"

def menu():
    game_file = save.save(FILE_NAME)
    save_data = game_file.load()
    
    while True:
        print("Welcome to the games menu! Pick a game to play:\n" +
          "1 - Rock-Paper-Scissors\n" +
          "2 - Number Guessing game\n" +
          "3 - Tic Tac Toe\n" +
          "4 - exit")
        choice = int(input("Enter # for which game you want to play: "))
        
        if choice == 1:
            print("1 - single-player\n2 - multi-player")
            mode = int(input("Pick gamemode: "))
            save_data[f"rps{mode}P"] = rps.rps(mode == 2, save_data[f"rps{mode}P"])
        elif choice == 2:
            save_data["guess"] = guess.number_guess(save_data["guess"])
        elif choice == 3:
            save_data["tictactoe"] = tictactoe.play_t3(save_data["tictactoe"])
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
    
    game_file.save(save_data)
    print("Thanks for playing, game over...")
    
menu()