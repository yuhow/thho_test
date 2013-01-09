#!/home/thho/thho_installed/local/bin/python
import os
import numpy
import gdspy

bool_cell = gdspy.Cell('BOOLEAN')
liPolygon = []

liUnitDummy = []
yPitch=6
for i in range(4):
    yMove = i*yPitch
    liUnitDummy.append(gdspy.Rectangle(51, (0, yMove+3), (18, yMove)).points)


frame_poly = gdspy.Rectangle(11,(-10,30),(30,-10)).points
frame_poly_list = [frame_poly]

#liPolygon.append(liUnitDummy)
subtraction = lambda p1, p2: p2 and not p1
bool_cell.add(gdspy.boolean(1,[gdspy.PolygonSet(0,liUnitDummy), gdspy.PolygonSet(0,frame_poly_list)], subtraction, max_points=199))
#bool_cell.add(gdspy.PolygonSet(1, liUnitDummy[0]+liUnitDummy[1]+liUnitDummy[2]+liUnitDummy[3]))
#bool_cell.add(liUnitDummy)






name = os.path.abspath(os.path.dirname(os.sys.argv[0])) + os.sep +\
       'gdspy-autodummy'
gdspy.gds_print(name + '.gds', unit=1.0e-6, precision=1.0e-9)
gdspy.LayoutViewer()
