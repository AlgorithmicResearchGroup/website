#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Algorithmic Research Group'
SITENAME = 'Algorithmic Research Group'
SITEDESCRIPTION = 'Algorithmic Research Group — open infrastructure for AI security research.'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = 'themes/custom'

# Blogroll
LINKS = (
    ('GitHub', 'https://github.com/AlgorithmicResearchGroup'),
    ('HuggingFace', 'https://huggingface.co/AlgorithmicResearchGroup'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static paths
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Page paths
PAGE_PATHS = ['pages']

# Article paths
ARTICLE_PATHS = ['blog', 'projects']
USE_FOLDER_AS_CATEGORY = True

# Custom settings
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Direct templates
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'blog', 'projects', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
PAGINATED_TEMPLATES = {
    'blog': None,
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
}

# URL settings — articles route by category
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORIES_URL = 'categories.html'
CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'

# Blog page
BLOG_SAVE_AS = 'blog/index.html'

# Projects page
PROJECTS_SAVE_AS = 'projects.html'

# Current year for footer
import datetime
CURRENT_YEAR = datetime.datetime.now().year
