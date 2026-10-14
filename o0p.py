class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.brand}, {self.model}, {self.year}, მანქანა მუშა მდგომარეობაშია")

    def info(self):
        print(f"ეს არის, {self.year} წლის, {self.brand}, {self.model}")

class sportscar(car):
    def __init__(self, top_speed, brand, model, year):
        super().__init__(brand, model, year)
        self.top_speed = top_speed

    def drive(self):
        print(f"გზაზე მიქრის, {self.brand} {self.model}, მისი სიჩქარეა, {self.top_speed} კმ/სთ")

class electircar(car):
    def __init__(self, battery_capacity, brand, model, year):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def drive(self):
        print(f"{self.brand} {self.model}, მოზრაობს ელექტროულად, {self.battery_capacity}, კილოვატი (არ ვიცი ეგ ქვია თუ არაა)")

class luxurycar(car):
    def __init__(self, features, brand, model, year):
        super().__init__(brand, model, year)
        self.features = features

    def drive(self):
        print(f"{self.brand} {self.model}, გთავაზობთ {self.features} მგზავრობას")


class hybirdcar(car):
    def __init__(self, battery_capacity, fuel_type, brand, year, model):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.fuel_type = fuel_type

    def drive(self):
        print(f"{self.brand} {self.model}, მუშაობს როგორც ელექტრონულად ({self.battery_capacity} რაღაცა კილოვატი), ისე ბენზინზე ({self.fuel_type}) ")

def compare(car1, car2):
    if car1.top_speed > car2.top_speed:
        print(f"{car1.brand} {car1.model} უფრო სწრაფია, ვიდრე {car2.brand} {car2.model}")
    elif car1.top_speed < car2.top_speed:
        print(f"{car2.brand} {car2.model} უფრო სწრაფია, ვიდრე {car1.brand} {car1.model}")
    else:
        print("ორივე მანქანა ერთნაირი სიჩქარისაა")

sport_car1 = sportscar(322, "Porshe", 911, 2026)
sport_car2 = sportscar(415, "Buggati", "veyron", 2026)
electiccar1 = electircar(100, "Tesla", "Model X", 2026)
luxurycar1 = luxurycar("მაგარია რა დაფლექსავ", "Mercedes", "maybach", 2026,)
hybridcar1 = hybirdcar(1.31, "regular", "Toyota", 2026, "prius")

sport_car1.drive()
sport_car2.drive()
sport_car1.info()
sport_car2.info()

electiccar1.drive()
electiccar1.info()

luxurycar1.drive()
luxurycar1.info()

hybridcar1.drive()
hybridcar1.info()

compare(sport_car1, sport_car2)

