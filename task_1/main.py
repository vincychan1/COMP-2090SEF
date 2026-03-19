import json
from goods import Goods, get_default_goods
from cart import ShoppingCart
from Cashier import Cashier


class SupermarketSystem:
    def setup(self):
        self.inventory = {}
        self.cart = ShoppingCart()
        self.admin_password = "admin123"
        self.goods_file = "goods.json"
        self.load_goods()

    def load_goods(self):
        self.inventory = {}
        try:
            with open(self.goods_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                gid = item.get("id")
                name = item.get("name")
                price = item.get("price")
                if gid and name and price is not None:
                    self.inventory[gid] = Goods(gid, name, float(price))
        except Exception:
            pass

        if len(self.inventory) == 0:
            for g in get_default_goods():
                self.inventory[g.id] = g

    def save_goods(self):
        with open(self.goods_file, "w", encoding="utf-8") as f:
            data = [g.to_dict() for g in self.inventory.values()]
            json.dump(data, f, ensure_ascii=False, indent=2)

    def show_goods(self):
        print("\n" + "=" * 45)
        print("ID      Name                Price")
        print("-" * 45)
        for g in self.inventory.values():
            print(f"{g.id:<8}{g.name:<20}${g.price:>8.2f}")
        print("=" * 45)

    def input_positive(self, prompt):
        try:
            n = float(input(prompt).strip())
            if n <= 0:
                return None
            return n
        except ValueError:
            return None

    def input_positive_int(self, prompt):
        text = input(prompt).strip()
        if not text.isdigit():
            return None
        n = int(text)
        if n <= 0:
            return None
        return n

    def show_main_menu(self):
        print("\n" + "=" * 45)
        print("         Supermarket Main Menu")
        print("=" * 45)
        print(" 1. Browse Products    2. View Cart")
        print(" 3. Edit Cart          4. Clear Cart")
        print(" 5. View Discounts     6. Checkout")
        print(" 7. Product Admin      8. Save and Exit")
        print("=" * 45)

    def show_manage_menu(self):
        print("\n" + "=" * 45)
        print("            Product Admin Menu")
        print("=" * 45)
        print(" 1. Manage Product")
        print(" 2. Back to Main Menu")
        print("=" * 45)

    def print_checkout_receipt(self):
        product = {}
        choice = []
        for goods_id in self.cart.items:
            goods = self.cart.items[goods_id][0]
            qty = self.cart.items[goods_id][1]
            product[goods.name] = goods.price
            choice.append((goods.name, qty))

        Cashier(product, choice).ticket()

    def manage_single_product(self):
        self.show_goods()
        modify = input("Do you want to modify this product? (y/n): ").strip().lower()
        if modify != "y":
                print("Cancelled.")
                return
        elif modify == "y":
            gid = input("Product ID: ").strip()
            if not gid:
                print("Invalid ID.")
                return

            if gid in self.inventory:
                old = self.inventory[gid]
                print(f"Found: {old.id} | {old.name} | ${old.price:.2f}")
            
            
            
                action = input("Choose action: [E]dit / [D]elete / [C]ancel: ").strip().lower()

            if action == "d":
                del self.inventory[gid]
                self.save_goods()
                print("Product deleted.")
            elif action == "e":
                name = input(f"Name [{old.name}]: ").strip() or old.name
                ptxt = input(f"Price [{old.price}]: ").strip()
                price = old.price
                if ptxt:
                    try:
                        p = float(ptxt)
                        if p > 0:
                            price = p
                    except ValueError:
                        print("Invalid price, keeping old price.")
                self.inventory[gid] = Goods(gid, name, price)
                self.save_goods()
                print("Product updated.")
            else:
                print("Cancelled.")
        else:
            print("Product not found.")
            if input("Add as new product? (y/n): ").strip().lower() != "y":
                return
            name = input("Name: ").strip()
            price = self.input_positive("Price: ")
            if not name or price is None:
                print("Invalid input.")
                return
            self.inventory[gid] = Goods(gid, name, price)
            self.save_goods()
            print("Product added.")

    def show_cart_edit_menu(self):
        print("\n" + "=" * 45)
        print("              Edit Cart Menu")
        print("=" * 45)
        print(" 1. Remove Product")
        print(" 2. Change Quantity")
        print("=" * 45)

    def manage_goods(self):
        while True:
            if input("Admin password: ").strip() == self.admin_password:
                break
            print("Wrong password, please try again.")

        while True:
            self.show_manage_menu()
            c = input("Choose (1-2): ").strip()
            if c == "1":
                self.manage_single_product()
            elif c == "2":
                break
            else:
                print("Invalid choice.")

    def run(self):
        self.setup()
        while True:
            self.show_main_menu()
            c = input("Choose (1-8): ").strip()

            if c == "1":
                self.show_goods()
                if input("Add product to cart? (y/n): ").strip().lower() != "y":
                    continue
                gid = input("Product ID: ").strip()
                if gid not in self.inventory:
                    print("ID not found.")
                    continue
                qty = self.input_positive_int("Quantity (integer): ")
                if qty is None:
                    print("Invalid quantity. Please enter a positive integer.")
                    continue
                self.cart.add_item(self.inventory[gid], qty)
            elif c == "2":
                self.cart.display_cart()
            elif c == "3":
                if self.cart.is_empty():
                    print("Cart is empty.")
                    continue
                self.cart.display_cart()
                self.show_cart_edit_menu()
                sub = input("Choose (1-2): ").strip()
                gid = input("Product ID: ").strip()
                if sub == "1":
                    self.cart.remove_item(gid)
                elif sub == "2":
                    qty = self.input_positive_int("New quantity (integer): ")
                    if qty is not None:
                        self.cart.update_quantity(gid, qty)
                    else:
                        print("Invalid quantity. Please enter a positive integer.")
                else:
                    print("Invalid choice.")
            elif c == "4":
                if input("Clear cart? (y/n): ").strip().lower() == "y":
                    self.cart.clear()
            elif c == "5":
                print("Discounts: >=300 -50, >=500 -100, >=1000 -300")
            elif c == "6":
                if self.cart.is_empty():
                    print("Cart is empty.")
                    continue
                self.print_checkout_receipt()
                if input("Confirm purchase? (y/n): ").strip().lower() == "y":
                    print("Payment successful.")
                    self.cart.clear()
            elif c == "7":
                self.manage_goods()
            elif c == "8":
                self.save_goods()
                print("Goodbye.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    SupermarketSystem().run()
