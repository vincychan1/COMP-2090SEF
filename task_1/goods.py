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

    def get_default_goods():
    return [
        Goods("001", "Apple", 6.5),
        Goods("002", "Milk", 12.0),
        Goods("003", "Chocolate", 8.0),
        Goods("004", "Biscuit", 7.5),
        Goods("005", "Bread", 10.0),
    ]

if __name__=="__main__":
    apple, milk, chocolate, biscuit, bread = get_default_goods()

    print(apple)
    print(milk)
    print(chocolate)
    print(biscuit)
    print(bread)

