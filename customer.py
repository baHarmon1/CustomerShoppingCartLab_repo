from shopping_cart import ShoppingCart


class Customer:
    def __init__(self, name):
        self.name = name
        self.cust_shopping_cart = ShoppingCart()

    def view_cart(self):
        for product in self.cust_shopping_cart.shopping_cart_products:
            print(product)
