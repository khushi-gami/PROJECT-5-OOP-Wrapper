# PROJECT-5-OOP-Wrapper
A menu-driven Employee Management System built with Python OOP, demonstrating classes, objects, encapsulation, private attributes, inheritance, method overriding, constructors, and super().

# Employee Management System - Python OOP Project

A console-based, menu-driven Python application that demonstrates the core concepts of **Object-Oriented Programming (OOP)** by managing three kinds of entities: a **Person**, an **Employee** and a **Manager**.

---

## 1. Introduction

The Employee Management System is a small project built to practise how real-world entities can be represented in code using classes and objects. The user interacts with the program through a text menu, creates a person, an employee or a manager by entering details, and can then view the stored details whenever required.

The project focuses more on **how the code is designed** (classes, data protection, reuse through inheritance) than on the amount of functionality.

---

## 2. Objective of the Project

- To understand and apply the fundamental pillars of OOP in Python.
- To model real-world entities (Person, Employee, Manager) as classes.
- To protect sensitive data such as salary and employee ID using encapsulation.
- To reuse existing code through inheritance instead of rewriting it.
- To build a complete interactive program using loops, conditions and user input.

---

## 3. Features

- A menu that keeps running until the user chooses to exit.
- Creation of a Person, an Employee and a Manager using user input.
- Display of the details of any created object.
- Salary and employee ID are kept private and accessed only through getter methods.
- A clear message is shown if the user tries to view details of an object that has not been created yet.
- Invalid menu choices are detected and reported instead of crashing the program.

---

## 4. Class Design

The project contains three classes.

### Person
Represents a general person. It stores the **name** and **age** and has a `display()` method that prints these details.

### Employee
Represents a person who works in an organisation. It stores the **name**, **age**, **employee ID** and **salary**. The employee ID and salary are private. The class provides `get_employee_id()` and `get_salary()` to read them and a `display()` method to print all employee details.

### Manager
Represents an employee who also manages a **department**. It is a child class of `Employee`, so it reuses the employee's attributes and methods and adds the `department` attribute. It also has its own version of `display()`.

| Class | Parent Class | Attributes | Methods |
|-------|--------------|------------|---------|
| `Person` | none | `name`, `age` | `display()` |
| `Employee` | none | `name`, `age`, `__employee_id` (private), `__salary` (private) | `get_employee_id()`, `get_salary()`, `display()` |
| `Manager` | `Employee` | all attributes of Employee, plus `department` | `display()` (overridden) |

---

## 5. OOP Concepts Used

### 5.1 Class and Object
A **class** is a blueprint that describes what data an entity has and what actions it can perform. An **object** is an actual instance created from that blueprint. In this project, `Person`, `Employee` and `Manager` are classes, while the variables `person`, `employee` and `manager` in the main program hold the objects created from them at run time.

### 5.2 Constructor (`__init__`)
The `__init__` method is a special method that runs automatically when an object is created. It receives the values entered by the user and stores them as attributes of the object using `self`. For example, creating an `Employee` immediately sets its name, age, employee ID and salary, so the object is always in a complete and valid state.

### 5.3 Encapsulation
Encapsulation means keeping data and the methods that work on that data together, and controlling how the data is accessed from outside.

In the `Employee` class, the employee ID and the salary are stored as **private attributes** by prefixing their names with a double underscore (`__employee_id`, `__salary`). Python does not allow these to be accessed directly from outside the class. To read them, the class provides **getter methods**: `get_employee_id()` and `get_salary()`.

This design protects important data from accidental or unauthorised changes and gives the class full control over how its data is used. Name and age are kept public because they are not sensitive.

### 5.4 Inheritance
Inheritance allows a class (child) to acquire the attributes and methods of another class (parent). Here, `Manager` inherits from `Employee`:

```python
class Manager(Employee):
```

A manager is also an employee, so it does not need to define name, age, ID and salary again. It automatically gets them from `Employee` and only adds what is new, the `department`. This avoids code duplication and makes the program easier to maintain.

### 5.5 The `super()` Function
Inside the `Manager` constructor, `super().__init__(...)` is used to call the constructor of the parent class `Employee`. This takes care of setting up name, age, employee ID and salary. After that, the `Manager` constructor sets its own extra attribute, `department`. In this way, the parent's initialisation logic is reused rather than rewritten.

### 5.6 Method Overriding
Both `Employee` and `Manager` have a `display()` method. When a child class defines a method with the same name as its parent, the child's version replaces the parent's version for objects of the child class. This is called **method overriding**.

`Manager.display()` prints the heading "Manager Details" and also shows the department, which the parent's method does not know about. So the same method name behaves differently depending on the type of object.

### 5.7 Accessing Private Data Through Getters
Because `__employee_id` and `__salary` are private to `Employee`, even the child class `Manager` cannot use them directly. The `Manager` class therefore reads them through `get_employee_id()` and `get_salary()`. This shows that encapsulation applies even between a parent and its child.

---

## 6. Program Logic (Step by Step)

### Step 1: Initial setup
At the start, a heading is printed and the three classes are defined. Then three variables are created and set to `None`:

```python
person = None
employee = None
manager = None
```

These variables will hold the objects once the user creates them. `None` means "nothing created yet", and the program later uses this to decide whether details can be shown.

### Step 2: Main loop
The whole program runs inside a `while True` loop, so the menu keeps coming back after every operation. The loop stops only when the user selects the exit option, which uses `break`.

### Step 3: Menu and user choice
In each iteration, the program prints five options (Create Person, Create Employee, Create Manager, Show Details, Exit) and reads the choice using `int(input())`. An `if / elif / else` chain then decides which block of code runs.

### Step 4: Creating a Person (choice 1)
The program asks for a name and an age, creates a `Person` object with these values and stores it in the `person` variable. A confirmation message with the entered details is printed.

### Step 5: Creating an Employee (choice 2)
The program asks for a name, age, employee ID and salary, creates an `Employee` object and stores it in the `employee` variable. The confirmation message reads the ID and salary through the getter methods because they are private.

### Step 6: Creating a Manager (choice 3)
The program asks for the same details as for an employee, plus the department. It creates a `Manager` object, which internally calls the parent constructor through `super()`, and stores the object in the `manager` variable.

### Step 7: Showing details (choice 4)
A second menu asks which details to show: Person, Employee or Manager. For the selected type, the program first checks:

```python
if obj is not None:
```

- If the object exists, its `display()` method is called and the details are printed.
- If the object is still `None`, a message such as "Person not created !" is shown.

This check prevents the program from trying to use an object that does not exist, which would cause an error.

### Step 8: Exit (choice 5)
The program prints an exit message and a goodbye message, and `break` ends the loop, which ends the program.

### Step 9: Invalid choice
If the entered number is not between 1 and 5, the `else` block prints "Invalid Choice" and the menu is shown again.

### Step 10: Repeating
After each operation, the message "Choose another Operation" is printed and the loop starts again from the menu.

---

## 7. Program Flow

```
Start
  |
  v
Print heading, define classes, set person/employee/manager = None
  |
  v
+-----------------> Show main menu
|                        |
|                        v
|                  Read user choice
|                        |
|   +--------+-----------+-----------+-----------+-----------+
|   |        |           |           |           |           |
|   1        2           3           4           5        other
| Create   Create      Create      Show        Exit      Invalid
| Person   Employee    Manager     Details     (break)   choice
|   |        |           |           |           |           |
+---+--------+-----------+-----------+           v           |
|                                            End program     |
+------------------------------------------------------------+
```

---

## 8. Sample Run

```
--- Python OOP Project : Employee Management System ---

Choose an operation :
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice (1 to 5) : 3

Enter Name : Riya
Enter Age : 30
Enter Employee ID : M101
Enter Salary : 80000
Enter Department : HR

Manager created with name : Riya, age : 30, ID : M101, salary : 80000, and department : HR.

--- Choose another Operation ---

Enter your choice (1 to 5) : 4

Choose details to show :
1. Person
2. Employee
3. Manager

Enter your choice (for show details) : 3

Manager Details :
Name : Riya
Age : 30
Employee ID : M101
Salary : 80000
Department : HR
```
