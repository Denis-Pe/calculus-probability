import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, date
import scipy.stats as stats
import zoneinfo

def log_return(p0, p1):
    return np.log(p1) - np.log(p0)

def simple_return(p0, p1):
    return (p1 - p0) / p0

all_candles = []
with open("./historical_data/Gemini_BTCUSD_d.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, )
    for row in csv_reader:
        all_candles.append(row)

## Scatterplot

candles = all_candles[:365*3]
xs = [datetime.fromtimestamp(int(c['unix'])/1000, zoneinfo.ZoneInfo('America/New_York')) for c in candles]
xs = xs[1:]
xs[-1]
# ys = [float(c['close']) for c in candles]
ys = []
for i in range(1, len(candles)):
    prev = candles[i-1]['close']
    curr = candles[i]['close']
    ys.append(simple_return(float(prev), float(curr)) * 100.0)

plt.scatter(xs, ys)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.show()

## Q-Q plot

candles = all_candles[:365*3]
datapoints = []
for i in range(1, len(candles)):
    prev = candles[i-1]['close']
    curr = candles[i]['close']
    datapoints.append(simple_return(float(prev), float(curr)) * 100.0)

np.mean(datapoints)
np.median(datapoints)

stats.probplot(datapoints, dist=stats.norm, plot=plt)
plt.grid()
plt.title("Simple Return Distribution")
plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
