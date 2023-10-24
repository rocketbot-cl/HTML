



# HTML
  
Módulo para abrir arquivos HTML e extrair ou adicionar informações   

 
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
|HTML como texto|Connect the HTML code passed as text, without having to create the file|`<!DOCTYPE html><html lang="pr"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title></title></head>`|
|Codificação|Encoding with which the HTML file is required to be opened. By default it is UTF-8|UTF-8|
|Atribuir resultado à variável|Variable where the result of Load HTML is stored|var|
|ID Sessão|Optional ID to identify open sessions|s1|

### Inserir Tag
  
Inserir um tag no HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão|ID of the open file to which you want to add the tag, in the case of having multiple open sessions|s1|
|Nome do tag|Name of the HTML tag to create the element|div|
|Texto do Tag|Text of the HTML Element to create with the tag|Oi Mundo|
|Atributo do Tag|HTML Attribute name for the tag to create|class|
|Texto do Atributo|HTML Attribute for the tag to create|minhaclasse|
|Local de inserção|Css selector or Xpath where the tag insertion will be made|body > p|
|Atribuir resultado à variável|Variable where the result of Insert Tag is stored|var|

### Salvar arquivo
  
Salvar dados em um arquivo HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo HTML|Path where the uploaded HTML file will be saved|C:/Users/usuario/Desktop/archivo.html|
|Codificação|Encoding with which to save the uploaded HTML file|UTF-8|
|Atribuir resultado à variável|Variable where the result of Save HTML is stored|var|
|ID Sessão|ID to identify the file to save in case of having multiple sessions|s1|

### Terminar Sessão
  
Remove uma sessão HTML e libera memória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão|ID to identify the file to close in case of having multiple sessions|s1|
|Atribuir resultado à variável|Variable where the result of End Session is stored|var|