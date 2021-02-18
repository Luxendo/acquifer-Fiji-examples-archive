"""
This script demonstrates how to use the plugin "Batch process hyperstack (script)" with a jython script or any other Fiji scripting language.
In this example, we just display the name of the stack and Z-projection (which can be null if no projection was made) to the log window. 

Scripts should have 2 script-parameters for the inputs (stack and proj as below).
Even if no projection was done (in this case, proj is just null).

Contrary than with macros, it is not necessary to display the images to process them with custom scripts.
The ImagePlus object in memory is directly passed from the batch-hyperstack plugin to the script, in a "headless" fashion.
"""
#@ImagePlus stack
#@ImagePlus proj
from ij import IJ
from ij.plugin import Commands

IJ.log("Processing stack : " + stack.getTitle())
IJ.log("Processing projection : " + proj.getTitle())


# Close images (and free memory)

# either one by one
stack.close()
proj.close()

# Or using close all
Commands.closeAll()
