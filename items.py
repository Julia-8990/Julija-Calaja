from abc import ABC, abstractmethod

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