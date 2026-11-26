
import unittest

from mortgage_logic import calculate_mortgage_data


class TestMortgageCalculator(unittest.TestCase):

    # Тест 1. Проверка расчёта ипотеки в рублях
    def test_calculation_in_rubles(self):
        result = calculate_mortgage_data(
            5000000, 1000000, 10, 20, "rubles"
        )

        self.assertEqual(result["loan_amount"], 4000000)
        self.assertAlmostEqual(result["monthly_payment"], 38600.87, places=2)

    # Тест 2. Проверка расчёта ипотеки в процентах
    def test_calculation_in_percent(self):
        result = calculate_mortgage_data(
            5000000, 20, 10, 20, "percent"
        )

        self.assertEqual(result["loan_amount"], 4000000)
        self.assertAlmostEqual(result["monthly_payment"], 38600.87, places=2)

    # Тест 3. Проверка нулевой процентной ставки
    def test_zero_interest_rate(self):
        result = calculate_mortgage_data(
            1200000, 200000, 0, 10, "rubles"
        )

        self.assertEqual(result["loan_amount"], 1000000)
        self.assertAlmostEqual(result["monthly_payment"], 1000000 / 120)

    # Тест 4. Проверка отрицательной стоимости недвижимости
    def test_negative_property_price(self):
        with self.assertRaises(ValueError):
            calculate_mortgage_data(
                -5000000, 1000000, 10, 20, "rubles"
            )

    # Тест 5. Проверка отрицательного первоначального взноса
    def test_negative_down_payment(self):
        with self.assertRaises(ValueError):
            calculate_mortgage_data(
                5000000, -100000, 10, 20, "rubles"
            )

    # Тест 6. Проверка первоначального взноса,
    # превышающего стоимость недвижимости
    def test_down_payment_exceeds_price(self):
        with self.assertRaises(ValueError):
            calculate_mortgage_data(
                5000000, 6000000, 10, 20, "rubles"
            )

    # Тест 7. Проверка первоначального взноса в 100%
    def test_down_payment_100_percent(self):
        with self.assertRaises(ValueError):
            calculate_mortgage_data(
                5000000, 100, 10, 20, "percent"
            )

    # Тест 8. Проверка отрицательной процентной ставки
    def test_negative_interest_rate(self):
        with self.assertRaises(ValueError):
            calculate_mortgage_data(
                5000000, 1000000, -5, 20, "rubles"
            )

    # Тест 9. Проверка некорректного срока ипотеки
    def test_invalid_loan_period(self):
        with self.assertRaises(ValueError):
            calculate_mortgage_data(
                5000000, 1000000, 10, 0, "rubles"
            )

    # Тест 10. Проверка общей суммы выплат
    def test_total_payment(self):
        result = calculate_mortgage_data(
            5000000, 1000000, 10, 20, "rubles"
        )

        expected_total = result["monthly_payment"] * 240

        self.assertAlmostEqual(
            result["total_payment"],
            expected_total,
            places=2
        )

    # Тест 11. Проверка переплаты по кредиту
    def test_overpayment(self):
        result = calculate_mortgage_data(
            5000000, 1000000, 10, 20, "rubles"
        )

        expected_overpayment = (
            result["total_payment"] - result["loan_amount"]
        )

        self.assertAlmostEqual(
            result["overpayment"],
            expected_overpayment,
            places=2
        )


if __name__ == "__main__":
    unittest.main()
