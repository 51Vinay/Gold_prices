def calculate_silver_price(price_per_ounce_usd, usd_to_inr, import_duty_percentage, gst_percentage):
    """
    Calculate the price per gram of silver in INR including import duty and GST.
    """
    troy_ounce_to_grams = 31.1035  # 1 Troy Ounce in grams

    # Calculate the price per gram in INR
    price_per_gram_inr = (price_per_ounce_usd * usd_to_inr) / troy_ounce_to_grams

    # Add import duty and GST
    price_with_import_duty = price_per_gram_inr * (1 + import_duty_percentage / 100)
    total_price_with_gst = price_with_import_duty * (1 + gst_percentage / 100)

    return total_price_with_gst


def display_results(price_per_gram):
    """
    Display results in an attractive format.
    """
    print("=" * 50)
    print("💰 SILVER PRICE CALCULATION 💰".center(50))
    print("=" * 50)
    print(f"Price per gram of silver (with GST and Duty): ₹{price_per_gram:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    print("Silver Price Calculator")
    print("=" * 50)

    # User Inputs
    price_per_ounce_usd = float(input("Enter the silver price per ounce in USD: "))
    usd_to_inr = float(input("Enter the current USD to INR conversion rate: "))
    import_duty_percentage = float(input("Enter the import duty percentage: "))
    gst_percentage = float(input("Enter the  GST percentage: "))

    # Calculate the price per gram of silver
    price_per_gram_silver = calculate_silver_price(price_per_ounce_usd, usd_to_inr, import_duty_percentage, gst_percentage)

    # Display results
    display_results(price_per_gram_silver)
