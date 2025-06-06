# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'picoDAQ'
copyright = '2025, Daniel A. Wagenaar'
author = 'Daniel A. Wagenaar'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

######################################################################
html_theme_options = {
    'logo': 'logo.png',
    'description': 'Data acquisition, but easy',
    'show_powered_by': False,
    }

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchfield.html', # searchbox.html
        #'relations.html',
        #'donate.html',
    ]
}

html_show_sourcelink = False
html_show_sphinx = False

autodoc_type_aliases = {
    'Iterable': 'Iterable',
    'List': 'List',
    'ArrayLike': 'ArrayLike',
    'Pulse': 'Pulse',
    'Time': 'Time',
    'Voltage': 'Voltage',
    'Deltas': 'Deltas',
}
autodoc_member_order = 'alphabetical'

