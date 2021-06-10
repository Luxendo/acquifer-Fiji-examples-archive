from acquifer.core.im04 import ImagePlane, Dataset
from acquifer.ij import Utils 
from ij import IJ

# Unfiltered dataset, get all images
dataset = Dataset(r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\Hanh\Lateral\subSet4X")
print dataset

Utils.printArray(dataset.getListImagePlanes())

# Filter the List<Metdata> 
filterWells        = ["B001","B002"]
#filterWells        = [] # empty list as filter should return all wells
filterSubPositions = []
filterChannels     = [8]
filterZslices      = []
filterTimepoints   = []

dataset2 = Dataset(r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\Hanh\Lateral\subSet4X", filterWells,
																								filterSubPositions,
																								filterChannels,
																								filterZslices,
																								filterTimepoints)

IJ.log("\nWith filters")
print dataset2
Utils.printArray(dataset2.getListImagePlanes())