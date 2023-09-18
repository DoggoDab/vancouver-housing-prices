import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)
plt.title("Vancouver Apartment Sales")

plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Sales")

apartment_data = {
    "years": ['2018', '2019', '2020', '2021', '2022', '2023'],
    "sales": [874, 1073, 1172, 1815, 1229, 1258]
}

df = pd.DataFrame(apartment_data)

arr = np.array([874, 1073, 1172, 1815, 1229, 1258])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df["years"], df["sales"], marker='o')
plt.show()