import json
class MenuManager:
    def __init__(self):
        with open("restorant_menu.json", "r") as menuj:
            self.menu=json.load(menuj)

    def add_item(self, name, price):
        a={}
        a["name"]=name
        a["price"]=price
        self.menu["items"].append(a)
        return True
    # #  – this method should add an item to the menu, although do not save the changes to the file yet.

    def remove_item(self, name):
        for i in range(0,len(self.menu["items"])):
            if name != self.menu["items"][i]["name"]:
                n=False
            else:
                del self.menu["items"][i]
                print (self.menu)
                n=True
                break

        return n
    # # – if the item is in the menu, this function should remove it from the menu. If the item was not in the menu, return False. 


a=MenuManager()
a.add_item("Apple", 5)
# item=input("food: ")
# print(a.remove_item(item))



    # - When the manager is finished updating the menu this function should be called and it should save 
    # all the updates and write them into the the restaurant_menu.json file (ie. the file which holds the menu).