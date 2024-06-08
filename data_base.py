import sqlite3

#Connect to daat base fille
def get_connection():
    return sqlite3.connect('speed_print_game.db')



#Create table 
def creat_table():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS game_data(
id_user INTEGER PRIMARY KEY AUTOINCREMENT,
user_name TEXT NOT NULL,
user_password TEXT NOT NULL
)
""")
    connect.commit()
    connect.close()

def table_exist(table_name):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name = ?", (table_name, ))
    exists = cursor.fetchone() is not None 
    connect.close()
    return exists

def add_user(user_name, user_password):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO game_data(user_name, user_password) VALUES (?, ?)', (user_name, user_password,))
    connect.commit()
    connect.close()

def fetchall_data():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM game_data')
    rows = cursor.fetchall()
    connect.close()
    return rows

def user_login(user_name, user_password):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT 1 FROM game_data WHERE user_name = ? AND user_password = ?', (user_name, user_password))
    exists = cursor.fetchone() is not None
    connect.close()
    return exists
