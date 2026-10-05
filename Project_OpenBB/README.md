# Project OpenBB

Small example of using [OpenBB](https://github.com/OpenBB-finance/OpenBB) as a Python dependency.

```bash
cd Project_OpenBB
pip install -r requirements.txt
python main.py MSFT
```

OpenBB is installed from source (GitHub) with the `routers` extra. The default data provider is `cboe`; pass another as the second argument (e.g. `python main.py AAPL nasdaq`). The `yfinance` provider is not part of the OpenBB repo anymore.
