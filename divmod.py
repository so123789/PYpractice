# x = divmod(9,3)
# print(x)

class Item:

    def __init__(self, name, price, quantity):
        print(f"The items are: {name}")
        #run validation of received arguements
        assert price>=0, "Price cannot be negative"
        #assign self objects
        self.name = name #dynamically creating the attributes

i0 = Item("Phone",-1,0)
i1 = Item("Laptop")