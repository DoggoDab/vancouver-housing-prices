import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)

plt.title("Vancouver Detached Benchmark Prices")

plt.xlabel("Years (from July 2018-July 2023)")
plt.ylabel("Benchmark Prices")

detached_data = {
    "years": ["2018", "2019", "2020", "2021", "2022", "2023"],
    "benchmark_prices": [1532233, 1424617, 1482725, 1776875, 1986758, 1907114]
}

df = pd.DataFrame(detached_data)

arr = np.array([1532233, 1424617, 1482725, 1776875, 1986758, 1907114])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df['years'], df['benchmark_prices'], color='red', marker='o')
plt.bar(df['years'], df['benchmark_prices'], color='blue')

plt.show()