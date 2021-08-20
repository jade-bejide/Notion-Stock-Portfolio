import yfinance as yf
from notion.client import NotionClient
from datetime import datetime

client = NotionClient(token_v2="<insert token_v2 here")

page = client.get_block("<Insert Relevant Page Here>")

cv = client.get_collection_view("<Insert URL of the Stock Table>")


tickers = {}

stockDictTemp = {'Ticker': None,
                 'Holdings': 0,
                 'Buy Price': 0,
                 'Profit': 0}

for value in tickers.values():
  price = yf.Ticker(value['Ticker'])
  row = cv.collection.add_row()

  #information:
  row.Date = datetime.today().strftime('%Y-%m-%d')
  row.Stock = value['Ticker']
  row.Original_Price = value['Buy Price']
  row.Current_Price = price.info["regularMarketPrice"]
  row.NumOfStock = value['Holdings']
  row.Amount = float(round(row.Current_Price * value['Holdings'], 2))
  row.Profit = float(row.Amount - value['Buy Price'])
  value['Profit'] = float(row.Amount - value['Buy Price'])
