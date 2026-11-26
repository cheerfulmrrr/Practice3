
def calculate_mortgage_data(price, down_payment, annual_rate, years, payment_type):
    # Проверка исходных данных
    if price <= 0:
        raise ValueError("Стоимость недвижимости должна быть больше нуля!")

    if down_payment < 0:
        raise ValueError("Первоначальный взнос не может быть отрицательным!")

    if annual_rate < 0:
        raise ValueError("Процентная ставка не может быть отрицательной!")

    if years <= 0:
        raise ValueError("Срок ипотеки должен быть больше нуля!")

    # Перевод первоначального взноса в рубли
    if payment_type == "percent":
        if down_payment >= 100:
            raise ValueError("Первоначальный взнос должен быть меньше 100%!")

        down_payment = price * down_payment / 100

    elif payment_type != "rubles":
        raise ValueError("Неизвестный способ ввода первоначального взноса!")

    if down_payment >= price:
        raise ValueError("Первоначальный взнос должен быть меньше стоимости недвижимости!")

    # Сумма кредита
    loan_amount = price - down_payment

    # Месячная процентная ставка
    monthly_rate = annual_rate / 100 / 12

    # Количество платежей
    months = years * 12

    # Расчёт ежемесячного платежа
    if monthly_rate == 0:
        monthly_payment = loan_amount / months
    else:
        monthly_payment = loan_amount * (
            monthly_rate * (1 + monthly_rate) ** months
        ) / ((1 + monthly_rate) ** months - 1)

    # Общая сумма выплат и переплата
    total_payment = monthly_payment * months
    overpayment = total_payment - loan_amount

    return {
        "loan_amount": loan_amount,
        "monthly_payment": monthly_payment,
        "total_payment": total_payment,
        "overpayment": overpayment
    }
