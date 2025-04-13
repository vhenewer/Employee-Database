import sqlite3
from employee import Employee
from dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    for emp in dao.get_all():
        dao.delete(emp.id)

    dao.cursor.execute("DELETE FROM sqlite_sequence WHERE name='employee'")
    dao.conn.commit()

    emp = Employee(name="Venera", position="Manager", salary=200000, hire_date="2025-05-25")
    dao.insert(emp)
    print("Inserted new employee.")

    print("\nAll employees:")
    for e in dao.get_all():
        print(e)

    print("\nGet employee by ID = 1:")
    employee = dao.get_by_id(1)
    if employee:
        print(employee)

    if employee:
        employee.salary = 250000
        dao.update(employee)
        print("\nUpdated salary.")
        print(dao.get_by_id(1))

    dao.delete(1)
    print("\nDeleted employee with ID = 1.")

    print("\nFinal employee list:")
    for e in dao.get_all():
        print(e)

if __name__ == "__main__":
    main()

def print_table_contents():
    conn = sqlite3.connect("employee_db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()

    print("\nContents of the employee table:")
    print("ID | Name | Position | Salary | Hire Date")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

    conn.close()

print_table_contents()
