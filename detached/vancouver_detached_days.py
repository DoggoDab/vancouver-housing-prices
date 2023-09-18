import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)

plt.title("Vancouver Detached Average Days on the Market")

plt.xlabel("Years (from July 2018-July 2023)")
plt.ylabel("Average Days on the Market")

detached_data = {
    "years": ["2018", "2019", "2020", "2021", "2022", "2023"],
    "avg_days": [53, 54, 45, 32, 31, 35]
}

df = pd.DataFrame(detached_data)

arr = np.array([53, 54, 45, 32, 31, 35])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df['years'], df['avg_days'], color='red', marker='o')
plt.bar(df['years'], df['avg_days'], color='blue')

plt.show()