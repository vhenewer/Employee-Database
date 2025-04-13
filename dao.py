import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self):
        self.conn = sqlite3.connect("employee_db.sqlite3")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL,
            hire_date TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, employee: Employee):
        query = 'INSERT INTO employee (name, position, salary, hire_date) VALUES (?, ?, ?, ?)'
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()

    def get_by_id(self, id: int):
        query = 'SELECT * FROM employee WHERE id = ?'
        cursor = self.conn.execute(query, (id,))
        row = cursor.fetchone()
        if row:
            return Employee(*row)
        return None

    def get_all(self):
        query = 'SELECT * FROM employee'
        cursor = self.conn.execute(query)
        return [Employee(*row) for row in cursor.fetchall()]

    def update(self, employee: Employee):
        query = 'UPDATE employee SET name = ?, position = ?, salary = ?, hire_date = ? WHERE id = ?'
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self, id: int):
        query = 'DELETE FROM employee WHERE id = ?'
        self.conn.execute(query, (id,))
        self.conn.commit()
