keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictin1 = dict(zip(keys, values))
print (dictin1)


family = {"Rick": 43, 'Beth': 13, 'Morty': 5, 'Summer': 8}
total_cost = 0
list_names = dict.keys(family)
print(list_names)
for name in list_names:
    if family[name]>3 and family[name]<12:
        price = 10
        print(name,":", price, "$") 
        total_cost = total_cost+10
    if family[name] >= 13:
        price = 15
        print(name, ":", price, "$") 
        total_cost = total_cost+10
    if family[name] < 3: 
        print(name, ": free of charge")
        total_cost = total_cost
print("Total sum equals:", total_cost, "$")
# ====================BONUS=============

family_unknown = {}
family = {"Rick": 43, 'Beth': 13, 'Morty': 5, 'Summer': 8}
total_cost = 0
list_names = dict.keys(family)
print(list_names)
for name in list_names:
    if family[name]>3 and family[name]<12:
        price = 10
        print(name,":", price, "$") 
        total_cost = total_cost+10
    if family[name] >= 13:
        price = 15
        print(name, ":", price, "$") 
        total_cost = total_cost+10
    if family[name] < 3: 
        print(name, ": free of charge")
        total_cost = total_cost
print("Total sum equals:", total_cost, "$")


# ====================ZARA=============

brand = {"name": "Zara",
        "creation_date": "1975",
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes": ["men", "women", "children", "home"], 
        "international_competitors": ["Gap", "H&M", "Benetton"],
        "number_stores": "7000",
        "major_color":  {
            "France": "blue", 
            "Spain": "red", 
            "US": ["pink", "green"]}
            }
print (brand)
brand["number_stores"] = 2
print(brand)
brand['clients'] = "everybody"
print(brand)
brand['country_creation'] = "Spain"
print(brand)
list_names = dict.keys(brand)
a = "international_competitors"
if a in list_names:
    brand["international_competitors"].append("Desigual")
print(brand)
del brand["creation_date"]
print(brand)
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())
more_on_zara = {"creation_date": "1975",
                "number_stores": "10000"}
brand.update(more_on_zara)

print("Updated info:", brand)
print(brand["number_stores"]) 
# info rewritten

# # --------------------Exercise 4---------------
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
result_b = {}
result_a = {}
i=0
for user in enumerate(users):
    result_b.update({user})
print (result_b)

for name in users:
    result_a.update({name:i})
    i=i+1
print (result_a)
