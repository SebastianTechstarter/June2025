import yfinance as yf

import datetime

ticker_symbols = ["AAPL", "MSFT", "TSLA", "GOOG", "META", "AMZN", "MC.PA"]

for symbol in ticker_symbols:
    print(symbol)
    with open("financechecker.txt", "a") as file:
        file.write(
            f" Für das Symbol {symbol} ist der aktuelle Kurs am: {datetime.datetime.now()}: {yf.Ticker(symbol).info["regularMarketPrice"]}\n"
        )
