import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)
plt.title("Vancouver Townhouse Benchmark Prices")
plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Benchmark Prices")

townhouse_data = {
    "years": ['2018', '2019', '2020', '2021', '2022', '2023'],
    "benchmark": [832833, 778592, 799608, 849875, 1080317, 1068600]
}

df = pd.DataFrame(townhouse_data)

arr = np.array([832833, 778592, 799608, 849875, 1080317, 1068600])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df["years"], df["benchmark"], marker='o')
plt.show()