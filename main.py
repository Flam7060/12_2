import tkinter as tk
from tkinter import messagebox
import math

def validate_triangle(a, b, c):
    # Проверка на положительность сторон
    if a <= 0 or b <= 0 or c <= 0:
        messagebox.showerror("Ошибка", "Стороны треугольника должны быть положительными числами.")
        return False
    # Проверка на существование треугольника (неравенство треугольника)
    if a + b <= c or a + c <= b or b + c <= a:
        messagebox.showerror("Ошибка", "Такие стороны не могут составить треугольник.")
        return False
    return True

def check_triangle_type(a, b, c):
    if not validate_triangle(a, b, c):
        return None
    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

def check_angles_and_area(a, b, c):
    if not validate_triangle(a, b, c):
        return None, None

    # Определение углов по теореме косинусов
    try:
        angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

        # Определение типа углов
        if angle_A > math.pi / 2 or angle_B > math.pi / 2 or angle_C > math.pi / 2:
            angle_type = "Тупоугольный"
        elif angle_A < math.pi / 2 and angle_B < math.pi / 2 and angle_C < math.pi / 2:
            angle_type = "Остроугольный"
        else:
            angle_type = "Прямоугольный"

        # Вычисление площади по формуле Герона
        s = (a + b + c) / 2  # Полупериметр
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Формула Герона

        return angle_type, area
    except ValueError:
        messagebox.showerror("Ошибка", "Ошибка при вычислении углов или площади.")
        return None, None

def create_interface():
    def on_check_triangle_type():
        try:
            # Получаем значения сторон
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            triangle_type = check_triangle_type(a, b, c)
            if triangle_type:
                messagebox.showinfo("Результат", f"Тип треугольника: {triangle_type}")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите правильные числа.")
    
    def on_check_angles_and_area():
        try:
            # Получаем значения сторон
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            angle_type, area = check_angles_and_area(a, b, c)
            if angle_type and area is not None:
                messagebox.showinfo("Результат", f"Тип углов треугольника: {angle_type}\nПлощадь: {area:.2f}")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите правильные числа.")
    
    root = tk.Tk()
    root.title("Определение типа треугольника")

    label_a = tk.Label(root, text="Сторона A:")
    label_a.grid(row=0, column=0)

    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1)

    label_b = tk.Label(root, text="Сторона B:")
    label_b.grid(row=1, column=0)

    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1)

    label_c = tk.Label(root, text="Сторона C:")
    label_c.grid(row=2, column=0)

    entry_c = tk.Entry(root)
    entry_c.grid(row=2, column=1)

    check_button = tk.Button(root, text="Проверить тип треугольника", command=on_check_triangle_type)
    check_button.grid(row=3, column=0, columnspan=2)

    check_angles_area_button = tk.Button(root, text="Проверить углы и площадь", command=on_check_angles_and_area)
    check_angles_area_button.grid(row=4, column=0, columnspan=2)

    root.mainloop()

create_interface()
