import csv
class items:
#Class Attributes
    pay_rate = 0.7 #discount for all products
    all = []

#instance attributes
    def __init__(self, name: str, price: int, quantity=0):        
        #Assign validations
        assert price>=0, f"amount is {price} but should be greater than or equal to zero"
        assert quantity>=0, f"quantity is {quantity} but should be greater than or equal to zero"
    
        #Assign to objects itself 
        self.name = name
        self.price = price
        self.quantity = quantity

        #Appending instances to all list
        items.all.append(self)

#instance methods
    def applying_discount(self):
        self.price = self.price * self.pay_rate
        return self.price
    
    def calculate_total_amount(self):
        return self.price * self.quantity

    def __repr__(self):
        return f'items("{self.name}",{self.price},{self.quantity})'

    @classmethod
    def instantiate_from_csv():

    items.instantiate_from_csv()

#input
item1 = items('sugar',100, 10)
print(item1.calculate_total_amount())
print(item1.applying_discount())

item2 = items('salt',10, 12)
item2.pay_rate = 0.6
print(item2.applying_discount())
print(item2.calculate_total_amount())

item3 = items('laptop',1000,1)
print(item3.calculate_total_amount())
item3.has_webcam = False

# All attributes belong to that class
print(items.__dict__)

# All attributes belong to that instance
print(item1.__dict__)

item4 = items('car',3000,1)
item5 = items('bike',6000,1)

for instance in items.all:
    print(instance.name)


print(items.all)