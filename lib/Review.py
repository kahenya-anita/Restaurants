class Review:

    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    @property
    def restaurant(self):
        return self._restaurant
    
    @property 
    def customer(self):
        return self._customer
    
    @property
    def rating(self):
        return self._rating
    
    @classmethod
    def all(cls):
        return cls.all_reviews