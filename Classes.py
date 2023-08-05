class items:
    def calculate_total_amount(self,x,y):
        return x*y

        
item1 = items()
item1.name = 'Bread'
item1.amount = 100
item1.quantity = 4
print(item1.calculate_total_amount(item1.amount, item1.quantity))

item2 = items()
item2.name = 'oil'
item2.amount = 3000
item2.quantity = 5
print(item2.calculate_total_amount(item2.amount, item2.quantity))
