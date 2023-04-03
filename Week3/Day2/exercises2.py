class Family:
    def __init__(self, last_name):
        self.members = [
                        {'name':'Michael','age':35,'gender':'Male','is_child':False},
                        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
                     ]
        self.last_name = last_name
    def born(self, new_member):
        self.members.append(new_member)
        if 0<new_member["age"]<7:
            new_member['is_child'] = True
            print('Congratulations!')
        else:
            new_member['is_child'] = False
    def is_18(self, old_guy):
        if old_guy["age"] > 18:
            a = True
        else:
            a=False
        return a         
    def family_presentation(self):
        print("The family name is: ", self.last_name)
        for mem in range(0, len(self.members)):
            one_person=self.members[mem]
            print("Name: ", one_person["name"])

class Incredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self_members =  [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
                         ]
    def use_power(self, member):
        if self.is_18(member) == True:
            print(f'The power of {member["name"]} is {member["power"]}')
    def incredible_presentation(self):
        print("The family name is: ", self.last_name)
        for mem in range(0, len(self.members)):
            one_person=self.members[mem]
            print (f'Name: , {one_person["name"]}, power: {one_person ["incredible_name"]}')


a = Family("Ivanov")  
print(a.members)
# new_member = {}
# new_member['name']=input("Input name: ")
# new_member['age'] = int(input("Input age: "))
# new_member['gender'] = input("Input gender: ")
# a.born(new_member)
# a.is_18(new_member)
# print(a.last_name)
# print(a.is_18(new_member))
# a.family_presentation()

new_member = {}
super = Incredibles("Super")
new_member['name']=input("Input name: ")
new_member['age'] = int(input("Input age: "))
new_member['gender'] = input("Input gender: ")
new_member['power'] = input("Input power: ")
new_member['incredible_name'] = input("Input incredible name: ")
super.born(new_member)
super.family_presentation()
super.use_power(new_member)
super.incredible_presentation()