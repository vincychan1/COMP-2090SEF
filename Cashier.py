#import _______ 
#import _______

class Cashier:
    #product=shop's products,choice=users' product
    def __init__(self,product,choice): 
        self.product=product
        self.choice=choice
        
    #calculate the total price
    #discount: 1.⁠ ⁠滿300-50, 2.⁠ ⁠⁠滿500-100, 3.⁠ ⁠⁠滿1000-300
    def sum(self):
        user_volume=len(self.choice)
        i=0
        while i<user_volume:
            product_name=self.choice[i][0]
            product_quantity=self.choice[i][1]
            total_price=total_price+self.product[product_name]*product_quantity
            i=i+1
        if total_price>1000:
            total_price=total_price-300
        elif total_price>500:
            total_price=total_price-100
        elif total_price>300:
            total_price=total_price-50

        return total_price

    def ticket(self):
        print("---RECEIPT---")
        for row in self.choice:
            print(f"{row[0]:<10}{row[1]:<15}")
            
        print("-"*25)
        print("Total price: $",sum())
