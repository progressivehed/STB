import ccxt

# Replace these with your KuCoin API credentials
api_key = 'your_kucoin_api_key'
api_secret = 'your_kucoin_api_secret'
api_passphrase = 'your_kucoin_api_passphrase'

exchange = ccxt.kucoin({
    'apiKey': api_key,
    'secret': api_secret,
    'password': api_passphrase,
    'enableRateLimit': True,  # Enable rate limiting to avoid being banned by the exchange
})

def place_order(symbol, side, type, price, size):
    try:
        order_params = {
            'symbol': symbol,
            'side': side,
            'type': type,
            'price': price,
            'size': size,
        }

        response = exchange.create_order(**order_params)
        print("Order placed successfully:", response)
    except ccxt.BaseError as e:
        print("Error placing order:", e)

if __name__ == '__main__':
    # Example usage
    place_order(symbol='BTC/USDT', side='buy', type='limit', price=50000, size=0.001)
