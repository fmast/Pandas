import datetime
import matplotlib.pyplot as plt
from pandas.io.data import DataReader

sp500 = DataReader("^GSPC", "yahoo", start=datetime.datetime(1960, 1, 1)) # returns a DataFrame
top = plt.subplot2grid((3,1), (0, 0), rowspan=2)
top.plot(sp500.index, sp500["Adj Close"])
bottom = plt.subplot2grid((3,1), (2,0))
bottom.bar(sp500.index, sp500.Volume)
plt.gcf().set_size_inches(18,8)