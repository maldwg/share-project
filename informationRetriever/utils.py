import requests
def getSymbol(company_name, stock_market_countrycode):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "does not matter"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()
    
    german_data = [ quote for quote in data["quotes"] if quote["exchange"] == stock_market_countrycode ][0]["symbol"]

    # company_code = data['quotes'][0]['symbol']
    return german_data