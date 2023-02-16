# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ModernDoc'
copyright = '2023, Šimon Tóth'
author = 'Šimon Tóth'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ "breathe", "exhale" ]
breathe_projects = {"ModernDoc":"xml"}
breathe_default_project = "ModernDoc"

exhale_args = {
    "containmentFolder": "./api",
    "rootFileName": "library_root.rst",
    "doxygenStripFromPath": "../src",
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/HappyCerberus/modern-documentation",
    "use_repository_button": True,
}