import psycopg2
HOSTNAME='localhost'
USERNAME='postgres'
PASSWORD='220879'
DATABASE='Menu'
connection=psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

class MenuItem:
    @classmethod
    def check_exist(cls, name):
        with connection.cursor() as cursor:
            query=f"Select * from menu where item ='{name}'"
            cursor.execute(query)
            res=cursor.fetchall()
            if res:
                return True
            else:
                return False

    def __init__(self, item, price):
        self.item=item 
        self.price=price

    def save(self):
        with connection.cursor() as cursor:
            print(self.check_exist(self.item))
            if self.check_exist(self.item)==False:
                query=f"INSERT into menu (item, price) values ('{self.item}', {self.price})"
                print(query)
                cursor.execute(query)
                connection.commit()
            else:
                return False
            
    def delete(self, item):   
        with connection.cursor() as cursor:
            if self.check_exist(self.item)==True:
                query1=f"DELETE from menu WHERE item='{self.item}'"
                cursor.execute(query1)
                connection.commit()
                x=True
                return x
            else:
                x=False
                return x
            
    def update(self, item, price):
        with connection.cursor() as cursor:
            if self.check_exist(self.item)==True:
                query2=f"UPDATE menu SET price ={price} WHERE item = '{item}'"
                cursor.execute(query2)
                connection.commit()
                return True
            else:
                return False
    def get_by_name(self, item):
        with connection.cursor() as cursor:
            if self.check_exist(item)!=True:
                print(self.item)
                return None
            else:
                query=f"Select item, price from menu where item ='{item}'"
                cursor.execute(query)
                res=cursor.fetchall()
                return res
    def all(self):
        with connection.cursor() as cursor:
            query=f"Select item, price from menu"
            cursor.execute(query)
            res=cursor.fetchall()
            return res
        


    # def load_all(self):
    #     with connection.cursor() as cursor:
    #         query=f"Select item, price from menu"
    #         cursor.execute(query)
    #         res=cursor.fetchall()  
    #         for i in res:




a=MenuItem("Soup", 10)
# # a.save()
# # a.delete("Bread")
# # a.update("Potatoes", 2)
# print(a.get_by_name("Soup"))
print(a.all())





