import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/mpeng/api/stock-and-options-trading-data-provider'

mcp = FastMCP('stock-and-options-trading-data-provider')

@mcp.tool()
def options(ticker: Annotated[str, Field(description='A ticker for U.S. Trading Stocks and ETF')]) -> dict: 
    '''Stock and Options Data'''
    url = 'https://stock-and-options-trading-data-provider.p.rapidapi.com/options/aapl'
    headers = {'X-RapidAPI-Proxy-Secret': 'a755b180-f5a9-11e9-9f69-7bf51e845926', 'x-rapidapi-host': 'stock-and-options-trading-data-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def straddle(ticker: Annotated[str, Field(description='Ticker for Intel Stock')]) -> dict: 
    '''Straddle Format'''
    url = 'https://stock-and-options-trading-data-provider.p.rapidapi.com/straddle/intc'
    headers = {'x-rapidapi-host': 'stock-and-options-trading-data-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
