import requests
import time

def get_btc_price():
    url = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
    response = requests.get(url)
    if response.status_code == 200: # 200 là giá trị trả về nếu trang web đồng ý truy cập
        data = response.json()
        btc_price = float(data["price"])
        return btc_price
    else:
        print("Error fetching data")
        return None

def main():
    while True:
        btc_price_usd = get_btc_price()
        if btc_price_usd is not None:
            print(f"Bitcoin price: {btc_price_usd} USD")
        else:
            print("Unable to fetch BTC price.")

        time.sleep(10)  # Chờ 10 giây trước khi cập nhật giá

if __name__ == "__main__":
    main()
