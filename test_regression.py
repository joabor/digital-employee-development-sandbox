import unittest
from invoice import invoice_total

class TestInvoiceRegression(unittest.TestCase):
    def test_empty_invoice(self):
        self.assertEqual(invoice_total([]), "0.00")

    def test_rounding_half_up_positive(self):
        # 2.675 * 1 = 2.675 -> 2.68
        self.assertEqual(invoice_total([("2.675", 1)]), "2.68")
        # 2.674 * 1 = 2.674 -> 2.67
        self.assertEqual(invoice_total([("2.674", 1)]), "2.67")
        # 2.676 * 1 = 2.676 -> 2.68
        self.assertEqual(invoice_total([("2.676", 1)]), "2.68")

    def test_multiple_items_rounding(self):
        # 2.675 * 1 = 2.675 -> 2.68
        # 1.005 * 1 = 1.005 -> 1.01
        # Total = 3.69
        self.assertEqual(invoice_total([("2.675", 1), ("1.005", 1)]), "3.69")

    def test_quantity_multiplication_before_rounding(self):
        # 2.675 * 2 = 5.35 -> 5.35
        # If we rounded 2.675 first, it would be 2.68 * 2 = 5.36
        self.assertEqual(invoice_total([("2.675", 2)]), "5.35")

    def test_large_quantity(self):
        # 1.005 * 100 = 100.5 -> 100.50
        self.assertEqual(invoice_total([("1.005", 100)]), "100.50")

if __name__ == "__main__":
    unittest.main()
