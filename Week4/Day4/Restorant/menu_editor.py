import menu_manager as m
def load_manager(a, price):
    new_dish=m.MenuItem(a, price)
    return new_dish
def show_user_menu():
    print("MENU")
    print("(a) Add an item")
    print("(d) Delete an item")
    print("(v) View the menu")
    print("(x) Exit")
    resul=input("")
    return resul
def add_item_to_menu(new_dish, item, price):
    new_dish.update(item, price)
    if new_dish.update(item, price)==True:
        return True 
    else:
        return False
def remove_item_from_menu(old_dish, item):
    old_dish.delete(item)
    if old_dish.delete(item)==True:
        return True
    else:
        return False
    
def show_restaurant_menu(watch):
    print(f'Here is our menu {watch.all()}')

whole_menu=[]
while True:
    b=show_user_menu()
    if b=='a':
        item=input("Which dish would you like to add?: ")
        price=input("What will be the price of the dish? ")
        new_dish=load_manager(item, price)
        new_dish.save()
        print(f'New dish {new_dish.item} with price {new_dish.price} added')


    if b=='d':
        item_del=input("Which dish would you like to delete?: ")
        old_dish=load_manager(item_del, 10)
        a= old_dish.delete(item_del)
        if a==True:
            print(f"You've deleted {old_dish.item}")
        else:
            print("There is no such dish") 
    

    if b=='v':
        watch=load_manager('item', 1)
        show_restaurant_menu(watch)
        break

    if b=='x':
        ex=load_manager("ext", 1)
        show_restaurant_menu(ex)
        break 


    
