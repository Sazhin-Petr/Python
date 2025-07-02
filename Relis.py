import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RepairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Учет ремонтов техники")

        # Подключение к БД
        self.conn = sqlite3.connect("repair_db.sqlite")
        self.cursor = self.conn.cursor()

        # Создание виджетов
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Таблица с данными
        self.tree = ttk.Treeview(self.root, columns=("ID", "Модель", "Описание", "Статус", "Дата"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Модель", text="Модель")
        self.tree.heading("Описание", text="Описание")
        self.tree.heading("Статус", text="Статус")
        self.tree.heading("Дата", text="Дата")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Кнопки
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.X)

        tk.Button(btn_frame, text="Добавить", command=self.add_repair).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Обновить", command=self.load_data).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Фильтровать", command=self.filter_data).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="График", command=self.show_chart).pack(side=tk.LEFT)

    def load_data(self):
        """Загрузка данных из БД в таблицу"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute("""
        SELECT repairs.id, vehicles.model, repairs.description, repairs.status, repairs.date
        FROM repairs
        JOIN vehicles ON repairs.vehicle_id = vehicles.id
        """)

        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

    def add_repair(self):
        """Окно добавления нового ремонта"""
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить ремонт")

        tk.Label(add_window, text="Модель техники:").grid(row=0, column=0)
        model_entry = tk.Entry(add_window)
        model_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Описание ремонта:").grid(row=1, column=0)
        desc_entry = tk.Entry(add_window)
        desc_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Статус:").grid(row=2, column=0)
        status_var = tk.StringVar(value="В работе")
        status_menu = tk.OptionMenu(add_window, status_var, "В работе", "Завершен", "Отменен")
        status_menu.grid(row=2, column=1)

        def save_repair():
            model = model_entry.get()
            desc = desc_entry.get()
            status = status_var.get()

            if not model or not desc:
                messagebox.showerror("Ошибка", "Заполните все поля!")
                return

            # Добавляем транспорт (если его нет)
            self.cursor.execute("INSERT OR IGNORE INTO vehicles (model) VALUES (?)", (model,))
            self.cursor.execute("SELECT id FROM vehicles WHERE model=?", (model,))
            vehicle_id = self.cursor.fetchone()[0]

            # Добавляем ремонт
            self.cursor.execute(
                "INSERT INTO repairs (vehicle_id, description, status) VALUES (?, ?, ?)",
                (vehicle_id, desc, status)
            )
            self.conn.commit()
            add_window.destroy()
            self.load_data()

        tk.Button(add_window, text="Сохранить", command=save_repair).grid(row=3, columnspan=2)

    def filter_data(self):
        """Фильтрация по статусу"""
        filter_window = tk.Toplevel(self.root)
        filter_window.title("Фильтр")

        status_var = tk.StringVar(value="Все")
        tk.OptionMenu(filter_window, status_var, "Все", "В работе", "Завершен", "Отменен").pack()

        def apply_filter():
            status = status_var.get()
            query = """
            SELECT repairs.id, vehicles.model, repairs.description, repairs.status, repairs.date
            FROM repairs
            JOIN vehicles ON repairs.vehicle_id = vehicles.id
            """
            if status != "Все":
                query += f" WHERE repairs.status = '{status}'"

            for row in self.tree.get_children():
                self.tree.delete(row)

            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                self.tree.insert("", tk.END, values=row)

            filter_window.destroy()

        tk.Button(filter_window, text="Применить", command=apply_filter).pack()

    def show_chart(self):
        """График статистики по статусам"""
        self.cursor.execute("SELECT status, COUNT(*) FROM repairs GROUP BY status")
        data = self.cursor.fetchall()

        statuses = [row[0] for row in data]
        counts = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.bar(statuses, counts)
        ax.set_title("Статистика ремонтов")

        # Встраиваем график в Tkinter
        chart_window = tk.Toplevel(self.root)
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack()


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = RepairApp(root)
    root.mainloop()