



# HTML
  
Módulo para abrir arquivos HTML e extrair ou adicionar informações   

*Read this in other languages: [English](Manual_HTML.md), [Português](Manual_HTML.pr.md), [Español](Manual_HTML.es.md)*
  
![banner](imgs/Banner_HTML.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Carregar arquivo HTML
  
Carregar dados de um arquivo HTML na memória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo HTML||C:/Users/usuario/Desktop/archivo.html|
|HTML como texto||<!DOCTYPE html>
<html lang="pr">
<head>
	 <meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title></title>
</head>|
|Codificação||utf-8|
|Atribuir resultado à variável||Variável|
|ID Sessão||Default|

### Inserir Tag
  
Inserir um tag no HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão||Default|
|Nome do tag||Nome|
|Texto do Tag||Texto|
|Atributo do Tag||Atributo|
|Texto do Atributo||Texto do Atributo|
|Local de inserção||body > p|
|Atribuir resultado à variável||Variável|

### Salvar arquivo
  
Salvar dados em um arquivo HTML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo HTML||C:/Users/usuario/Desktop/archivo.html|
|Codificação||utf-8|
|Atribuir resultado à variável||Variável|
|ID Sessão||Default|

### Terminar Sessão
  
Remove uma sessão HTML e libera memória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão||Default|
|Atribuir resultado à variável||Variável|
