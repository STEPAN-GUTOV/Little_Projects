import datetime
import os
expenses_list = {}
class Expenses():
    __num = 0
    def __init__(self, purchase_value = '', price_value = '0'):
        self.__purchase = purchase_value
        self.__price = price_value
        self.__id = str(Expenses.__num)
        Expenses.__num += 1
        expenses_list[str(Expenses.__num)] = self
    def __str__(self):
        return str(self.id)+ '    ' + str(self.purchase) + ' - ' + str(self.price)+'$'
    @property
    def price(self):
        return(self.__price)
    @price.setter
    def price(self, value):
        self.__price = value
    @property
    def purchase(self):
        return(self.__purchase)
    @purchase.setter
    def purchase(self, value):
        self.__purchase = value
    @property
    def id(self):
        return(self.__id)
    @id.setter
    def id(self, value):
        self.__id = value

def total(expenses_list = expenses_list):
    summ = 0
    for i in expenses_list:
        summ += int(expenses_list[i].price)
    return str(summ)
def print_expenses(expenses_list = expenses_list):
    for i in expenses_list:
        print(expenses_list[i])
