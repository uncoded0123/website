import sqlite3

def create_on_off():
    conn = sqlite3.connect('my_db.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS on_off3 (
    id TEXT,
    state TEXT
    )
    """)
    conn.commit()
    conn.close()
#create_on_off()

def create_read_sensor():
    conn = sqlite3.connect('my_db.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sensor_table (
    id TEXT,
    data TEXT
    )
    """)
    conn.commit()
    conn.close()
#create_read_sensor()

#on/off
def first_data_on_off():   
    conn = sqlite3.connect('my_db.db') # /var/www/FlaskApp/FlaskApp/my_db.db
    cur = conn.cursor()
    cur.execute('REPLACE INTO on_off3 (id, state) VALUES (?, ?)',  ('name1','hi'))
    conn.commit()
    conn.close()
#first_data_on_off()

#read sensor
def first_data_read_sensor():    
    conn = sqlite3.connect('my_db.db') # /var/www/FlaskApp/FlaskApp/my_db.db
    cur = conn.cursor()
    cur.execute('REPLACE INTO sensor_table (id, data) VALUES (?, ?)',  ('name2','hi'))
    conn.commit()
    conn.close()
#first_data_read_sensor()
