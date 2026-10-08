import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------------------------------------------------------
# Employee Management System (GUI version using tkinter)
# Console version me display() print karta tha.
# GUI me text window me dikhana hai, isliye display() ab text RETURN karta hai.
# ----------------------------------------------------------------------------

# Destructor ke messages yahan save honge, taaki window me dikha sakein
destroyed_messages = []


# ----------------------------------- Create Person Class ------------------------------------
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        text = "Person Details : \n"
        text += f"Name : {self.name}\n"
        text += f"Age : {self.age}\n"
        return text


# ----------------------------------- Create Employee Class ------------------------------------
class Employee(Person):

    # Constructor overloading : default arguments (=None)
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
        text = "Employee Details : \n"
        text += f"Name : {self.name}\n"
        text += f"Age : {self.age}\n"

        if self.__employee_id is None:
            text += "Employee ID : Not assigned\n"
        else:
            text += f"Employee ID : {self.__employee_id}\n"

        if self.__salary is None:
            text += "Salary : Not assigned\n"
        else:
            text += f"Salary : {self.__salary}\n"

        return text

    # ----------------- Destructor
    def __del__(self):
        message = f"Employee object '{self.name}' is being destroyed."
        destroyed_messages.append(message)
        print(message)


# ----------------------------------- Create Manager Class ------------------------------------
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        text = "Manager Details : \n"
        text += f"Name : {self.name}\n"
        text += f"Age : {self.age}\n"
        text += f"Employee ID : {self.get_employee_id()}\n"
        text += f"Salary : {self.get_salary()}\n"
        text += f"Department : {self.department}\n"
        return text


# ----------------------------------- Create Developer Class ------------------------------------
class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        text = "Developer Details : \n"
        text += f"Name : {self.name}\n"
        text += f"Age : {self.age}\n"
        text += f"Employee ID : {self.get_employee_id()}\n"
        text += f"Salary : {self.get_salary()}\n"
        text += f"Programming Language : {self.programming_language}\n"
        return text


# For show details..
person = None
employee = None
manager = None
developer = None


# ------------------------- Safe input functions (validation) -------------------------
# Galat input par program crash nahi hota, error box dikhta hai aur None return hota hai.

def read_text(entry, field_name):
    text = entry.get().strip()
    if text == "":
        messagebox.showerror("Invalid Input", f"{field_name} cannot be empty.")
        return None
    return text


def read_age(entry):
    try:
        age = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Age must be a whole number.")
        return None

    if age < 1 or age > 120:
        messagebox.showerror("Invalid Input", "Age must be between 1 and 120.")
        return None
    return age


def read_salary(entry):
    try:
        salary = float(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Salary must be a number.")
        return None

    if salary < 0:
        messagebox.showerror("Invalid Input", "Salary cannot be negative.")
        return None
    return salary


# Text box me message likhne ke liye
def write_text(box, text):
    box.config(state="normal")
    box.delete("1.0", tk.END)
    box.insert(tk.END, text)
    box.config(state="disabled")


# ------------------------- Create tab functions -------------------------

def on_type_change(event=None):
    kind = create_type.get()

    # Pehle sab fields enable karte hain
    for entry in (id_entry, salary_entry, extra_entry):
        entry.config(state="normal")

    if kind == "Person":
        extra_label.config(text="Extra :")
        for entry in (id_entry, salary_entry, extra_entry):
            entry.delete(0, tk.END)
            entry.config(state="disabled")

    elif kind == "Employee":
        extra_label.config(text="Extra :")
        extra_entry.delete(0, tk.END)
        extra_entry.config(state="disabled")

    elif kind == "Manager":
        extra_label.config(text="Department :")

    elif kind == "Developer":
        extra_label.config(text="Programming Language :")


def create_object():
    global person, employee, manager, developer

    kind = create_type.get()

    name = read_text(name_entry, "Name")
    if name is None:
        return

    age = read_age(age_entry)
    if age is None:
        return

    if kind == "Person":
        person = Person(name, age)
        status_label.config(text=f"Person created with name : {person.name} and age : {person.age}.")

    else:
        emp_id = read_text(id_entry, "Employee ID")
        if emp_id is None:
            return

        salary = read_salary(salary_entry)
        if salary is None:
            return

        if kind == "Employee":
            employee = Employee(name, age, emp_id, salary)
            status_label.config(text=f"Employee created with name : {employee.name}, ID : {emp_id}, salary : {salary}.")

        elif kind == "Manager":
            department = read_text(extra_entry, "Department")
            if department is None:
                return
            manager = Manager(name, age, emp_id, salary, department)
            status_label.config(text=f"Manager created with name : {manager.name}, ID : {emp_id}, department : {department}.")

        elif kind == "Developer":
            language = read_text(extra_entry, "Programming Language")
            if language is None:
                return
            developer = Developer(name, age, emp_id, salary, language)
            status_label.config(text=f"Developer created with name : {developer.name}, ID : {emp_id}, language : {language}.")

    # Form clear kar dete hain
    for entry in (name_entry, age_entry, id_entry, salary_entry, extra_entry):
        if str(entry.cget("state")) == "normal":
            entry.delete(0, tk.END)


# ------------------------- Show Details tab function -------------------------

def show_details():
    kind = show_type.get()

    if kind == "Person":
        selected = person
    elif kind == "Employee":
        selected = employee
    elif kind == "Manager":
        selected = manager
    else:
        selected = developer

    if selected is None:
        write_text(show_box, f"{kind} not created !")
    else:
        write_text(show_box, selected.display())


# ------------------------- Update tab function (setters) -------------------------

def update_details():
    kind = update_type.get()

    if kind == "Employee":
        selected = employee
    elif kind == "Manager":
        selected = manager
    else:
        selected = developer

    if selected is None:
        write_text(update_box, f"{kind} is not created yet !")
        return

    new_id = read_text(new_id_entry, "New Employee ID")
    if new_id is None:
        return

    new_salary = read_salary(new_salary_entry)
    if new_salary is None:
        return

    # use of setter methods
    selected.set_employee_id(new_id)
    selected.set_salary(new_salary)

    write_text(update_box, "Details updated !! Updated details are : \n\n" + selected.display())
    new_id_entry.delete(0, tk.END)
    new_salary_entry.delete(0, tk.END)


# ------------------------- Constructor Overloading Demo -------------------------

def run_demo():
    destroyed_messages.clear()

    result = "Constructor overloading : same Employee class, 3 different ways to create object.\n\n"

    result += "1 --- Employee(name, age)\n"
    demo1 = Employee("Khushi", 25)
    result += demo1.display() + "\n"

    result += "2 --- Employee(name, age, ID)\n"
    demo2 = Employee("Rahul", 27, "E101")
    result += demo2.display() + "\n"

    result += "3 --- Employee(name, age, ID, salary)\n"
    demo3 = Employee("Shivani", 30, "E102", 45000.0)
    result += demo3.display() + "\n"

    # using del we can call destructor ----> (__del__)
    del demo1
    del demo2
    del demo3

    result += "Deleting demo objects (destructor called) : \n"
    for message in destroyed_messages:
        result += message + "\n"

    write_text(demo_box, result)


# ------------------------- Exit function -------------------------

def exit_program():
    global person, employee, manager, developer

    # Objects ko None karne par destructor chalta hai (resources free hote hain)
    person = None
    employee = None
    manager = None
    developer = None

    root.destroy()


# =============================== Build the Window ===============================

root = tk.Tk()
root.title("Python OOP Project : Employee Management System")
root.geometry("760x640")

style = ttk.Style()
style.theme_use("clam")

title_label = tk.Label(root, text="Employee Management System", font=("Arial", 18, "bold"))
title_label.pack(pady=(12, 2))

# issubclass() check
inherit_text = (
    f"Employee is subclass of Person : {issubclass(Employee, Person)}   |   "
    f"Manager is subclass of Employee : {issubclass(Manager, Employee)}   |   "
    f"Developer is subclass of Employee : {issubclass(Developer, Employee)}"
)
inherit_label = tk.Label(root, text=inherit_text, font=("Arial", 9), fg="green", wraplength=720)
inherit_label.pack(pady=(0, 6))

# Tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=5)

tab_create = ttk.Frame(notebook, padding=15)
tab_show = ttk.Frame(notebook, padding=15)
tab_update = ttk.Frame(notebook, padding=15)
tab_demo = ttk.Frame(notebook, padding=15)

notebook.add(tab_create, text="  Create  ")
notebook.add(tab_show, text="  Show Details  ")
notebook.add(tab_update, text="  Update (Setters)  ")
notebook.add(tab_demo, text="  Overloading Demo  ")


# ---------------- Tab 1 : Create ----------------
ttk.Label(tab_create, text="Create :").grid(row=0, column=0, sticky="w", pady=6)
create_type = ttk.Combobox(tab_create, values=["Person", "Employee", "Manager", "Developer"],
                           state="readonly", width=30)
create_type.current(0)
create_type.grid(row=0, column=1, pady=6, padx=10)
create_type.bind("<<ComboboxSelected>>", on_type_change)

ttk.Label(tab_create, text="Name :").grid(row=1, column=0, sticky="w", pady=6)
name_entry = ttk.Entry(tab_create, width=33)
name_entry.grid(row=1, column=1, pady=6, padx=10)

ttk.Label(tab_create, text="Age :").grid(row=2, column=0, sticky="w", pady=6)
age_entry = ttk.Entry(tab_create, width=33)
age_entry.grid(row=2, column=1, pady=6, padx=10)

ttk.Label(tab_create, text="Employee ID :").grid(row=3, column=0, sticky="w", pady=6)
id_entry = ttk.Entry(tab_create, width=33)
id_entry.grid(row=3, column=1, pady=6, padx=10)

ttk.Label(tab_create, text="Salary :").grid(row=4, column=0, sticky="w", pady=6)
salary_entry = ttk.Entry(tab_create, width=33)
salary_entry.grid(row=4, column=1, pady=6, padx=10)

extra_label = ttk.Label(tab_create, text="Extra :")
extra_label.grid(row=5, column=0, sticky="w", pady=6)
extra_entry = ttk.Entry(tab_create, width=33)
extra_entry.grid(row=5, column=1, pady=6, padx=10)

ttk.Button(tab_create, text="Create", command=create_object).grid(row=6, column=1, pady=15, sticky="w", padx=10)

on_type_change()   # starting me Person ke hisaab se fields set karo


# ---------------- Tab 2 : Show Details ----------------
ttk.Label(tab_show, text="Show details of :").grid(row=0, column=0, sticky="w", pady=6)
show_type = ttk.Combobox(tab_show, values=["Person", "Employee", "Manager", "Developer"],
                         state="readonly", width=20)
show_type.current(0)
show_type.grid(row=0, column=1, padx=10, pady=6)
ttk.Button(tab_show, text="Show", command=show_details).grid(row=0, column=2, padx=5)

show_box = tk.Text(tab_show, height=14, width=70, state="disabled", font=("Consolas", 11))
show_box.grid(row=1, column=0, columnspan=3, pady=10)


# ---------------- Tab 3 : Update ----------------
ttk.Label(tab_update, text="Update details of :").grid(row=0, column=0, sticky="w", pady=6)
update_type = ttk.Combobox(tab_update, values=["Employee", "Manager", "Developer"],
                           state="readonly", width=30)
update_type.current(0)
update_type.grid(row=0, column=1, padx=10, pady=6)

ttk.Label(tab_update, text="New Employee ID :").grid(row=1, column=0, sticky="w", pady=6)
new_id_entry = ttk.Entry(tab_update, width=33)
new_id_entry.grid(row=1, column=1, padx=10, pady=6)

ttk.Label(tab_update, text="New Salary :").grid(row=2, column=0, sticky="w", pady=6)
new_salary_entry = ttk.Entry(tab_update, width=33)
new_salary_entry.grid(row=2, column=1, padx=10, pady=6)

ttk.Button(tab_update, text="Update", command=update_details).grid(row=3, column=1, sticky="w", padx=10, pady=10)

update_box = tk.Text(tab_update, height=10, width=70, state="disabled", font=("Consolas", 11))
update_box.grid(row=4, column=0, columnspan=2, pady=10)


# ---------------- Tab 4 : Overloading Demo ----------------
ttk.Button(tab_demo, text="Run Constructor Overloading Demo", command=run_demo).pack(anchor="w", pady=5)

demo_box = tk.Text(tab_demo, height=20, width=70, state="disabled", font=("Consolas", 10))
demo_box.pack(pady=10)


# ---------------- Bottom : status + Exit ----------------
status_label = tk.Label(root, text="Welcome ! Choose a tab to start.", anchor="w", fg="blue",
                        wraplength=720, justify="left")
status_label.pack(fill="x", padx=12)

ttk.Button(root, text="Exit", command=exit_program).pack(pady=8)

root.protocol("WM_DELETE_WINDOW", exit_program)

root.mainloop()