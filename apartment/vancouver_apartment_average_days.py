import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)
plt.title("Vancouver Apartment Average Days on Market")

plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Average Days on Market")

apartment_data = {
    "years": ['2018', '2019', '2020', '2021', '2022', '2023'],
    "average_days": [32, 40, 33, 27, 23, 29]
}

df = pd.DataFrame(apartment_data)

arr = np.array([32, 40, 33, 27, 23, 29])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df["years"], df["average_days"], marker='o')
plt.show()