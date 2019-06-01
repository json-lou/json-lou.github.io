#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jayson Lou'
SITENAME = "Jayson's Portfolio"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = '/Users/jayson.lou/Documents/json-lou/themes/pelican-themes/clean-blog'

COLOR_SCHEME_CSS = 'github.css'

EMAIL_URL = 'mailto:jayson.lou@gmail.com'
LINKEDIN_URL = 'https://www.linkedin.com/in/jaysonlou/'
GITHUB_URL = 'https://github.com/json-lou'
