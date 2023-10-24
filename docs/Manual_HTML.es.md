



# HTML
  
Modulo para abrir archivos HTML y extraer o agregar información  

*Read this in other languages: [English](Manual_HTML.md), [Português](Manual_HTML.pr.md), [Español](Manual_HTML.es.md)*
  
![banner](imgs/Banner_HTML.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Cargar archivo HTML
  
Carga datos de un archivo HTML en memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo HTML||C:/Users/usuario/Desktop/archivo.html|
|HTML como texto||<!DOCTYPE html>
<html lang="es">
<head>
	 <meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title></title>
</head>|
|Codificación||utf-8|
|Asignar resultado a variable||Variable|
|ID Sesión||Default|

### Insertar Etiqueta
  
Inserta una etiqueta en el HTML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión||Default|
|Nombre de Etiqueta||Nombre|
|Texto de la Etiqueta||Texto|
|Atributo de la Etiqueta||Atributo|
|Texto del Atributo||Texto del Atributo|
|Ubicación de la inserción||body > p|
|Asignar resultado a variable||Variable|

### Guardar archivo
  
Guarda datos en un archivo HTML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo HTML||C:/Users/usuario/Desktop/archivo.html|
|Codificación||utf-8|
|Asignar resultado a variable||Variable|
|ID Sesión||Default|

### Cerrar Sesión
  
Quita una sesión de HTML y libera memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión||Default|
|Asignar resultado a variable||Variable|
