from tkinter import *

def finish():
    root.destroy()
    print('Закрытие приложения')

root = Tk()
root.title('Первое окно')
root.geometry('600x700+1000+500')  #  размеры окна о положение по Х и У
# root.attributes('-fullscreen', True)   # На весь экран

root.attributes('-alpha', 0.5)  #  Прозрачность окна

# root.attributes('-toolwindow', True)  # отключение верхней панели

root.protocol('WM_DELETE_WINDOW', finish)
label =Label(text='Привет Пепа')
label.pack()

root.mainloop()