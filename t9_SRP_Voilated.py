"""

+----------------------+
|       Product        |
+----------------------+
| - name  : String     |
| - price : double     |
+----------------------+

            0..*
             |
             |
             v
+-------------------------------+
|        ShoppingCart           |
+-------------------------------+
| - products : List<Product>    |
+-------------------------------+
| + calcTotalPrice() : double   |
| + printInvoice()   : void     |
| + saveToDB()       : void     |
+-------------------------------+

Voilates SRP as shopping cart has 3 responsibilities
"""

class Product:

    def __init__(self, name , price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class ShoppingCart:

    def __init__(self):
        self._products:Product = []

    @property
    def products(self):
        return self._products
    
    def add_products(self, product):
        self._products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price 

        return total

    # voilates SRP
    def print_invoice(self):
        print("Invoice")
        for product in self.products:
            print(product)
        print(f"Total : ${self.calculate_total()}")

    # voilates SRP
    def save_to_db(self):
        print("Saving shopping cart to DB")


p1 = Product('Laptop', 50000)
p2 = Product('Mouse', 500)

c = ShoppingCart()
c.add_products(p1)
c.add_products(p2)

c.print_invoice()
c.save_to_db()