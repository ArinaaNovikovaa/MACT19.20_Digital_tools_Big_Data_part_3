import pandas as pd
import geopandas
import seaborn as sns
import matplotlib.pyplot as plt

# Layers: Please double check you set the path to the layers folder
layers_path = '/home/diego/Documents/maps/Barcelona/layers/'
buildings_path = layers_path + 'constru_table.csv'

buildings = pd.read_csv(buildings_path)



# Calculating built area per neighbourhood
buildings_change = buildings.groupby('FECHABAJA', as_index=False)
buildings_change = buildings_change['PARCELA'].count()
buildings_change.columns = ['end_date', 'count']

# Bar plot Changes in buildings across time
ax = sns.barplot('end_date', 'count', data=buildings_change)
plt.close()

