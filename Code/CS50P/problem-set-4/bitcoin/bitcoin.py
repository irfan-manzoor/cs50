import sys
import requests

def get_bitcoin_price():
    try:
        # Fetch Bitcoin price from CoinDesk API
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise exception for 4xx or 5xx status codes
        data = response.json()
        bitcoin_price = data['bpi']['USD']['rate_float']
        return bitcoin_price
    except (requests.RequestException, KeyError):
        print("Error: Failed to fetch Bitcoin price from the API.")
        sys.exit(1)

def main():
    # Check if command-line argument is provided
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    # Try to convert the argument to a float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins * bitcoin_price

    # Output the cost with 4 decimal places and thousands separator
    print(f"Total cost of {bitcoins:,.4f} Bitcoins: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
