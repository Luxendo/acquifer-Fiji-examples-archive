"""
Although not super useful, you can call the hyperstack plugin to show up via scripting too.
Either using macro-recording which will give you something like IJ.run(..)
Or using the command below.
"""
from acquifer.im04.plugins import Hyperstack_Maker
#from acquifer.im04.plugins import Hyperstack_Maker # Uncoment this line for IM03

# Call the plugin
Hyperstack_Maker.run()