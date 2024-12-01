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


def calculate_purity_price(price_per_gram, purity_percentage):
    """
    Calculate the silver price per gram for a given purity percentage.
    """
    return price_per_gram * (purity_percentage / 100)


def display_results(price_per_gram, purity_prices):
    """
    Display results in an attractive format.
    """
    print("=" * 50)
    print("💰 SILVER PRICE CALCULATION 💰".center(50))
    print("=" * 50)
    print(f"Price per gram of Fine Silver (99.9%): ₹{price_per_gram:.2f}")
    print("=" * 50)
    print("⚖️ PURITY-WISE PRICE ⚖️".center(50))
    print(f"{'Purity Level':<20}{'% Silver Content':<20}{'Price (₹)':>10}")
    print("-" * 50)
    for purity, price in purity_prices.items():
        print(f"{purity:<20}{price['percentage']:<20.1f}{price['price']:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    print("Silver Price Calculator")
    print("=" * 50)

    # User Inputs
    price_per_ounce_usd = float(input("Enter the silver price per ounce in USD: "))
    usd_to_inr = float(input("Enter the current USD to INR conversion rate: "))
    import_duty_percentage = float(input("Enter the import duty percentage: "))
    gst_percentage = 3  # GST is fixed at 3% for silver in India

    # Calculate the price per gram of fine silver (99.9%)
    price_per_gram_fine_silver = calculate_silver_price(price_per_ounce_usd, usd_to_inr, import_duty_percentage, gst_percentage)

    # Purity Levels (Silver Purity Chart)
    purity_levels = {
        "Fine Silver (99.9%)": 99.9,
        "Sterling Silver (92.5%)": 92.5,
        "Coin Silver (90.0%)": 90.0,
        "Britannia Silver (95.8%)": 95.8,
        "Standard Silver (80.0%)": 80.0
    }

    # Calculate prices for each purity level
    purity_prices = {
        purity: {
            "percentage": percentage,
            "price": calculate_purity_price(price_per_gram_fine_silver, percentage)
        }
        for purity, percentage in purity_levels.items()
    }

    # Display results
    display_results(price_per_gram_fine_silver, purity_prices)
 