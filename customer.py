class Customer:
    #customers lists
    customers = []
    #instance attributes
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.all(self)

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

customer1 = Customer('John', 'Doe')
customer2 = Customer('Matthew', 'Wambugu')
print(customer1.given_name)# John
print(customer2.full_name()) # Matthew Wambugu
Customer.print_customers() # customers in dictionary format