# Day 03 — Operators and Calculations

## Goals
- Use arithmetic operators.
- Understand assignment operators.
- Build a simple calculator.

## Example
```python
a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
```

## Challenge
Calculate the original price and tax amount when a tax-inclusive total is 100,000 and the tax rate is 5%.

```python
total = 100000
tax_rate = 5
base = total * 100 / (100 + tax_rate)
tax = total - base

print("Base:", base)
print("Tax:", tax)
```

Try to write the solution yourself before using the hint.

## Reflection
- What does `%` return?
- Why can division produce a decimal?
