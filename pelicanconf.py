AUTHOR = 'Omar Kamal Hosney'
SITENAME = 'Simply'
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
DISQUS_SITENAME = 'http-omkamal-github-io-simply'


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'sitemap','asciidoc_reader','plantuml']
ASCIIDOC_CMD = 'asciidoctor'

# Blogroll
LINKS = (('Home', 'https://omkamal.github.io/simply'),
         ('Blog Author','https://omkamal.github.io/simply/pages/blog-author.html'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/omarebnelkhattab-hosney-9a931b3'),
          ('twitter', 'https://twitter.com/omkamal'),)

DEFAULT_PAGINATION = 4


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
FILENAME_METADATA = '(?P<title>.*)'
DISPLAY_PAGES_ON_MENU = False

#STATIC_PATHS
#PAGE_PATHS
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
#STATIC_SAVE_AS
# Example
STATIC_PATHS = ['images', 'extra']
# pelicanconf.py
RELATIVE_URLS = True
