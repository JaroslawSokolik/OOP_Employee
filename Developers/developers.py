from Base.employee import Employee


class Developer(Employee):
    def __init__(self, first_name, last_name, pay, prog_lang, skill_level):  # Office init called
        super().__init__(first_name, last_name, pay)  # Employee init called
        self.prog_lang = prog_lang
        self.skill_level = skill_level

    def print_skill_level(self):
        print("My skill level is " + self.skill_level)

