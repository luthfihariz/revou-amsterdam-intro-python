# example of singleton in python
# database connection


class Database:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.init_connection()
        return cls._instance

    def init_connection(self):
        print("Database connection initialized")

    def __init__(self):
        print("Database instance created")


# Usage
db1 = Database.get_instance()
db2 = Database.get_instance()


print(db1 is db2)
