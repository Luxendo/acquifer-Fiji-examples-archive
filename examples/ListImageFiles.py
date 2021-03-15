"""
This jython script demonstrates how to list image files from an Imaging Machine experiment directory.
The function getListImageFiles accept optional filters in the form of lists, to return only image files for a specific well, subposition, channel, timepoint or Z-slice.
The list of files is then parsed to extract the metadata for each image file.

The script relies on the acquifer-core java package, provided with the acquifer update site.
This script can be run in the Fiji script editor, and requires a dataset of IM images.
Similar scripts in other scripting language can be written by adapting the import statements and general syntax.

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
#@ File (label="Select an IM directory", style="directory") image_directory

from acquifer.im   import Metadatas
from acquifer.im04 import FileUtils, MetadataParser
#from acquifer.im03 import FileUtils, MetadataParser # For an IM03 dataset, simply replace the import statment from the previous line with this line

image_directory = image_directory.toString()

def printAligned(array):
	"""
	This function just print each elements of an array on a new line for better visibility.
	""" 
	for i in array:
		print i

utils = FileUtils()
listFull = utils.getListImageFiles(image_directory) # without additional parameters, all IM03 image files are returned

print "\nList of image files"
printAligned(listFull)

# Add filters for specific wells 
# If none, no filter is applied for this dimension
listSubpositions = None 
listChannel = None
listZslice = None
listTimepoint = None

listWell = ["A002","B001","B002","B003","B010"]
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
listMetadatas = utils.getListMetadatas(listFiltered)

print "\nImages metadata"
printAligned(listMetadatas)

# List wells actually present in the dataset
print "\nUnique wells"
print Metadatas.listUniqueWells(listMetadatas)