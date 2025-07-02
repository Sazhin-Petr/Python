import sqlite3

# Подключение к базе (или создание, если её нет)
conn = sqlite3.connect("repair_db.sqlite")
cursor = conn.cursor()

# Создание таблицы "Транспортные средства"
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    year INTEGER,
    plate_number TEXT UNIQUE
)
""")

cursor.execute('INSERT INTO vehicles VALUES(1, "Tatra 815", 2014, "Е102УС")')

# Создание таблицы "Ремонты"
cursor.execute("""
CREATE TABLE IF NOT EXISTS repairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER,
    description TEXT,
    status TEXT CHECK(status IN ('В работе', 'Завершен', 'Отменен')),
    date TEXT DEFAULT CURRENT_DATE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
)
""")

conn.commit()
conn.close()