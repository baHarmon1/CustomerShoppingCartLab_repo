

class ShoppingCart:
    def __init__(self):
        self.shopping_cart_products = []

    def check_cart_total(self):
        self.total_products_in_cart = len(self.shopping_cart_products)
        print(self.total_products_in_cart)

    def add_product_to_cart(self):
        cust_done = False
        while cust_done == False:
            product = input("What would you like to add to your cart? ")
            self.shopping_cart_products.append(product)
            is_cust_done = input("Would you like to add anything else? ")
            if is_cust_done.upper() == "YES":
                cust_done = False
            else:
                cust_done = True

    def empty_cart(self):
        user_verification_empty_cart = input(
            "Are you sure you want to empty your shopping cart? ")
        if user_verification_empty_cart.upper() == "YES":
            self.shopping_cart_products = [""]
            print("Ok, your shopping cart is now empty.")
        else:
            print(
                f"Ok, your shopping cart is still {self.shopping_cart_products}. ")
