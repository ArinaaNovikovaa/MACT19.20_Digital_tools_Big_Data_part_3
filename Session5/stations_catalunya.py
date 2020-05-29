import pandas as pd
import geopandas
import seaborn as sns
import matplotlib.pyplot as plt

# Layers: Please double check you set the path to the layers folder
measurement_path = './data/data_air_catalonia.csv'
stations_path = 'stations_catalonia.geojson'
measurement = pd.read_csv(measurement_path, nrows=100000)
measurement['DATA'] = pd.to_datetime(measurement['DATA'])

# Calculating built area per neighbourhood
stations = measurement.groupby(['CODI MUNICIPI', 'CODI ESTACIÓ', 'NOM ESTACIÓ', 'MUNICIPI', 'LATITUD',
                                'LONGITUD', 'ALTITUD'], as_index=False).count()
stations = geopandas.GeoDataFrame(stations, geometry=geopandas.points_from_xy(stations.LONGITUD, stations.LATITUD))

# Brief visualisation
stations.plot()
plt.show()

# Save file to be used in QGIS
stations.to_file(stations_path, driver='GeoJSON')



#################################################
### Plot
measurement_poblenou = measurement[measurement['NOM ESTACIÓ'] == 'Barcelona (Poblenou)']
measurement_poblenou_pm10 = measurement_poblenou[measurement_poblenou['CONTAMINANT'] == 'PM10']
sns.lineplot(x='DATA', y='H10', data=measurement_poblenou_pm10)
plt.show()

ax = sns.lineplot(x='DATA', y='H24', data=measurement_poblenou_pm10)
ax1 = sns.lineplot(x='DATA', y='H06', data=measurement_poblenou_pm10)
ax2 = sns.lineplot(x='DATA', y='H12', data=measurement_poblenou_pm10)
ax3 = sns.lineplot(x='DATA', y='H18', data=measurement_poblenou_pm10)
plt.show()
