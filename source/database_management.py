import tinydb as db

def create_database_connection(db_path):
    db_conection = db.TinyDB(db_path)
    return db_conection

items_db_path = "./items/items.json"
items_db = create_database_connection(items_db_path)
print(items_db)
