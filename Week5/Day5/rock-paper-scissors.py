from game import Game

def play():
    game = Game()
    user_item = game.get_user_item()
    comp_item = game.get_computer_item()
    game_results =game.get_game_result()
    print(f"you played {user_item} and the computer played {comp_item}. the result is {game_results}")
    return game_results


def get_user_menu_choice():
    doing = input("You can Play, show results or quit: ")
    if doing == "quit":
        return doing
    elif doing == "play":
        return doing
    elif doing == "results":
        return doing        

def  print_result(results):
    user_wins = results["wins"]
    user_lossses = results["losses"]
    user_ties = results["ties"]
    print(f"You have won {user_wins} games, lost {user_lossses} games and tied {user_ties} games")  

def main():
    results = {
        "wins": 0,
        "losses": 0,
        "ties": 0
    }
    while True:
        choice = get_user_menu_choice()
        if choice == "quit":
            break
        if choice == "play":
           result = play()
           if result == "draw":
               results["ties"] += 1
               continue
           elif result == "You won":
               results["wins"] += 1
               continue
           elif result == "computer won":
               results["losses"] += 1
               continue
        if choice == "results":
            print_result(results)
        else:
            print("not a valid choice")
    print_result(results)

main()