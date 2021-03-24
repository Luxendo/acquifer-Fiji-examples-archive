"""
Once images from a directory are listed, and metadata extracted, one can sort the list of images in a custom order of dimensions.
The default sorting order is as following (well, subposition, timepoint, Z-slice, -channel).
-channel means that the channels are sorted in reverse order, ie channel 6 (Brightfield) first.

This script takes a image directory and return the list of IM image files first unsorted and then sorted using the default order.

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
#@ File (label="Select an IM directory", style="directory") image_directory

from acquifer.im04 import FileUtils, MetadataParser
#from acquifer.im03 import FileUtils, MetadataParser # For an IM03 dataset, simply replace the import statement from the previous line with this line

from acquifer.im   import Metadatas
from java.util     import Collections 
from ij            import IJ

image_directory = image_directory.toString()

def printAligned(array):
	"""
	This function is designed to print each elements of an array on a new line.
	""" 
	for i in array:
		print i

utils = FileUtils()
listFiles = utils.getListImageFiles(image_directory)

# Get Metadatas
parser = MetadataParser()
listMetadatas = utils.getListMetadatas(listFiles)

print "\nImages metadata (unsorted)"
printAligned(listMetadatas)

# Sort list of metadatas in the following order (well, subposition, timepoint, Z-slice, -channel), for channels reversed (CO6: Brightfield first)

# Sort the list and store it in a new list (ie duplicated the data)
sortedMetadatas = Metadatas.sortCopy(listMetadatas)

# Or sort the list in place
Metadatas.sort(listMetadatas)
# equivalent to
# Collections.sort(listMetadatas, Metadatas.defaultOrder)
# listMetadatas is initially a java ArrayList, which also has a .sort(Comparator) method, but in jython, it is overwritten by the .sort(callable) method


IJ.log("Sorted copy == in-place sorted list :" + str(sortedMetadatas == listMetadatas))
print "\nImages metadata (sorted)"
printAligned(sortedMetadatas)