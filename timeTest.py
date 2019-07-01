# sample data
import numpy as np
import pandas as pd

N = 30
drange = pd.date_range("2014-01", periods=N, freq="MS")
values = {'values':np.random.randint(1,20,size=N)}
df = pd.DataFrame(values, index=drange)

# use formatters to specify major and minor ticks
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


fig, ax = plt.subplots()
ax.plot(df.index, df.values)
#ax.set_xticks(df.index)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%H-%M"))
_=plt.xticks(rotation=90) 