# Source: https://github.com/groundhogday321/python-calendar-heatmaps/blob/master/Python%20Calendar%20Heatmaps.ipynb

import calmap
import calplot
import pandas as pd
import calmap
from vega_datasets import data as vds
import matplotlib.pyplot as plt
import numpy as np

# BASIC EXAMPLE
# data argument for plot is pandas series and must be indexed by a DatetimeIndex
heatmap_series = pd.Series(data=np.random.rand(366), 
                           index=pd.date_range(start='1-1-16', end='12-31-16'))
heatmap_series.head()

# calendar heatmap
calmap.yearplot(data=heatmap_series);

# calendar heatmap
calmap.yearplot(data=heatmap_series);


# CALENDAR HEATMAP FOR ONE YEAR
# data
# data = 'https://raw.githubusercontent.com/groundhogday321/dataframe-datasets/master/jacksonville_florida_weather.csv'
# jacksonville_df = pd.read_csv(data)
jacksonville_df = pd.read_csv('sample_weather.csv')

# convert date to datetime if needed
jacksonville_df['Date'] = pd.to_datetime(jacksonville_df['Date'])

# set index to date
jacksonville_df = jacksonville_df.set_index('Date')

# preview data
jacksonville_df.head(2)

# test if DatetimeIndex
isinstance(jacksonville_df.index, pd.DatetimeIndex)
# jacksonville_df.index

# data argument for plot is pandas series and must be indexed by a DatetimeIndex
precipitation = pd.Series(jacksonville_df.Precipitation_Inches)
precipitation.head()

# calendar heatmap
plt.figure(figsize=(16,8))
calmap.yearplot(data=precipitation, year=2017);
plt.suptitle('Calendar Heatmap', y=.65, fontsize=20);

###########
# CALENDAR HEATMAP FOR SEVERAL YEARS
# data argument for plot is pandas series and must be indexed by a DatetimeIndex
avg_temp = pd.Series(jacksonville_df.Avg_Temp_Fahrenheit)
avg_temp.head()

# calendar heatmap
calmap.calendarplot(data=avg_temp, fig_kws=dict(figsize=(16,8)));


# example using calplot

# calendar heatmap
# notice the colorbar is added automatically
calplot.calplot(data=avg_temp, cmap='Reds', figsize=(16,8));
plt.suptitle('Calendar Heatmap', y=1.0, fontsize=20);


# EXTRA EXAMPLE WITH CALPLOT
# example uses resample to put data in proper form

# temperatures in San Francisco
# data argument for plot is pandas series and must be indexed by a DatetimeIndex
sf_temps = vds.sf_temps()
sf_temps = sf_temps.set_index('date')
# temp resample data by day
temps = pd.Series(sf_temps.resample('D').max().temp)
temps.head()

# calendar heatmap
calplot.calplot(data=temps, cmap='coolwarm', suptitle='Calendar Heatmap');