class Cashier:
    #product=shop's products,choice=users' product
    def __init__(self,product,choice): 
        self.product=product
        self.choice=choice
        
    #calculate the total price
    #discount: 1.⁠ ⁠滿100-20 2.滿300-50, 3.⁠ ⁠⁠滿500-100, 4.⁠ ⁠⁠滿1000-300
    def sum(self):
        user_volume=len(self.choice)
        i=0
        total_price=0
        while i<user_volume:
            product_name=self.choice[i][0]
            product_quantity=self.choice[i][1]
            total_price=total_price+self.product[product_name]*product_quantity
            i=i+1
        if total_price>=1000:
            total_price=total_price-300
        elif total_price>=500:
            total_price=total_price-100
        elif total_price>=300:
            total_price=total_price-50
        elif total_price>=100:
            total_price=total_price-20


        return total_price

    def ticket(self):
        print("---RECEIPT---")
        total_before_discount = 0
        for row in self.choice:
            price = self.product[row[0]] * row[1]
            total_before_discount += price
            print(f"{row[0]:<10}{row[1]:<10}${self.product[row[0]]:.2f}  ${price:.2f}")
            
        print("-"*35)
        total_after_discount = self.sum()
        print(f"Subtotal: ${total_before_discount:.2f}")
        if total_after_discount < total_before_discount:
            discount = total_before_discount - total_after_discount
            print(f"Discount: -${discount:.2f}")
        print(f"Total: ${total_after_discount:.2f}")
