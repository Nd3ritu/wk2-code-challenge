class Customer:
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
    #prints family name
    def family_name(self):
        return self.family_name
    #prints full nam
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls,customer):
        cls.customers.append(customer)

customer1 = Customer('John', 'Doe')
customer2 = Customer('Matthew', 'Wambugu')
# print(customer1.given_name)
# print(customer2.full_name())
# customers=Customer.customers

# for customer in customers:
#     print(vars(customer))


# customer_names = [customermatthew@Dell-Precision-7530:~/p3/codechallenge$.full_name() for customer in Customer.customers]
# print(customer_names)

Customer.print_customers()