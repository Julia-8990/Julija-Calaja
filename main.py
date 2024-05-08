import matplotlib.pyplot as plt
import numpy as np
from items import Cosmetics, Food, Clothing, Entertainment, Shop, Item
from shopping_cart import ShoppingCart

class Cosmetics:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

class Food:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

class Clothing:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

class Entertainment:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

class Shop:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class ItemFactory:
    @staticmethod
    def create_item(name, category, prices):
        if category.lower() == "cosmetics":
            return Cosmetics(name, prices)
        elif category.lower() == "food":
            return Food(name, prices)
        elif category.lower() == "clothing":
            return Clothing(name, prices)
        elif category.lower() == "entertainment":
            return Entertainment(name, prices)
        elif category.lower() == "shop":
            return Shop(name, prices)
        else:
            raise ValueError("Unsupported category")


cart = ShoppingCart()

cart.add_item(ItemFactory.create_item("Skin Care Cosmetics", "Cosmetics", [50, 55, 60]))
cart.add_item(ItemFactory.create_item("Decorative Cosmetics", "Cosmetics", [30, 35, 40]))
cart.add_item(ItemFactory.create_item("McDonald's", "Food", [20, 22, 25]))
cart.add_item(ItemFactory.create_item("Express Pizza", "Food", [15, 18, 20]))
cart.add_item(ItemFactory.create_item("Manami", "Food", [15, 18, 20]))
cart.add_item(ItemFactory.create_item("Sushi city", "Food", [0, 0, 0]))
cart.add_item(ItemFactory.create_item("Wok", "Food", [0, 0, 0]))
cart.add_item(ItemFactory.create_item("Gan bei", "Food", [10, 12, 15]))
cart.add_item(ItemFactory.create_item("Can can", "Food", [0, 0, 0]))
cart.add_item(ItemFactory.create_item("Bershka", "Clothing", [80, 85, 90]))
cart.add_item(ItemFactory.create_item("H&M", "Clothing", [50, 55, 60]))
cart.add_item(ItemFactory.create_item("Pull&Bear", "Clothing", [0, 0, 0]))
cart.add_item(ItemFactory.create_item("Stradivarius", "Clothing", [0, 0, 0]))
cart.add_item(ItemFactory.create_item("Sizeer", "Clothing", [200, 210, 220]))
cart.add_item(ItemFactory.create_item("Mohito", "Clothing", [100, 110, 120]))
cart.add_item(ItemFactory.create_item("Zara", "Clothing", [100, 105, 110]))
cart.add_item(ItemFactory.create_item("Movie Tickets", "Entertainment", [25, 28, 30]))
cart.add_item(ItemFactory.create_item("Park", "Entertainment", [10, 12]))
cart.add_item(ItemFactory.create_item("Attractions", "Entertainment", [100, 110]))
cart.add_item(ItemFactory.create_item("Museum", "Entertainment", [0, 0]))
cart.add_item(ItemFactory.create_item("Ice rink", "Entertainment", [10, 12, 15]))
cart.add_item(ItemFactory.create_item("Maxima", "Shop", [100, 90, 110]))
cart.add_item(ItemFactory.create_item("Norfa", "Shop", [50, 55]))
cart.add_item(ItemFactory.create_item("Iki", "Shop", [60, 65, 70]))
cart.add_item(ItemFactory.create_item("Rimi", "Shop", [0, 0]))


item_names = [item.name for item in cart.items if np.mean(item.prices) > 0]
item_prices = [np.mean(item.prices) for item in cart.items if np.mean(item.prices) > 0]


plt.style.use('dark_background')

plt.figure(figsize=(10, 10))
plt.pie(item_prices, labels=item_names, autopct='%1.1f%%', startangle=90, colors=plt.cm.viridis(np.linspace(0, 1, len(item_names))))
plt.title('Distribution of Item Costs in Cart')

plt.figure(figsize=(12, 8))
plt.bar(item_names, item_prices, color=plt.cm.plasma(np.linspace(0, 1, len(item_names))))
plt.xlabel('Items')
plt.ylabel('Average Price')
plt.title('Average Prices of Items')
plt.xticks(rotation=90)

for i, price in enumerate(item_prices):
    plt.text(i, price + 1, f'{price:.1f}', ha='center', color='white')

plt.tight_layout()
plt.show()
plt.show()
