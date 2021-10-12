from customer import Customer
from shopping_cart import ShoppingCart
from product import Product

cust_1 = Customer("Brycen")
cust_1.cust_shopping_cart.add_product_to_cart()
print(cust_1.cust_shopping_cart.shopping_cart_products)
print(cust_1.view_cart())
