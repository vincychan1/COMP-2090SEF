from goods import Goods
from cart import ShoppingCart
from cashier import Cashier, MemberDiscount, FullReductionDiscount
import json
import os
from typing import Dict, List


class SupermarketSystem:
    """Supermarket checkout system main class"""
    
    def __init__(self):
        """Initialize system"""
        self.inventory: Dict[str, Goods] = {}  # Product inventory, product ID to Goods object mapping
        self.cart = ShoppingCart()
        self.cashier = Cashier(cashier_id="001", counter_no="01")
        self.data_dir = "data"
        self.goods_file = os.path.join(self.data_dir, "goods.json")
        
        # Create data directory
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        # Load product data
        self.load_goods()
    
    def load_goods(self) -> None:
        """Load product data from JSON file"""
        if not os.path.exists(self.goods_file):
            print(f"Product file {self.goods_file} does not exist, creating default products")
            self.create_default_goods()
            return
        
        try:
            with open(self.goods_file, 'r', encoding='utf-8') as f:
                goods_list = json.load(f)
            
            self.inventory.clear()
            for goods_data in goods_list:
                goods = Goods.from_dict(goods_data)
                self.inventory[goods.id] = goods
            
            print(f"Successfully loaded {len(self.inventory)} products")
        except Exception as e:
            print(f"Failed to load product data: {e}")
            self.create_default_goods()
    
    def create_default_goods(self) -> None:
        """Create default product data"""
        default_goods = [
            {"id": "001", "name": "Apple", "price": 6.5, "unit": "lb"},
            {"id": "002", "name": "Milk", "price": 12.0, "unit": "carton"},
            {"id": "003", "name": "Bread", "price": 8.9, "unit": "loaf"},
            {"id": "004", "name": "Eggs", "price": 1.5, "unit": "egg"},
            {"id": "005", "name": "Rice", "price": 5.8, "unit": "lb"}
        ]
        
        for goods_data in default_goods:
            goods = Goods.from_dict(goods_data)
            self.inventory[goods.id] = goods
        
        self.save_goods()
        print("Created default product data")
    
    def save_goods(self) -> None:
        """Save product data to JSON file"""
        try:
            goods_list = [goods.to_dict() for goods in self.inventory.values()]
            with open(self.goods_file, 'w', encoding='utf-8') as f:
                json.dump(goods_list, f, ensure_ascii=False, indent=4)
            print(f"Product data saved to {self.goods_file}")
        except Exception as e:
            print(f"Failed to save product data: {e}")
    
    def display_goods(self) -> None:
        """Display all products"""
        print("\n" + "="*50)
        print("Product List:")
        print("-"*50)
        print("ID\tName\tPrice")
        for goods in self.inventory.values():
            print(f"{goods.id}\t{goods.name}\t${goods.price:.2f}/{goods.unit}")
        print("="*50)
    
    def add_to_cart(self) -> None:
        """Add product to cart"""
        self.display_goods()
        
        goods_id = input("Enter product ID: ").strip()
        if goods_id not in self.inventory:
            print(f"Error: Product ID {goods_id} does not exist")
            return
        
        try:
            quantity = float(input("Enter quantity: ").strip())
            if quantity <= 0:
                print("Error: Quantity must be greater than 0")
                return
            
            goods = self.inventory[goods_id]
            self.cart.add_item(goods, quantity)
        except ValueError:
            print("Error: Please enter a valid number")
    
    def view_cart(self) -> None:
        """View shopping cart"""
        self.cart.display_cart()
    
    def remove_from_cart(self) -> None:
        """Remove product from cart"""
        if self.cart.is_empty():
            print("Shopping cart is empty")
            return
        
        self.view_cart()
        goods_id = input("Enter product ID to remove: ").strip()
        self.cart.remove_item(goods_id)
    
    def update_cart_item(self) -> None:
        """Update cart item quantity"""
        if self.cart.is_empty():
            print("Shopping cart is empty")
            return
        
        self.view_cart()
        goods_id = input("Enter product ID to update: ").strip()
        
        try:
            quantity = float(input("Enter new quantity: ").strip())
            self.cart.update_quantity(goods_id, quantity)
        except ValueError:
            print("Error: Please enter a valid number")
    
    def clear_cart(self) -> None:
        """Clear shopping cart"""
        confirm = input("Are you sure you want to clear the cart? (y/n): ").strip().lower()
        if confirm == 'y':
            self.cart.clear()
    
    def set_discount(self) -> None:
        """Set discount strategy"""
        print("\nSelect discount strategy:")
        print("1. No discount")
        print("2. Member discount (5% off)")
        print("3. Full reduction (Spend $100 save $10)")
        
        choice = input("Choose (1-3): ").strip()
        
        if choice == '1':
            from cashier import DiscountStrategy
            self.cashier.set_discount_strategy(DiscountStrategy())
        elif choice == '2':
            self.cashier.set_discount_strategy(MemberDiscount(0.95))
        elif choice == '3':
            self.cashier.set_discount_strategy(FullReductionDiscount(100, 10))
        else:
            print("Invalid choice")
    
    def checkout(self) -> None:
        """Checkout"""
        if self.cart.is_empty():
            print("Shopping cart is empty, cannot checkout")
            return
        
        self.cashier.start_checkout(self.cart)
        receipt_data = self.cashier.checkout()
        
        if receipt_data:
            # Ask whether to save receipt
            save_choice = input("\nSave receipt? (1-JSON, 2-Text, 3-No): ").strip()
            if save_choice == '1':
                self.cashier.save_receipt_to_json(receipt_data)
            elif save_choice == '2':
                self.cashier.save_receipt_to_txt(receipt_data)
            
            # Clear cart after checkout
            self.cart.clear()
    
    def manage_goods(self) -> None:
        """Manage products"""
        while True:
            print("\n" + "="*50)
            print("Product Management")
            print("="*50)
            print("1. View all products")
            print("2. Add new product")
            print("3. Delete product")
            print("4. Modify product")
            print("5. Return to main menu")
            
            choice = input("Choose (1-5): ").strip()
            
            if choice == '1':
                self.display_goods()
            elif choice == '2':
                self.add_new_goods()
            elif choice == '3':
                self.delete_goods()
            elif choice == '4':
                self.modify_goods()
            elif choice == '5':
                break
            else:
                print("Invalid choice")
    
    def add_new_goods(self) -> None:
        """Add new product"""
        print("\nAdd new product:")
        
        goods_id = input("Product ID: ").strip()
        if goods_id in self.inventory:
            print(f"Error: Product ID {goods_id} already exists")
            return
        
        name = input("Product name: ").strip()
        if not name:
            print("Error: Product name cannot be empty")
            return
        
        try:
            price = float(input("Product price: ").strip())
            if price <= 0:
                print("Error: Price must be greater than 0")
                return
        except ValueError:
            print("Error: Please enter a valid number")
            return
        
        unit = input("Product unit: ").strip()
        if not unit:
            print("Error: Product unit cannot be empty")
            return
        
        goods = Goods(goods_id, name, price, unit)
        self.inventory[goods_id] = goods
        self.save_goods()
        print(f"Product {name} added successfully")
    
    def delete_goods(self) -> None:
        """Delete product"""
        self.display_goods()
        goods_id = input("Enter product ID to delete: ").strip()
        
        if goods_id in self.inventory:
            goods_name = self.inventory[goods_id].name
            confirm = input(f"Are you sure you want to delete {goods_name}? (y/n): ").strip().lower()
            if confirm == 'y':
                del self.inventory[goods_id]
                self.save_goods()
                print(f"Product {goods_name} deleted")
        else:
            print(f"Error: Product ID {goods_id} does not exist")
    
    def modify_goods(self) -> None:
        """Modify product information"""
        self.display_goods()
        goods_id = input("Enter product ID to modify: ").strip()
        
        if goods_id not in self.inventory:
            print(f"Error: Product ID {goods_id} does not exist")
            return
        
        goods = self.inventory[goods_id]
        print(f"\nCurrent product info: {goods}")
        print("Enter new information (press Enter to keep current value):")
        
        name = input(f"Product name [{goods.name}]: ").strip()
        if name:
            goods.name = name
        
        try:
            price_str = input(f"Product price [{goods.price}]: ").strip()
            if price_str:
                price = float(price_str)
                if price <= 0:
                    print("Error: Price must be greater than 0")
                else:
                    goods.price = price
        except ValueError:
            print("Error: Please enter a valid number")
        
        unit = input(f"Product unit [{goods.unit}]: ").strip()
        if unit:
            goods.unit = unit
        
        self.save_goods()
        print("Product information updated")
    
    def run(self) -> None:
        """Run main program"""
        print("\n" + "="*50)
        print("Welcome to OOP Supermarket Checkout System")
        print("="*50)
        
        while True:
            print("\nMain Menu:")
            print("1. Browse products")
            print("2. Add to cart")
            print("3. View cart")
            print("4. Modify cart")
            print("5. Clear cart")
            print("6. Set discount strategy")
            print("7. Checkout")
            print("8. Product management")
            print("9. Save and exit")
            
            choice = input("\nSelect operation (1-9): ").strip()
            
            if choice == '1':
                self.display_goods()
            elif choice == '2':
                self.add_to_cart()
            elif choice == '3':
                self.view_cart()
            elif choice == '4':
                print("\nModify Cart:")
                print("1. Remove item")
                print("2. Update quantity")
                sub_choice = input("Choose (1-2): ").strip()
                if sub_choice == '1':
                    self.remove_from_cart()
                elif sub_choice == '2':
                    self.update_cart_item()
                else:
                    print("Invalid choice")
            elif choice == '5':
                self.clear_cart()
            elif choice == '6':
                self.set_discount()
            elif choice == '7':
                self.checkout()
            elif choice == '8':
                self.manage_goods()
            elif choice == '9':
                self.save_goods()
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Invalid choice, please try again")


if __name__ == "__main__":
    system = SupermarketSystem()
    system.run()
