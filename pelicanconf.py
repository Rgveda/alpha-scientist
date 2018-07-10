#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chad Gray, CFA'
SITENAME = 'The Alpha Scientist'
SITEURL = 'https://alphascientist.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

LOCALE = ('usa', 'jpn',      # On Windows
           'en_US', 'ja_JP'   # On Unix/Linux
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'), )

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/chadgraycfa/'),
          ('Twitter', 'https://twitter.com/data2alpha'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

OUTPUT_PATH = 'docs/'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

STATIC_PATHS = ['images']

THEME = 'themes/octopress'
SITEIMAGE = '/images/profile.jpg width=400 height=250'
SITESUBTITLE = 'Generating stock market alpha using data science'

HIDE_AUTHORS = True

DISQUS_SITENAME = 'alphascientist-com'

DISPLAY_PAGES_ON_MENU = True

FACEBOOK_LIKE = True
TWITTER_USER = 'data2alpha'
