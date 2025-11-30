class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours = None, rest_days = None, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        
    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
        
    def salary(self):
        return self.hours * self.hourly_payment
    
    
employee1 = EmployeeSalary.get_hours("Ivan", rest_days=2, email=None)
print(employee1.hours)     # 40
print(employee1.salary())  # 40 * 400 = 16000
print(employee1.hourly_payment)

employee2 = EmployeeSalary.get_email("Anna", hours=30, rest_days=1)
print(employee2.email)     # Anna@email.com
print(employee2.salary())  # 30 * 400 = 12000

print(EmployeeSalary.hourly_payment)   # 400
EmployeeSalary.set_hourly_payment(500)
print(EmployeeSalary.hourly_payment)   # 500