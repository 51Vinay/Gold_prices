def calculate_gold_price(price_per_ounce_usd, usd_to_inr, import_duty_percentage, gst_percentage):
    """
    Calculate the price per gram of gold in INR including import duty and GST.
    """
    troy_ounce_to_grams = 31.1035  # 1 Troy Ounce in grams

    # Calculate the price per gram in INR
    price_per_gram_inr = (price_per_ounce_usd * usd_to_inr) / troy_ounce_to_grams

    # Add import duty and GST
    price_with_import_duty = price_per_gram_inr * (1 + import_duty_percentage / 100)
    total_price_with_gst = price_with_import_duty * (1 + gst_percentage / 100)

    return total_price_with_gst


def display_results(price_per_gram, carat_data):
    """
    Display results in an attractive format.
    """
    print("=" * 50)
    print("💰 GOLD PRICE CALCULATION 💰".center(50))
    print("=" * 50)
    print(f"Price per gram of 24K gold (with GST): ₹{price_per_gram:.2f}")
    print("=" * 50)
    print("⚖️ CARAT-WISE CALCULATION ⚖️".center(50))
    for carat in carat_data:
        carat_number = carat["carat"]
        purity = carat["purity_percentage"]
        price = price_per_gram * (purity / 100)
        print(f"{carat_number} Carat - Purity: {purity:.2f}% - Price: ₹{price:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    print("Gold Price Calculator")
    print("=" * 50)

    # User Inputs
    price_per_ounce_usd = float(input("Enter the gold price per ounce in USD: "))
    usd_to_inr = float(input("Enter the current USD to INR conversion rate: "))
    import_duty_percentage = float(input("Enter the import duty percentage: "))
    gst_percentage = float(input("Enter the GST percentage: "))

    # Carat Purity Data
    carat_data = [
        {"carat": 9, "purity_percentage": 37.5},
        {"carat": 10, "purity_percentage": 41.7},
        {"carat": 12, "purity_percentage": 50.0},
        {"carat": 14, "purity_percentage": 58.3},
        {"carat": 18, "purity_percentage": 75.0},
        {"carat": 22, "purity_percentage": 91.7},
        {"carat": 24, "purity_percentage": 99.9},
    ]

    # Calculate the price per gram of 24K gold
    price_per_gram_24k = calculate_gold_price(price_per_ounce_usd, usd_to_inr, import_duty_percentage, gst_percentage)

2649.87    # Display results
    display_results(price_per_gram_24k, carat_data)
