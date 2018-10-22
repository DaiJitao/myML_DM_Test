
# 查询网站所使用的技术
import builtwith
import whois
"""
pip install python-whois
pip install builtwith
"""
print(builtwith.parse('http://www.douban.com'))
print(builtwith.parse('http://www.baidu.com'))
print(whois.whois('baidu.com'))