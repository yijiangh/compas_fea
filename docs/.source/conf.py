# -*- coding: utf-8 -*-

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

import sphinx_compas_theme

# -- General configuration ------------------------------------------------

templates_path   = ['_templates', ]
source_suffix    = ['.rst', ]
master_doc       = 'index'
project          = 'COMPAS'
copyright        = '2017, Block Research Group - ETH Zurich'
author           = 'Andrew Liew, Tomas Mendez, Tom Van Mele'
version          = '0.1'
release          = '0.1.0'
language         = None
exclude_patterns = []
pygments_style   = 'sphinx'
show_authors     = True
add_module_names = True


# -- Extension configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'matplotlib.sphinxext.plot_directive',
]

# autodoc options

autodoc_default_flags = [
    'undoc-members',
    'private-members',
    'special-members',
    'show-inheritance',
]

autodoc_member_order = 'alphabetical'

# autosummary options

autosummary_generate = True

# napoleon options

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = False
napoleon_use_rtype = False

# plot options

# plot_include_source
# plot_pre_code
# plot_basedir
# plot_formats
# plot_rcparams
# plot_apply_rcparams
# plot_working_directory
# plot_template

plot_html_show_source_link = False
plot_html_show_formats = False

# intersphinx options

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'compas': ('https://compas-dev.github.io/main', 'https://compas-dev.github.io/main/objects.inv'),
}


# -- Options for HTML output ----------------------------------------------

html_theme = 'compaspkg'
html_theme_path = sphinx_compas_theme.get_html_theme_path()
html_theme_options = {}
html_context = {}
html_static_path = ['_static']
html_last_updated_fmt = ''
html_copy_source = False
html_show_sourcelink = False
html_add_permalinks = ''
html_experimental_html5_writer = True
html_compact_lists = True
