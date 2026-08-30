import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime

filename = "data_source.json"

datetime_list_initial = []
datetime_list_2 = []

with open(filename, encoding='utf-8') as file:
	storage = json.load(file)

for each_object in storage['objects']:
    datetime_list_initial.append((each_object['id'], datetime.fromisoformat(each_object['start_time'])),)

datetime_list_initial.sort(key=lambda x: x[1])

for dates in datetime_list_initial:
    datetime_list_2.append( (dates[0],dates[1].strftime("%Y-%m-%d  %H:%M:%S")))

# printing sanity

print(datetime_list_2[0])
print(datetime_list_2[1])
print(datetime_list_2[2])
print(datetime_list_2[2])
print()
print(datetime_list_2[100])
print(datetime_list_2[200])
print()
print(datetime_list_2[-4])
print(datetime_list_2[-3])
print(datetime_list_2[-2])
print(datetime_list_2[-1])

# plotting part

# dates = [
#     pd.Timestamp('2025-01-15'), pd.Timestamp('2025-01-16'),
#     pd.Timestamp('2025-01-20'), pd.Timestamp('2025-02-01'),
#     pd.Timestamp('2025-02-15'), pd.Timestamp('2025-02-16')
# ]

date_series = pd.Series(dates_list)

# bins задает количество интервалов
date_series.hist(bins=100, color='skyblue', edgecolor='black')

plt.title('Распределение событий во времени')
plt.xlabel('Дата')
plt.ylabel('Количество')
plt.xticks(rotation=45) # Поворачиваем даты для красоты
plt.tight_layout()
plt.show()
