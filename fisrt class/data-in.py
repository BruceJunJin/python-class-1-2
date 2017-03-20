import pandas_datareader as pdr
import numpy as np
data=pdr.get_data_yahoo('AAPL')
data.tail()
