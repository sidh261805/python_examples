class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)
    
    def phone_name(self):
        return f"{self.brand} {self.model}"
    
    def __str__(self):
        return f"{self.brand} {self.model} and price is {self.price}"

    def __repr__(self):  #representation
        return f"Phone ('{self.brand}','{self.model}','{self.price}')"

    def __len__(self):
        return len(self.phone_name())

    def __add__(self,other):
        return self.price + other.price

    def __sub__(self,other):
        return self.price - other.price
    

class Smartphone(Phone):
    def __init__(self,brand,model,price,camera):
        super().__init__(brand,model,price)
        self.camera = camera

    def phone_name(self):  #method override
        return f"{self.brand} {self.model} {self.camera}"


phone1 = Phone('Nokia','7600',5000)
phone2 = Phone('MI','note7',15000)
print(phone1)
print(phone1.__repr__())
print(len(phone1))

print(phone1+phone2)
print(phone2-phone1)

phone2 = Smartphone('MI','note7',15000,'16 MP')
print(phone1.phone_name())
print(phone2.phone_name())