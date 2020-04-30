import qgis
from qgis.analysis import QgsRasterCalculatorEntry, QgsRasterCalculator

lyr_red = 'T31TDF_20191109T104251_B04_10m'
lyr_ir = 'T31TDF_20191109T104251_B08_10m'
# Set this path before runing the script
lyr_ndvi = '/home/diego/Documents/maps/Barcelona/images/T31TDF_20191109_NDVI.tif'

# Set up raster bands as variables
ras_red = QgsRasterCalculatorEntry()
ras_ir = QgsRasterCalculatorEntry()
# Set up the references
ras_red.ref = 'red@1'
ras_ir.ref = 'ir@1'
# Set up raster values
ras_red.raster = QgsProject.instance().mapLayersByName(lyr_red)[0]
ras_ir.raster = QgsProject.instance().mapLayersByName(lyr_ir)[0]
# Set up the band to read digital levels
ras_red.bandNumber = 1
ras_ir.bandNumber = 1
# Set entries for the Raster Calculator
entries = []
entries.append( ras_red )
entries.append( ras_ir )
# Set the formula and execute it
calc = QgsRasterCalculator( '("ir@1" - "red@1") / ("ir@1" + "red@1")', lyr_ndvi, 'GTiff', ras_red.raster.extent(), ras_red.raster.width(), ras_red.raster.height(), entries )
calc.processCalculation()
print('Executed')