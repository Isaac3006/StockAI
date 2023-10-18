from BrokerageAPI import tradier
import yfinance as yf

x = yf.download("AAPL", start="2023-02-12", end="2023-02-15", interval = "15m")



# tradier.brokerage("SPY", "r")