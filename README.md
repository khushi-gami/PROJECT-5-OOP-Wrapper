Project-5-OOP-Wrapper (VIDEO)
https://drive.google.com/file/d/10tsRbk9GxQ_A7BfyiOQ5nLbGgkeYmutP/view?usp=sharing

# PROJECT-5-OOP-Wrapper - Employee Management System

A simple console-based Python project that uses **Object-Oriented Programming (OOP)**
to create and manage Person, Employee, Manager and Developer data.

The program shows a menu. The user can create objects, view their details,
update employee data and see how some OOP concepts work.

---

## Project Files

```
oops_wrapper.py          -> main Python program (code)
oops_wrapper_ui.py       -> program (ui code)
README.md                -> project explanation (this file)
```

## Class Structure

```
Person
  |
Employee
  |-- Manager
  |-- Developer
```

| Class | Inherits from | Attributes | Extra details |
|---|---|---|---|
| `Person` | - | `name`, `age` | Base class |
| `Employee` | `Person` | `__employee_id`, `__salary` (private) | Getters, setters, destructor |
| `Manager` | `Employee` | `department` | Overrides `display()` |
| `Developer` | `Employee` | `programming_language` | Overrides `display()` |

---

## OOP Concepts and How They Are Used

### 1. Classes and Objects
A class is a blueprint and an object is created from it.
Example: `Employee("Rahul", 27, "E101")` creates one Employee object.

### 2. Inheritance
A child class gets the features of its parent class.
- `Employee` inherits from `Person`, so it already has `name` and `age`.
- `Manager` and `Developer` inherit from `Employee`, so they also get employee ID, salary, getters and setters.

### 3. Constructor (`__init__`) and `super()`
`__init__` runs automatically when an object is created.
In child classes, `super().__init__(...)` calls the parent class constructor,
so the common data (name, age, ID, salary) is not written again.

### 4. Encapsulation (Private Data)
`employee_id` and `salary` are sensitive data, so they are written with double
underscore (`self.__employee_id`, `self.__salary`). This makes them **private**:
they cannot be accessed directly from outside the class.

### 5. Getter and Setter Methods
Since private data cannot be accessed directly, we use methods:

| Method | Work |
|---|---|
| `get_employee_id()` | returns the employee ID |
| `get_salary()` | returns the salary |
| `set_employee_id(employee_id)` | changes the employee ID |
| `set_salary(salary)` | changes the salary |

Menu option 6 uses the setter methods to update ID and salary.

### 6. Method Overriding
`display()` is written in `Person`, and again in `Employee`, `Manager` and `Developer`.
Each child class gives its own version:
- `Manager.display()` also shows the **department**
- `Developer.display()` also shows the **programming language**

### 7. Method Overloading
Python allows only one `__init__`, so overloading is done using **default arguments**:

```python
def __init__(self, name, age, employee_id=None, salary=None):
```

Because `employee_id` and `salary` are optional, an Employee can be created in 3 ways:

```python
Employee("Khushi", 25)                   # name, age
Employee("Rahul", 27, "E101")            # name, age, ID
Employee("Shivani", 30, "E102", 45000.0) # name, age, ID, salary
```

If ID or salary is not given, `display()` shows "Not assigned".
Menu option 7 demonstrates all 3 ways.

### 8. Destructor (`__del__`)
`__del__` runs automatically when an object is deleted.
In this project it prints a message like:
`Employee object 'Rahul' is being destroyed.`

In menu option 7, the `del` keyword is used to delete the demo objects,
so the destructor message can be seen. Objects that are still alive when the
program ends are also destroyed by Python automatically.

### 9. `issubclass()`
At the start of the program, `issubclass()` checks the class relationships:

```
Employee is subclass of Person : True
Manager is subclass of Employee : True
Developer is subclass of Employee : True
```

---

## Input Validation (Safe Input)

Normal `int(input())` crashes the program if the user types text.
To avoid this, three helper functions are used:

| Function | Work |
|---|---|
| `int_input(message, minimum, maximum)` | Takes a whole number. Asks again if the input is text or outside the allowed range |
| `float_input(message)` | Takes a decimal number (salary). Asks again if the input is invalid or negative |
| `text_input(message)` | Takes text (name, ID, etc.). Asks again if the input is empty |

**Logic:** each function runs a `while True` loop. It uses `try/except` to catch
`ValueError`. The loop stops (`return`) only when a valid value is entered.

---

## Menu Options and Program Flow

```
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Update Salary / Employee ID (Setter method)
7. Constructor Overloading Demo
8. Exit
```

The menu runs inside a `while True` loop, so it repeats until the user chooses Exit.

| Option | What happens |
|---|---|
| 1 - 4 | Takes input from the user, creates the object and prints a confirmation message |
| 5 | Asks which object to show (Person / Employee / Manager / Developer) and calls its `display()`. If it is not created yet, a message is shown |
| 6 | Asks which employee type to update, takes a new ID and salary, calls the setters and shows the updated details |
| 7 | Creates 3 Employee objects in 3 different ways, displays them, then deletes them to show the destructor |
| 8 | Prints the exit message and stops the loop using `break` |

Objects are first set to `None` (`person = None`, `employee = None`, ...).
This helps the program check whether an object is created before showing or updating it.

---

## Sample Output

```
--- Python OOP Project : Employee Management System ---

Verify Inheritance :
Employee is subclass of Person : True
Manager is subclass of Employee : True
Developer is subclass of Employee : True

Choose an operation :
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Update Salary / Employee ID (Setter method)
7. Constructor Overloading Demo
8. Exit

Enter your choice (1 to 8) : 2

Enter Name : Jane Smith
Enter Age : 28
Enter Employee ID : E123
Enter Salary : 50000

Employee created with name : Jane Smith, age : 28, ID : E123, and salary : 50000.0.

--- Choose another Operation ---
```

---

## Author

**Name:** [Khushi Gami]