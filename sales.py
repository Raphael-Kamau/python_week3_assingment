# function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
        Calculates the final price after applying a discount.
        Applies the discount only if it is 20% or higher.
        """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

try:
    # collect price value
    price = float(input("Enter the original price of the item: "))
    # collect discount value
    discount_percent = float(input("Enter the discount offered in percentage: " ))
    # calculate the final price
    final_price = calculate_discount(price, discount_percent)

    if discount_percent <= 20:
        print(f'''
        Discount offered. Price to be paid: {final_price:.2f}
        ''')
    else:
        print(f"Sorry no discount for you. Price to be paid: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")
