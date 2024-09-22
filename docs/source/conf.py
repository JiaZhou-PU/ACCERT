# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
import subprocess



# -- Project information -----------------------------------------------------

project = 'ACCERT'
copyright = '© 2023 UChicago Argonne, LLC'
author = 'Argonne National Laboratory'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',  
    'sphinx_design',
    'nbsphinx', 
    'myst_parser', 
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'private-members': False,
    'special-members': '__init__',
    'inherited-members': True,
    'show-inheritance': True,
}

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'  

# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css',]


# -- Custom Functions and Setup ----------------------------------------------

def run_generate_sp_docs(app):
    """
    Runs the generate_sp_docs.py script to generate documentation for stored procedures.
    """
    # Determine the path to the script relative to conf.py
    script_dir = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(script_dir, 'generate_sp_docs.py')
    
    # Check if the script exists
    if not os.path.exists(script_path):
        app.warn(f"Documentation script not found at {script_path}")
        return
    
    # Run the script using the same Python interpreter as Sphinx
    try:
        subprocess.check_call([sys.executable, script_path])
        print("Successfully ran generate_sp_docs.py")
    except subprocess.CalledProcessError as e:
        app.warn(f"Error running generate_sp_docs.py: {e}")

def setup(app):
    app.connect('builder-inited', run_generate_sp_docs)