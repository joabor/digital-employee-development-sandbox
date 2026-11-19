import unittest

from invoice import invoice_total


class InvoiceTests(unittest.TestCase):
    def test_normal_invoice(self):
        self.assertEqual(invoice_total([("12.50", 2), ("3.00", 1)]), "28.00")

    def test_fractional_cent(self):
        self.assertEqual(invoice_total([("2.675", 1)]), "2.68")


if __name__ == "__main__":
    unittest.main()
