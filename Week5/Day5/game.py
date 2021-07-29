import random
class Game:
    def __init__(self):
        self.user_input = ""
        self.computer_input = ""
    
    def get_user_item(self):
        user_input = input("your choice of rock, paper, or scissor please: ")
        user_input.lower()
        while True:
           if user_input  == "rock" or user_input  == "paper" or user_input  == "scissor":
                self.user_input = user_input
                return user_input
           user_input = input("your choice of rock, paper, or scissor please: ")
   
    def get_computer_item(self):
        computer_input = random.choice(["rock","paper","scissor"])
        self.computer_input = computer_input

        return computer_input

    def get_game_result(self):
        draw = "draw"
        user_win = "You won"
        computer_win = "computer won"
        # user_item = self.get_user_item()
        # computer_item = self.get_computer_item()
        user_item = self.user_input
        computer_item = self.computer_input
        if user_item == computer_item:
            return draw
        elif user_item == "rock" and computer_item == "scissor" :
            return user_win   
        elif user_item == "scissor" and computer_item == "paper" :
            return user_win
        elif user_item == "paper" and computer_item == "rock" :
            return user_win 
        elif computer_item == "rock" and user_item == "scissor" :
            return computer_win   
        elif computer_item == "scissor" and user_item == "paper" :
            return computer_win   
        elif computer_item == "paper" and user_item == "rock" :
            return computer_win   

