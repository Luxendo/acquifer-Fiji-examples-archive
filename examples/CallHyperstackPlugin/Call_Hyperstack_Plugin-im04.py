"""
Although not super useful, you can call the hyperstack plugin to show up via scripting too.
Either using macro-recording which will give you something like IJ.run(..)
Or using the command below.
"""
from acquifer.im04.plugins import Hyperstack_Maker_IM04

# Call the plugin
Hyperstack_Maker_IM04().run()