"""
This script demonstrates how you can reuse the batch dialog used by various acquifer plugin in custom plugins.
The class BatchDialog is derived from the ImageJ1 GenericDialog class, and thus offer the same functionalities (in particular macro-recording), 
in addition to custom functionalities.  
You can also use some functions available with the BatchDialog class, with custom GenericDialog

You can consult the GenericDialog API documentation at: 
https://imagej.nih.gov/ij/developer/api/ij/gui/GenericDialog.html

and the BatchDialog API documentation at: 
https://acquifer.github.io/acquifer-IJ/acquifer/gui/BatchDialog.html
"""
from acquifer.gui import BatchDialog 
from ij import IJ

dialog = BatchDialog("Test batch dialog") 
dialog.addStringField("Some input", "default") # Add a string input for the sake of example
dialog.showDialog()

if dialog.wasOKed():

	# this function will read the inputs for the GUI elements composing the left panel of the GUI
	# the inputs are stored as attribute of the dialog object.
	dialog.getDefaultInputs() 

	# Once the default inputs were read, one can check that their value fits in the allowed range
	# ex: no negative channel index, slice index...
	if not dialog.validateInputs(): 
		msg = "Input not valid."
		IJ.error(msg)
		raise Exception(msg) # this stops the script execution and raises an exception

	# We can now get the default inputs, this also works after having called getDefaultInputs
	print "image directory: ", dialog.getImageDirectory()
	print "selected wells: ",  dialog.getWells()
	print "subpositions:"   ,  dialog.getSubpositions()
	print "channels: "      ,  dialog.getChannels()
	print "Z-slice: "       ,  dialog.getZslice()
	print "Timepoints: "    ,  dialog.getTimepoints()

	# Finally we can get the custom string field
	stringField = dialog.getNextString()
	print "Custom string input: ", stringField
	 