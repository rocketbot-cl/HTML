



# HTML
  
Module to work with HTML. Read and edit HTML files  

![banner](imgs/Modulo_HTML.jpg)


## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Load HTML File
  
Load data from an HTML file into memory
|Parameters|Description|example|
| --- | --- | --- |
|HTML file path|Link the HTML file to the corresponding path|C:/Users/usuario/Desktop/archivo.html|
|HTML as text|Connect the HTML code passed as text, without having to create the file|`<!DOCTYPE html><html lang="pr"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title></title></head>`|
|Encoding|Encoding with which the HTML file is required to be opened. By default it is UTF-8|utf-8|
|Assign result to variable|Variable where the result of Load HTML is stored|var|
|Session ID|Optional ID to identify open sessions|s1|

### Insert Tag
  
Insert tag on HTML
|Parameters|Description|example|
| --- | --- | --- |
|Session ID|ID of the open file to which you want to add the tag, in the case of having multiple open sessions|s1|
|Tag name|Name of the HTML tag to create the element|div|
|Tag Text|Text of the HTML Element to create with the tag|Hello World|
|Tag Attribute|HTML Attribute name for the tag to create. Optional.|class|
|Attribute Value|HTML attribute value for the tag to create. Optional.|myclass|
|Insertion location|Css selector or Xpath where the tag insertion will be made|body > p|
|Assign result to variable|Variable where the result of Insert Tag is stored|var|

### List to HTML Tables
  
Convert a list to an HTML format table
|Parameters|Description|example|
| --- | --- | --- |
|List|List to be converted to an HTML format table|[['s1', 's2', 's3'], ['t1', 't2', 't3']]|
|Assign result to variable|Variable where the converted HTML table is stored|var|

### HTML Tables to List
  
Convert an HTML format table to a list
|Parameters|Description|example|
| --- | --- | --- |
|Table|HTML format table to be converted to a List|`<table><tr><td>1</td><td>Jane</td></tr><tr><td>2</td><td>John</td></tr></table>`|
|Assign result to variable|Variable where the converted list is stored|var|

### Save File
  
Save HTML File
|Parameters|Description|example|
| --- | --- | --- |
|HTML file path|Path where the uploaded HTML file will be saved|C:/Users/usuario/Desktop/archivo.html|
|Encoding|Encoding with which to save the uploaded HTML file|UTF-8|
|Assign result to variable|Variable where the result of Save HTML is stored|var|
|Session ID|ID to identify the file to save in case of having multiple sessions|s1|

### End Session
  
Remove an HTML session from memory
|Parameters|Description|example|
| --- | --- | --- |
|Session ID|ID to identify the file to close in case of having multiple sessions|s1|
|Assign result to variable|Variable where the result of End Session is stored|var|
