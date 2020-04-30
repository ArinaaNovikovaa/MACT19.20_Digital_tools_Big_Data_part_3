import pandas as pd
import geopandas
import seaborn as sns
import matplotlib.pyplot as plt

# Layers: Please double check you set the path to the layers folder
layers_path = '/home/diego/Documents/maps/Bogota/layers/'
buildings_path = layers_path + 'cons_upla.csv'
neighbourhoods_path = layers_path + 'UPla.shp'
population_path = layers_path +'population_upz_2015.csv'
buildings = pd.read_csv(buildings_path)
neighbourhoods = geopandas.read_file(neighbourhoods_path)
population = pd.read_csv(population_path)


# Calculating built area per neighbourhood
built_area = buildings.groupby('code', as_index=False)
built_area = built_area['built_area'].sum()
neighbourhoods = neighbourhoods.join(built_area, rsuffix='_b')

# Scatter plot Total Area Vs. Built Area
ax = sns.scatterplot('UPlArea', 'built_area', data=neighbourhoods)
plt.close()

# Adding population
neighbourhoods = neighbourhoods.join(population, rsuffix='_p')
ax = sns.scatterplot('total', 'built_area', data=neighbourhoods)
plt.close()

# Normalising values. Population density and built square metres per square kilometres
neighbourhoods['built_sqkm'] = neighbourhoods['built_area'] / (neighbourhoods['UPlArea'] / 1000000)
neighbourhoods['pop_sqkm'] = neighbourhoods['total'] / (neighbourhoods['UPlArea'] / 1000000)
neighbourhoods['sqm_per_capita'] = neighbourhoods['UPlArea'] / neighbourhoods['total']
ax = sns.scatterplot('pop_sqkm', 'built_area', hue='total', size='total', sizes=(1, 200), data=neighbourhoods)
ax.set(xlabel='Population density per square Km', ylabel='Built area in Square Km',
       title='Population and built area in Bogotá - Colombia')
plt.close()

neighbourhoods.to_file('upla_joined.json', driver='GeoJSON')
