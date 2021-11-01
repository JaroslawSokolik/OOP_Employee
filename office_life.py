from Developers.developers import Developer
from Management.management import Management
from Office.office import Office

boss = Management("Bossy", "Kowalski", 2300, "Angry")
boss.full_name()
boss.count_company_income()
developer_1 = Developer("John", "Smith", 2300, "Java", "Intermediate")
developer_1.full_name()
developer_1.print_skill_level()
office_worker_1 = Office("Anna", "Smith", 500, "Iphone 10")
office_worker_1.full_name()
office_worker_1.print_provided_phone()
office_worker_1.respond_time()
