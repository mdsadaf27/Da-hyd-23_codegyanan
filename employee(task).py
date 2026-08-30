class Employee:
    count = 0

    def __init__(self, name, salary):
        self.__name = name      
        self.salary = salary
        Employee.count += 1

    def display(self):
        print("Name:", self.__name)
        print("Salary:", self.salary)

    def details(self):
        print("Employee:", self.__name)

    # Static Method
    @staticmethod
    def get_employee_count():
        return Employee.count

    # Class Method
    @classmethod
    def get_employee_count_classmethod(cls):
        return cls.count

    # Operator Overloading
    def __str__(self):
        return self.__name

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary


# Inheritance
class Manager(Employee):
    def details(self):
        print("Manager:", self._Employee__name)


class Developer(Employee):
    def details(self):
        print("Developer:", self._Employee__name)


# Taking input
name1 = input("Enter Manager name: ")
salary1 = int(input("Enter Manager salary: "))

name2 = input("Enter Developer name: ")
salary2 = int(input("Enter Developer salary: "))

# Objects
manager = Manager(name1, salary1)
developer = Developer(name2, salary2)

# Display
manager.display()
manager.details()

developer.display()
developer.details()

# Static method
print("Employee count:", Employee.get_employee_count())

# Class method
print("Employee count:", Employee.get_employee_count_classmethod())

# Operator overloading
print("Manager:", manager)
print("Developer:", developer)

print("Same salary:", manager == developer)
print("Manager salary < Developer salary:", manager < developer)
print("Manager salary > Developer salary:", manager > developer)