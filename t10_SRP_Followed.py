"""
+----------------+
|    Product     |
+----------------+
| - name: String |
| - price: double|
+----------------+
       ^
       |
       | 0..* simple association 
+-----------------------------+
|       ShoppingCart          |
+-----------------------------+
| + addProduct(p: Product)    |
| + calculateTotal(): double  |
+-----------------------------+
      ♦                    ♦
      | composition        | composition
      |                    |             
+----------------------------+   +----------------------------+
|   CartInvoicePrinter       |   |     CartDBStorage          |
+----------------------------+   +----------------------------+
| cart: ShoppingCart         |   | cart: ShoppingCart         |
| printInvoice()             |   | saveToDb()                 |
+----------------------------+   +----------------------------+

all arrows are straight and not dotted 
"""

class Product:

    def __init__(self, name , price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"{self.name} - ${self.price}"


class ShoppingCart:

    def __init__(self):
        self._products:list[Product] = []

    @property
    def products(self):
        return self._products
    
    def add_product(self, product):
        self._products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price 

        return total


class CartInvoice:

    def __init__(self, cart):
        self._cart: ShoppingCart = cart

    def print_invoice(self):
        print("Invoice")
        for product in self._cart.products:
            print(product)
        print(f"Total : ${self._cart.calculate_total()}")


class CartSaveToDb:

    def __init__(self, cart):
        self._cart: ShoppingCart = cart 

    def save_to_db(self):
        print("Saving shopping cart to DB")

p1 = Product('Laptop', 50000)
p2 = Product('Mouse', 500)

c = ShoppingCart()
c.add_product(p1)
c.add_product(p2)

i = CartInvoice(c)
i.print_invoice()

d = CartSaveToDb(c)
d.save_to_db()