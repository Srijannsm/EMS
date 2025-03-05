from helpers.database import Database
import csv
class EmployeeManager:
    
    def __init__(self):
        self.db = Database()
        
    def add_employee(self, name, age, department, salary):
        conn = self.db.connect_database()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            query = """
                    INSERT INTO employees (name, age, department, salary)
                    VALUES (%s, %s, %s, %s)
                    """
            cursor.execute(query,(name, age, department, salary))
            conn.commit()
            print("New Employee added successfully")
            
        except Exception as e:
            print("Error in adding new employee : {e}")
            
        finally:
            self.db.close()
        
    def view_employees(self):
        conn = self.db.connect_database()
        if not conn:
            return 
        
        try:
            cursor = conn.cursor()
            query = """
                    SELECT * FROM employees
                    """
            cursor.execute(query)
            employees = cursor.fetchall()
            conn.commit()
            for emp in employees:
                print(f"[ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}]")
            return employees
            
        except Exception as e:
            print("Error displaying employee : {e}")
            
        finally:
            self.db.close()
            
    def search_employee(self, name = None, department = None):
        conn = self.db.connect_database()
        if not conn:
            return 
        
        try:
            cursor = conn.cursor()
            query = """
                    SELECT * FROM employees
                    WHERE name = %s OR department = %s
                    """
            cursor.execute(query,(name, department))
            employees = cursor.fetchall()
            conn.commit()
            print("\n Search Results: ")
            if not employees:
                print("No employee found.")
                return
            for emp in employees:
                print(f"[ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}]")
            
        except Exception as e:
            print("Error displaying employee : {e}")
            
        finally:
            self.db.close()
            
    def update_employee(self, id, name, age, department, salary):
        conn = self.db.connect_database()
        if not conn:
            return 
        
        try:
            cursor = conn.cursor()
            query = """
                    UPDATE employees
                    SET name = %s, age = %s, department = %s, salary = %s
                    WHERE id = %s
                    """
            cursor.execute(query,(name, age, department, salary, id))
            conn.commit() 
            print("Employee updated successfully")
            
        except Exception as e:
            print("Error updating employee : {e}")
            
        finally:
            self.db.close()
            
    def delete_employee(self, id):
        conn = self.db.connect_database()
        if not conn:
            return 
        
        try:
            cursor = conn.cursor()
            query = """
                    DELETE FROM employees
                    WHERE id = %s
                    """
            cursor.execute(query,(id,))
            conn.commit() 
            print("Employee deleted successfully")
            
        except Exception as e:
            print("Error deleting employee : {e}")
            
        finally:
            self.db.close()
            
    def calculate_salary_stats(self):
        conn = self.db.connect_database()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            query = """
                    SELECT AVG(salary), MAX(salary) , MIN(salary)
                    FROM employees
                    """
            cursor.execute(query)
            stats = cursor.fetchone()
            # print(stats)
            print("\n Salary Statistics: ")
            print(f"Average salary: {stats[0]}")
            print(f"Maximum salary: {stats[1]}")
            print(f"Minimum salary: {stats[2]}")
            
        except Exception as e:
            print("Error calculating salary stats : {e}")
            
        finally:
            self.db.close()
            
    def export_to_csv(self):
        try:
            employees = self.view_employees()
            if employees is None:
                raise Exception("No employees to export")
            
            with open("employees.csv", "w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Age", "Department", "Salary"])
                writer.writerows(employees)
            print("Data exported to employees.csv successfully")
            
        except Exception as e:
            print("Error exporting data to csv : {e}")
            
        finally:
            self.db.close()