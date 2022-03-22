Pyodita (Building)
==================
"Este es Pyodita mi libreria de ejercicios de python 😊"

There are a variety of metadata and options supported here. This is in configparser format; do not place quotes around values. This example package uses a relatively minimal set of metadata:

- `name` is the distribution name of your package. This can be any name as long as it only contains letters, numbers, _ , and -. It also must not already be taken on pypi.org. Be sure to update this with your username, as this ensures you won’t try to upload a package with the same name as one which already exists.

- `version` is the package version. See PEP 440 for more details on versions. You can use file: or attr: directives to read from a file or package attribute.

- `author` and `author_email` are used to identify the author of the package.

- `description` is a short, one-sentence summary of the package.

- `long_description` is a detailed description of the package. This is shown on the package detail page on the Python Package Index. In this case, the long description is loaded from README.md (which is a common pattern) using the file: directive.

- `long_description_content_type` tells the index what type of markup is used for the long description. In this case, it’s Markdown.

- `url` is the URL for the homepage of the project. For many projects, this will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting service.

- `project_urls` lets you list any number of extra links to show on PyPI. Generally this could be to documentation, issue trackers, etc.

- `classifiers` gives the index and pip some additional metadata about your package. In this case, the package is only compatible with Python 3, is licensed under the MIT license, and is OS-independent. You should always include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on. For a complete list of classifiers, see https://pypi.org/classifiers/.
- `include_package_data`

Docs
===

```
$$ sphinx-quickstart
Bienvenido a la utilidad de inicio rápido de Sphinx 4.4.0.

Ingrese los valores para las siguientes configuraciones (solo presione Entrar para
aceptar un valor predeterminado, si se da uno entre paréntesis).

Ruta raíz seleccionada: .

Tiene dos opciones para colocar el directorio de compilación para la salida de Sphinx.
O usas un directorio "_build" dentro de la ruta raíz, o separas
directorios "fuente" y "compilación" dentro de la ruta raíz.
> Separar directorios fuente y compilado (y/n) [n]: y

El nombre del proyecto aparecerá en varios lugares en la documentación construida.
> Nombre de proyecto: Pyodita
> Autor(es): Ferreira Juan David
> Liberación del proyecto []: 0.0.1

Si los documentos deben escribirse en un idioma que no sea inglés,
puede seleccionar un idioma aquí por su código de idioma. Sphinx entonces
traducir el texto que genera a ese idioma.

Para obtener una lista de códigos compatibles, vea
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Lenguaje del proyecto [en]: en

Creando archivo /home/juniordavid/Escritorio/Mentorias/pycellid/docs/source/conf.py.
Creando archivo /home/juniordavid/Escritorio/Mentorias/pycellid/docs/source/index.rst.
Creando archivo /home/juniordavid/Escritorio/Mentorias/pycellid/docs/Makefile.
Creando archivo /home/juniordavid/Escritorio/Mentorias/pycellid/docs/make.bat.

Terminado: se ha creado una estructura de directorio inicial.

Ahora debe completar su archivo maestro /home/juniordavid/Escritorio/Mentorias/pycellid/docs/source/index.rst y crear otros archivos fuente
de documentación.Use el archivo Makefile para compilar los documentos, así ejecute el comando:
    make builder
donde "builder" es uno de los constructores compatibles, por ejemplo, html, latex o linkcheck.

$$
```