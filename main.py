import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('f:/Download/visits.csv', sep='\t')
data['date_time'] = pd.to_datetime(data['date_time'], format = '%Y%m%dT%H%M%S')
data.insert(4,"local_time", data['date_time'] + pd.Timedelta(hours=3))
data['local_time'] = pd.to_datetime(data['local_time'], format = '%Y%m%dT%H%M%S')
data.insert(5,"date_hour", data['local_time'].round("H"))

data.insert(6,"too_fast",  data['time_spent'] < 60)
#print(data['too_fast'].mean())
too_fast_stat = data.pivot_table(values="too_fast", index="id")

data.insert(6,"too_slow",  data['time_spent'] > 1000)
too_slow_stat = data.pivot_table(values="too_slow", index="id")
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
#print(len(good_data))
good_data = good_data.query('60 <= time_spent <= 1000')
#print(len(data))
#print(len(good_data))
#too_slow_stat.hist(bins=60)
#plt.show()

good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')
#good_stations_stat.hist(bins=50)
#plt.show()
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat = data.pivot_table(index='name', values='time_spent')
stat.insert(1,"good_time_spent",  good_stat['time_spent'])
id_name= good_data.pivot_table(index="id", values="name", aggfunc=['first','count'])
print(id_name.head(5))