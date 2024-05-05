import matplotlib.pyplot as plt
import numpy as np
from items import Cosmetics, Food, Clothing, Entertainment, Shop, Item
from shopping_cart import ShoppingCart

# Create instances of items and add them to the cart
cosmetics1 = Cosmetics("Skin Care Cosmetics", [50, 55, 60])
cosmetics2 = Cosmetics("Decorative Cosmetics", [30, 35, 40])
food1 = Food("McDonald's", [20, 22, 25])
food2 = Food("Express Pizza", [15, 18, 20])
food3 = Food("Manami", [15, 18, 20])
food4 = Food("Sushi city", [0, 0, 0])
food5 = Food("Wok", [0, 0, 0])
food6 = Food("Gan bei", [10, 12, 15])
food7 = Food('Can can', [0, 0, 0])
clothing1 = Clothing("Bershka", [80, 85, 90])
clothing2 = Clothing("H&M", [50, 55, 60])
clothing3 = Clothing("Pull&Bear", [0, 0, 0])
clothing4 = Clothing("Stradivarius", [0, 0, 0])
clothing5 = Clothing("Sizeer", [200, 210, 220])
clothing6 = Clothing("Mohito", [100, 110, 120])
clothing7 = Clothing("Zara", [100, 105, 110])
entertainment1 = Entertainment("Movie Tickets", [25, 28, 30])
entertainment2 = Entertainment("Park", [10, 12])
entertainment3 = Entertainment("Attractions", [100, 110])
entertainment4 = Entertainment("Museum", [0, 0])
entertainment5 = Entertainment("Ice rink", [10, 12, 15])
shop1 = Shop("Maxima", [100, 90, 110])
shop2 = Shop("Norfa", [50, 55])
shop3 = Shop("Iki", [60, 65, 70])
shop4 = Shop("Rimi", [0, 0])

# Create a shopping cart
cart = ShoppingCart()
cart.add_item(cosmetics1)
cart.add_item(cosmetics2)
cart.add_item(food1)
cart.add_item(food2)
cart.add_item(food3)
cart.add_item(food4)
cart.add_item(food5)
cart.add_item(food6)
cart.add_item(food7)
cart.add_item(clothing1)
cart.add_item(clothing2)
cart.add_item(clothing3)
cart.add_item(clothing4)
cart.add_item(clothing5)
cart.add_item(clothing6)
cart.add_item(clothing7)
cart.add_item(entertainment1)
cart.add_item(entertainment2)
cart.add_item(entertainment3)
cart.add_item(entertainment4)
cart.add_item(entertainment5)
cart.add_item(shop1)
cart.add_item(shop2)
cart.add_item(shop3)
cart.add_item(shop4)

# Prepare data for the graphs
item_names = [item.name for item in cart.items if np.mean(item.prices) > 0]
item_prices = [np.mean(item.prices) for item in cart.items if np.mean(item.prices) > 0]

# Use dark theme for the graphs
plt.style.use('dark_background')

# Build a pie chart
plt.figure(figsize=(10, 10))
plt.pie(item_prices, labels=item_names, autopct='%1.1f%%', startangle=90, colors=plt.cm.viridis(np.linspace(0, 1, len(item_names))))
plt.title('Distribution of Item Costs in Cart')

# Build a bar chart
plt.figure(figsize=(12, 8))
plt.bar(item_names, item_prices, color=plt.cm.plasma(np.linspace(0, 1, len(item_names))))
plt.xlabel('Items')
plt.ylabel('Average Price')
plt.title('Average Prices of Items')
plt.xticks(rotation=90)  # Rotate item names by 90 degrees for better readability
plt.tight_layout()  # Automatic adjustment of the subplot parameters to give specified padding

# Display all graphs simultaneously
plt.show()
