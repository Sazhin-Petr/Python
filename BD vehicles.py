import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class VehicleRepairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Учет технического состояния автотранспорта предприятия")

        # Подключение к БД
        self.conn = sqlite3.connect("vehicles.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Создание интерфейса
        self.create_widgets()
        self.load_data()

    # Создание таблицы с данными
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT NOT NULL,
                plate_number TEXT UNIQUE,
                status TEXT DEFAULT 'На линии' CHECK(status IN ('На линии', 'Ремонт')))
            """)

        vehicles_data = [
            ("Татра 815", "Е102УС", "На линии"),
            ("Нива Шевроле", "В598ВТ", "На линии"),
            ("Нива Шевроле", "Н053УК", "На линии"),
            ("LADA GRANTA", "О862ОТ", "На линии"),
            ("Газель NEXT", "М322ХУ", "На линии"),
            ("НЕФАЗ", "К806КВ", "На линии"),
            ("Камаз КМУ", "Н715УУ", "На линии"),
            ("АГП-24 ГАЗ", "Н952РХ", "На линии"),
            ("АГП-24 Зил", "Х507ТО", "На линии"),
            ("АГП-24 КАМАЗ", "А885МА", "На линии"),
            ("Daewoo", "Е471МУ", "На линии"),
            ("КС-55717", "Н089УУ", "На линии"),
            ("КС-55717", "О202АТ", "На линии"),
            ("КС-55717", "О072УК", "На линии"),
            ("КС-55717", "Е373МУ", "На линии"),
            ("КАМАЗ 53114", "Х091ОВ", "На линии"),
            ("ГАЗ-3309", "Р247УК", "На линии"),
            ("КАМАЗ УЗСТ", "Н330УУ", "На линии")
        ]

        for vehicle in vehicles_data:
            try:
                self.cursor.execute(
                    "INSERT INTO vehicles (model, plate_number, status) VALUES (?, ?, ?)",
                    vehicle
                )
            except sqlite3.IntegrityError:
                pass

        self.conn.commit()

    def create_widgets(self):
        """Создаем интерфейс"""
        # Таблица с автомобилями
        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Модель", "Госномер", "Статус"),
            show="headings"
        )
        self.tree.heading("ID", text="#")
        self.tree.heading("Модель", text="Модель")
        self.tree.heading("Госномер", text="Госномер")
        self.tree.heading("Статус", text="Статус")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Фрейм с кнопками
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Button(
            btn_frame,
            text="Добавить авто",
            command=self.add_vehicle
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame,
            text="На линии",
            command=lambda: self.change_status("На линии"),
            bg="lightgreen"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame,
            text="В ремонт",
            command=lambda: self.change_status("Ремонт"),
            bg="salmon"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame,
            text="Удалить авто",
            command=self.delete_vehicle,
            bg="indianred",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame,
            text="Обновить",
            command=self.load_data
        ).pack(side=tk.RIGHT, padx=5)

    def load_data(self):
        """Загружаем данные в таблицу"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute("SELECT id, model, plate_number, status FROM vehicles")
        for vehicle in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=vehicle)

    def add_vehicle(self):
        """Добавляем новое авто"""
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить автомобиль")

        tk.Label(add_window, text="Модель:").grid(row=0, column=0, padx=5, pady=5)
        model_entry = tk.Entry(add_window)
        model_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Госномер:").grid(row=1, column=0, padx=5, pady=5)
        plate_entry = tk.Entry(add_window)
        plate_entry.grid(row=1, column=1, padx=5, pady=5)

        def save_vehicle():
            model = model_entry.get()
            plate = plate_entry.get()

            if not model or not plate:
                messagebox.showerror("Ошибка", "Заполните все поля!")
                return

            try:
                self.cursor.execute(
                    "INSERT INTO vehicles (model, plate_number) VALUES (?, ?)",
                    (model, plate)
                )
                self.conn.commit()
                add_window.destroy()
                self.load_data()
            except sqlite3.IntegrityError:
                messagebox.showerror("Ошибка", "Авто с таким госномером уже есть!")

        tk.Button(
            add_window,
            text="Сохранить",
            command=save_vehicle
        ).grid(row=2, columnspan=2, pady=10)

    def change_status(self, new_status):
        """Меняем статус выбранного авто"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите автомобиль!")
            return

        vehicle_id = self.tree.item(selected_item)['values'][0]
        self.cursor.execute(
            "UPDATE vehicles SET status = ? WHERE id = ?",
            (new_status, vehicle_id)
        )
        self.conn.commit()
        self.load_data()

    def delete_vehicle(self):
        """Удаляем выбранное авто"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите автомобиль для удаления!")
            return

        vehicle_id = self.tree.item(selected_item)['values'][0]
        vehicle_model = self.tree.item(selected_item)['values'][1]

        if not messagebox.askyesno(
                "Подтверждение",
                f"Удалить автомобиль {vehicle_model}? Данные нельзя будет восстановить!"):
            return

        try:
            self.cursor.execute("DELETE FROM vehicles WHERE id = ?", (vehicle_id,))
            self.conn.commit()
            self.load_data()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить авто: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x440")
    app = VehicleRepairApp(root)
    root.mainloop()
