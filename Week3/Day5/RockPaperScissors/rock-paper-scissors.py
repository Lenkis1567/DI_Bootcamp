import game
x="g"
results_list=[]
while x!="x":
    print("Menu")
    print("(g)Play a new game")
    print("(x) Show scores and exit")
    x=input()
    print("Select(r) rock, (p) paper or (s) scissors")
    a=Game()
    computer_item=a.get_computer_item()
    figure=input()
    result=a.get_game_result(figure, computer_item)
    print(result)
    results_list.append(result)
else:
    # to calculate each letter appearance
    print("Game results:")
    print(f"You won: {w} times")
    print(f"You lost: {l} times")
    print(f"You drew: {d} times")
