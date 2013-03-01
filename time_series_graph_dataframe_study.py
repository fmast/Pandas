import pandas.io.data as web
from pandas import DataFrame

# Create pandas Time series data structure
all_data = {}
ticker = "^GSPC"
all_data= web.get_data_yahoo(ticker, '01/1/2013', '02/28/2013')

# Global Variables
Volume = all_data["Volume"]
High = all_data["High"]
Low = all_data["Low"]
Close = all_data["Adj Close"]
Open = all_data["Open"]
Pivot = (Open + High + Low + Close)/4

# Defining Resistance Levels 1 - 3
R1 = Pivot + (Pivot - Low)
R2 = Pivot + (High - Low)
R3 = High + (2 * (Pivot - Low))

# Defining Support Levels 1 - 3
S1 = Pivot - (High - Pivot)
S2 = Pivot - (High - Low)
S3 = Low - (2 * (High - Pivot))


dataFrameAll = DataFrame({'Open': Open, 'R1': R1, 'R2': R2, 'R3': R3, 'Pivot': Pivot, 'S1': S1, 'S2': S2, 'S3': S3})
dataFrameAll.plot(figsize = (20,9), title = ("Pivot Points"))

dataFrameS3 = DataFrame({'R3': R3, 'Pivot': Pivot, 'S3': S3})
dataFrameS3.plot(figsize = (20,9), title = ("R3 <Pivot> S3"))

dataFrameOpen = DataFrame({'R3': R3, 'Open': Open, 'Pivot': Pivot, 'S3': S3})
dataFrameOpen.plot(figsize = (20,9), title = ("R3 <=> Open <Pivot> S3"))
