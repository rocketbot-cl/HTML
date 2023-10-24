



# HTML
  
Module to open HTML files and get or add data  

*Read this in other languages: [English](Manual_HTML.md), [Português](Manual_HTML.pr.md), [Español](Manual_HTML.es.md)*
  
![banner](imgs/Banner_HTML.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Load HTML File
  
Load data from an HTML file into memory
|Parameters|Description|example|
| --- | --- | --- |
|HTML file path||C:/Users/usuario/Desktop/archivo.html|
|HTML as text||<!DOCTYPE html>
<html lang="en">
<head>
	 <meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title></title>
</head>|
|Encoding||utf-8|
|Assign result to variable||Variable|
|Session ID||Default|

### Insert Tag
  
Insert tag on HTML
|Parameters|Description|example|
| --- | --- | --- |
|Session ID||Default|
|Tag name||Name|
|Tag Text||Text|
|Tag Attribute||Attribute|
|Attribute Text||Attribute Text|
|Insertion location||body > p|
|Assign result to variable||Variable|

### Save File
  
Save HTML File
|Parameters|Description|example|
| --- | --- | --- |
|HTML file path||C:/Users/usuario/Desktop/archivo.html|
|Encoding||utf-8|
|Assign result to variable||Variable|
|Session ID||Default|

### End Session
  
Remove an HTML session from memory
|Parameters|Description|example|
| --- | --- | --- |
|Session ID||Default|
|Assign result to variable||Variable|
