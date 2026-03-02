from goods import Goods, DiscountedGoods
from cart import Cart
from cashier import Cashier


def setup_test_data():
    """Create test product data"""
    
    # Regular goods
    apple = Goods("G001", "Fuji Apple", 8.5, "Fruits")
    banana = Goods("G002", "Imported Banana", 6.8, "Fruits")
    milk = Goods("G003", "Fresh Milk 1L", 12.9, "Dairy")
    bread = Goods("G004", "Whole Wheat Bread", 9.9, "Bakery")
    
    # Discounted goods
    cola = DiscountedGoods("G005", "Cola 500ml", 3.5, "Beverages", 0.8)  # 20% off
    chocolate = DiscountedGoods("G006", "Dark Chocolate", 15.0, "Snacks", 0.75)  # 25% off
    
    goods_dict = {
        "G001": apple,
        "G002": banana,
        "G003": milk,
        "G004": bread,
        "G005": cola,
        "G006": chocolate
    }
    
    return goods_dict


def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("       OOP SUPERMARKET CHECKOUT SYSTEM")
    print("="*50)
    print("1. View Products")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Update Item Quantity")
    print("5. Remove Item")
    print("6. Checkout")
    print("7. View Sales Report")
    print("8. Clear Cart")
    print("0. Exit System")
    print("-"*50)


def main():
    """Main function"""
    
    # Initialize
    goods_dict = setup_test_data()
    cart = Cart()
    cashier = Cashier("01")
    
    print("Welcome to OOP Supermarket Checkout System!")
    
    while True:
        display_menu()
        choice = input("Select option (0-8): ").strip()
        
        if choice == "0":
            print("Thank you for using. Goodbye!")
            break
        
        elif choice == "1":
            print("\nProduct List:")
            for goods in goods_dict.values():
                print(f"  {goods}")
        
        elif choice == "2":
            print("\nAvailable Products:")
            for gid, goods in goods_dict.items():
                print(f"  {gid}: {goods.name} - ${goods.price}")
            
            gid = input("Enter Product ID: ").strip().upper()
            if gid not in goods_dict:
                print("Product ID not found!")
                continue
            
            try:
                qty = int(input("Enter quantity: ").strip())
                cart.add_item(goods_dict[gid], qty)
            except ValueError:
                print("Quantity must be an integer!")
        
        elif choice == "3":
            cart.display_cart()
        
        elif choice == "4":
            cart.display_cart()
            gid = input("Enter Product ID to update: ").strip().upper()
            try:
                new_qty = int(input("Enter new quantity: ").strip())
                cart.update_quantity(gid, new_qty)
            except ValueError:
                print("Quantity must be an integer!")
        
        elif choice == "5":
            cart.display_cart()
            gid = input("Enter Product ID to remove: ").strip().upper()
            cart.remove_item(gid)
        
        elif choice == "6":
            if not cart.get_items():
                print("Cart is empty, cannot checkout")
                continue
            
            cashier.start_checkout(cart)
            
            try:
                tax_rate = float(input("Enter tax rate (e.g., 0.13 for 13%, Enter for 0): ").strip() or "0")
                amount = float(input("Enter payment amount: ").strip())
                cashier.process_payment(amount, tax_rate)
            except ValueError:
                print("Invalid input format!")
        
        elif choice == "7":
            cashier.get_sales_report()
        
        elif choice == "8":
            confirm = input("Clear cart? (y/n): ").strip().lower()
            if confirm == 'y':
                cart.clear()
        
        else:
            print("Invalid option, please try again!")


if __name__ == "__main__":
    main()
