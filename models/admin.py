from models.users import User
from helpers.database import Database

class Admin(User):
    
    def __init__(self, username, password):
        super().__init__(username, password)
        
    def add_user(self, new_username, new_password, role):
        db = Database()
        conn = db.connect_database()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            hashed_password = self.hash_password(new_password)
            new_user = cursor.execute('INSERT INTO users (username, password, role) VALUES(%s, %s, %s)',
                           (new_username, new_password, role))
            conn.commit()
            return new_user
        
        except Exception as e:
            print(f"Error adding user : {e}")
            
        finally:
            db.close()
