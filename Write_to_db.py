import pyodbc
from datetime import date

class NorthWindDB:
    def __init__(self):
        self.name = "NorthWind"
        self.server = "localhost,1433"
        self.database_name = "NorthWind"
        self.user_name = "SA"
        self.password = "Passw0rd2018"
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database_name+';UID='+self.user_name+';PWD='+ self.password)
        self.my_northwind_cursor = self.connection.cursor()

class Table(NorthWindDB):
    def __init__(self):
        super().__init__()

    def create_operation(self,cardict):
        today = date.today()
        brand = cardict["Brand"]
        model = cardict["Model"]
        fuel_type = cardict["Fuel_type"]
        condition = cardict["Condition"]
        seller = cardict["Seller_name"]
        price = cardict["Price"]

        sql = "INSERT INTO Cars (Brand, Model, Fuel_type, Condition, Date_added, Seller_name, Price) Values('{}','{}','{}','{}','{}','{}','{}')".format(brand,model,fuel_type,condition,today,seller,price)
        insert_result_set = self.my_northwind_cursor.execute(sql)
        insert_result_set.commit()