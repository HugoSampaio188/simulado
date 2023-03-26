import numpy as np
from scipy.stats import norm

stock_price = 50
risk_free_rate = 0.1
vol = 0.2
time_to_expiry = 0.5
strike_price = 60
type = 'put'

N = norm.cdf

d1 = (np.log(stock_price/strike_price) + (risk_free_rate + np.power(vol,2)/2) * time_to_expiry) / (vol * np.sqrt(time_to_expiry))
d2 = d1 - vol * np.sqrt(time_to_expiry)

if type == 'call':
    opt_price = stock_price * N(d1) - strike_price * np.exp(-risk_free_rate*time_to_expiry)*N(d2)
elif type == 'put':
    opt_price = strike_price * np.exp(-risk_free_rate*time_to_expiry) * N(-d2) - stock_price * N(-d1)
else:
    print('WRONG TYPE')
    exit()

print('PRECO ATRAVES DE BSM')
print(opt_price)
