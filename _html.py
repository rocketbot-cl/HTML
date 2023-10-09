import os
from lxml import etree

class HTML:
    
    def __init__(self, path:str=None, code:str=None):
        self.path = path
        self.code = code
        self._html = None
        
    def open_html(self, encoding='utf-8'):
            
        if not self.path:
            raise FileNotFoundError('Html File Missing')
            
        with open(self.path, encoding=encoding) as f:
            self.code = f.read()
            self._html = etree.HTML(self.code)

    def add_tag(self, tag, tag_text, attr, attr_text, xpath=None):
            
            
        if not tag:
            raise Exception('Tag name undefined')
        
        if self._html is None:
            raise FileNotFoundError('The HTML file is not open')
        
        new_tag = etree.Element(tag) #crea la nueva etiqueta
        new_tag.text = tag_text
        new_tag.set(attr, attr_text) #setea el atributo

        if xpath: #si se proporciona la ubicacion
            
            location = self._html.xpath(xpath) #busca el elemento xpath
            location.append(new_tag) #agrega la nueva etiqueta

        else: #sino, lo agrega al final
            self._html.append(new_tag)
       
        
    def save_html(self, path_save=None, decode='utf-8'):

        if self._html is None:
            raise FileNotFoundError('The HTML file is not open')

        try:

            if path_save is None:
                path_save = self.path
                
            with open(path_save) as saved_html:
                saved_html.write(self.to_string(decode))
                    
        except Exception as e:
            print('Error')


    def to_string(self, decode='utf-8'):
        return etree.tostring(self._html, encoding=decode).decode(decode)


    


    
            
