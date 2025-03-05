import psycopg2
import hashlib

DB_SERVER_CONFIG = {
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

DB_CONFIG = {
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432",
    "dbname": "employees"
}

# QUERIES
CREATE_DATABASE_QUERY = "CREATE DATABASE employees"

CREATE_USERS_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(20) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL,
        role VARCHAR(20) CHECK (role IN ('admin', 'employee')) NOT NULL
    )
"""

CREATE_EMPLOYEES_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS employees(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        department VARCHAR(100),
        salary DECIMAL(10,2)
    )
"""

SEED_ADMIN_USER = """
    INSERT INTO users(username,password,role) VALUES('admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918','admin')
"""

class Database:
    def __init__(self):
        self.conn = None

    def connect_database_server(self):
        try:
            self.conn = psycopg2.connect(**DB_SERVER_CONFIG)
            return self.conn
        except Exception as e:
            print(f"There was a problem connecting to the database server: {e}")
            return None

    def connect_database(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            return self.conn
        except Exception as e:
            print(f"There was a problem connecting to the database: {e}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()

    def setup_database(self):
        
        conn = self.connect_database_server()
        if conn:
            try:
                conn.autocommit = True
                cursor = conn.cursor()
                cursor.execute(CREATE_DATABASE_QUERY)
                print("The database has been created successfully.")
            except Exception as e:
                print(f"Error creating database: {e}")
            finally:
                self.close()
        else:
            print("Skipping database creation due to connection failure.")

    
        conn = self.connect_database()
        if conn:
            try:
                conn.autocommit = True
                cursor = conn.cursor()
                cursor.execute(CREATE_USERS_TABLE_QUERY)
                cursor.execute(CREATE_EMPLOYEES_TABLE_QUERY)
                cursor.execute(SEED_ADMIN_USER)
                print("The tables have been created successfully.")
            except Exception as e:
                print(f"Error creating tables: {e}")
            finally:
                self.close()
        else:
            print("Skipping table creation due to connection failure.")


