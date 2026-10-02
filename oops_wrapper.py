print("--- Python OOP Project : Employee Management System ---")

print()

# ----------------------------------- Create Person Class ------------------------------------
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Person Details : ")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        
# ----------------------------------- Create Employee Class ------------------------------------
class Employee():
    def __init__(self,name,age,employee_id,salary):
        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def display(self):
        print("Employee Details : ")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Employee ID : {self.get_employee_id()}")
        print(f"Salary : {self.get_salary()}")


# ----------------------------------- Create Manager Class ------------------------------------
class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):

        super().__init__(name,age,employee_id,salary)
        self.department = department 

    def display(self):
        print("Manager Details : ")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Employee ID : {self.get_employee_id()}")
        print(f"Salary : {self.get_salary()}")
        print(f"Department : {self.department}")

# For show details..
person = None
employee = None
manager = None


while True:

    print("Choose an operation : ")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    print()

    # Take Choice option from user..
    choice = int(input("Enter your choice (1 to 5) : "))

    print()

# ----------------------------------- Get Person Details ------------------------------------
    if choice == 1:

        person = Person(
            input("Enter Name : "),
            int(input("Enter Age : "))
            )

        print()
        
        # print person details..
        print(f"Person created with name : {person.name} and age : {person.age}.")

        print()
        
# ----------------------------------- Get Employee Details ------------------------------------
    elif choice == 2:

        employee = Employee(
            input("Enter Name : "),
            int(input("Enter Age : ")),
            input("Enter Employee ID : "),
            int(input("Enter Salary : "))
            )

        print()
       
        # print employee details..
        print(f"Employee created with name : {employee.name}, age : {employee.age}, ID : {employee.get_employee_id()}, and salary : {employee.get_salary()}. ")

        print()

# ----------------------------------- Get Manager Details ------------------------------------
    elif choice == 3:

        manager = Manager(
            input("Enter Name : "),
            int(input("Enter Age : ")),
            input("Enter Employee ID : "),
            int(input("Enter Salary : ")),
            input("Enter Department : ")
            )

        print()
        
        # print manager details..
        print(f"Manager created with name : {manager.name}, age : {manager.age}, ID : {manager.get_employee_id()}, salary : {manager.get_salary()}, and department : {manager.department}. ")

        print()


# ----------------------------------- Show All Details ---------------------------------------
    elif choice == 4 :

        print("Choose details to show : ")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        print()

        show_details_choice = int(input("Enter your choice (for show details) : "))

        print()


        if show_details_choice == 1 :

            # Get Person Details...
            if person is not None:
                
                # print person details..
                person.display()

                print()

            else :

                print("Person not created !")

                print()
        
        elif show_details_choice == 2:

            # Get Employee Details...
            if employee is not None:

                # print employee details..
                employee.display()

                print()

            else:

                print("Employee not created !")

                print()

        elif show_details_choice == 3 :

            # Get Manager Details...
            if manager is not None:
                
                # print manager details..
                manager.display()

                print()
           
            else :

                print("Manager is not created !")

                print()
                
# ----------------------------------- Exit Programme  ------------------------------------

    elif choice == 5:

        print("Exiting the system. All resources have been freed.")

        print()

        print("Goodbye!")
     
        break
    
    else:
        # when user entered invalid choice..
        print("Invalid Choice Entered !")

        print()
 
    print("--- Choose another Operation ---")

    print()
