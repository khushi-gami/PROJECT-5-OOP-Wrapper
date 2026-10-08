print("--- Python OOP Project : Employee Management System ---")

print()

# ------------------------- For safe user input -------------------------

def int_input(message, minimum, maximum):
    while True:
        try:
            number = int(input(message))
            if number < minimum or number > maximum:
                print(f"Please enter a number between {minimum} and {maximum}.")
                print()
            else:
                return number
        except ValueError:
            print("Invalid input ! Please enter a number.")
            print()


def float_input(message):
    while True:
        try:
            number = float(input(message))
            if number < 0:
                print("Value cannot be negative.")
                print()
            else:
                return number
        except ValueError:
            print("Invalid input ! Please enter a number.")
            print()


def text_input(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("This field cannot be empty.")
            print()
        else:
            return text


# ----------------------------------- Create Person Class ------------------------------------
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Person Details : ")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


# ----------------------------------- Create Employee Class ------------------------------------
class Employee(Person):

    def __init__(self, name, age, employee_id=None, salary=None):
        super().__init__(name, age)      
        self.__employee_id = employee_id     
        self.__salary = salary               

    # ---------- Getter methods 
    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    # ---------- Setter methods
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
            self.__salary = salary

    def display(self):
        print("Employee Details : ")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

        if self.__employee_id is None:
            print("Employee ID : Not assigned")
        else:
            print(f"Employee ID : {self.__employee_id}")

        if self.__salary is None:
            print("Salary : Not assigned")
        else:
            print(f"Salary : {self.__salary}")

    # ----------------- Destructor
    def __del__(self):
        print(f"Employee object '{self.name}' is being destroyed.")


# ----------------------------------- Create Manager Class ------------------------------------
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        print("Manager Details : ")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Employee ID : {self.get_employee_id()}")
        print(f"Salary : {self.get_salary()}")
        print(f"Department : {self.department}")


# ----------------------------------- Create Developer Class ------------------------------------
class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        print("Developer Details : ")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Employee ID : {self.get_employee_id()}")
        print(f"Salary : {self.get_salary()}")
        print(f"Programming Language : {self.programming_language}")


# ----------------------------------- issubclass() check ------------------------------------
print("Verify Inheritance : ")
print("Employee is subclass of Person :", issubclass(Employee, Person))
print("Manager is subclass of Employee :", issubclass(Manager, Employee))
print("Developer is subclass of Employee :", issubclass(Developer, Employee))

print()

# For show details..
person = None
employee = None
manager = None
developer = None
selected_object = None   # -------------- for update information using setter method


while True:

    print("Choose an operation : ")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Update Salary / Employee ID (Setter method)")
    print("7. Constructor Overloading Demo")
    print("8. Exit")

    print()

    # Take Choice option from user..
    choice = int_input("Enter your choice (1 to 8) : ", 1, 8)

    print()

# ----------------------------------- Get Person Details ------------------------------------
    if choice == 1:
        
        person = Person(
            text_input("Enter Name : "),
            int_input("Enter Age : ",1,120),
        )

        print()

        print(f"Person created with name : {person.name} and age : {person.age}.")

        print()

# ----------------------------------- Get Employee Details ------------------------------------
    elif choice == 2:
        
        employee = Employee(
            text_input("Enter Name : "),
            int_input("Enter Age : ",1,120),
            text_input("Enter Employee ID : "),
            float_input("Enter Salary : "),
        )

        print()

        print(f"Employee created with name : {employee.name}, age : {employee.age}, ID : {employee.get_employee_id()}, and salary : {employee.get_salary()}.")

        print()

# ----------------------------------- Get Manager Details ------------------------------------
    elif choice == 3:
        
        manager = Manager(
            text_input("Enter Name : "),
            int_input("Enter Age : ",1,120),
            text_input("Enter Employee ID : "),
            float_input("Enter Salary : "),
            text_input("Enter Department : ")
        )

        print()

        print(f"Manager created with name : {manager.name}, age : {manager.age}, ID : {manager.get_employee_id()}, salary : {manager.get_salary()}, and department : {manager.department}.")

        print()

# ----------------------------------- Get Developer Details ----------------------------------
    elif choice == 4:
        
        developer = Developer(
            text_input("Enter Name : "),
            int_input("Enter Age : ",1,120),
            text_input("Enter Employee ID : "),
            float_input("Enter Salary : "),
            text_input("Enter Programming Language : "),
        )

        print()

        print(f"Developer created with name : {developer.name}, age : {developer.age}, ID : {developer.get_employee_id()}, salary : {developer.get_salary()}, and programming language : {developer.programming_language}.")

        print()

# ----------------------------------- Show All Details ---------------------------------------
    elif choice == 5:

        print("Choose choice to show details : ")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")

        print()

        show_details_choice = int_input("Enter your choice (for show details) : ", 1, 4)

        print()

        if show_details_choice == 1:

            if person is not None:
                person.display()
            else:
                print("Person not created !")

        elif show_details_choice == 2:

            if employee is not None:
                employee.display()
            else:
                print("Employee not created !")

        elif show_details_choice == 3:

            if manager is not None:
                manager.display()
            else:
                print("Manager not created !")

        elif show_details_choice == 4:

            if developer is not None:
                developer.display()
            else:
                print("Developer not created !")

        print()

# -------------------------------- Update using setter method ------------------------------

    elif choice == 6:

        print("Details do you want to update ? ")
        print("1. Employee")
        print("2. Manager")
        print("3. Developer")

        print()

        update_choice = int_input("Enter your choice (for update) : ", 1, 3)

        print()


        if update_choice == 1:
            selected_object = employee
        elif update_choice == 2:
            selected_object = manager
        else:
            selected_object = developer

        if selected_object is None:
            print("This object is not created yet !")
        else:
            new_id = text_input("Enter new employee ID : ")
            new_salary = float_input("Enter new salary : ")

            # use of setter method
            selected_object.set_employee_id(new_id)
            selected_object.set_salary(new_salary)

            print()
            print("Details updated !! Updated details are : ")
            print()
            selected_object.display()

        print()

# ----------------------------------- Method Overloading ---------------------------

    elif choice == 7:
        print("Method Overloading : ")
        print("In Employee class, constructor overloading is demonstrated by creating objects in 3 different ways using default arguments. : ") 
        print()

        print("1 --- Employee(name, age)")
        demo1 = Employee("Khushi", 25)
        demo1.display()
        print()

        print("2 --- Employee(name, age , ID)")
        demo2 = Employee("Rahul", 27, "E101")
        demo2.display()
        print()

        print("3 --- Employee(name, age, ID, salary)")
        demo3 = Employee("Shivani", 30, "E102", 45000.0)
        demo3.display()
        print()

        # using del we can call destructor ----> (__del__) 
        print("Deleting demo objects : ")
        del demo1
        del demo2
        del demo3

        print()

# ----------------------------------- Exit Programme  ------------------------------------

    elif choice == 8:

        print()

        print("Exiting the system. All resources have been freed.")

        print()

        print("Goodbye!")

        break

    print("--- Choose another Operation ---")

    print()