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
