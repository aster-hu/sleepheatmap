from datetime import timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import july
from july.utils import date_range
from cmap_custom import cmap_sb_custom

# dates = date_range("2020-01-01", "2020-12-31")
# data = np.random.randint(0, 14, len(dates))

sleep_df = pd.read_csv('_data/sleeptime.csv')

# convert date to datetime
sleep_df['sleepdatetime'] = pd.to_datetime(sleep_df['Date'] + ' ' + sleep_df['Sleep_time'], format="%Y-%m-%d %H:%M")

# add conditional column
sleep_df['sleepdate'] = sleep_df.sleepdatetime + timedelta(days = 1)
sleep_df.loc[sleep_df.sleepdatetime.dt.hour>7, 'sleepdate'] = sleep_df.sleepdatetime

# set sleep target time, e.g. 00:30:00
sleep_df['target'] = pd.to_datetime(sleep_df['Date'] + ' ' + '00:30:00') + timedelta(days = 1)

sleep_df['min_diff'] = (sleep_df['sleepdate'] - sleep_df['target']).astype('timedelta64[m]')

# divide difference in minutes to hours
sleep_df['hour_diff'] = sleep_df['min_diff']/ 60

# preview data
sleep_df.head()

# dates = date_range("2021-01-01", "2020-12-31")
dates = pd.to_datetime(sleep_df['Date'])

# data argument for plot is pandas series and must be indexed by a DatetimeIndex
sleeptime = pd.Series(sleep_df.hour_diff)
sleeptime.head()

plt.figure(facecolor='white')
ax = july.heatmap(dates, sleeptime, year_label=False, month_grid=True, cmap=cmap_sb_custom, cmin=-2, cmax=4)
plt.suptitle('Sleeptime Heatmap', y=0.95, fontsize=20)
plt.savefig('heatmap.jpg', bbox_inches='tight', pad_inches=0.4, dpi=300)