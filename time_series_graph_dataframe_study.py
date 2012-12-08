import pandas.io.data as web
from pandas import DataFrame

# Create pandas Time series data structure
all_data = {}
ticker = "^GSPC"
all_data= web.get_data_yahoo(ticker, '11/1/2012', '12/7/2012')

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

frame = DataFrame({'Open': Open, 'R1': R1, 'R2': R2, 'R3': R3, 'Pivot': Pivot, 'S1': S1, 'S2': S2, 'S3': S3})
print(frame)
