/*
 * This macro demonstrates how to parse the metadata from an image file name, for an image acquired with an Imaging Machine. 
 * You can directly run this macro, it is preconfigured with an example filename.
 * The metadata will be printed to a log window.
 * 
 * The first line loads the Acquifer macro extension, which allows calling the functions using the "Ext" mechanism.
 * 2 different macro extensions cannot be loaded simultaneously (if you need functionalities from another update site/package).
 * However, you can load another extension at the end of this script for instance, such that Ext will be refering to this new extension, and not to the Acquifer extension anymore.
 *
 * NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
 * Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
 * Use File > Save As... to save a copy of this example, and keep your modificationss.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
 */

run("Acquifer IM04 macro extensions");  // this line is necessary to have access to the acquifer macro-functions via the Ext mechanism
//run("Acquifer IM03 macro extensions"); // uncomment this line for IM03

filename = "-A002--PO01--LO001--CO6--SL001--PX32500--PW0080--IN0020--TM281--X023590--Y011262--Z211710--T0200262822--WE00002.tif";
//filename = "WE00020---B005--PO01--LO001--CO6--SL010--PX16250--PW0040--IN0020--TM246--X050299--Y019906--Z212275--T1375574652.tif"; // uncomment this line for IM03

print("Image name :", filename);

ID = Ext.getWellId(filename);
print("Well Id :", ID);

Ext.getWellColumn(filename, column);
print("Plate column : ", column);

row = Ext.getWellRow(filename);
print("Plate row : ", row);

Ext.getWellSubPosition(filename, subPos);
print("Well subposition : ", subPos);

Ext.getWellIndex(filename, index);
print("Well index (order of acquisition) : ", index);

Ext.getXYPosition(filename, X, Y);
print("Positions (mm) X: ", X, " Y: ", Y);

Ext.getZPosition(filename, Z);
print("Position Z (um) : ",Z);

Ext.getZSlice(filename, slice);
print("Z-slice : ", slice);

Ext.getLightPower(filename, power);
print("Light power (%) : ", power);

Ext.getLightExposure(filename, exposure);
print("Exposure time (ms) : ", exposure);

Ext.getChannelIndex(filename, channel);
print("Channel index : ", channel);

Ext.getObjectiveMagnification(filename, mag);
print("Objective Magnification (X) : ", mag);

Ext.getObjectiveNA(filename, NA);
print("Objective NA : ", NA);

Ext.getPixelSize(filename, pixSize); // this function also exists in ImageJ, hence the different text-color
print("Pixel Size (um) : ", pixSize);

Ext.getLoopIteration(filename, iteration);
print("Loop iteration : ", iteration);

Ext.getTemperature(filename, temp);
print("Temperature (°C) : ", temp);