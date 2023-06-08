import yfinance as yf

eur_usd = yf.Ticker("EURUSD=X")
hist = eur_usd.history(period="max")
print(hist.head())
print(hist.tail())