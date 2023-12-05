from customer import Customer
from review import Review
from restaurant import Restaurant

#customer instances
customer1 = Customer('Matthew', 'Wambugu')
customer2 = Customer('Mark', 'Njuguna')
customer3 = Customer('Tiffany', 'Wanjiku')
#restaurant name
restaurant = Restaurant('Star4')

review1 = Review(customer1, restaurant, 2)
review2 = Review(customer2, restaurant, 10)
review3 = Review(customer3,restaurant, 8)

#add reviews t0 restaurant
restaurant.add_review(review1)
restaurant.add_review(review2)
restaurant.add_review(review3)

#print all reviews added of restaurant
print("REVIEWS")
for review in restaurant.reviews():
    print(f"Rating: {review.rating},    Customer: {review.customer.full_name()}")

#print unique customers who reviewed
print("CUSTOMERS WHO REVIEWED")
for customer in restaurant.customers():
    print(f"Customer Name: {customer.full_name()}")