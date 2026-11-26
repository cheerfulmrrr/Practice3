
import tkinter as tk
from tkinter import messagebox
from mortgage_logic import calculate_mortgage_data


# Функция расчёта ипотеки
def calculate_mortgage():
    try:
        # Получаем данные из полей
        price = float(entry_price.get())
        down_payment = float(entry_down_payment.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        # Выполняем расчёты с помощью отдельного модуля
        results = calculate_mortgage_data(
            price,
            down_payment,
            annual_rate,
            years,
            payment_type.get()
        )

        # Получаем результаты расчётов
        loan_amount = results["loan_amount"]
        monthly_payment = results["monthly_payment"]
        total_payment = results["total_payment"]
        overpayment = results["overpayment"]

        # Выводим результаты
        result_text.set(
            f"Сумма кредита: {loan_amount:,.2f} руб.\n"
            f"Ежемесячный платёж: {monthly_payment:,.2f} руб.\n"
            f"Общая сумма выплат: {total_payment:,.2f} руб.\n"
            f"Переплата: {overpayment:,.2f} руб."
        )

    except ValueError as error:
        messagebox.showerror("Ошибка", str(error))


# Функция очистки полей
def clear_fields():
    entry_price.delete(0, tk.END)
    entry_down_payment.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_years.delete(0, tk.END)

    payment_type.set("rubles")
    result_text.set("")


# Создание главного окна
window = tk.Tk()
window.title("Калькулятор ипотеки")
window.geometry("500x550")
window.resizable(False, False)

# Заголовок
title = tk.Label(
    window,
    text="Калькулятор ипотеки",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Стоимость недвижимости
tk.Label(
    window,
    text="Стоимость недвижимости (руб.):",
    font=("Arial", 11)
).pack()

entry_price = tk.Entry(window, width=35, font=("Arial", 11))
entry_price.pack(pady=7)

# Первоначальный взнос
tk.Label(
    window,
    text="Первоначальный взнос:",
    font=("Arial", 11)
).pack()

entry_down_payment = tk.Entry(window, width=35, font=("Arial", 11))
entry_down_payment.pack(pady=7)

# Выбор способа ввода первоначального взноса
payment_type = tk.StringVar(value="rubles")

payment_frame = tk.Frame(window)
payment_frame.pack(pady=5)

tk.Radiobutton(
    payment_frame,
    text="В рублях",
    variable=payment_type,
    value="rubles",
    font=("Arial", 10)
).pack(side=tk.LEFT, padx=10)

tk.Radiobutton(
    payment_frame,
    text="В процентах",
    variable=payment_type,
    value="percent",
    font=("Arial", 10)
).pack(side=tk.LEFT, padx=10)

# Процентная ставка
tk.Label(
    window,
    text="Годовая процентная ставка (%):",
    font=("Arial", 11)
).pack()

entry_rate = tk.Entry(window, width=35, font=("Arial", 11))
entry_rate.pack(pady=7)

# Срок ипотеки
tk.Label(
    window,
    text="Срок ипотеки (лет):",
    font=("Arial", 11)
).pack()

entry_years = tk.Entry(window, width=35, font=("Arial", 11))
entry_years.pack(pady=7)

# Кнопки управления
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

calculate_button = tk.Button(
    button_frame,
    text="Рассчитать",
    command=calculate_mortgage,
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15
)
calculate_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Очистить",
    command=clear_fields,
    font=("Arial", 11, "bold"),
    bg="#E57373",
    fg="white",
    width=12
)
clear_button.pack(side=tk.LEFT, padx=5)

# Вывод результатов
result_text = tk.StringVar()

result_label = tk.Label(
    window,
    textvariable=result_text,
    font=("Arial", 10),
    justify="left",
    wraplength=450
)
result_label.pack(pady=10)

# Запуск программы
window.mainloop()
