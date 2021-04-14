from acquifer.core.im04 import Metadata
from java.io import File
import os

# There are different ways to create a Metadata object
imagePath = r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\ValerioSubset\-A001--PO01--LO003--CO5--SL009--PX16250--PW0100--IN0100--TM286--X015530--Y010642--Z204727--T0028985883--WE00001.tif"
imageFile = File(imagePath)

imageName = "-A001--PO01--LO003--CO6--SL001--PX16250--PW0100--IN0030--TM285--X015530--Y010642--Z206327--T0028987029--WE00001.tif"

incompletePath = os.path.join("myDir", imageName) 

m1 = Metadata(imageFile)
m2 = Metadata(imageName)
m3 = Metadata(incompletePath)

print m1, "exists:", m1.exists()
print m2, "exists:", m2.exists()
print m3, "exists:", m3.exists()

