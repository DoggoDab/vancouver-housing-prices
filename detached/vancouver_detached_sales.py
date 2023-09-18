import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure().set_figwidth(100)

plt.title("Vancouver Detached Sales")

plt.xlabel("Years (from July 2018-July 2023)")
plt.ylabel("Vancouver Sales")

detached_data = {
    "years": ["2018", "2019", "2020", "2021", "2022", "2023"],
    "sales": [536, 685, 901, 1175, 694, 703]
}

df = pd.DataFrame(detached_data)

arr = np.array([536, 685, 901, 1175, 694, 703])
median = np.median(arr)
plt.axhline(median, linestyle='dashed', color='yellow', label='median')

plt.plot(df['years'], df['sales'], color='red', marker='o')
plt.bar(df['years'], df['sales'], color='blue')

plt.show()
