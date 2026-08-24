

class ShoppingCart:

    def __init__(self):
        self.cart = []

    def add_item(self, name, price, qty=1):
        for item in self.cart:
            if item["name"].lower() == name.lower():
                item["qty"] += qty
                print(f"Updated '{item['name']}': quantity is now {item['qty']}")
                return

        self.cart.append({"name": name, "price": price, "qty": qty})
        print(f"Added '{name}' (qty: {qty}, price: ${price:.2f})")

    def remove_item(self, name):
        self.cart = [item for item in self.cart if item["name"].lower() != name.lower()]
        print(f"Removed '{name}' from cart (if it existed).")

    def update_quantity(self, name, qty):
        for item in self.cart:
            if item["name"].lower() == name.lower():
                if qty <= 0:
                    self.remove_item(name)
                else:
                    item["qty"] = qty
                    print(f"'{item['name']}' quantity updated to {qty}")
                return
        print(f"'{name}' not found in cart.")

    def apply_discount(self, percent):
        if 1 <= percent <= 99:
            self.discount = percent
            print(f"Discount of {percent}% applied.")
        else:
            print("Error: discount percent must be between 1 and 99.")

    def subtotal(self):
        return sum(item["price"] * item["qty"] for item in self.cart)

    def generate_bill(self):
        if not self.cart:
            print("\nYour cart is empty.")
            return

        discount = getattr(self, "discount", 0)
        sub = self.subtotal()
        disc_amt = sub * discount / 100
        total = sub - disc_amt

        print(f"\n{'Item':<20}{'Qty':<6}{'Price':<10}{'Total'}")
        print("-" * 46)
        for item in self.cart:
            line_total = item["price"] * item["qty"]
            print(f"{item['name']:<20}{item['qty']:<6}${item['price']:<9.2f}${line_total:.2f}")

        print("-" * 46)
        print(f"{'Subtotal:':<36}${sub:.2f}")
        if discount:
            print(f"{'Discount (' + str(discount) + '%):':<36}-${disc_amt:.2f}")
        print(f"{'TOTAL:':<36}${total:.2f}")

    def most_expensive(self):
        if not self.cart:
            print("Cart is empty.")
            return
        item = max(self.cart, key=lambda i: i["price"])
        print(f"Most expensive item: '{item['name']}' at ${item['price']:.2f}")

    def sort_by_price(self):
        self.cart.sort(key=lambda i: i["price"], reverse=True)
        print("Cart sorted by price (highest first).")



if __name__ == "__main__":

    cart = ShoppingCart()

    cart.add_item("Apple", 0.50, 6)
    cart.add_item("Bread", 3.25, 2)
    cart.add_item("Milk", 2.75, 1)
    cart.add_item("Coffee", 8.99, 1)
    cart.add_item("Eggs", 4.10, 1)

    cart.add_item("Apple", 0.50, 4)   # should bump qty to 10, not duplicate

    cart.update_quantity("Bread", 5)

    cart.remove_item("Eggs")

    cart.most_expensive()

    cart.sort_by_price()

    cart.apply_discount(10)

    cart.generate_bill()