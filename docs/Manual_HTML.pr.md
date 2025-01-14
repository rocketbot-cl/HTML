



# HTML
  
Módulo para trabalhar com HTML. Ler e editar arquivos HTML  

*Read this in other languages: [English](Manual_HTML.md), [Português](Manual_HTML.pr.md), [Español](Manual_HTML.es.md)*
  
![banner](imgs/Modulo_HTML.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Carregar arquivo HTML
  
Carregar dados de um arquivo HTML na memória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo HTML|Link the HTML file to the corresponding path|C:/Users/usuario/Desktop/archivo.html|
|HTML como texto|Connect the HTML code passed as text, without having to create the file|<!DOCTYPE html>
<html lang="pr">
<head>
	 <meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title></title>
</head>|
|Codificação|Encoding with which the HTML file is required to be opened. By default it is UTF-8|utf-8|
|Atribuir resultado à variável|Variable where the result of Load HTML is stored|var|
|ID Sessão|Optional ID to identify open sessions|s1|

### Inserir Tag
  
Inserir um tag no HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão|ID of the open file to which you want to add the tag, in the case of having multiple open sessions|s1|
|Nome do tag|Name of the HTML tag to create the element|div|
|Texto do Tag|Text of the HTML Element to create with the tag|Oi Mundo|
|Atributo do Tag|HTML Attribute name for the tag to create. Optional.|class|
|Valor do atributo|HTML attribute value for the tag to create. Optional.|minhaclasse|
|Local de inserção|Css selector or Xpath where the tag insertion will be made|body > p|
|Atribuir resultado à variável|Variable where the result of Insert Tag is stored|var|

### Lista para tabela HTML
  
Converter uma lista em uma tabela no formato HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Lista|List to be converted to an HTML format table|[['s1', 's2', 's3'], ['t1', 't2', 't3']]|
|Atribuir resultado à variável|Variable where the converted HTML table is stored|var|

### Tabela HTML para Lista
  
Converter uma tabela de formato HTML em uma lista
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tabela|HTML format table to be converted to a List|<table>
<tr>
	<td>1</td>
	<td>Joana</td>
</tr>
<tr>
	<td>2</td>
	<td>João</td>
</tr>
</table>|
|Atribuir resultado à variável|Variable where the converted list is stored|var|

### Salvar arquivo
  
Salvar dados em um arquivo HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo HTML|Path where the uploaded HTML file will be saved|C:/Users/usuario/Desktop/archivo.html|
|Codificação|Encoding with which to save the uploaded HTML file|UTF-8|
|Atribuir resultado à variável|Variable where the result of Save HTML is stored|var|
|ID Sessão|ID to identify the file to save in case of having multiple sessions|s1|

### Extrair dado
  
Extrair dados de um arquivo HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dados a serem extraídos do arquivo HTML|Dados a serem extraídos do arquivo HTML|{'nome': 'Nombre:','link_pdf': 'Pdf_geral:'}|
|HTML|Código HTML|HTML|
|Atribuir resultado à variável|Variável que guarda o resultado|var|

### Terminar Sessão
  
Remove uma sessão HTML e libera memória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão|ID to identify the file to close in case of having multiple sessions|s1|
|Atribuir resultado à variável|Variable where the result of End Session is stored|var|
