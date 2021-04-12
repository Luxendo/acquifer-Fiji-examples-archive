"""
This jython script demonstrates how to list images and their dimension-metadatas from a directory of images.
The list of images and metadatas (actually a list of Metadatas objects) is then filtered to keep only specific dimensions.
It also shows how to recover the set of unique wells present in a list of Metadatas objects

The script relies on the acquifer-core java package, provided with the acquifer update site.
This script can be run in the Fiji script editor, and requires a dataset of IM images.
Similar scripts in other scripting language can be written by adapting the import statements and general syntax.

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
#@ File (label="Select an IM directory", style="directory") image_directory

from acquifer.core.im04 import FileUtils, Metadatas
#from acquifer.core.im03 import FileUtils, Metadatas # For an IM03 dataset, simply replace the import statment from the previous line with this line
from acquifer.ij.Utils  import printArray
from ij import IJ

image_directory = image_directory.toString()

utils = FileUtils()
listFull = utils.getListMetadatas(image_directory) # list IM files and parse dimensions metadatas

# Filter the List<Metdata> 
filterWells        = ["B001","B002"]
#filterWells        = [] # empty list as filter should return all wells
filterSubPositions = []
filterChannels     = []
filterZslices      = [1]
filterTimepoints   = []

filteredByWell         = Metadatas.filterWells(listFull, filterWells)
filteredMultiDimension = Metadatas.filter(listFull,
										  filterWells,
										  filterSubPositions,
										  filterChannels,     
										  filterZslices,      
										  filterTimepoints)
print len(listFull)
print len(filteredByWell)
print len(filteredMultiDimension)

print "See log window for list of filtered metadatas"
printArray(filteredMultiDimension)

print Metadatas.listUniqueWells(listFull) 
print Metadatas.listUniqueWells(filteredByWell) 
print Metadatas.listUniqueWells(filteredMultiDimension)