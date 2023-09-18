import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)

plt.title("Vancouver Townhouse Active Listings")

plt.xlabel("Years (from July 2018-July 2023)")
plt.ylabel("Active Listings")

townhouse = {
    "years": ["2018", "2019", "2020", "2021", "2022", "2023"],
    "active_listings": [1824, 2076, 1658, 1155, 1271, 1303]
}

df = pd.DataFrame(townhouse)

arr = np.array([1824, 2076, 1658, 1155, 1271, 1303])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df['years'], df['active_listings'], marker='o')

plt.show()
