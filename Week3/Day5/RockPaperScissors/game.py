import random
list=["r", "p", "s"]
class Game:
    # def __init__(self,figure):
        
    def get_computer_item(self):
        computer_item=random.choice(list)
        return computer_item
    
    def get_game_result(self, figure, computer_item):
        print(f'your choice: {figure}, computer"s choice: {computer_item}')
        if computer_item==figure:
            return ["d", figure, computer_item]
        elif figure=="s" and computer_item=="p":
            return ["w", figure, computer_item]
        elif figure=="s" and computer_item=="r":
            return ["l", figure, computer_item]
        elif figure=="p" and computer_item=="s":
            return ["l", figure, computer_item]
        elif figure=="p" and computer_item=="r":
            return ["w", figure, computer_item]
        elif figure=="r" and computer_item=="s":
            return ["w", figure, computer_item]
        elif figure=="r" and computer_item=="p":
            return ["l", figure, computer_item]
         
a=Game()
comp=a.get_computer_item()
print(a.get_game_result("r", comp))