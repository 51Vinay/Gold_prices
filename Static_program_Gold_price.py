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
 
 
def calculate_carat_purity_price(price_per_gram, carat):
    """
    Calculate the gold price per gram based on carat purity.
    24K = 100% purity, 22K = 91.67%, 18K = 75%, etc.
    """
    purity_percentage = (carat / 24) * 100
    return price_per_gram * (purity_percentage / 100), purity_percentage
 
 
def display_results(price_per_gram, carat_prices):
    """
    Display results in an attractive format.
    """
    print("=" * 50)
    print("💰 GOLD PRICE CALCULATION 💰".center(50))
    print("=" * 50)
    print(f"Price per gram of 24K gold (with GST): ₹{price_per_gram:.2f}")
    print("=" * 50)
    print("⚖️ CARAT-WISE CALCULATION ⚖️".center(50))
    for carat, (price, purity) in carat_prices.items():
        print(f"{carat}K Gold - Purity: {purity:.2f}% - Price: ₹{price:.2f}")
    print("=" * 50)
 
 
# Main Program
if __name__ == "__main__":
    # Constants
    price_per_ounce_usd = 2649.87  # Gold price per ounce in USD
    usd_to_inr = 84.56  # Conversion rate of 1 USD to INR
    import_duty_percentage = 6  # Import duty percentage
    gst_percentage = 3  # GST percentage
 
    # Calculate the price per gram of 24K gold
    price_per_gram_24k = calculate_gold_price(price_per_ounce_usd, usd_to_inr, import_duty_percentage, gst_percentage)
 
    # Calculate carat-wise prices
    carats = [24, 22, 20, 18, 14, 10]  # Common gold carats
    carat_prices = {carat: calculate_carat_purity_price(price_per_gram_24k, carat) for carat in carats}
 
    # Display results
    display_results(price_per_gram_24k, carat_prices)