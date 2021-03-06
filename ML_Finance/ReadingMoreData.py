# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:44:38 2016

@author: DevAdmin
"""

"""Utility functions"""

import os
import pandas as pd
infile = 'F:/Training/MachineLearningGeorgiaTech/data/'

def symbol_to_path(symbol, base_dir=infile):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp=pd.read_csv(symbol_to_path(symbol,infile),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df=df.join(df_temp,how='inner')
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)
    print (df)


if __name__ == "__main__":
    test_run()