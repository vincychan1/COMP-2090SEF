from goods import Goods
from Cashier import Cashier


class ShoppingCart:

    def __init__(self):
        # {product_id: [Goods, quantity]}
        self.items = {}

    def add_item(self, goods: Goods, quantity: float) -> None:
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if goods.id in self.items:
            self.items[goods.id][1] += quantity
            print(f"Updated {goods.name} quantity: {self.items[goods.id][1]}")
        else:
            self.items[goods.id] = [goods, quantity]
            print(f"Added to cart: {goods.name} x {quantity}")

    def remove_item(self, goods_id: str) -> None:
        if goods_id in self.items:
            name = self.items[goods_id][0].name
            del self.items[goods_id]
            print(f"Removed: {name}")
        else:
            print("Product not found in cart.")

    def update_quantity(self, goods_id: str, quantity: float) -> None:
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if goods_id not in self.items:
            print("Product not found in cart.")
            return

        self.items[goods_id][1] = quantity
        print("Quantity updated.")

    def clear(self) -> None:
        self.items.clear()
        print("Cart cleared.")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def get_total(self, apply_discount: bool = False) -> float:
        total = 0
        for goods_id in self.items:
            goods = self.items[goods_id][0]
            qty = self.items[goods_id][1]
            total += goods.price * qty

        if not apply_discount:
            return total

        if total >= 1000:
            return total - 300
        if total >= 500:
            return total - 100
        if total >= 300:
            return total - 50
        return total

    def display_cart(self) -> None:
        if self.is_empty():
            print("Cart is empty.")
            return

        print("\nCart:")
        print("-" * 45)
        for goods_id in self.items:
            goods = self.items[goods_id][0]
            qty = self.items[goods_id][1]
            subtotal = goods.price * qty
            print(f"{goods.id} {goods.name} x {qty} = ${subtotal:.2f}")
        print("-" * 45)
        print(f"Total (after discount): ${self.get_total(True):.2f}")

    def print_receipt(self) -> None:
        if self.is_empty():
            print("Cart is empty, cannot checkout.")
            return

        product = {}
        choice = []
        for goods_id in self.items:
            goods = self.items[goods_id][0]
            qty = self.items[goods_id][1]
            product[goods.name] = goods.price
            choice.append((goods.name, qty))

        Cashier(product, choice).ticket()
