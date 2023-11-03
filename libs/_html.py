from bs4 import BeautifulSoup


class HTML:
    
    def __init__(self, path:str=None, code:str=None):
        self.path = path
        self.code = code
        self._html = None
        
    def open_html(self, encoding='utf-8'):
            
        if self.path:

            with open(self.path, encoding=encoding) as f:
                self.code = f.read()
            
        self._html = BeautifulSoup(self.code, 'html.parser')


    def add_tag(self, tag, tag_text, attr:str=None, attr_text:str=None, css=None):        
            
        if not tag:
            raise Exception('Tag name undefined')
        
        new_tag = self._html.new_tag(tag)
        new_tag.string = tag_text 

        if attr and attr_text:
            new_tag[attr]=attr_text

        if css:
            
            location = self._html.select(css) 
            location = location[0]
            print(location)
    
            location.append(new_tag)            

        else:
            self._html.append(new_tag)
       
        
    def save_html(self, path_save=None, decode='utf-8'):
        
        if self._html is None:
            raise FileNotFoundError('The HTML file is not open')

        if path_save is None:
            path_save = self.path
                
        with open(path_save, 'w', encoding=decode) as saved_html:
            
            saved_html.write(self.to_string(decode))
        print('Successfully Saved')    
        

    def to_string(self, decode='utf-8'):
        return self._html.prettify(decode).decode(decode)

    def list_to_table(list):

        table = "<table>\n"
        for row in list:
            table += "<tr>"
            for item in row:
                table += "<td>{}</td>".format(item)
            table += "</tr>\n"
        table += "</table>"
        return table

    def table_to_list(html_table):
    
        soup = BeautifulSoup(html_table, 'html.parser') #crea el objeto bs para analizar la tabla html
        table = soup.find('table') #encuentra la primer tabla
        rows = table.find_all('tr') #encuentra las filas de la tabla
        
        data = [] #inicializa data para almacenar los datos de la tabla

        for row in rows: #itera por cada fila y por cada celda de esa fila de la tabla
            cells = row.find_all('td') #guarda los datos de una fila
            row_data = [cell.get_text() for cell in cells] #extrae el texto de cada celda y crea una lista de datos  
            data.append(row_data) #esa lista de datos se añade a data

        return data



# Ejemplo de uso table_to_list()
# html_table = """
# <table>
#     <tr>
#         <td>1</td>
#         <td>John</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>Jane</td>
#     </tr>
# </table>
# """

# list_result = HTML.table_to_list(html_table)
# print(list_result)

# modo de uso list_to_table:
# my_list = [['s1', 's2', 's3'], ['t1', 't2', 't3'], ['u1', 'u2', 'u3']]
# html_table = HTML.list_to_table(list=my_list)
# print(html_table)

# Primeras funciones
# html = HTML(r'C:\Users\pc\Desktop\readHTML\contacto.html')
# html.open_html()
# print(html.to_string())
# html.add_tag('div', 'Hola3','class', 'new_class3', css='body > p')
# print(html.to_string())  
# html.save_html(path_save='listas.html')

