import random
from Base.employee import Employee


class Management(Employee):
    def __init__(self, first_name, last_name, pay, mood):  # Management init called
        super().__init__(first_name, last_name, pay)  # Employee init called
        self.mood = mood

    def count_company_income(self):
        print("Company income is only " + str(random.randint(2000, 100000)) + " we can't afford a payrise")

