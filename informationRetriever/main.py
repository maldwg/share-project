from fastapi import FastAPI
from utils import getSymbol
import yfinance as yf
import pandas as pd
import json
from pydantic.utils import deep_update

app = FastAPI()

@app.get("/api/stocks/history/{stockname}")
async def retrieveStockInfo(stockname: str, period: str = "1mo",countryCode: str = "GER"):
    symbol_name = getSymbol(stockname, countryCode)
    ticker = yf.Ticker(symbol_name)
    return json.loads(ticker.history(period=period).to_json())


@app.get("/api/stocks/info/{stockname}")
async def retrieveStockInfo(stockname: str, period: str = "1mo",countryCode: str = "GER"):
    symbol_name = getSymbol(stockname, countryCode)
    ticker = yf.Ticker(symbol_name)
    ticker.history(period=period)
    income = json.loads(ticker.income_stmt.to_json())
    balance = json.loads(ticker.balance_sheet.to_json())
    result = deep_update(income, balance)
    return result

