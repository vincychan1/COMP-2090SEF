from goods import Goods, DiscountedGoods
class Cart:
    """Shopping cart class"""
    
    def __init__(self):
        """Initialize empty cart"""
        self.items = {}  # dictionary: {goods_id: {"goods": Goods object, "quantity": quantity}}
        self.total_price = 0.0
    
    def add_item(self, goods, quantity=1):
        """
        Add item to cart
        
        Args:
            goods (Goods): Product object
            quantity (int): Quantity
        
        Returns:
            bool: Success status
        """
        if quantity <= 0:
            print("Quantity must be greater than 0")
            return False
        
        goods_id = goods.goods_id
        if goods_id in self.items:
            self.items[goods_id]["quantity"] += quantity
        else:
            self.items[goods_id] = {"goods": goods, "quantity": quantity}
        
        self._update_total()
        print(f"Added {goods.name} x{quantity} to cart")
        return True
    
    def remove_item(self, goods_id, quantity=None):
        """
        Remove item from cart
        
        Args:
            goods_id (str): Product ID
            quantity (int, optional): Quantity to remove, None means remove all
        
        Returns:
            bool: Success status
        """
        if goods_id not in self.items:
            print(f"Product ID {goods_id} not in cart")
            return False
        
        if quantity is None or quantity >= self.items[goods_id]["quantity"]:
            # Remove all
            removed = self.items.pop(goods_id)
            print(f"Removed all {removed['quantity']} {removed['goods'].name}")
        else:
            # Remove partially
            self.items[goods_id]["quantity"] -= quantity
            print(f"Removed {self.items[goods_id]['goods'].name} x{quantity}")
        
        self._update_total()
        return True
    
    def update_quantity(self, goods_id, new_quantity):
        """
        Update item quantity
        
        Args:
            goods_id (str): Product ID
            new_quantity (int): New quantity
        
        Returns:
            bool: Success status
        """
        if goods_id not in self.items:
            print(f"Product ID {goods_id} not in cart")
            return False
        
        if new_quantity <= 0:
            return self.remove_item(goods_id)
        
        self.items[goods_id]["quantity"] = new_quantity
        self._update_total()
        print(f"Updated {self.items[goods_id]['goods'].name} quantity to {new_quantity}")
        return True
    
    def _update_total(self):
        """Update cart total price (internal method)"""
        self.total_price = 0.0
        for item in self.items.values():
            goods = item["goods"]
            quantity = item["quantity"]
            if isinstance(goods, DiscountedGoods):
                price = goods.get_discounted_price()
            else:
                price = goods.price
            self.total_price += price * quantity
    
    def get_items(self):
        """Get all items in cart"""
        return self.items
    
    def clear(self):
        """Clear cart"""
        self.items.clear()
        self.total_price = 0.0
        print("Cart cleared")
    
    def display_cart(self):
        """Display cart contents"""
        if not self.items:
            print("Cart is empty")
            return
        
        print("\n" + "="*50)
        print("Shopping Cart Contents:")
        print("-"*50)
        for i, (goods_id, item) in enumerate(self.items.items(), 1):
            goods = item["goods"]
            quantity = item["quantity"]
            unit_price = goods.get_discounted_price() if isinstance(goods, DiscountedGoods) else goods.price
            subtotal = unit_price * quantity
            
            discount_info = f" (Original: ${goods.price:.2f})" if isinstance(goods, DiscountedGoods) else ""
            print(f"{i}. {goods.name}{discount_info}")
            print(f"   Unit: ${unit_price:.2f} x {quantity} = ${subtotal:.2f}")
        
        print("-"*50)
        print(f"Total: ${self.total_price:.2f}")
        print("="*50)
    
    def __len__(self):
        """Return number of item types in cart"""
        return len(self.items)
    
    def __iter__(self):
        """Make cart iterable"""
        return iter(self.items.values())


class CartIterator:
    """Iterator for cart items"""
    
    def __init__(self, cart):
        self.cart = cart
        self.items = list(cart.items.values())
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item
