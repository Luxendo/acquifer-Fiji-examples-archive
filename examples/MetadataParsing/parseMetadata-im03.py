"""
This jython script demonstrates the parsing of metadata from image filename for images acquired with an IM03.
This script can be directly run in the Fiji script editor.
It relies on the acquifer-core java package, shipped with the acquifer update site.
These functions can also be used in other java programs, as long as the acquifer-core package is available.
"""
from acquifer.im03 import MetadataParser

parser = MetadataParser()

filename = "WE00019---B006--PO01--LO001--CO6--SL010--PX16250--PW0040--IN0020--TM246--X059308--Y019906--Z212725--T1375564662.tif" # example filename

print "Image name :", filename

print "Well Id :", parser.getWellId(filename) 

print "Plate column :", parser.getWellColumn(filename)
print "Plate row :",    parser.getWellRow(filename)

print "Well subposition :", parser.getWellSubPosition(filename)

print "Well index (order of acquisition) :", parser.getWellIndex(filename)

print "Positions XY (mm): ", parser.getXYPosition(filename).tolist()
print "Position Z (um): ",   parser.getZPosition(filename)

print "Z-slice Number : ", parser.getZSlice(filename)

print "Light power (%) :", parser.getLightPower(filename)

print "Exposure time (ms) :", parser.getLightExposure(filename)

print "Channel index :", parser.getChannelIndex(filename) 

print "Objective Magnification :", parser.getObjectiveMagnification(filename)

print "Pixel Size (um): ", parser.getPixelSize(filename)

print "Objective NA :", parser.getObjectiveNA(filename)

print "Loop iteration :", parser.getLoopIteration(filename)

print "Temperature (°C)", parser.getTemperature(filename)
