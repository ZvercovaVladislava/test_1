import tkinter as tk
import threading

class MultiTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная №1")
        self.root.geometry("700x300") 

        # Флаг работы
        self.running = True

        # Панель для смены цвета
        self.color_panel = tk.Frame(root, bg="lightgray", height=100, width=700)  
        self.color_panel.pack(fill="x")

        # Метка для события
        self.time_label = tk.Label(root, text="Жду событие...", font=("Arial", 16), width=40)
        self.time_label.pack(pady=15)

        # Счётчик
        self.counter = 0
        self.counter_label = tk.Label(root, text="Счётчик: 0", font=("Arial", 16), width=40)
        self.counter_label.pack(pady=15)

        # Таймеры
        self.toggle = False
        self.start_timers()

        # Обработка закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

       #таймер 1: повтор каждые 2 секунды
    def change_color(self):
        if not self.running:
            return
        self.toggle = not self.toggle #переключатель (True ↔ False)
        new_color = "orange" if self.toggle else "green"
        self.root.after(0, lambda: self.color_panel.config(bg=new_color))
        threading.Timer(2, self.change_color).start() #создаётся новый потоковый таймер, который через 2 секунды снова вызовет change_color.


    # таймер 2: однократное событие через 5 секунд 
    def show_message(self):
        if not self.running:
            return
        self.root.after(0, lambda: self.time_label.config(text="Событие наступило!"))

    #таймер 3: счётчик с периодом 1 секунда
    def update_counter(self):
        if not self.running:
            return
        self.counter += 1
        self.root.after(0, lambda: self.counter_label.config(text=f"Счётчик: {self.counter}"))
        threading.Timer(1, self.update_counter).start()

    def start_timers(self):
        threading.Timer(0, self.change_color).start()
        threading.Timer(5, self.show_message).start()
        threading.Timer(1, self.update_counter).start()

    def on_close(self):
        self.running = False   # таймеры останавливаются
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MultiTimerApp(root)
    root.mainloop()
