/*
 * This macro can be copy/pasted in the custom macro field of the Batch Process Hyperstack (macro)
 * It demonstrates how to recover the current image names from the plugin using the getArguments() function. 
 * 
 * The getArguments method returns as one string the names of the stack and/or projection images generated by the plugin for the current iteration.
 * The image names are separated by a commas, therefore we split this String to recover the individual image names.
 * Once you have the image name, you can process the image after selecting it with selectImage(name)
 * 
 * NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
 * Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
 * Use File > Save As... to save a copy of this example, and keep your modifications.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
 */

run("Acquifer IM04 macro extensions");         // provides the Ext.splitArguments function
image_titles = getArgument();                   // this is a single string which can be in the form "yourStack, yourProj", "yourStack" (only stack displayed), or ",yourProj" if only projection is displayed  
Ext.splitArguments(image_titles, stack, projection);  // recover the individual image names as separate variables

// Print the images titles
// if the stack or the projection is not displayed, then its variable will be an empty string ("")
print("\nNext well/subposition");
print("title stack: ", stack);
print("title projection: " , projection);


// You can remove the "if" block if you know that you will always display the stack and/or projection
if (stack != ""){
	print("Process stack");
	selectImage(stack);
	// other commands of your choice
}

if (projection != ""){
	print("Process projection");
	selectImage(projection);
	// other commands of your choice
}
