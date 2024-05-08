# Kursinio darbo ataskaita 
## Įvadas 
Šio kursinio darbo tikslas yra sukurti programą, kuri valdo išlaidas skirtingose kategorijose.
Programa leidžia vartotojams stebėti savo išlaidas įvairiose srityse, tokiose kaip kosmetika, maistas, drabužiai, pramogos ir bendros pirkinių kategorijos. Programa yra „Python“ programa, skirta padėti  vartotojams sekti jų išlaidas pagal kategorijas. Ji leidžia vartotojams įvesti savo išlaidas įvairiems produktams, juos klasifikuoti, o tada analizuoti savo vartotojų įpročius su vizualizacijomis.

Norėdami paleisti programą, įsitikinkite, kad jūsų kompiuteryje yra įdiegtas „Python“. Tada įvykdykite „Python“ scenarijų, kuriame yra programa. 

Paleidus programą, vartotojai gali pridėti prekių į krepšelį, 
nurodydami jų pavadinimą ir kainą. Programa automatiškai klasifikuoja prekes pagal iš anksto nustatytas kategorijas. Pridėjus visas prekes, vartotojas gali apskaičiuoti bendras išlaidas ir vizualizuoti savo išlaidų paskirstymą, naudojant skritulines ir stulpelines diagramas.

# Analizė 

Ši programinė įranga yra apsipirkimo išlaidų analizės programa, kurioje duomenų vizualizavimui naudojama Matplotlib biblioteka. Ji modeliuoja pirkinių krepšelį su įvairiomis skirtingų kategorijų prekėmis ir paslaugomis, o paskui pateikia duomenis taip, kad būtų lengviau suprasti išlaidų pasiskirstymą.


#### Singleton modelis
Programoje naudojama ShoppingCart klasė, kuri atvaizduoja pirkinių krepšelį. Ji įgyvendina Singleton šabloną, nes sukuriamas tik vienas pirkinių krepšelio egzempliorius.

~~~
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
~~~
#### Factory Method
Šiame pavyzdyje pateiktas fabrikinis metodas yra create_item metodas klasėje ShoppingCart. Šis metodas priima tris argumentus: name, category ir prices, ir pagal nurodytą prekės kategoriją sukuria atitinkamą prekės objektą. Taigi, šis metodas veikia kaip fabrikinis metodas, kuris sukuria ir grąžina konkrečios kategorijos prekės objektą pagal nurodytus duomenis.
~~~
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
...
~~~
#### Polymorphism and Abstraction
Šiame kode polimorfizmas pasireiškia panaudojant paveldėjimą ir abstrakčią bazinę klasę Item. Paveldėtos klasės (Cosmetics, Food, Clothing, Entertainment, Shop) yra įgyvendinamos su skirtingais kategorijų pavadinimais. Tai parodo, kad jos panaudoja abstrakčią Item klasę, tačiau turi unikalų elgesį, kuris priklauso nuo kategorijos. Taigi, kiekviena iš šių klasių turi get_category() metodą, bet šio metodo elgesys skiriasi priklausomai nuo to, kokia yra konkreti klasė. Tai yra polimorfinis elgesys, nes tas pats metodas gali būti iškviečiamas iš Item tipo objekto, bet jo elgesys bus skirtingas pagal konkretų objektą.
~~~
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
~~~

#### Inheritance
Šioje programoje kiekviena produktų kategorija paveldi bendras savybes ir metodus iš elemento sąsajos, todėl juos galima vienodai naudoti programoje.
~~~
class Item(ABC):
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices
        ...
class Food(Item):
    def __init__(self, name, prices):
        super().__init__(name, prices)
        ...
~~~
#### Encapsulation
Šis kodo fragmentas demonstruoja enkapsuliaciją. ShoppingCart klasė turi privačią savybę items, kurioje saugomi visi krepšelyje esantys elementai. Ši savybė yra pasiekiamas tik per klasės metodus, pavyzdžiui, add_item. Taip pat, calculate_total metodas leidžia apskaičiuoti krepšelio prekių sumą ir yra prieinamas tik per ShoppingCart sąsają. Tai užtikrina, kad išoriniai vartotojai negalės tiesiogiai prieiti prie krepšelio turinio ar jo skaičiavimo logikos, išlaikant krepšelio būsenos saugumą ir suteikiant valdymą per klasės sąsają.
~~~
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
~~~
# Rezultatai ir Santrauka 
## Rezultatai 
Programa sėkmingai stebi išlaidas skirtingose kategorijose. Komplikacijos, su kuriomis susidūrėme vykdant realizaciją, apima: 
- Tikslaus prekių klasifikavimo ir skirtingų įvesties formatų tvarkymo užtikrinimas. 
- Diagramų dizaino pakeitimas, siekiant pagerinti jų skaitymą ir estetiką. 
- Sėkmingai įgyvendinta programos struktūra ir funkciniai galimybės, tačiau gali kilti sunkumų su naujų funkcijų pridėjimu ar esamų pakeitimu, reikalaujančiu didesnio sistemos pertvarkymo.
- Galimi sunkumai gali kilti ir su programos veikimo efektyvumu, ypač esant dideliems duomenų kiekiams, reikalingiems analizei, kurie gali paveikti programos našumą ir atsakymo laiką.

# Išvada
Kursiniame darbe sėkmingai sukurta programa, skirta analizuoti ir vizualizuoti išlaidas įvairių kategorijų prekėms tarpusavio apsipirkimo krepšelyje. Modeliuodama skirtingas prekių kategorijas, įtraukdama jas į pirkinių krepšelį ir vėliau analizuodama, programa vartotojui pateikia naudingas išvadas apie išlaidas. Programos išvestis apima tikslius bendrų išlaidų pagal kategorijas skaičiavimus ir jų vizualizavimą skritulinės ir stulpelinės diagramos pavidalu. Programos ateities perspektyvos apima funkcionalumo išplėtimą, kad būtų galima lanksčiau analizuoti duomenis, vartotojo sąsajos tobulinimą, kad būtų lengviau naudotis, ir našumo optimizavimą apdorojant didelius duomenų kiekius.
