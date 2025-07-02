from tkinter import *
from tkinter import ttk
import re
from tkinter.messagebox import showinfo



def finish():
    root.destroy()
    print('Закрытие приложения')

# root = Tk()
# root.title('Первое окно')
# root.geometry('600x700+1000+500')  #  размеры окна о положение по Х и У
# # root.attributes('-fullscreen', True)   # На весь экран
#
# root.attributes('-alpha', 0.5)  #  Прозрачность окна

# def click():
#     print('Hello')
#
#
# def show_message():
#     label["text"] = entry.get()
#
#
# # root.attributes('-toolwindow', True)  # отключение верхней панели
# root.protocol('WM_DELETE_WINDOW', finish)
#
# label =Label(text='Привет Пепа', font=('Arial', 14), background='red')
# label.pack()
#
# label = ttk.Label(text="Hello Tkinter", background="#FFCDD2", foreground="#B71C1C", padding=8)
# label.pack(expand=True)
#
# btn = ttk.Button(text='Button', command=show_message)
# btn.place(height=200, width=300)
# btn.pack(anchor='w', padx=1, pady=300)  #  кнопка в окне


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Python")
notebook.add(frame2, text="Java")

root.mainloop()
