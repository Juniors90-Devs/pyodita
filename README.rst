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