import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# IN THE LAST 5 YEARS (JULY 2018-JULY 2023)
plt.figure().set_figwidth(100)

plt.title("Vancouver Detached Active Listings")

plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Active Listings")

detached_data = {
    "year": ["2018", "2019", "2020", "2021", "2022", "2023"],
    "activelistings": [6012, 5601, 4000, 3604, 3737, 3463],
}

df = pd.DataFrame(detached_data)

arr = np.array([6012, 5601, 4000, 3604, 3737, 3463])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df["year"], df["activelistings"], color='red', marker='o')
plt.bar(df['year'], df['activelistings'], color='blue')

plt.show()
