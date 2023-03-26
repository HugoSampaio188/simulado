from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import datetime
import pandas as pd
import numpy as np
import statsmodels.api as sm

data_inicio = '2019-01-01'
data_fim = '2023-01-01'
ticker_list = ['PETR4.SA', 'VALE3.SA']
index = '^BVSP'

today = date.today()
for ticker in ticker_list:
    start_date= datetime.datetime.strptime(data_inicio, '%Y-%m-%d')
    end_date= datetime.datetime.strptime(data_fim, '%Y-%m-%d')
    data_ticker = pdr.get_data_yahoo(ticker, start=start_date, end=today).rename(columns={'Adj Close':'AssetPrice'})
    data_index = pdr.get_data_yahoo(index, start=start_date, end=today).rename(columns={'Adj Close':'IndexPrice'})
    data_ticker = data_ticker['AssetPrice']
    data_index = data_index['IndexPrice']
    data_beta = pd.concat([data_ticker, data_index], axis=1)
    data_beta['AssetReturn'] = data_beta['AssetPrice'] / data_beta['AssetPrice'].shift(1) - 1
    data_beta['IndexReturn'] = data_beta['IndexPrice'] / data_beta['IndexPrice'].shift(1) - 1
    data_beta = data_beta[['AssetReturn', 'IndexReturn']]
    data_beta = data_beta.dropna()
    a = data_beta.cov()['AssetReturn'][1]
    b = data_beta.var()['IndexReturn']
    beta = a/b
    print('BETA BETWEEN '+ ticker + ' AND '+ index)
    print(beta)

'''
# confirmando

# Variáveis independentes
X = data_beta.drop(['AssetReturn'],axis=1)
#Variável dependentes
y = data_beta['AssetReturn']
modelo = (sm.OLS(y,sm.add_constant(X)).fit())
modelo.summary(title='Sumário do modelo com intercepto')

print(modelo.params)
'''




