# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

total_investment = 0
portfolio = []

print("===================================")
print("    STOCK PORTFOLIO TRACKER")
print("===================================")

while True:
    stock = input("\nEnter Stock Name (AAPL/TSLA/GOOGL/MSFT/AMZN) or 'done' to finish: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name! Please try again.")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    portfolio.append((stock, quantity, investment))

print("\n========== PORTFOLIO ==========")

for stock, quantity, investment in portfolio:
    print(f"{stock} - Quantity: {quantity}, Investment: ${investment}")

print("-------------------------------")
print(f"Total Investment Value: ${total_investment}")

# Save the portfolio to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=========================\n")

    for stock, quantity, investment in portfolio:
        file.write(f"{stock} - Quantity: {quantity}, Investment: ${investment}\n")

    file.write("-------------------------\n")
    file.write(f"Total Investment Value: ${total_investment}")

print("\nPortfolio saved successfully in 'portfolio.txt'")