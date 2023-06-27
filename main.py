import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('f:/Download/visits.csv', sep='\t')
data['date_time'] = pd.to_datetime(data['date_time'], format = '%Y%m%dT%H%M%S')
data.insert(4,"local_time", data['date_time'] + pd.Timedelta(hours=3))
data['local_time'] = pd.to_datetime(data['local_time'], format = '%Y%m%dT%H%M%S')
data.insert(5,"date_hour", data['local_time'].round("H"))

data.insert(6,"too_fast",  data['time_spent'] < 60)
print(data['too_fast'].mean())
too_fast_stat = data.pivot_table(values="too_fast", index="id")
print(too_fast_stat.head(5))

too_fast_stat.hist(bins=30)
plt.show()