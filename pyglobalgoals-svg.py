
# coding: utf-8

# # pyglobalgoals-svg

# * | Src:
# * | Nbviewer:

# In[3]:

get_ipython().system(u'pip install svgwrite')
# https://svgwrite.readthedocs.org/en/latest/overview.html
import svgwrite

get_ipython().system(u'pip install -e git+https://github.com/scardine/image_size@324affe#egg=image-size')
import get_image_size


# In[ ]:

dwg = svgwrite.Drawing(height=800, width=600)
print(('dwg', dwg))
img = svgwrite.image.Image(href='./data/images/partnership.png')
print(('img', img))
dwg.add(img)
print(('dwg', dwg))
print(('elements', dwg.elements))
for e in dwg.elements:
    print((e, e.tostring()))
print(('dwg_svg', dwg.tostring()))

def prettify_xml(obj):
    return (bs4.BeautifulSoup(dwg.tostring(), features='xml').prettify())
print("")
print(prettify_xml(dwg.tostring()))


# In[4]:

import glob
files = glob.glob('./data/images/*.png')
for img_path in files:
    md = get_image_size.get_image_metadata(img_path)
    print((img_path, md.height, md.width)) #, md ))


# In[ ]:



