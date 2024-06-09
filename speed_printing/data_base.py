import sqlite3

#Connect to daat base fille
def get_connection():
    return sqlite3.connect('speed_print_game.db')



#Create table 
def creat_table():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id_user INTEGER PRIMARY KEY AUTOINCREMENT,
user_name TEXT NOT NULL,
user_password TEXT NOT NULL
)""")
                   
    cursor.execute("""
CREATE TABLE IF NOT EXISTS UserAchievements(
achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_name TEXT NOT NULL,
time_records INTEGER,
accuracy INTEGER,
FOREIGN KEY(user_name) REFERENCES Users(user_name)
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
    cursor.execute('INSERT INTO Users(user_name, user_password) VALUES (?, ?)', (user_name, user_password,))
    connect.commit()
    connect.close()

def fetchall_data():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Users')
    rows = cursor.fetchall()
    connect.close()
    return rows

def user_login(user_name, user_password):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT 1 FROM Users WHERE user_name = ? AND user_password = ?', (user_name, user_password))
    exists = cursor.fetchone() is not None
    connect.close()
    return exists

def set_user_achievement(user_name, time_records, accuracy):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO UserAchievements(user_name, time_records, accuracy) VALUES (?, ?, ?)', (user_name, time_records, accuracy,))
    connect.commit()
    connect.close()

def get_time_records(user_name):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT MAX(time_records) FROM UserAchievements WHERE user_name = ?', (user_name, ))
    record = cursor.fetchone()[0]
    connect.close()
    return record if record is not None else 0

def get_accuracy_records(user_name):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT MAX(accuracy) FROM UserAchievements WHERE user_name = ?', (user_name,))
    record = cursor.fetchone()[0]
    connect.close()
    return record

def get_all_records(user_name):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM UserAchievements WHERE user_name = ?', (user_name, ))
    rows = cursor.fetchall()
    connect.close()
    return rows
