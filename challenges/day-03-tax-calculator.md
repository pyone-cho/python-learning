# Day 03 Challenge — Tax Calculator

## Submitted solution

File: [day-03-tax-calculator.py](day-03-tax-calculator.py)

The learner completed the bonus test using a tax-inclusive total of 1,000,000 and a tax rate of 5%.

## Code review

**Passed**
- Correctly calculates the original amount using `total_amount * 100 / (100 + tax_rate)`.
- Correctly calculates the tax amount using `total_amount * tax_rate / (100 + tax_rate)`.
- Uses `round(value, 2)` to display two decimal places.
- Prints the total, original amount, tax rate, and tax amount.

## Verified result

For total amount 1,000,000 MMK and tax rate 5%:

- Original amount: 952,380.95 MMK
- Tax amount: 47,619.05 MMK
- Total: 1,000,000.00 MMK

## Suggested improvements

- Use consistent label capitalization, such as `Original Amount:`.
- The original challenge's base test amount was 105,000. The submitted solution demonstrates the bonus amount of 1,000,000; the base test is still useful for additional practice.

## Review status

- Formula and arithmetic: passed.
- Bonus test (1,000,000): passed.
- Base test (105,000): not yet submitted.
- Day 03: in progress.
