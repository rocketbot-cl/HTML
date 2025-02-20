# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import os

base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'HTML', 'libs')

if cur_path not in sys.path:
        sys.path.append(cur_path)

from _html import HTML


# Globals declared here.
global mod_html_sessions
# Defaults declared here.
SESSION_DEFAULT = "default"
# Initialize settings for the module here.

try:
    if not mod_html_sessions :
        mod_html_sessions = {SESSION_DEFAULT:{}}
except NameError:
    mod_html_sessions = {SESSION_DEFAULT:{}}


"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")



try:

    if module == "htmlsession":
        """ 
        HTML Session: Open session, read html from file or text
        """
        path = GetParams('path')
        var_ = GetParams('result')
        session = GetParams('session')
        html_ = GetParams('html')
        encoding = GetParams('encoding')
        res = True

        if not session:
            session = SESSION_DEFAULT
        if not encoding:
            encoding = "utf-8"

        try:
            if path:   
                html = HTML(path)
            
            else:
                html = HTML(code=html_)

            html.open_html()
            mod_html_sessions[session]={'path': path, 'html': html}
            
        except Exception as e:
            PrintException()
            res = False
            raise e
        
        if var_:
            SetVar(var_, res)

    if module == "htmlsessionend":
        """
        HTML Session end: Remove from sessions a HTML
        """
        session = GetParams('session')
        var_ = GetParams('result')

        res = True
        
        try:
            if not session:
                session = SESSION_DEFAULT
            if session in mod_html_sessions:
                del mod_html_sessions[session]
                if session == SESSION_DEFAULT:
                    mod_html_sessions[SESSION_DEFAULT] = {}
            else:
                raise Exception("The session you want to delete does not exist")
        except Exception as e:
            PrintException()
            res = False
            raise e
        
        if var_:
            SetVar(var_, res)

    if module == "addTag":
        """
        HTML Insert Tag: add new tag to HTML
        """
        var_ = GetParams('result')
        tag = GetParams('tagName')
        tag_text = GetParams('tagText')
        attr = GetParams('attrName')
        attr_text = GetParams('attrText')
        session = GetParams('session')
        css = GetParams('css')
        res = None

        if not tag:
            raise Exception('Tag name undefined')
        
        # Set Default session
        if not session:
            session = SESSION_DEFAULT

        if not 'html' in mod_html_sessions[session]:
            # Remember set session
            raise Exception('The session no exists')
        
        try:

            html = mod_html_sessions[session]['html']
            
            html.add_tag(tag, tag_text, attr, attr_text, css)
            

            res = html.to_string()

        except Exception as e:
            PrintException()
            raise e

        if var_:
            SetVar(var_, res)

    if module == "listToTable":
        """
        List to HTML Table: convert a list to a HTML format table
        """
        var_ = GetParams('result')
        list = GetParams('list')
        res = None
        
        try:
            list = eval(list)
            html_table = HTML.list_to_table(list)
            
        except Exception as e:
            PrintException()
            raise e
        
        if var_:
            res = html_table
            SetVar(var_, res)

    if module == "tableToList":
        """
        HTML Table to List: convert a HTML format table to a list
        """
        var_ = GetParams('result')
        table = GetParams('table')
        res = None
        
        try:
            
            html_list = HTML.table_to_list(table)
            
        except Exception as e:
            PrintException()
            raise e
        
        if var_:
            res = html_list
            SetVar(var_, res)

    if module == 'savehtml':
        path_save = GetParams('pathSave')
        var_ = GetParams('result')
        session = GetParams('session')
        decode = GetParams('decode')

        if not session:
            session = SESSION_DEFAULT
        
        if not decode:
            decode = 'utf-8'

        res = True
        
        try:
            html = mod_html_sessions[session]['html']
            html.save_html(path_save, decode)
            
        except Exception as e:
            PrintException()
            res= False
            raise e
        
        if var_:
            SetVar(var_, res)

    if module == 'extractData':
        html = GetParams('html')
        var_ = GetParams('result')
        queries = GetParams('queries')

        if queries:
            queries = eval(queries)
        
        try:
            soup = BeautifulSoup(html, 'html.parser')
            results = {}

            for key, pattern in queries.items():
                def find_with_pattern(t, pattern=pattern):
                    return t and pattern in t

                match = soup.find(text=find_with_pattern) 
                if match:
                    results[key] = match.split(":")[1].strip("; ").replace("\\xa0", " ")
                else:
                    results[key] = None

            for key, pattern in queries.items():
                if key.startswith('link_'):
                    def find_pattern(t, pattern=pattern):
                        return pattern in t 

                    elements = soup.find_all(text=find_pattern) 

                    for element in elements:
                        link = element.find_next('a')
                        if link:
                            results[key] = link['href']
                            break
                    
            SetVar(var_, results)
            
        except Exception as e:
            PrintException()
            raise e

except Exception as e:
    PrintException()
    raise e

