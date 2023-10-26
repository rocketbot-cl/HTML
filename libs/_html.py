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



