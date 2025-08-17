def  calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount.
    Applies discount only if discount_percent >= 20.
    """
    if discount_percent >= 20:
       final_price=price * (1 - discount_percent / 100)
       return final_price
    else:
      final_price = price
      return final_price

price=int(input("Enter the price of the item: "))
discount_percent=int(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print(f"The final price after discount is: {final_price}")