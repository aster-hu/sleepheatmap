import calmap
import calplot
import pandas as pd
import calmap
from vega_datasets import data as vds
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# # BASIC EXAMPLE
# # data argument for plot is pandas series and must be indexed by a DatetimeIndex
# # define date range: start and end date
# heatmap_series = pd.Series(data=np.random.rand(104), 
#                            index=pd.date_range(start='6-6-21', end='09-17-21'))
# heatmap_series.head()

# # calendar heatmap
# calmap.yearplot(data=heatmap_series);

# # calendar heatmap
# calmap.yearplot(data=heatmap_series);

# CALENDAR HEATMAP FOR ONE YEAR
# data
sleep_df = pd.read_csv('data/sleeptime.csv')

# convert date to datetime if needed
sleep_df['sleepdatetime'] = pd.to_datetime(sleep_df['Date'] + ' ' + sleep_df['Sleep_time'], format="%Y-%m-%d %I:%M")
sleep_df['sleepdate'] = pd.to_datetime(sleep_df['Date'], format="%Y-%m-%d")
sleep_df['target'] = pd.to_datetime(sleep_df['Date'] + ' ' + '00:00:00')

sleep_df['min_diff'] = (sleep_df['sleepdatetime'] - sleep_df['target']).astype('timedelta64[m]')
# Divide difference in minutes to hours
sleep_df['hour_diff'] = sleep_df['min_diff']/ 60

# set index to date
sleep_df = sleep_df.set_index('sleepdate')

# preview data
sleep_df.head(2)

# test if DatetimeIndex
isinstance(sleep_df.index, pd.DatetimeIndex)

# data argument for plot is pandas series and must be indexed by a DatetimeIndex
sleeptime = pd.Series(sleep_df.hour_diff)
sleeptime.head()

# calendar heatmap
plt.figure(figsize=(16,8))
calmap.yearplot(data=sleeptime, year=2021);
plt.suptitle('Calendar Heatmap', y=.65, fontsize=20);

###########
# # CALENDAR HEATMAP FOR SEVERAL YEARS
# # data argument for plot is pandas series and must be indexed by a DatetimeIndex
# avg_temp = pd.Series(jacksonville_df.Avg_Temp_Fahrenheit)
# avg_temp.head()

# # calendar heatmap
# calmap.calendarplot(data=avg_temp, fig_kws=dict(figsize=(16,8)));


# # example using calplot

# # calendar heatmap
# # notice the colorbar is added automatically
# calplot.calplot(data=avg_temp, cmap='Reds', figsize=(16,8));
# plt.suptitle('Calendar Heatmap', y=1.0, fontsize=20);


# # EXTRA EXAMPLE WITH CALPLOT
# # example uses resample to put data in proper form

# # temperatures in San Francisco
# # data argument for plot is pandas series and must be indexed by a DatetimeIndex
# sf_temps = vds.sf_temps()
# sf_temps = sf_temps.set_index('date')
# # temp resample data by day
# temps = pd.Series(sf_temps.resample('D').max().temp)
# temps.head()

# # calendar heatmap
# calplot.calplot(data=temps, cmap='coolwarm', suptitle='Calendar Heatmap');