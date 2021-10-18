from Base.employee import Employee


class Office(Employee):
    def __init__(self, first_name, last_name, pay, phone):
        super().__init__(first_name, last_name, pay)
        self.phone = phone

    def print_provided_phone(self):
        print("I am eqquped with " + self.phone)

