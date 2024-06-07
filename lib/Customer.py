class Customer:

    all_customers = []

    def __init__(self, family_name, given_name):
        self.family_name = family_name
        self.given_name = given_name
        Customer.all_customers.append(self)

    @property
    def given_name(self):
        return self._given_name
    
    @given_name.setter
    def given_name(self, value):
        self._given_name = value

    @property
    def family_name(self):
        return self._family_name
    
    @family_name.setter
    def family_name(self, value):
        self._family_name = value

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers