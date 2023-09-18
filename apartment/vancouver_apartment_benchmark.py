import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)
plt.title("Vancouver Apartment Benchmark Prices")

plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Benchmark Prices")

apartment_data = {
    "years": ['2018', '2019', '2020', '2021', '2022', '2023'],
    "benchmark_prices": [683117, 655917, 623750, 669425, 766225, 748857]
}

df = pd.DataFrame(apartment_data)

arr = np.array([683117, 655917, 623750, 669425, 766225, 748857])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df["years"], df["benchmark_prices"], marker='o')
plt.show()