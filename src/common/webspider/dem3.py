import requests
import lxml.html as htl
from lxml import etree

page = 1
url = 'http://www.jikexueyuan.com/course/?pageNum=' + str(page)
html = requests.get(url)

print(html.content)

selector = etree.HTML(html.text)
content_field = selector.xpath('//div[@class="lesson-list"]/ul/li')
print(content_field)

root = etree.Element('root')
print(root)
print(root.tag)
print(etree.tostring(root))