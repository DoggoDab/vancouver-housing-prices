import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)
plt.title("Vancouver Apartment Active Listings")

plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Active Listings")

apartment_data = {
    "years": ['2018', '2019', '2020', '2021', '2022', '2023'],
    "active_listings": [4266, 4978, 4966, 4105, 3792, 3790]
}

df = pd.DataFrame(apartment_data)

arr = np.array([4266, 4978, 4966, 4105, 3792, 3790])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df["years"], df["active_listings"], marker='o')
plt.show()
