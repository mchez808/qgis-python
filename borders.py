# for use in Python console of
# QGIS v3.6.0-Noosa
layer = iface.addVectorLayer("C:/Users/markc/wd/mchez808/qgis-python/naturalearthdata/physical/TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp", "TM_WORLD_BORDERS-0.3", "ogr")

# zoom into Southern California using mapCanvas object
soCal_xmin = -125; soCal_ymin = 31; soCal_xmax = -113; soCal_ymax = 38
iface.mapCanvas().setExtent(QgsRectangle(soCal_xmin, soCal_ymin, soCal_xmax, soCal_ymax))
# restore resolution
iface.mapCanvas().refresh()

# change ocean background color
from qgis.PyQt.QtGui import QColor
iface.mapCanvas().setCanvasColor(QColor("#6060FF"))

# simple geospatial analysis: print all centroids
for feature in layer.getFeatures():
    geometry = feature.geometry()
    centroid = geometry.centroid().asPoint()
    name = feature.attribute("NAME")
    print(name, centroid.x(), centroid.y())
