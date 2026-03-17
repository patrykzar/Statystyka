import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

taxi = pd.read_parquet('yellow_tripdata_2021-05.parquet', engine='auto', columns=['trip_distance'])


taxi.query('trip_distance > 0 and trip_distance < 10', inplace=True)

taxi_mean = taxi.mean().iloc[0]
taxi_median = taxi.median().iloc[0]
taxi_mode = taxi.mode().iloc[0,0]
taxi_trim_mean = stats.trim_mean(taxi['trip_distance'], 0.1)


print(f'Taxi mean {taxi_mean}')
print(f'Taxi Median {taxi_median}')
print(f'Taxi Mode {taxi_mode}')
print(f'Taxi trim mean {taxi_trim_mean}')
