import requests
from string import Template

html_template = Template('''
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>aves</title>
</head>
<body>
 $body   
</body>
</html>                       
''') 
elem_template = Template(''' <h2>$nombre_espanol</h2>
                             <h3>$nombre_ingles</h3>
                             <img src="$url" alt="">
                          ''')


def requests_get(url):
    return requests.get(url).json()

def build_html(url):
    response = requests_get(url)
    texto = ''

    for ave in response:
        nombre_espanol = ave['name']['spanish']
        nombre_ingles = ave['name']['english']
        imagen_url = ave['images']['main']
        texto += elem_template.substitute(nombre_espanol=nombre_espanol, 
                                  nombre_ingles=nombre_ingles,  
                                  url=imagen_url)
    return html_template.substitute(body=texto)
    
html = build_html('https://aves.ninjas.cl/api/birds')
with open('aves.html','w') as f:
    f.write(html)
