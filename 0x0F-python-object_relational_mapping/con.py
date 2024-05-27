import MySQLdb

#connection info
db_host = "localhost"
db_name = "Kitchenette"
db_user = "root"
db_passwd = "Kamau@1980!"

db = MySQLdb.connect(
host = db_host,
user = db_user,
passwd = db_passwd,
db = db_name
)
#cursor for db interaction
db_cursor = db.cursor()
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS Recipes(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
ingredients TEXT,
instructions TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
#commit changes
db.commit()
#close the connection
db_cursor.close()
db.close()


