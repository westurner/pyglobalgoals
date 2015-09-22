
# coding: utf-8

# In[1]:

import tweepy
import bs4
import requests

import pyglobalgoals.pyglobalgoals as gg


# In[2]:

url = "http://www.globalgoals.org/"
req = requests.get(url)
print(req)
print(sorted(dir(req)))


# In[3]:

if not req.ok:
    raise Exception(req)
content = req.content
print(content[:20])


# In[4]:

bs = bs4.BeautifulSoup(req.content)
print(bs.prettify())


# In[5]:

tiles = bs.find_all(class_='goal-tile-wrapper')
tiles


# In[6]:

tile = tiles[0]
tile


# In[7]:

link = tile.findNext('a')
img = link.findNext('img')
img_title = img['alt'][:-5]
img_src = img['src']
link_href = link['href']
{'name': img_title, 'img_src': img_src, 'href': link_href}


# In[8]:

import collections
def get_data_from_goal_tile_wrapper_div(node, n=None):
    link = node.findNext('a')
    img = link.findNext('img')
    img_title = img['alt'][:-5]
    img_src = img['src']
    link_href = link['href']
    output = collections.OrderedDict({'@type': 'GlobalGoal'})
    if n:
        output['n'] = n
    output['name'] = img_title
    output['image'] = img_src
    output['url'] = link_href
    return output

def get_goal_tile_data(bs):
    for i, tile in enumerate(bs.find_all(class_='goal-tile-wrapper'), 1):
        yield get_data_from_goal_tile_wrapper_div(tile, n=i) 
        
tiles = list(get_goal_tile_data(bs))
import json
print(json.dumps(tiles, indent=2))


# In[9]:

goal_tiles = tiles[:-1]
goal_tiles


# In[ ]:



