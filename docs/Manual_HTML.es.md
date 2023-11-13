



# HTML
  
Módulo para trabajar con HTML. Lee y edita archivos HTML  
  
![banner](imgs/Modulo_HTML.jpg)


## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Cargar archivo HTML
  
Carga datos de un archivo HTML en memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo HTML|Conecta el archivo HTML correspondiente a la ruta|C:/Users/usuario/Desktop/archivo.html|
|HTML como texto|Conecta el código HTML pasado como texto, sin necesidad de tener creado el archivo|`<!DOCTYPE html><html lang="pr"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title></title></head>`|
|Codificación|Codificación con la que se requiere abrir el archivo HTML. Por default es UTF-8|utf-8|
|Asignar resultado a variable|Variable donde se almacena el resultado de Cargar HTML|var|
|ID Sesión|ID opcional para poder identificar sesiones abiertas|s1|

### Insertar Etiqueta
  
Inserta una etiqueta en el HTML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión|ID del archivo abierto al que se le quiere agregar la etiqueta, en el caso de tener multiples sesiones abiertas|s1|
|Nombre de Etiqueta|Nombre de la etiqueta HTML para crear el elemento|div|
|Texto de la Etiqueta|Texto del Elemento HTML a crear con la etiqueta|Hola Mundo|
|Atributo de la Etiqueta|Nombre del Atributo HTML para la etiqueta a crear. Opcional.|class|
|Valor del Atributo|Valor del atributo HTML para la etiqueta a crear. Opcional.|miclase|
|Ubicación de la inserción|Selector css o Xpath donde se realizara la inserción de la etiqueta|body > p|
|Asignar resultado a variable|Variable donde se almacena el resultado de Insertar Etiqueta|var|

### Lista a Tabla HTML
  
Convierte una lista en una tabla de formato HTML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Lista|Lista que se va a convertir en una tabla de formato HTML|[['s1', 's2', 's3'], ['t1', 't2', 't3']]|
|Asignar resultado a variable|Variable donde se almacena la tabla HTML convertida|var|

### Tabla HTML a Lista
  
Convierte una tabla de formato HTML en una lista
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tabla|Tabla de formato HTML que se va a convertir en una Lista|`<table><tr><td>1</td><td>Juana</td></tr><tr><td>2</td><td>Juan</td></tr></table>`|
|Asignar resultado a variable|Variable donde se almacena la lista convertida|var|

### Guardar archivo
  
Guarda datos en un archivo HTML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo HTML|Ruta donde se va a guardar el archivo HTML cargado|C:/Users/usuario/Desktop/archivo.html|
|Codificación|Codificación con la que se va a guardar el archivo HTML cargado|UTF-8|
|Asignar resultado a variable|Variable donde se almacena el resultado de Guardar HTML|var|
|ID Sesión|ID para poder identificar el archivo a guardar en caso de tener múltiples sesiones|s1|

### Cerrar Sesión
  
Quita una sesión de HTML y libera memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión|ID para poder identificar el archivo a cerrar en caso de tener múltiples sesiones|s1|
|Asignar resultado a variable|Variable donde se almacena el resultado de Cerrar Sesión|var|
