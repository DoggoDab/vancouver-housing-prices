import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)

plt.title("Vancouver Townhouse Average Days")
plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Average Days on the Market")

townhouse_data = {
    "years": ['2018', '2019', '2020', '2021', '2022', '2023'],
    "average_days": [35, 42, 35, 22, 21, 26]
}

df = pd.DataFrame(townhouse_data)

arr = np.array([35, 42, 35, 22, 21, 26])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df["years"], df["average_days"], marker='o')
plt.show()