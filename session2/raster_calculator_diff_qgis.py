import qgis
from qgis.analysis import QgsRasterCalculatorEntry, QgsRasterCalculator

ndvi_before = 'T31TDF_20150802_NDVI'
ndvi_after = 'T31TDF_20191109_NDVI'
# Set this path before runing the script
lyr_dif = '/home/diego/Documents/maps/Barcelona/images/ndvi_diff.tif'

# Set up raster bands as variables
ndvi_b = QgsRasterCalculatorEntry()
ndvi_a = QgsRasterCalculatorEntry()
# Set up the references
ndvi_b.ref = 'bef@1'
ndvi_a.ref = 'aft@1'
# Set up raster values
ndvi_b.raster = QgsProject.instance().mapLayersByName(ndvi_before)[0]
ndvi_a.raster = QgsProject.instance().mapLayersByName(ndvi_after)[0]
# Set up the band to read digital levels
ndvi_b.bandNumber = 1
ndvi_a.bandNumber = 1
# Set entries for the Raster Calculator
entries = []
entries.append( ndvi_b )
entries.append( ndvi_a )
# Set the formula and execute it
calc = QgsRasterCalculator( '"aft@1" - "bef@1"', lyr_dif, 'GTiff', ndvi_a.raster.extent(), ndvi_a.raster.width(), ndvi_a.raster.height(), entries )
calc.processCalculation()
print('Executed')