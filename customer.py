from review import Review
class Customer:
    #customers lists
    customers = []
    #instance attributes
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all(self)

    #prints customers
    @classmethod
    def print_customers(cls):
        for customer in Customer.customers:
            print(vars(customer))


    #returns given name of customer
    def given_name(self):
        return self.given_name
    #returns family name of customer
    def family_name(self):
        return self.family_name
    #returns full name of customer
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    #adds customer to customers list
    @classmethod
    def all(cls,customer):
        cls.customers.append(customer)

    def restaurants(self):
        #unique restaurants from reviews
        unique_restaurants = set()
        for review in self._reviews:
            unique_restaurants.add(review.restaurant)
        return list(unique_restaurants)
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_give_name(cls,name):
        matching_customers = [customer for customer in cls.customers if customer.given_name == name]
        return matching_customers
    

    

# customer1 = Customer('John', 'Doe')
# customer2 = Customer('Matthew', 'Wambugu')
# print(customer1.given_name)              # John
# print(customer2.full_name())            # Matthew Wambugu
# Customer.print_customers()             # customers in dictionary format