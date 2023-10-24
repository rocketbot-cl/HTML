from bs4 import BeautifulSoup


class HTML:
    
    def __init__(self, path:str=None, code:str=None):
        self.path = path
        self.code = code
        self._html = None
        
    def open_html(self, encoding='utf-8'):
            
        if not self.path:
            raise FileNotFoundError('HTML File Missing')
            
        with open(self.path, encoding=encoding) as f:
            
            self.code = f.read()
            
            self._html = BeautifulSoup(self.code, 'html.parser')

    def add_tag(self, tag, tag_text, attr, attr_text, css=None):        
            
        if not tag:
            raise Exception('Tag name undefined')
        
        if self._html is None:
            raise FileNotFoundError('HTML file is not open')
        
        new_tag = self._html.new_tag(tag) #crea la nueva etiqueta
        new_tag.string = tag_text #setea la leyenda de la etiqueta
        new_tag[attr]=attr_text #setea el atributo

        if css: #si se proporciona la ubicacion
            
            location = self._html.select(css) #busca el elemento xpath
            print(location)
            location = location[0]
            print(location)
    
            location.append(new_tag)            

        else: #sino, lo agrega al final
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


# html = HTML(r'C:\Users\pc\Desktop\readHTML\contacto.html')
# html.open_html()
# print(html.to_string())
# html.add_tag('div', 'Hola3','class', 'new_class3', css='body > p')
# print(html.to_string())  
# html.save_html(path_save='listas.html')


