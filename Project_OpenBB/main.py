"""Minimal OpenBB demo: fetch recent historical prices for a ticker.

Usage:
    pip install -r requirements.txt
    python main.py [TICKER]
"""
import sys

from openbb import obb


def main() -> None:
    symbol = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = obb.equity.price.historical(symbol, provider="yfinance")
    df = result.to_df()
    print(f"Last 5 rows for {symbol}:")
    print(df.tail())


if __name__ == "__main__":
    main()
