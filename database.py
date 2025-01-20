import sqlite3

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bot_data (
            id INTEGER PRIMARY KEY,
            direction TEXT,
            start BOOLEAN,
            stop BOOLEAN,
            speed INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arm_data (
            id INTEGER PRIMARY KEY,
            baseRight TEXT,
            baseLeft TEXT,
            shoulderDown TEXT,
            shoulderUp TEXT,
            elbowDown TEXT,
            elbowUp TEXT,
            wristDown TEXT,
            wristUp TEXT,
            gripDown TEXT,
            gripUp TEXT,
            motor BOOLEAN
        )
    ''')
    
    conn.commit()
    conn.close()

# Store the data in the database
def store_data(data):
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()

    # Insert data into bot_data table
    cursor.execute('''
        INSERT INTO bot_data (direction, start, stop, speed)
        VALUES (?, ?, ?, ?)
    ''', (data['bot']['direction'], data['bot']['start'], data['bot']['stop'], data['bot']['speed']))

    # Insert data into arm_data table
    cursor.execute('''
        INSERT INTO arm_data (baseRight, baseLeft, shoulderDown, shoulderUp, elbowDown, elbowUp, wristDown, wristUp, gripDown, gripUp, motor)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['arm']['baseRight'], data['arm']['baseLeft'], data['arm']['shoulderDown'], data['arm']['shoulderUp'], data['arm']['elbowDown'], data['arm']['elbowUp'], data['arm']['wristDown'], data['arm']['wristUp'], data['arm']['gripDown'], data['arm']['gripUp'], data['arm']['motor']))

    conn.commit()
    conn.close()
