class Laptop:
    discount_percentage = 10    #class variable
    count_instance = 0  #class variable
    def __init__(self,brand,model_name,price):
        self.brand = brand   #instance variable
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand +' '+model_name
        Laptop.count_instance += 1
    
    @classmethod #class method ctor
    def from_string(cls,string):
        brand,model_name,price = string.split(',')
        print(f"{type(brand)}{type(model_name)}{type(price)}")
        return cls(brand,model_name,int(price))
    
    def apply_discount(self):   #instance method
        off_price = (self.discount_percentage/100)*self.price
        return self.price - off_price
    
    def fullname(self):
        return self.model_name +' '+self.brand

    @classmethod
    def count_instances(cls):  #class method
        return (f"you have created {cls.count_instance} instances of {cls.__name__} class")

    @staticmethod
    def hello():
        print('hello, static !!!!!')
    

laptop1 = Laptop('sony','abcd1234',50000)
laptop2 = Laptop('hp','qwerty',100000)
laptop2.discount_percentage=30
print(laptop1.apply_discount())
print(laptop2.apply_discount())

print(Laptop.apply_discount(laptop1))

print(Laptop.count_instance)

laptop2 = Laptop('hp','qwerty',100000)
print(Laptop.count_instances()) #also work laptop2.count_instances()

laptop3 = Laptop.from_string('lenovo,asdf1234,75000')
print(Laptop.fullname(laptop3))
print(laptop3.apply_discount())

Laptop.hello()



