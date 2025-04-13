# Employee Database

## Overview
A simple Python application that uses SQLite to manage employee data, demonstrating CRUD operations.

---

##  Objectives

- Create a SQLite database to store employee information.
- Build an `Employee` class for data representation.
- Build an `EmployeeDAO` class for interacting with the database.
- Perform full CRUD operations.
- Demonstrate the functionality via a test script.

---

##  Classes Overview

### - `Employee` Class (employee.py)

Represents an employee record with:

- `id`: int (auto-incremented by DB)
- `name`: str
- `position`: str
- `salary`: float
- `hire_date`: str (format: YYYY-MM-DD)

Includes constructor, getters/setters, and a `__str__()` method for pretty-printing.

---

### - `EmployeeDAO` Class (dao.py)

Handles database operations:

- `insert(employee: Employee)`
- `get_by_id(id: int) -> Employee`
- `get_all() -> List[Employee]`
- `update(employee: Employee)`
- `delete(id: int)`
- Initializes and creates the `employee` table if not exists.

---

## How to Run
1. Clone the repository
2. Run `main.py` using Python:
   ```bash
   python main.py

This will:
- Insert a new employee
- Display all employees
- Retrieve employee by ID
- Update employee's salary
- Delete employee by ID
- Display final list
