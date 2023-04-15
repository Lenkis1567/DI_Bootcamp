import menu_manager as manager
def load_manager():
    a=manager.MenuManager()
    return a
def show_user_menu(self):
    print(self.menu) 
    order=input("What would you like to order? ")

def add_item_to_menu(self):
    name=input("What would you like to add? ")
    price=int(input("By which price? "))
    manager.add_item(name, price)

def remove_item_from_menu(self):
    name=input("What would you like to remove from the menu ")
    manager.remove_item(self, name)


n=load_manager()
show_user_menu(n)
add_item_to_menu(n)
remove_item_from_menu(n)
