class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] 
    def __init__(self, name: str, price: float):
        # Run validations to the received arguments
        assert price >=0, f"The price {price} is not greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price 
        print("the object {} was initiated, its price is {}".format(self.name,self.price))
        
        # Actions to execute 
        Item.all.append(self)

        def __repr__(self):
            return self.name

item1 = Item("Iphone", 200)
print(item1)

