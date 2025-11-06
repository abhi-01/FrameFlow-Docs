# Configuration file for the Sphinx documentation builder.
project = "Frame Flow"
author = "Abhishek Kumar"
copyright = "2025, Abhishek Kumar"
release = "1.0 Official"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.viewcode", "sphinx.ext.githubpages"]
templates_path = ["_templates"]
exclude_patterns = []
html_theme = "classic"
html_static_path = ["_static"]
html_context = {"display_github": True, "github_user": "abhi-01", "github_repo": "FrameFlow-Docs", "github_version": "main", "conf_py_path": "/docs/"}
autodoc_default_options = {"members": True, "undoc-members": True, "show-inheritance": True}
