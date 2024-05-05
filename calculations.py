import matplotlib.pyplot as plt
from items import Item

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
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Spending Distribution")

def plot_bar_chart(categories, subcategories, expenses):
    plt.figure(figsize=(12, 8))
    for i in range(len(categories)):
        bars = plt.bar([j + i*0.1 for j in range(len(subcategories[i]))], expenses[i], width=0.1, label=categories[i])
        for j, bar in enumerate(bars):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"${expenses[i][j]}", ha='center', va='bottom')
            plt.text(bar.get_x() + bar.get_width() / 2, -5, subcategories[i][j], ha='center', va='bottom', rotation=90)

    plt.xlabel('Categories')
    plt.ylabel('Expenses')
    plt.title('Expenses by Categories and Subcategories')
    plt.legend()
    plt.tight_layout()