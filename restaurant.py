class Restaurant:
    #creating  restaurant instance
    def __init__(self, name):
        self._name = name
        self._reviews = []
    #the decorator enforces restriction and makes sure an instance of a restaurant does not get renamed
    @property
    def name(self):
        return self._name
    
    def add_review(self,review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews
    
    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer)
        return list(unique_customers)
    
    def average_star_rating(self):
        if not self._reviews:
            return 0
        
        total_rates = sum(review.rating for review in self._reviews)
        return total_rates / len(self._reviews)
    
#restaurant1 = Restaurant('star4')
#print("Restaurant 1 is:", restaurant1.name) # star4
#attempt to change restaurant 1 name
#restaurant1.name = 'STARLIGHT'
#print(restaurant1.name) # Attribute error