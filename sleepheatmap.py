from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt
import july
from july.utils import date_range
from cmap_custom import cmap_sb_custom

# import data. data format: date, sleep time (24 hours)
sleep_df = pd.read_csv('_data/sleeptime.csv')

# convert date to datetime
sleep_df['sleepdatetime'] = pd.to_datetime(sleep_df['Date'] + ' ' + sleep_df['Sleep_time'], format="%Y-%m-%d %H:%M")

# normalize sleep time: if the time of sleep > 7, it's in same day; otherwise the date should be + 1
sleep_df['sleepdate'] = sleep_df.sleepdatetime + timedelta(days = 1)
sleep_df.loc[sleep_df.sleepdatetime.dt.hour > 7, 'sleepdate'] = sleep_df.sleepdatetime

# filter from the beginning of the year to now
month_number = pd.Timestamp.now().month
# sleep_df = sleep_df[sleep_df.sleepdate > pd.Timestamp.now() - pd.offsets.MonthBegin(month_number)]

# filter for recent 6 months (option 2)
sleep_df = sleep_df[sleep_df.sleepdate > pd.Timestamp.now() - pd.offsets.MonthBegin(6)]

## CUSTOM FIELD ##
# set sleep target time, e.g. 00:30:00
sleep_df['target'] = pd.to_datetime(sleep_df['Date'] + ' ' + '00:45:00') + timedelta(days = 1)

# calculate the gap between target and actual sleep time
sleep_df['min_diff'] = (sleep_df['sleepdate'] - sleep_df['target']).astype('timedelta64[m]')
# divide the gap from minutes to hours
sleep_df['hour_diff'] = sleep_df['min_diff']/ 60

# preview data
sleep_df.head()
# build data for dates
dates = pd.to_datetime(sleep_df['Date'])

# build pandas data for sleeptime gap
sleeptime = pd.Series(sleep_df.hour_diff)
# preview data
sleeptime.head()

# generate heatmap
fig = plt.figure(facecolor='white')
# july argument: show monthly grid, use custom cmap, threshold: -2 < gap < 4
ax = july.heatmap(dates, sleeptime, year_label=False, month_grid=True, cmap=cmap_sb_custom, cmin=-2, cmax=4)
# set Y = 0.75 if the data is for 12 months (option 1); set Y to 0.9 if the data is for 6 months (option 2)
plt.suptitle('Sleep Time Heatmap', y=0.9, fontsize=20, fontweight='bold') 
plt.savefig('heatmap.png', facecolor=fig.get_facecolor(),edgecolor='none', bbox_inches='tight', pad_inches=0.4, dpi=300)