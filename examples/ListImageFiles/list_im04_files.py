"""
This jython script demonstrates how to list image files from an Imaging Machine (version 4 ie IM04) experiment directory.
The function getListImageFiles accept optional filter in the form of list, to return only image files for a specific well, subposition, channel, timepoint or Z-slice.
The list of files is then parsed to extract the metadata for each image file.

The script relies on the acquifer-core java package, provided with the acquifer update site.
This script can be run in the Fiji script editor, and requires a dataset of IM03 images.
Similar scripts in other scripting language can be written by adapting the import statements and general syntax.
"""
#@ File (label="Select an IM04 directory", style="directory") image_directory
from acquifer.im04 import FileUtils, MetadataParser

image_directory = image_directory.toString()

def printAligned(array):
	"""
	This function is designed to print each elements of an array on a new line.
	""" 
	for i in array:
		print i

utils = FileUtils()
listFull = utils.getListImageFiles(image_directory) # without additional parameters, all IM03 image files are returned

print "\nList of image files"
printAligned(listFull)

# Add filters for specific wells 
# If none, no filter is applied for this dimension
listWell = ["A002","B010"]
listSubpositions = None 
listChannel = None
listZslice = None
listTimepoint = None

listFiltered = utils.getListImageFiles(image_directory, 
										listWell, 
										listSubpositions, 
										listChannel, 
										listZslice, 
										listTimepoint)
print "\nWith dimension filter"
printAligned(listFiltered)

# Parse the metadata for the list of image files that were filtered
parser = MetadataParser()
listInfos = parser.getImagesInfos(listFiltered)

print "\nImages metadata"
printAligned(listInfos)