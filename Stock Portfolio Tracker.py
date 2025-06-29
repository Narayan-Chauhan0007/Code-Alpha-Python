# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 300
}

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks and their prices (per share):")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

portfolio = {}
while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("⚠️ Stock symbol not found in the list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of shares for {stock}: "))
        if quantity <= 0:
            print("⚠️ Quantity should be positive.")
            continue
    except ValueError:
        print("⚠️ Please enter a valid integer quantity.")
        continue

    # Add or update the portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
total_value = 0
print("\nYour portfolio summary:")
for stock, qty in portfolio.items():
    stock_value = stock_prices[stock] * qty
    total_value += stock_value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_value}")

print(f"\n💰 Total investment value: ${total_value}")

# Optional: save to file
save_option = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save_option == 'yes':
    filename = "portfolio_summary.txt"
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=======================\n")
        for stock, qty in portfolio.items():
            stock_value = stock_prices[stock] * qty
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_value}\n")
        f.write(f"\nTotal investment value: ${total_value}\n")
    print(f"✅ Summary saved to {filename}")

print("\nThanks for using Stock Portfolio Tracker!")
