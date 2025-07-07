import sqlite3

with sqlite3.connect('vehicles.db') as con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT NOT NULL,
            plate_number TEXT UNIQUE,
            status TEXT DEFAULT 'На линии' CHECK(status IN ('На линии', 'Ремонт')))
        """)

cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("Татра 815", "Е102УС", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("Нива Шевроле", "В598ВТ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("Нива Шевроле", "Н053УК", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("LADA GRANTA", "О862ОТ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("Газель NEXT", "М322ХУ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("НЕФАЗ", "К806КВ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("Камаз КМУ", "Н715УУ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("АГП-24 ГАЗ", "Н952РХ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("АГП-24 Зил", "Х507ТО", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("АГП-24 КАМАЗ", "А885МА", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("Daewoo", "Е471МУ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("КС-55717", "Н089УУ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("КС-55717", "О202АТ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("КС-55717", "О072УК", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("КС-55717", "Е373МУ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("КАМАЗ 53114", "Х091ОВ", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("ГАЗ-3309", "Р247УК", "На линии"))
cur.execute("INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
            ("КАМАЗ УЗСТ", "Н330УУ", "На линии"))


con.commit()
con.close()