class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Cart:
    def __init__(self):
        self.products = []

    def __str__(self):
        return f"Total cost: {self.total()}"

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def total(self):
        return sum(map(lambda p: p.price, self.products))
    
cart = Cart()

tshirt = Product("Футболка", 1200, "Верхняя одежда")
sneekers = Product("Кроссовки", 2700, "Спортивная обувь")
winter_hat = Product("Зимняя шапка", 900, "Зимняя одежда")

cart.add_product(tshirt)
cart.add_product(sneekers)
cart.add_product(winter_hat)

cart.remove_product(winter_hat)

print(cart)