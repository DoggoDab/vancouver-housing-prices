import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)
plt.title("Vancouver Townhouse Sales")

plt.xlabel("Years (July 2018-July 2023)")
plt.ylabel("Sales")

townhouse_data = {
    "years": ['2018', '2019', '2020', '2021', '2022', '2023'],
    "sales": [297, 386, 514, 678, 415, 444]
}

df = pd.DataFrame(townhouse_data)

arr = np.array([297, 386, 514, 678, 415, 444])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df['years'], df['sales'], marker='o')
plt.show()