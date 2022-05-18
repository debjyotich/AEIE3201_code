class Emp:

    def __init__(self, name, salary):  # class constructor
        self.name = name
        self.salary = salary

    def printName(self):  # class function
        print(f"The name is: {self.name}")

    def printSalary(self):
        print(f"The salary is: {self.salary}")

    def printDetails(self):
        print(f"The salary of {self.name} is {self.salary}")


my_obj_Deb = Emp("Deb", 11.5)  # class instance
my_obj_Alex = Emp("Alex", 12.5)  # class instance
my_obj_Alice = Emp("Alice", 10.5)  # class instance

# my_obj_Deb.salary = 1000

my_obj_Deb.printDetails()
my_obj_Alex.printDetails()
my_obj_Alice.printDetails()


