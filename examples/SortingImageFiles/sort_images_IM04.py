"""
Once images from a directory are listed, and metadata extracted, one can sort the list of images in a custom order of dimensions.
The default sorting (well, subposition, timepoint, Z-slice, -channel).
-channel means that the channels are sorted in reverse order, ie channel 6 (Brightfield) first.
"""
#@ File (label="Select an IM04 directory", style="directory") image_directory
from acquifer.im04 import FileUtils, MetadataParser
from acquifer.im   import ImageInfos
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

# Get ImageInfos
parser = MetadataParser()
listInfos = parser.getImagesInfos(listFiles)

print "\nImages metadata (unsorted)"
printAligned(listInfos)

# Sort list of infos in the following order (well, subposition, timepoint, Z-slice, -channel), for channels reversed (CO6: Brightfield first)

# Sort the list and store it in a new list (ie duplicated the data)
sortedInfos = ImageInfos.sortCopy(listInfos)

# Or sort the list in place
ImageInfos.sort(listInfos)
# equivalent to
# Collections.sort(listInfos, ImageInfos.defaultOrder)
# listInfos is initially a java ArrayList, which also has a .sort(Comparator) method, but in jython, it is overwritten by the .sort(callable) method


IJ.log("Sorted copy == in-place sorted list :" + str(sortedInfos == listInfos))
print "\nImages metadata (sorted)"
printAligned(sortedInfos)



