from Base.employee import Employee


class Office(Employee):
    def __init__(self, first_name, last_name, pay, phone):  # Office init called
        super().__init__(first_name, last_name, pay)  # Employee init called
        self.phone = phone

    def print_provided_phone(self):
        print("I am eqquped with " + self.phone)

