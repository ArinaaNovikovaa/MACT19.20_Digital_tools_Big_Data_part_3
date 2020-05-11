import qgis
from qgis.analysis import QgsRasterCalculatorEntry, QgsRasterCalculator

lyr_ir11 = 'T31TDF_20191109T104251_B11_20m'
lyr_ir8 = 'T31TDF_20191109T104251_B08_10m'
# Set this path before runing the script
lyr_ndvi = '/home/diego/Documents/maps/Barcelona/images/NDBI_2019_int.tif'

# Set up raster bands as variables
ras_ir11 = QgsRasterCalculatorEntry()
ras_ir8 = QgsRasterCalculatorEntry()
# Set up the references
ras_ir11.ref = 'ir11@1'
ras_ir8.ref = 'ir8@1'
# Set up raster values
ras_ir11.raster = QgsProject.instance().mapLayersByName(lyr_ir11)[0]
ras_ir8.raster = QgsProject.instance().mapLayersByName(lyr_ir8)[0]
# Set up the band to read digital levels
ras_ir11.bandNumber = 1
ras_ir8.bandNumber = 1
# Set entries for the Raster Calculator
entries = []
entries.append( ras_ir11 )
entries.append( ras_ir8 )
# Set the formula and execute it
calc = QgsRasterCalculator( '("ir11@1" - "ir8@1") / ("ir11@1" + "ir8@1") * 100', lyr_ndvi, 'GTiff', ras_ir11.raster.extent(), ras_ir11.raster.width(), ras_ir11.raster.height(), entries )
calc.processCalculation()
print('Executed')