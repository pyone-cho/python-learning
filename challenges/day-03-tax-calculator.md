# Day 03 Challenge — Tax Calculator

## Submitted solution

File: [day-03-tax-calculator.py](day-03-tax-calculator.py)

The learner completed both the base test (105,000) and the bonus test (1,000,000), each with a 5% tax rate included in the total amount.

## Current submitted code

```python
total_amount = 105000
tax_rate = 5

# original_amount
original_amount = total_amount * 100 / (100 + tax_rate)

# tax_amount
tax_amount = total_amount * tax_rate / (100 + tax_rate)

print("===== TAX CALCULATOR =====")
print("Total Amount : ", round(total_amount, 2))
print("Original Amount:", round(original_amount, 2))
print("Tax Rate : ", tax_rate, "%")
print("Tax Amount : ", round(tax_amount, 2))
print("==========================")
```

## Code review

**Passed**
- Correctly calculates the original amount using `total_amount * 100 / (100 + tax_rate)`.
- Correctly calculates the tax amount using `total_amount * tax_rate / (100 + tax_rate)`.
- Uses `round(value, 2)` to display two decimal places.
- Prints the total, original amount, tax rate, and tax amount.
- Uses a clear `Original Amount` output label.

## Verified results

**Base test — 105,000 MMK at 5%**
- Original amount: 100,000.00 MMK
- Tax amount: 5,000.00 MMK
- Total: 105,000.00 MMK

**Bonus test — 1,000,000 MMK at 5%**
- Original amount: 952,380.95 MMK
- Tax amount: 47,619.05 MMK
- Total: 1,000,000.00 MMK

## Day 03 result

- Arithmetic operators and calculations: completed.
- Tax-inclusive formula: passed.
- Base test (105,000): passed.
- Bonus test (1,000,000): passed.
- Day 03 challenge: completed.
