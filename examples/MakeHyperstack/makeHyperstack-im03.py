"""
From a directory, a well and subposition, this scripts list the image files and make a hyperstack for a selected well and subposition.
the following variables should be updated to match your local image dataset:
- inputDir
- selectedWell and selectedSubpositions
- listChannel, Zslice and Timepoint
"""
from acquifer.im03         import FileUtils, MetadataParser
from acquifer.im03.plugins import Hyperstack_Maker_IM03

inputDir = r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\Fish\IM03_BISCHOFF_DORSAL_2ndGO_4x" # IM03

# Applying a dimension filter
selectedWell = ["A002"]
selectedSubpositions = [1]
listChannel   = None # if None or [], all available channels will be displayed, same for other dimensions
listZslice    = None
listTimepoint = None

def printAligned(array):
	"""
	This function is designed to print each elements of an array on a new line.
	""" 
	for i in array:
		print i

listFiltered = FileUtils().getListImageFiles(inputDir, 
                                             selectedWell, 
                                             selectedSubpositions, 
                                             listChannel, 
                                             listZslice, 
                                             listTimepoint)
print "\nList files"
printAligned(listFiltered)

# Get metadatas
listInfos = MetadataParser().getImagesInfos(listFiltered)
print "\nImages metadata"
printAligned(listInfos)

# Make hyperstacks
hyperstack = Hyperstack_Maker_IM03().makeHyperStack(listInfos)
hyperstack.show()