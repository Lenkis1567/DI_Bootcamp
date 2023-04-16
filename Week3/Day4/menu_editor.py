import menu_manager as manager
def load_manager():
    a=manager.MenuManager()
    return a
def show_user_menu(a):
    print(a.menu) 
    order=input("What would you like to order? ")

def add_item_to_menu(a):
    name=input("What would you like to add? ")
    price=int(input("By which price? "))
    a.add_item(name, price)
    if a.add_item(name, price)==True:
        print("added")

def remove_item_from_menu(a):
    name=input("What would you like to remove from the menu ")
    a.remove_item(name)
    if a.remove_item(name)==True:
        print("Done")
    else:
        print("There is no such item in the menu")
n=load_manager()
show_user_menu(n)
add_item_to_menu(n)
remove_item_from_menu(n)
