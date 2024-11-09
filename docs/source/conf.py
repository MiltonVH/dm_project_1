# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DM Project One'
copyright = '2024, Milton Vásquez'
author = 'Milton Vásquez'
release = '1.0.0'

master_doc = 'index'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

extensions = [
    'myst_parser',  # extensión para poder usar MyST y  MARKDONW
    'sphinx_design',
    #'sphinx_rtd_theme', #  configuración rtd_theme
    # 'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.todo',
    # 'sphinx.ext.mathjax',
    #'sphinx.ext.napoleon',
    # 'sphinx.ext.autosummary', # solamente si se la quiere usar
     'sphinx.ext.viewcode',
    'sphinx_copybutton',
    "sphinx.ext.githubpages",
]

# MyST configuration ----------------------------------------------------------

myst_enable_extensions = [
#     "amsmath",
    "colon_fence",
    "deflist",
#     "dollarmath",
    "fieldlist",
#     "html_admonition",
#     "html_image",
#     "replacements",
#     "smartquotes",
     "substitution",
#     "tasklist",
]

#myst_heading_anchors = 2

#panels_add_bootstrap_css = False


templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# html_css_files = [
#     'css/custom.css',
# ]


html_theme_options = {
    # 'home_page_in_toc': True,
    'use_download_button': True,
    #"repository_url": "https://github.com/MiltonVH",
    "use_repository_button": True,
    # "use_edit_page_button": True,
    # "use_fullscreen_button": True,
    'collapse_navigation': True,
    #'sticky_navigation': True,
    "show_navbar_depth": 2,
    # 'titles_only': False,
    "show_toc_level": 2
}


html_title = ''
html_logo = '_static/img/logo.png'
# show_navbar_depth = 2
html_copy_source = True
html_sourcelink_suffix = ""


# html_sidebars = {
#     "**": ["sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
# }

# html_sidebars = {
#     "posts/*": ["sbt-sidebar-footer.html"]
# }

# Configuración para rtd_theme________________________________________________
numfig = True
numfig_format = {'figure': 'Fig. %s.', 'table': 'Tabla %s.',
                 'code-block': 'Código %s', 'section': 'Sección %s.'}
numfig_secnum_depth = 1
math_numfig = True
math_eqref_format = 'Ec. {number}'


# -- Options for LATEX output -------------------------------------------------


latex_engine = 'pdflatex'
latex_documents = [
    (master_doc, 'proyecto.tex', project,
     author, 'manual'),
]

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',
    'releasename': " ",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align': 'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '11pt',
}

# Para incluir tabla de contenido en el alateral -----------------------------
# ** parece que lo hace automaticamente el tema de sphinx*

# html_sidebars = {'**': ['globaltoc.html', 'relations.html',
#                         'sourcelink.html', 'searchbox.html'], }


#-----------------------------------------------------------------------------