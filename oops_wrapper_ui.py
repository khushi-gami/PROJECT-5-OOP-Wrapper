import tkinter as tk
from tkinter import ttk, messagebox


# ----------------------------------- Person Class ------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return (
            "Person Details\n"
            "----------------------\n"
            f"Name : {self.name}\n"
            f"Age  : {self.age}\n"
        )


# ----------------------------------- Employee Class ------------------------------------
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def display(self):
        return (
            "Employee Details\n"
            "----------------------\n"
            f"Name        : {self.name}\n"
            f"Age         : {self.age}\n"
            f"Employee ID : {self.get_employee_id()}\n"
            f"Salary      : {self.get_salary()}\n"
        )


# ----------------------------------- Manager Class ------------------------------------
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        return (
            "Manager Details\n"
            "----------------------\n"
            f"Name        : {self.name}\n"
            f"Age         : {self.age}\n"
            f"Employee ID : {self.get_employee_id()}\n"
            f"Salary      : {self.get_salary()}\n"
            f"Department  : {self.department}\n"
        )


# ----------------------------------- Application UI ------------------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Management System")
        self.geometry("560x520")
        self.minsize(520, 480)

        # Stored objects (same as person / employee / manager variables)
        self.person = None
        self.employee = None
        self.manager = None

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)

        ttk.Label(self, text="Python OOP Project : Employee Management System",
                  style="Title.TLabel").pack(pady=(14, 8))

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(fill="both", expand=True, padx=14, pady=6)

        self.build_person_tab()
        self.build_employee_tab()
        self.build_manager_tab()
        self.build_show_tab()

        self.status = tk.StringVar(value="Ready.")
        ttk.Label(self, textvariable=self.status, foreground="#2e7d32").pack(
            anchor="w", padx=16, pady=(2, 0))

        ttk.Button(self, text="Exit", command=self.exit_app).pack(pady=10)

    # ---------- helpers ----------
    def make_form(self, parent, fields):
        """Create labelled entries; returns {label: StringVar}."""
        frame = ttk.Frame(parent, padding=20)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(1, weight=1)
        vars_ = {}
        for i, label in enumerate(fields):
            ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w", pady=8)
            var = tk.StringVar()
            ttk.Entry(frame, textvariable=var).grid(
                row=i, column=1, sticky="ew", padx=(12, 0), pady=8)
            vars_[label] = var
        return frame, vars_, len(fields)

    @staticmethod
    def get_int(value, field):
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"{field} must be a whole number.")

    @staticmethod
    def get_text(value, field):
        value = value.strip()
        if not value:
            raise ValueError(f"{field} is required.")
        return value

    @staticmethod
    def clear(vars_):
        for v in vars_.values():
            v.set("")

    # ---------- tab 1 : person ----------
    def build_person_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Create Person")
        frame, self.pv, n = self.make_form(tab, ["Name", "Age"])
        ttk.Button(frame, text="Create Person", command=self.create_person).grid(
            row=n, column=0, columnspan=2, pady=16)

    def create_person(self):
        try:
            name = self.get_text(self.pv["Name"].get(), "Name")
            age = self.get_int(self.pv["Age"].get(), "Age")
        except ValueError as e:
            return messagebox.showerror("Invalid input", str(e))
        self.person = Person(name, age)
        self.status.set(f"Person created with name : {name} and age : {age}.")
        self.clear(self.pv)

    # ---------- tab 2 : employee ----------
    def build_employee_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Create Employee")
        frame, self.ev, n = self.make_form(
            tab, ["Name", "Age", "Employee ID", "Salary"])
        ttk.Button(frame, text="Create Employee", command=self.create_employee).grid(
            row=n, column=0, columnspan=2, pady=16)

    def create_employee(self):
        try:
            name = self.get_text(self.ev["Name"].get(), "Name")
            age = self.get_int(self.ev["Age"].get(), "Age")
            emp_id = self.get_text(self.ev["Employee ID"].get(), "Employee ID")
            salary = self.get_int(self.ev["Salary"].get(), "Salary")
        except ValueError as e:
            return messagebox.showerror("Invalid input", str(e))
        self.employee = Employee(name, age, emp_id, salary)
        self.status.set(
            f"Employee created with name : {name}, age : {age}, "
            f"ID : {emp_id}, and salary : {salary}.")
        self.clear(self.ev)

    # ---------- tab 3 : manager ----------
    def build_manager_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Create Manager")
        frame, self.mv, n = self.make_form(
            tab, ["Name", "Age", "Employee ID", "Salary", "Department"])
        ttk.Button(frame, text="Create Manager", command=self.create_manager).grid(
            row=n, column=0, columnspan=2, pady=16)

    def create_manager(self):
        try:
            name = self.get_text(self.mv["Name"].get(), "Name")
            age = self.get_int(self.mv["Age"].get(), "Age")
            emp_id = self.get_text(self.mv["Employee ID"].get(), "Employee ID")
            salary = self.get_int(self.mv["Salary"].get(), "Salary")
            dept = self.get_text(self.mv["Department"].get(), "Department")
        except ValueError as e:
            return messagebox.showerror("Invalid input", str(e))
        self.manager = Manager(name, age, emp_id, salary, dept)
        self.status.set(
            f"Manager created with name : {name}, age : {age}, ID : {emp_id}, "
            f"salary : {salary}, and department : {dept}.")
        self.clear(self.mv)

    # ---------- tab 4 : show details ----------
    def build_show_tab(self):
        tab = ttk.Frame(self.tabs, padding=16)
        self.tabs.add(tab, text="Show Details")

        buttons = ttk.Frame(tab)
        buttons.pack(fill="x")
        for text, kind in (("Person", "person"), ("Employee", "employee"),
                           ("Manager", "manager")):
            ttk.Button(buttons, text=text,
                       command=lambda k=kind: self.show_details(k)).pack(
                side="left", expand=True, fill="x", padx=4)

        self.output = tk.Text(tab, height=10, font=("Consolas", 11),
                              state="disabled", bg="#f7f7f7", relief="flat",
                              padx=12, pady=12)
        self.output.pack(fill="both", expand=True, pady=(14, 0))

    def show_details(self, kind):
        obj = getattr(self, kind)
        text = obj.display() if obj is not None else f"{kind.capitalize()} not created !"
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", text)
        self.output.config(state="disabled")

    # ---------- exit ----------
    def exit_app(self):
        if messagebox.askyesno("Exit", "Do you want to exit the system?"):
            messagebox.showinfo(
                "Goodbye!", "Exiting the system. All resources have been freed.")
            self.destroy()


if __name__ == "__main__":
    App().mainloop()