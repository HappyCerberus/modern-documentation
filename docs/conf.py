# Basic configuration
project = 'ModernDoc'
copyright = '2023, Šimon Tóth'
author = 'Šimon Tóth'

# Extensions to use
extensions = [ "breathe", "exhale" ]

# Configuration for the breathe extension
# Which directory to read the Doxygen output from
breathe_projects = {"ModernDoc":"xml"}
breathe_default_project = "ModernDoc"

# Configuration for the exhale extensions
exhale_args = {
    "containmentFolder": "./api",
    "doxygenStripFromPath": "../src",
    "rootFileName": "library_root.rst",
    "rootFileTitle": "Library API",
}

# Configuration for the theme
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/HappyCerberus/modern-documentation",
    "use_repository_button": True,
}