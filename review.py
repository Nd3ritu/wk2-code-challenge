class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all(self)

    @classmethod
    def all(cls,review):
        cls.reviews.append(review)

    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant