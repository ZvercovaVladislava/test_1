import tkinter as tk
import threading

class MultiTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Мульти-таймеры (threading.Timer)")
        self.root.geometry("400x250")

        # Флаг работы
        self.running = True

        # Панель для смены цвета
        self.color_panel = tk.Frame(root, bg="lightgray", height=80)
        self.color_panel.pack(fill="x")

        # Метка для события
        self.time_label = tk.Label(root, text="Ждём события...", font=("Arial", 14))
        self.time_label.pack(pady=10)

        # Счётчик
        self.counter = 0
        self.counter_label = tk.Label(root, text="Счётчик: 0", font=("Arial", 14))
        self.counter_label.pack(pady=10)

        # Таймеры
        self.toggle = False
        self.start_timers()

        # Обработка закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # === Таймер 1: повтор каждые 2 секунды (смена цвета) ===
    def change_color(self):
        if not self.running:
            return
        self.toggle = not self.toggle
        new_color = "cyan" if self.toggle else "lightgray"
        self.root.after(0, lambda: self.color_panel.config(bg=new_color))
        threading.Timer(2, self.change_color).start()

    # === Таймер 2: однократное событие через 5 секунд ===
    def show_message(self):
        if not self.running:
            return
        self.root.after(0, lambda: self.time_label.config(text="Событие наступило!"))

    # === Таймер 3: счётчик с периодом 1 секунда ===
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
        self.running = False   # останавливаем все таймеры
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MultiTimerApp(root)
    root.mainloop()

    #bgch
