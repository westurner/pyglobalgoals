
# coding: utf-8

# # globalgoals-pyglobalgoals.py.ipynb
# 
# A jupyter notebook demonstrating HTML parsing, JSON-LD, RDFa, and schema.org in order to add Schema.org RDFa markup to @TheGlobalGoals for Sustainable Development at http://www.globalgoals.org/

# ## Background
# 
# * Homepage: **http://www.globalgoals.org/**
# - Twitter: https://twitter.com/TheGlobalGoals
# - Twitter: https://twitter.com/GlobalGoalsUN
# - Instagram: https://instagram.com/TheGlobalGoals/
# - Facebook: https://www.facebook.com/globalgoals.org
# - YouTube: https://www.youtube.com/channel/UCRfuAYy7MesZmgOi1Ezy0ng/
# - Hashtag: **#GlobalGoals**
#   - https://twitter.com/hashtag/GlobalGoals
#   - https://instagram.com/explore/tags/GlobalGoals/
#   - https://www.facebook.com/hashtag/GlobalGoals
# - Hashtag: #TheGlobalGoals
#   - https://twitter.com/hashtag/TheGlobalGoals
#   - https://instagram.com/explore/tags/TheGlobalGoals/
#   - https://www.facebook.com/hashtag/TheGlobalGoals
# - Hashtag: #Goal17
#   - https://twitter.com/hashtag/Goal17
#   - https://instagram.com/explore/tags/Goal17/
#   - https://www.facebook.com/hashtag/Goal17
# - Hashtag: #GlobalGoal17
#   - https://twitter.com/hashtag/GlobalGoal17
#   - https://instagram.com/explore/tags/GlobalGoal17/
#   - https://www.facebook.com/hashtag/GlobalGoal17
# - Hashtag: #GG17
#   - https://twitter.com/hashtag/GG17
#   - https://instagram.com/explore/tags/GG17/
#   - https://www.facebook.com/hashtag/GG17
# 
# 
# ### pyglobalgoals
# 
# * Homepage: https://github.com/westurner/pyglobalgoals
# * Src: https://github.com/westurner/pyglobalgoals
# * Download: https://github.com/westurner/pyglobalgoals/releases
# 
# ### Objectives
# 
# * [x] ENH: Read and parse TheGlobalGoals from globalgoals.org
# * [x] ENH: Download (HTTP GET) each GlobalGoal tile image to ``./notebooks/data/images/``
# * [-] ENH: Generate e.g. tweets for each GlobalGoal (e.g. **##gg17** / **##GG17**)
# * [x] ENH: Save TheGlobalGoals to a JSON-LD document
# * [-] ENH: Save TheGlobalGoals with Schema.org RDF vocabulary (as JSON-LD)
# * [-] ENH: Save TheGlobalGoals as ReStructuredText with headings and images
# * [-] ENH: Save TheGlobalGoals as Markdown with headings and images
# * [-] ENH: Save TheGlobalGoals as RDFa with headings and images
# * [ ] ENH: Save TheGlobalGoals as RDFa with images like http://globalgoals.org/
# * [-] DOC: Add narrative documentation where necessary
# * [-] REF: Refactor and extract methods from ``./notebooks/`` to ``./pyglobalgoals/``
#   
# ## Implementation
# 
# * Python package: [**pyglobalgoals**](#pyglobalgoals)
# 
# * Jupyter notebook: **``./notebooks/globalgoals-pyglobalgoals.py.ipynb``**
#   * Src: https://github.com/westurner/pyglobalgoals/blob/master/notebooks/globalgoals-pyglobalgoals.py.ipynb
#   * Src: https://github.com/westurner/pyglobalgoals/blob/master/notebooks/globalgoals-pyglobalgoals.py.py
#   * Src: https://github.com/westurner/pyglobalgoals/blob/develop/notebooks/globalgoals-pyglobalgoals.py.ipynb
#   * Src: https://github.com/westurner/pyglobalgoals/blob/v0.1.2/notebooks/globalgoals-pyglobalgoals.py.ipynb
#   * Src: https://github.com/westurner/pyglobalgoals/blob/v0.2.5/notebooks/globalgoals-pyglobalgoals.py.ipynb
# 
#   * [x] Download HTML with requests
#   * [x] Parse HTML with beautifulsoup
#   * [x] Generate JSON[-LD] with ``collections.OrderedDict``
#   * [-] REF: Functional methods -> more formal type model -> ``pyglobalgoals.<...>``
# 
# 
# * [JSON-LD](#JSONLD) document: **``./notebooks/data/globalgoals.jsonld``**
#   * Src: https://github.com/westurner/pyglobalgoals/blob/master/notebooks/data/globalgoals.jsonld
# 
# 
# ### JSON-LD
# 
# * Wikipedia: https://en.wikipedia.org/wiki/JSON-LD
# * Homepage: http://json-ld.org/
# * Docs: http://json-ld.org/playground/
# * Hashtag: #JSONLD
# 
# ### RDFa
# 
# * Wikipedia: https://en.wikipedia.org/wiki/RDFa
# * Standard: http://www.w3.org/TR/rdfa-core/
# * Docs: http://www.w3.org/TR/rdfa-primer/
# * Hashtag: #RDFa
# 
# ## License
# 
# * pyglobalgoals: BSD License
#   (``LICENSE``)
# * GlobalGoals explanations and descriptions:
#   Creative Commons Attribution-ShareAlike 3.0
#   https://creativecommons.org/licenses/by-sa/3.0/
#   (``LICENSE.cc-by-sa-3.0.html``)
# * GlobalGoals images (provided by Getty Images):
#   http://www.globalgoals.org/asset-licence/
#   (``LICENSE.globalgoals-asset-license.html``)

# In[1]:

#!conda install -y beautiful-soup docutils jinja2 requests
get_ipython().system(u"pip install -U beautifulsoup4 html5lib jinja2 'requests<2.8' requests-cache version-information # tweepy")


import bs4
import jinja2
import requests
import requests_cache

requests_cache.install_cache('pyglobalgoals_cache')

#!pip install -U version_information
get_ipython().magic(u'load_ext version_information')
get_ipython().magic(u'version_information jupyter, bs4, html5lib, jinja2, requests, requests_cache, version_information')


# In[2]:

url = "http://www.globalgoals.org/"
req = requests.get(url)

#print(req)
#print(sorted(dir(req)))
#req.<TAB>
#req??<[Ctrl-]Enter>

if not req.ok:
    raise Exception(req)
content = req.content
print(type(req.content))
print(content[:20])


# In[ ]:




# In[3]:

bs = bs4.BeautifulSoup(req.content, "html5lib")
print(bs.prettify())


# In[4]:

tiles = bs.find_all(class_='goal-tile-wrapper')
pp(tiles)


# In[5]:

tile = tiles[0]
print(tile)
print('##')
print(tile.prettify())


# In[6]:

link = tile.findNext('a')
img = link.findNext('img')
img_title = img['alt'][:-5]
img_src = img['src']
link_href = link['href']
example = {'name': img_title, 'img_src': img_src, 'href': link_href}
print(example)


# In[7]:

import collections
def get_data_from_goal_tile_wrapper_div(node, n=None):
    link = node.findNext('a')
    img = link.findNext('img')
    img_title = img['alt'][:-5]
    img_src = img['src']
    link_href = link['href']
    output = collections.OrderedDict({'@type': 'un:GlobalGoal'})
    if n:
        output['n'] = n
    output['name'] = img_title
    output['image'] = img_src
    output['url'] = link_href
    return output

def get_goal_tile_data(bs):
    for i, tile in enumerate(bs.find_all(class_='goal-tile-wrapper')[:-1], 1):
        try:
            yield get_data_from_goal_tile_wrapper_div(tile, n=i)
        except KeyError as e:
            print((i, tile))
            raise
        
tiles = list(get_goal_tile_data(bs))
import json
print(json.dumps(tiles, indent=2))
goal_tiles = tiles


# In[ ]:




# In[8]:


import codecs
from path import Path

def build_default_context():
    context = collections.OrderedDict()
    # context["dc"] = "http://purl.org/dc/elements/1.1/"
    context["schema"] = "http://schema.org/"
    # context["xsd"] = "http://www.w3.org/2001/XMLSchema#"
    # context["ex"] = "http://example.org/vocab#"
    # context["ex:contains"] = {
    #    "@type": "@id"
    # }
    
    # default attrs (alternative: prefix each with schema:)
    #  schema.org/Thing == schema:Thing (!= schema:thing)
    context["name"] = "http://schema.org/name"
    context["image"] = {
        "@type": "@id",
        "@id": "http://schema.org/image"
    }
    context["url"] = {
        "@type": "@id",
        "@id":"http://schema.org/url"
    }
    context["description"] = {
        "@type": "http://schema.org/Text",
        "@id": "http://schema.org/description"
    }
    return context

DEFAULT_CONTEXT = build_default_context()

def goal_tiles_to_jsonld(nodes, context=None, default_context=DEFAULT_CONTEXT):
    data = collections.OrderedDict()
    if context is None and default_context is not None:
        data['@context'] = build_default_context()
    elif context:
        data['@context'] = context
    elif default_context:
        data['@context'] = default_context
    data['@graph'] = nodes
    
    return data



DATA_DIR = Path('.') / 'data'
#DATA_DIR = Path(__file__).dirname
#DATA_DIR = determine_path_to(current_notebook) # PWD initially defaults to nb.CWD
DATA_DIR.makedirs_p()
GLOBAL_GOALS_JSONLD_PATH = DATA_DIR / 'globalgoals.jsonld'

def write_global_goals_jsonld(goal_tiles, path=GLOBAL_GOALS_JSONLD_PATH):
    goal_tiles_jsonld = goal_tiles_to_jsonld(goal_tiles)
    with codecs.open(path, 'w', 'utf8') as fileobj:
        json.dump(goal_tiles_jsonld, fileobj, indent=2)

def read_global_goals_jsonld(path=GLOBAL_GOALS_JSONLD_PATH, prettyprint=True):
    with codecs.open(path, 'r', 'utf8') as fileobj:
        global_goals_dict = json.load(fileobj,
                                     object_pairs_hook=collections.OrderedDict)
    return global_goals_dict

def print_json_dumps(global_goals_dict, indent=2):
    print(json.dumps(global_goals_dict, indent=indent))

    
write_global_goals_jsonld(goal_tiles)

global_goals_dict = read_global_goals_jsonld(path=GLOBAL_GOALS_JSONLD_PATH)

assert global_goals_dict == goal_tiles_to_jsonld(goal_tiles)

print_json_dumps(global_goals_dict)


# In[9]:


for node in goal_tiles:
    img_basename = node['image'].split('/')[-1]
    node['image_basename'] = img_basename
    
print(json.dumps(goal_tiles, indent=2))


# In[10]:

#!conda install -y pycurl
try:
    import pycurl
except ImportError as e:
    import warnings
    warnings.warn(unicode(e))
def pycurl_download_file(url, dest_path, follow_redirects=True):
    with open(dest_path, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, f)
        if follow_redirects:
            c.setopt(c.FOLLOWLOCATION, True)
        c.perform()
        c.close()
    return (url, dest_path)


# In[11]:

import requests
def requests_download_file(url, dest_path, **kwargs):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(dest_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return (url, dest_path)


# In[12]:

import urllib
def urllib_urlretrieve_download_file(url, dest_path):
    """
    * https://docs.python.org/2/library/urllib.html#urllib.urlretrieve
    """
    (filename, headers) = urlllib.urlretrieve(url, dest_path)
    return (url, filename)


# In[13]:


def deduplicate_on_attr(nodes, attr='image_basename'):
    attrindex = collections.OrderedDict()
    for node in nodes:
        attrindex.setdefault(node[attr], [])
        attrindex[node[attr]].append(node)
    return attrindex
        
def check_for_key_collisions(dict_of_lists):
    for name, _nodes in dict_of_lists.items():
        if len(_nodes) > 1:
            raise Exception(('duplicate filenames:')
                (name, nodes))
    
attrindex = deduplicate_on_attr(goal_tiles, attr='image_basename')
check_for_key_collisions(attrindex)
#

IMG_DIR = DATA_DIR / 'images'
IMG_DIR.makedirs_p()

def download_goal_tile_images(nodes, img_path):
    for node in nodes:
        dest_path = img_path / node['image_basename']
        source_url = node['image']
        (url, dest) = requests_download_file(source_url, dest_path)
        node['image_path'] = dest
        print((node['n'], node['name']))
        print((node['image_path']))
        # time.sleep(1)  # see: requests_cache
    
download_goal_tile_images(goal_tiles, IMG_DIR)

tiles_jsonld = goal_tiles_to_jsonld(goal_tiles)
print(json.dumps(tiles_jsonld, indent=2))


# In[14]:

#import jupyter.display as display
import IPython.display as display
display.Image(goal_tiles[0]['image_path'])


# In[15]:

import IPython.display
for tile in goal_tiles:
    x = IPython.display.Image(tile['image_path'])
x


# In[16]:

import IPython.display
def display_goal_images():
    for tile in goal_tiles:
        yield IPython.display.Image(tile['image_path'])
x = list(display_goal_images())
#pp(x)
IPython.display.display(*x)


# In[17]:


import string
print(string.punctuation)

NOT_URI_CHARS = dict.fromkeys(string.punctuation + string.digits)
NOT_URI_CHARS.pop('-')
NOT_URI_CHARS.pop('_')
def _slugify(txt):
    """an ~approximate slugify function for human-readable URI #fragments"""
    txt = txt.strip().lower()
    chars = (
        (c if c != ' ' else '-') for c in txt if
             c not in NOT_URI_CHARS)
    return u''.join(chars)

def _slugify_single_dash(txt):
    """
    * unlike docutils, this function does not strip stopwords like 'and' and 'or'
    TODO: locate this method in docutils
    """
    def _one_dash_only(txt):
        count = 0
        for char in txt:
            if char == '-':
                count += 1
            else:
                if count:
                    yield '-'
                yield char
                count = 0
    return u''.join(_one_dash_only(_slugify(txt)))
    
            

for node in goal_tiles:
    node['name_numbered'] = "%d. %s" % (node['n'], node['name'])
    node['slug_rst'] = _slugify_single_dash(node['name'])
    node['slug_md'] = _slugify_single_dash(node['name'])
    node['sdgLink'] = 'https://sustainabledevelopment.un.org/sdg{}'.format(node['n'])
    node['sdgReport2016Link'] = 'http://unstats.un.org/sdgs/report/2016/goal-{:02d}'.format(node['n'])
    
print_json_dumps(goal_tiles)

GLOBAL_GOALS_EXTRA_JSONLD_PATH = DATA_DIR / 'globalgoals-extra.jsonld'
with codecs.open(GLOBAL_GOALS_EXTRA_JSONLD_PATH, 'w', 'utf8') as fileobj:
    json.dump(goal_tiles, fileobj, indent=2)


# In[18]:

def build_tweet_for_goal_tile(node):
     return '#Goal{n}: {name} {url} {image} @TheGlobalGoals #GlobalGoals'.format(**node)

for node in goal_tiles:
    node['tweet_txt'] = build_tweet_for_goal_tile(node)
    print(node['tweet_txt'])


# In[19]:

import IPython.display
def display_goal_images():
    for tile in goal_tiles:
        yield IPython.display.Markdown("## %s" % tile['name_numbered'])
        yield IPython.display.Image(tile['image_path'])
        yield IPython.display.Markdown(tile['tweet_txt'].replace('##', '\##'))
x = list(display_goal_images())
#pp(x)
IPython.display.display(*x)


# In[38]:

TMPL_RST = """

The Global Goals
******************

.. contents::

{% for node in nodes %}
{{ node['name_numbered'] }}
======================================================
| {{ node['url'] }}

.. image:: {{ node['image'] }}{# node['image_path'] #}
   :target: {{ node['url'] }}
   :alt: {{ node['name'] }} 

- SDG{{ node['n'] }}: {{ node['sdgLink'] }}
- UN Stats SDG{{ node['n'] }} 2016 Report: {{ node['sdgReport2016Link'] }}

..

   {{ node['tweet_txt'] }}
   
{% endfor %}
"""
tmpl_rst = jinja2.Template(TMPL_RST)
output_rst = tmpl_rst.render(nodes=goal_tiles)
print(output_rst)



# In[21]:

output_rst_path = DATA_DIR / 'globalgoals.rst'
with codecs.open(output_rst_path, 'w', encoding='utf-8') as f:
    f.write(output_rst)
    print("# wrote goals to %r" % output_rst_path)


# In[22]:

import docutils.core
output_rst_html = docutils.core.publish_string(output_rst, writer_name='html')
print(bs4.BeautifulSoup(output_rst_html).find(id='the-global-goals'))


# In[23]:

IPython.display.HTML(output_rst_html)


# In[39]:


TMPL_MD = """

# The Global Goals

**Contents:**
{% for node in nodes %}
* [{{ node['name_numbered'] }}](#{{ node['slug_md'] }})
{%- endfor %}

{% for node in nodes %}
## {{ node['name_numbered'] }}
{{ node['url'] }}

[![{{node['name_numbered']}}]({{ node['image'] }})]({{ node['url'] }})

- SDG{{ node['n'] }}: {{ node['sdgLink'] }}
- UN Stats SDG{{ node['n'] }} 2016 Report: {{ node['sdgReport2016Link'] }}

> {{ node['tweet_txt'] }}

{% endfor %}
"""
tmpl_md = jinja2.Template(TMPL_MD)
output_markdown = tmpl_md.render(nodes=goal_tiles)
print(output_markdown)


# In[25]:

output_md_path = DATA_DIR / 'globalgoals.md'
with codecs.open(output_md_path, 'w', encoding='utf-8') as f:
    f.write(output_markdown)
    print("# wrote goals to %r" % output_md_path)


# In[26]:

IPython.display.Markdown(output_markdown)


# In[27]:

context = dict(nodes=goal_tiles)


# In[49]:

TMPL_HTML = """

<h1>The Global Goals</h1>

<h2>Contents:</h2>
{% for node in nodes %}
<li><a href="#{{node.slug_md}}">{{node.name_numbered}}</a></li>
{%- endfor %}
{% for node in nodes %}
<div class="goal-tile">
  <h2><a name="#{{node.slug_md}}">{{ node.name_numbered }}</a></h2>
  <a href="{{node.url}}">
    <img src="{{node.image}}" alt="{{node.name_numbered}}"/>{{node.url}} </a>
  <ul>
    <li>Goal{{ node['n'] }}: <a href="{{node.url}}">{{node.url}} </a></li>
    <li>SDG{{ node['n'] }}: <a href="{{ node['sdgLink'] }}">{{ node['sdgLink'] }}</a></li>
    <li>UN Stats SDG{{ node['n'] }} 2016 Report: <a href="{{ node['sdgReport2016Link'] }}">{{ node['sdgReport2016Link'] }}</a></li>
  </ul>
  <div style="margin-left: 12px">
  {{ node.tweet_txt }}
  </div>
</div>
{% endfor %}
"""
tmpl_html = jinja2.Template(TMPL_HTML)
output_html = tmpl_html.render(**context)
print(output_html)


# In[50]:

output_html_path = DATA_DIR / 'globalgoals.html'
with codecs.open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(output_html)
    print("# wrote goals to %r" % output_html_path)


# In[51]:

IPython.display.HTML(output_html)


# In[46]:

import jinja2
# TODO: prefix un:
TMPL_RDFA_HTML5 = ("""
<div prefix="schema: http://schema.org/
             un: http://schema.un.org/#">
<h1>The Global Goals</h1>
<h2>Contents:</h2>
{%- for node in nodes %}
<li><a href="#{{node.slug_md}}">{{node.name_numbered}}</a></li>
{%- endfor %}
{% for node in nodes %}
<div class="goal-tile" resource="{{node.url}}" typeof="un:GlobalGoal">
  <div style="display:none">
    <meta property="schema:name">{{node.name}}</meta>
    <meta property="schema:image">{{node.image}}</meta>
    <meta property="#n">{{node.n}}</meta>
  </div>
  <h2><a name="#{{node.slug_md}}">{{ node.name_numbered }}</a></h2>
  <a href="{{node.url}}">
    <img src="{{node.image}}" alt="{{node.name_numbered}}"/>{{node.url}} </a>
  <ul>
    <li>Goal{{ node['n'] }}: <a href="{{node.url}}" property="schema:url">{{node.url}} </a></li>
    <li>SDG{{ node['n'] }}: <a href="{{ node['sdgLink'] }}" property="#sdgLink">{{ node['sdgLink'] }}</a></li>
    <li>UN Stats SDG{{ node['n'] }} 2016 Report: <a href="{{ node['sdgReport2016Link'] }}" property="#sdgReport2016Link">{{ node['sdgReport2016Link'] }}</a></li>
  </ul>
  <div style="margin-left: 12px">
  {{ node.tweet_txt }}
  </div>
</div>
{% endfor %}
</div>
"""
)
tmpl_rdfa_html5 = jinja2.Template(TMPL_RDFA_HTML5)
output_rdfa_html5 = tmpl_rdfa_html5.render(**context)
print(output_rdfa_html5)


# In[47]:

output_rdfa_html5_path = DATA_DIR / 'globalgoals.rdfa.html5.html'
with codecs.open(output_rdfa_html5_path, 'w', encoding='utf-8') as f:
    f.write(output_rdfa_html5_path)
    print("# wrote goals to %r" % output_rdfa_html5_path)


# In[48]:

IPython.display.HTML(output_rdfa_html5)


# In[34]:

# tmpl_html
# tmpl_rdfa_html5
import difflib
for line in difflib.unified_diff(
    TMPL_HTML.splitlines(),
    TMPL_RDFA_HTML5.splitlines()):
    print(line)

