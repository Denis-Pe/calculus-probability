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

def take_last(arr, n):
    return arr[len(arr) - n:]

all_candles = []
with open("./historical_data/Gemini_BTCUSD_d.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, )
    for row in csv_reader:
        all_candles.append(dict(row))
all_candles.reverse()

for i in range(1, len(all_candles)):
    prev = all_candles[i-1]['close']
    curr = all_candles[i]['close']
    all_candles[i]["simple_return"] = simple_return(float(prev), float(curr)) * 100.0
    all_candles[i]["log_return"] = log_return(float(prev), float(curr)) * 100.0
all_candles[0]["simple_return"] = 1
all_candles[0]["log_return"] = 1

## Scatterplot

candles = take_last(all_candles, 365*3)
xs = [datetime.fromtimestamp(int(c['unix'])/1000, zoneinfo.ZoneInfo('America/New_York')) for c in candles]
ys = [c["simple_return"] for c in candles]

plt.scatter(xs, ys)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.show()

## Q-Q plot

candles = take_last(all_candles, 365*3)
simple_returns = [c["simple_return"] for c in candles]

stats.probplot(simple_returns, dist=stats.norm, plot=plt)
plt.grid()
plt.title("Simple Return Distribution")
plt.show()

## Normal Distribution

candles = take_last(all_candles, 365*8)
candles_above_5 = [c for c in candles if c["simple_return"] > 8]
for c in candles_above_5:
    print(c)
print(len(candles_above_5))

simple_returns = [c["simple_return"] for c in candles]

mean = np.mean(simple_returns)
std_dev = np.std(simple_returns)

std_variance = 3
plot_x = np.linspace(mean - std_variance * std_dev, mean + std_variance * std_dev, 1000)
plot_y = stats.norm.pdf(plot_x, mean, std_dev)

a,b = 8, 50
prob = (stats.norm.cdf(b, mean, std_dev) - stats.norm.cdf(a, mean, std_dev)) * 100.0

plt.figure(figsize=(10, 6))
plt.plot(plot_x, plot_y, 'b-', linewidth=2, label=f'Normal ($\\mu$={mean}, $\\sigma$={std_dev})')
plt.fill_between(plot_x, plot_y, alpha=0.3)
plt.title('Normal Distribution')
plt.xlabel('')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
