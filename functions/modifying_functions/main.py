# Task 1: Define a function to apply a discount with a default discount value of 5%
def apply_discount(price, discount=0.05):
    # Calculate and return the discounted price
    return price * (1 - discount)

# Task 2: Define a function to apply tax with a default tax rate of 7%
def apply_tax(price, tax=0.07):
    # Calculate and return the price with tax
    return price * (1 + tax)

# Task 3: Define a function to calculate the total price by applying both discount and tax
def calculate_total(price, discount=0.05, tax=0.07):
    # Apply the discount first
    discounted_price = apply_discount(price, discount)
    
    # Apply tax on the discounted price
    final_price = apply_tax(discounted_price, tax)
    
    # Return the final total price
    return final_price

# Task 4: Call `calculate_total` using only the default discount and tax values
total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

# Task 5: Call `calculate_total` with a custom discount of 10% and a custom tax of 8%
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")