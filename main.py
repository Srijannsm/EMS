from helpers.database import Database
from models.admin import Admin
from models.users import User
from helpers.employee_manager import EmployeeManager

def main():
    while True:
        print("\n Employee Management System")
        print("1. Login")
        print("2. Migrate Database")
        print("3. Exit")
        #Git pull example
        #Git pull example 2
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            user = Admin(username, password) if username == 'admin' else User(username, password)
            
            if not user.authenticate():
                print (f"Invalid username or password")
            
            emp_manager = EmployeeManager()
                
            while True:
                print (f"\nEmployee Management System")
                print ("1. Add Employee")
                print ("2. View Employee")
                print ("3. Search Employee")
                print ("4. Update Employee")
                print ("5. Delete Employee")
                print ("6. View Salary Statistics")
                print ("7. Add User (Admin Only)")
                print ("8. Export to CSV")
                print ("9. Logout")
                
                choice = input("Enter your choice : ")
                
                if choice == "1":
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    department = input("Enter department: ")
                    salary = float(input("Enter salary: "))
                    
                    emp_manager.add_employee(name, age, department, salary)
                
                
                if choice == "2":
                    emp_manager.view_employees()
                    #Local comment
                
                if choice == "3":
                    name = input("Enter Name (or leave blank) :")
                    department = input("Enter Department (or leave blank) :")
                    
                    emp_manager.search_employee(name or None, department or None)
                
                if choice == "4":
                    id = int(input("Enter Employee ID to be updated: "))
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    department = input("Enter department: ")
                    salary = float(input("Enter salary: "))
                    
                    emp_manager.update_employee(id, name, age, department, salary)
                
                if choice == "5":
                    id = int(input("Enter Employee ID to be deleted: "))
                    emp_manager.delete_employee(id)
                
                if choice == "6":
                    emp_manager.calculate_salary_stats()
                
                if choice == "7" and isinstance(user, Admin):
                    new_username = input("Enter new username: ")
                    new_password = input("Enter new password: ")
                    role = input("Enter role (admin or employee): ")
                    
                    user.add_user(new_username, new_password, role)
            
                
                if choice == "8":
                    emp_manager.export_to_csv()
                
                if choice == "9":
                    print ("Logging out....")
                    break
                
        
        elif choice == "2":
            database = Database()
            database.setup_database()
        
        elif choice == "3":
            print("Exiting.....")
            break
            
        else:
            print("Invalid choice. Please try again.")    

if __name__ == "__main__":
    main()
