from goods import Goods
from typing import Dict, List, Optional

class CartItem:
    """Shopping cart item class, representing a product and its quantity in the cart"""
    
    def __init__(self, goods: Goods, quantity: float):
        """
        Initialize a cart item
        
        Args:
            goods: Product object
            quantity: Product quantity
        """
        self.goods = goods
        self.quantity = quantity
    
    def get_subtotal(self) -> float:
        """
        Calculate subtotal amount
        
        Returns:
            float: Subtotal amount
        """
        return self.goods.price * self.quantity
    
    def __str__(self):
        """Return string representation of cart item"""
        return f"{self.goods.name}\t${self.goods.price:.2f}/{self.goods.unit}\t{self.quantity}{self.goods.unit}\t${self.get_subtotal():.2f}"
    
    def to_dict(self) -> dict:
        """
        Convert cart item to dictionary
        
        Returns:
            dict: Dictionary containing cart item information
        """
        return {
            "goods": self.goods.to_dict(),
            "quantity": self.quantity,
            "subtotal": self.get_subtotal()
        }


class ShoppingCart:
    """Shopping cart class, managing products in the cart"""
    
    def __init__(self):
        """Initialize an empty shopping cart"""
        self.items: Dict[str, CartItem] = {}  # Use product ID as key
    
    def add_item(self, goods: Goods, quantity: float) -> None:
        """
        Add product to cart
        
        Args:
            goods: Product object
            quantity: Product quantity
        """
        if quantity <= 0:
            print(f"Error: Quantity must be greater than 0")
            return
        
        if goods.id in self.items:
            # Product already exists, increase quantity
            self.items[goods.id].quantity += quantity
            print(f"Updated {goods.name} quantity, current total: {self.items[goods.id].quantity}{goods.unit}")
        else:
            # Product doesn't exist, add new item
            self.items[goods.id] = CartItem(goods, quantity)
            print(f"Added {goods.name} {quantity}{goods.unit} to cart")
    
    def remove_item(self, goods_id: str) -> None:
        """
        Remove product from cart
        
        Args:
            goods_id: Product ID
        """
        if goods_id in self.items:
            removed_item = self.items.pop(goods_id)
            print(f"Removed {removed_item.goods.name} from cart")
        else:
            print(f"Error: Product ID {goods_id} not in cart")
    
    def update_quantity(self, goods_id: str, quantity: float) -> None:
        """
        Update quantity of a product in cart
        
        Args:
            goods_id: Product ID
            quantity: New quantity
        """
        if quantity <= 0:
            print(f"Error: Quantity must be greater than 0")
            return
        
        if goods_id in self.items:
            old_quantity = self.items[goods_id].quantity
            self.items[goods_id].quantity = quantity
            goods_name = self.items[goods_id].goods.name
            print(f"Updated {goods_name} quantity from {old_quantity} to {quantity}")
        else:
            print(f"Error: Product ID {goods_id} not in cart")
    
    def get_items(self) -> List[CartItem]:
        """
        Get all items in the cart
        
        Returns:
            List[CartItem]: List of cart items
        """
        return list(self.items.values())
    
    def clear(self) -> None:
        """Clear the shopping cart"""
        self.items.clear()
        print("Shopping cart cleared")
    
    def is_empty(self) -> bool:
        """
        Check if cart is empty
        
        Returns:
            bool: True if cart is empty, False otherwise
        """
        return len(self.items) == 0
    
    def get_total(self) -> float:
        """
        Calculate total amount of the cart
        
        Returns:
            float: Total amount
        """
        total = 0.0
        for item in self.items.values():
            total += item.get_subtotal()
        return total
    
    def get_item_count(self) -> int:
        """
        Get number of product types in cart
        
        Returns:
            int: Number of product types
        """
        return len(self.items)
    
    def display_cart(self) -> None:
        """Display cart contents"""
        if self.is_empty():
            print("Shopping cart is empty")
            return
        
        print("\n" + "="*50)
        print("Shopping Cart Contents:")
        print("-"*50)
        print("Product Name\tPrice\t\tQuantity\tSubtotal")
        for item in self.get_items():
            print(f"{item.goods.name}\t${item.goods.price:.2f}/{item.goods.unit}\t{item.quantity}{item.goods.unit}\t${item.get_subtotal():.2f}")
        print("-"*50)
        print(f"Total:\t\t\t\t${self.get_total():.2f}")
        print("="*50)
    
    def to_dict(self) -> dict:
        """
        Convert cart contents to dictionary
        
        Returns:
            dict: Dictionary containing cart information
        """
        return {
            "items": [item.to_dict() for item in self.items.values()],
            "total": self.get_total(),
            "item_count": self.get_item_count()
        }
    
    @classmethod
    def from_dict(cls, data: dict, inventory: Dict[str, Goods]) -> 'ShoppingCart':
        """
        Create shopping cart object from dictionary
        
        Args:
            data: Dictionary containing cart information
            inventory: Product inventory dictionary for looking up product objects
            
        Returns:
            ShoppingCart: Shopping cart object
        """
        cart = cls()
        for item_data in data.get('items', []):
            goods_data = item_data.get('goods', {})
            goods_id = goods_data.get('id')
            
            if goods_id in inventory:
                # Use product from inventory
                goods = inventory[goods_id]
                quantity = item_data.get('quantity', 0)
                cart.add_item(goods, quantity)
            else:
                print(f"Warning: Product {goods_id} not in inventory, skipped")
        
        return cart
