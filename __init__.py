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

        mod_html_sessions[session]={'path': path}
        
        try:
            if path: #Si pasan un path
                with open(path, encoding=encoding) as f:
                    html = f.read()
            else:
                    html = html_

            mod_html_sessions[session]['data'] = BeautifulSoup(html, 'html.parser')

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
        if not session:
            session = SESSION_DEFAULT
        if session in mod_html_sessions:
            del mod_html_sessions[session]
            if session == SESSION_DEFAULT:
                mod_html_sessions[SESSION_DEFAULT] = {}
        else:
            raise Exception("The session you want to delete does not exist")
    
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

        if not 'data' in mod_html_sessions[session]:
            # Remember set session
            raise Exception('The session no exists')
        
        global xpath_to_css

        def xpath_to_css(xpath):
            if not xpath:
                    raise Exception('Xpath undefined')

            css_parts = []
            parts = xpath.split("/")

            for part in parts:
                
                if not part or part == "":
                    continue

                # Selector de id
                if "@id=" in part:
                    id_name = part.split('="')[1].split('"')[0]
                    css_parts.append(f"#{id_name}")

                # Selector de clase
                elif "contains(@class," in part:
                    class_name = part.split('="')[1].split('"')[0]
                    css_parts.append(f".{class_name}")

                # Selector de nth-child
                elif "[" in part and "]" in part:
                    tag_name, child_num = part.split("[")
                    child_num = child_num.strip("]")
                    css_parts.append(f"{tag_name}:nth-child({child_num})")

                # Selector de tag
                else:
                    css_parts.append(part)

            # Unir las partes para formar el selector CSS completo
            css = " > ".join(css_parts)
            print(css)
            return css

        # Verifica si el selector es un XPath
        if css.startswith('//') or css.startswith('/'):
            # si lo es, lo convierte a CSS selector
            css = xpath_to_css(css)

        new_tag = mod_html_sessions[session]['data'].new_tag(tag) #crea la nueva etiqueta
        new_tag.string = tag_text #setea la leyenda de la etiqueta
        new_tag[attr]=attr_text #setea el atributo

        try:
            if css: #si se proporciona la ubicacion
            
                location = mod_html_sessions[session]['data'].select(css)
                location = location[0]
                location.append(new_tag)            

            else: #sino, lo agrega al final
                mod_html_sessions[session]['data'].append(new_tag)
            
        except Exception as e:
            PrintException()
            res = False
            raise e
              
        if var_:
            res = mod_html_sessions[session]['data'].prettify('utf-8').decode('utf-8')
            SetVar(var_, res)

    if module == 'savehtml':
        path_save = GetParams('pathSave')
        var_ = GetParams('result')
        session = GetParams('session')
        decode = GetParams('decode')

        if not session:
            session = SESSION_DEFAULT
        
        res = True
        
        try:
            if path_save is None:
                path_save = path  
                
            with open(path_save, 'w', encoding=decode) as saved_html:
              saved_html.write(mod_html_sessions[session]['data'].prettify(decode).decode(decode))    

        except Exception as e:
            PrintException()
            res= False
            raise e
        
        if var_:
            SetVar(var_, res)

   
except Exception as e:
    PrintException()
    raise e
