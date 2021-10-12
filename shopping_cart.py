class ShoppingCart:
    def __init__(self):
        self.shopping_cart_products = [""]

    def check_cart_total(self):
        self.total_products_in_cart = len(self.shopping_cart_products)
        print(self.total_products_in_cart)

    def add_new_product_to_cart(self, product):
        self.add_product = product
        self.shopping_cart_products.append(product)

    def empty_cart(self):
        user_verification_empty_cart = input(
            "Are you sure you want to empty your shopping cart? ")
        if user_verification_empty_cart.upper() == "YES":
            self.shopping_cart_products = [""]
            print("Ok, your shopping cart is now empty.")
        else:
            print(
                f"Ok, your shopping cart is still {self.shopping_cart_products}. ")
