class Restaurant:
    #creating  restaurant instance
    def __init__(self, name):
        self._name = name
    #the decorator enforces restriction and makes sure an instance of a restaurant does not get renamed
    @property
    def name(self):
        return self._name
    
restaurant1 = Restaurant('star4')
print("Restaurant 1 is:", restaurant1.name) # star4
#attempt to change restaurant 1 name
restaurant1.name = 'STARLIGHT'
print(restaurant1.name) # Attribute error