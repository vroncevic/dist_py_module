# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = u'dist_py_module'
copyright = u'2017, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'v2.4.8'
release = u'https://github.com/vroncevic/dist_py_module/releases'
extensions = ['sphinx.ext.viewcode', 'sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'dist_py_moduledoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'dist_py_module.tex', u'dist\\_py\\_module Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'dist_py_module', u'dist_py_module Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'dist_py_module', u'dist_py_module Documentation',
    author, 'dist_py_module', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
