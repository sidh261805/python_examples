class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
        
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self, phone_number):
        return f"calling {phone_number} ..."

    def full_name(self):
        return f"{self.brand} {self.model}"

class Smartphone(Phone):
    def __init__(self,brand,model,price,ram,internal_mem,rear_camera):
        # Phone.__init__(self,brand,model,price)  -> uncommon way
        super().__init__(brand,model,price)
        self.ram = ram
        self.internal_mem = internal_mem
        self.rear_camera = rear_camera

    def full_name(self): #method override
        return f"{self.brand} {self.model} and price is {self._price} and ram {self.ram} and internal_memory {self.internal_mem}"

class Flagshipphone(Smartphone):
    def __init__(self,brand,model,price,ram,internal_mem,rear_camera,front_camera):
        super().__init__(brand,model,price,ram,internal_mem,rear_camera)
        self.front_camera = front_camera

        

phone1 =Phone('Nokia','7600',5000)
phone2 =Smartphone('MI','note7',16000,'6 GB','64 GB','64 MP')
phone3 =Flagshipphone('MI','note11',40000,'8 GB','128 GB','124 MP','12 MP')
phone1.price = 3000
print(phone1.price)
print(phone1.complete_specification)
print(phone2.complete_specification)
print(phone3.complete_specification)
print(phone1.full_name())
print(phone2.full_name())
print(phone3.full_name())

note7 =Smartphone('MI','note7',16000,'6 GB','64 GB','64 MP')
note11 =Flagshipphone('MI','note11',40000,'8 GB','128 GB','124 MP','12 MP')
print(isinstance(note7,Smartphone))
print(isinstance(note7,Phone))
print(isinstance(note7,Flagshipphone))

print(isinstance(note11,Flagshipphone))
print(isinstance(note11,Smartphone))
print(isinstance(note11,Phone))


print(issubclass(Smartphone,Phone))
print(issubclass(Smartphone,Flagshipphone))

# print(help(Flagshipphone))