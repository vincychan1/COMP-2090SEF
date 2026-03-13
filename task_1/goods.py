class Goods:
    def __init__(self,id:str,name:str,price:float):
        self.__id=id
        self.__name=name
        self.__price=price
    
    @property
    def id(self):
        return self.__id
    #product id
    
    @property
    def name(self):
        return self.__name
    #product name
    
    @property
    def price(self):
        return self.__price
    #product price

if __name__=="__main__":
    apple=Goods("001","Apple",7.5)
    milk=Goods("002","Milk",17.0)
    chocolate=Goods("003","Chocolate",20.0)
    biscuit=Goods("004","Biscuit",30.0)
    bread=Goods("005","Bread",15.5)
    instant_noodles=Goods("006","Instant noodles",25.5)
    soda=Goods("007","Soda",13.0)
    jelly=Goods("008","Jelly",10.0)
    potato_chips=Goods("009","Potato chips",18.0)
    rice_ball=Goods("010","Rice ball",10.0)
    sandwich=Goods("011","Sandwich",18.0)
    candy=Goods("012","Candy",15.0)

    print(apple)
    print(milk)
    print(chocolate)
    print(biscuit)
    print(bread)
    print(instant_noodles)
    print(soda)
    print(jelly)
    print(potato_chips)
    print(rice_ball)
    print(sandwich)
    print(candy)

