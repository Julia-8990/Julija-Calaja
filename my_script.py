from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import seaborn as sns

class Item(ABC):
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

    @abstractmethod
    def get_category(self):
        pass

class Cosmetics(Item):
    def get_category(self):
        return "Cosmetics"

class Food(Item):
    def get_category(self):
        return "Food"

class Clothing(Item):
    def get_category(self):
        return "Clothing"

class Entertainment(Item):
    def get_category(self):
        return "Entertainment"
    
class Shop(Item):
    def get_category(self):
        return "Shop"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += sum(item.prices)
        return total

class PercentageCalculator:
    def calculate_percentage(self, total, category_totals):
        percentages = {}
        for category, amount in category_totals.items():
            percentage = (amount / total) * 100
            percentages[category] = percentage
        return percentages


def plot_pie_chart(percentages):
    labels = percentages.keys()
    sizes = percentages.values()
    plt.figure(figsize=(6, 6))
    sns.set_style("darkgrid")
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Spending Distribution")




def plot_bar_chart(categories, subcategories, expenses):
    plt.figure(figsize=(12, 8))
    sns.set_style("dark")
    for i in range(len(categories)):
        sns.barplot(x=subcategories[i], y=expenses[i], label=categories[i])
    plt.xlabel('Categories')
    plt.ylabel('Expenses')
    plt.title('Expenses by Categories and Subcategories')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()



def calculate_expenses(items):
    return [sum(item.prices) for item in items]


# Create instances of items
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


# Create a shopping cart and add items
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


# Calculate total spent
total_spent = cart.calculate_total()

# Calculate sums for each category
category_totals = {"Cosmetics": 0, "Food": 0, "Clothing": 0, "Entertainment": 0, "Shop": 0}
for item in cart.items:
    category = item.get_category()
    category_totals[category] += sum(item.prices)

# Calculate percentage distribution
calculator = PercentageCalculator()
percentages = calculator.calculate_percentage(total_spent, category_totals)

# Define categories and subcategories
categories = ['Cosmetics', 'Food', 'Entertainment', 'Clothing', 'Shop']
subcategories = [
    ['Skin Care Cosmetics', 'Decorative Cosmetics'],
    ['McDonald\'s', 'Express Pizza', 'Manami', 'Sushi city', 'Wok', 'Gan bei', 'Can can'],
    ['Movie Tickets', 'Park', 'Attractions', 'Museum', 'Ice rink'],
    ['Bershka', 'H&M', 'Pull&bear', 'Stradivarius', 'Sizeer', 'Mohito', 'Zara'],
    ['Maxima', 'Norfa', 'Iki', 'Rimi']
]

# Calculate expenses for each category
expenses = [
    calculate_expenses([cosmetics1, cosmetics2]),
    calculate_expenses([food1, food2, food3, food4, food5, food6, food7]),
    calculate_expenses([entertainment1, entertainment2, entertainment3, entertainment4, entertainment5]),
    calculate_expenses([clothing1, clothing2, clothing3, clothing4, clothing5, clothing6, clothing7]),
    calculate_expenses([shop1, shop2, shop3, shop4])
]

# Plot the bar chart and pie chart
plot_bar_chart(categories, subcategories, expenses)
plot_pie_chart(percentages)
plt.show()
