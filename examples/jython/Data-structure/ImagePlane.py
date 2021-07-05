"""
This snippet demonstrates the handling of ImagePlane, which represents a single IM image.
Typically you obtain ImagePlane via a Dataset object (see the dedicated Dataset example script).
"""
from acquifer.core.im04 import ImagePlane
from ij import IJ

filePath = r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\Valerio\-A001--PO01--LO001--CO3--SL005--PX16250--PW0100--IN0100--TM285--X015530--Y010642--Z206027--T0021785290--WE00001.tif"
plane = ImagePlane(filePath)
print "Image Plane :", plane

# TODO add link to API docu online
# Just like wit the MetadataParser, one can recover metadata from an ImagePlane
print "Channel :",    plane.getChannel()
print "Z-slice :",    plane.getZslice()
print "Timepoint: ",  plane.getTimepoint()
print "Pixel-size: ", plane.getPixelSize() , "um"

print "Directory: ", plane.getDirectoryName()

# Other possible commands
# Note some attributes (temperature, timepoint...) are read-only attributes
for command in dir(plane):
	print command

# Show the image contained in the ImagePlane
imp = IJ.openImage(plane.getPath())
print imp
imp.show()
