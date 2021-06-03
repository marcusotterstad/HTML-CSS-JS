import yfinance as yf
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
today = date.today()
buyDate = '2020-7-21'
endDate = today.strftime("%Y-%m-%d")

def createDf(tickerSymbol, amount):
    
    var = yf.Ticker(tickerSymbol)
    tickerDf = var.history(period='1d', start=buyDate, end=endDate)
    
    tickerDf.columns = ['x','y','z', tickerSymbol,'v', 'e', 't']
    
    return tickerDf[tickerSymbol]*amount
    

gold = createDf('GLD', 3)
coms = createDf('DBC', 44)
activision = createDf('ATVI', 1)
shortbond = createDf('IEF', 9)
netflix = createDf('NFLX', 0.15)
nasdaq = createDf('QQQ', 4)
longbond = createDf('TLT', 18)
stock = createDf('VTI', 7)
portfolio = pd.concat([gold,coms,activision,shortbond,netflix,nasdaq,longbond,stock], axis=1)
portfolio['SUM'] = portfolio.sum(axis=1)
portofaje = portfolio["SUM"]
portofaje.to_csv("portfolio_returns.csv")
ax1 = sns.lineplot(x=portfolio.index, y="SUM", data=portfolio)

plt.title("Ray Dalio all weather Nasdaq")
plt.xlabel("Days since bought")
plt.ylabel("Total value of portfolio")
plt.style.use('grayscale')
plt.savefig('static/new_plot.png')
plt.close()