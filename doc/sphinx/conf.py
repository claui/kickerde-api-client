# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pylint: skip-file
# type: ignore

project = 'API client for kicker.de'
executable_name = 'kickerde-api-client'
author = 'Claudia Pellegrino <clau@tiqua.de>'
description = (
    'Unofficial Python bindings for the public kicker.de news API'
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'autoapi.extension',
]

autoapi_dirs = ['../../kickerde_api_client']
autoapi_keep_files = True
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
    'imported-members',
]
autoapi_type = 'python'
autodoc_typehints = 'description'

html_theme = 'sphinx_rtd_theme'


def skip_module(app, what, name, obj, skip, options):
    if what != 'module':
        return skip
    if name in [
        'kickerde_api_client.version',
        'kickerde_api_client.settings',
    ]:
        return True
    return skip


def setup(sphinx):
    sphinx.connect('autoapi-skip-member', skip_module)


templates_path = []
exclude_patterns = [
    '**/kickerde_api_client/version/**',
    '**/kickerde_api_client/settings/**',
]
