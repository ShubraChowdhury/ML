# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:52:13 2016

@author: DevAdmin
"""

import os
import pandas as pd
import matplotlib as plt
infile = 'F:/Training/MachineLearningGeorgiaTech/data/'

def symbol_to_path(symbol, base_dir=infile):
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))
    
def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)    
    symbols.insert(0,'SPY')
    
    for ticker in symbols:
        df_ticker = pd.read_csv(symbol_to_path(ticker,infile),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        df_ticker=df_ticker.rename(columns={'Adj Close':ticker})
        df = df.join(df_ticker,how ='inner')
    return df    
def plot_data(df,title="Stock Price"):
    
    ax=df.plot(title=title,fontsize =2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    #plt.show()
    
def test_run():
  dates = pd.date_range('2010-01-01','2010-12-31')    
  
  symbols =['GOOG','IBM','GLD']
  
  df = get_data(symbols, dates)
  
  #print(df)#.ix['2010-01-01':'2010-01-31'])  
  print(df.ix['2010-03-15':'2010-03-10',['GOOG','GLD']]) 
  plot_data(df,"Stk Plot")
 
    
if __name__ ==  "__main__": 
  test_run()
    