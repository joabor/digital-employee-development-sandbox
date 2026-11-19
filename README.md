# Invoice rounding bug

Our small invoice library sometimes produces incorrect totals for fractional-cent
unit prices. Repair `invoice_total` in `invoice.py` and add regression coverage.

Contract: prices are nonnegative finite decimal strings, quantities are positive
integers. Multiply each unit price by its quantity, round each extended line to
cents using ROUND_HALF_UP, then sum those rounded amounts. Return a string with
exactly two decimal places. Empty invoices return `0.00`. Input validation and
other currencies are outside this task. Preserve existing tests and other files.

Run the supplied tests with `python -m unittest discover -v`.
