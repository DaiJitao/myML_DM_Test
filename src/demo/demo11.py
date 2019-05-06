#coding:utf-8
import time
import datetime


def ISOString2Time(s):
    '''
    convert a ISO format time to second
    from:2006-04-12 16:46:40 to:23123123
    把一个时间转化为秒
    '''
    d = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    return time.mktime(d.timetuple())


def Time2ISOString(s):
    '''
    convert second to a ISO format time
    from: 23123123 to: 2006-04-12 16:46:40
    把给定的秒转化为定义的格式
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(s)))

    a = "2018-11-28 17:38:02"
    b = ISOString2Time(a)
    print(b)
    print(Time2ISOString(1543485130))

if __name__ == '__main__':
    context = "新华网北京4月30日电 4月29日，中国移动联合40家通信、互联网、教育等领域的企事业单位、高校和科研机构在杭州宣布成立5G智慧教育合作联盟。联盟首批成员包括北师大、华为、科大讯飞、好未来、网龙、戴尔、拓维等，中国移动任联盟首届理事长单位。&lt;/p&gt;&lt;p&gt;该联盟以打造5G网络下智慧教育“教”“学”“产”“研”“投”合作体系为宗旨，以推动5G与智慧教育技术发展和融合为目标，共同开展5G环境下的智慧教育标准制定、关键技术研究、业务试点示范、交流合作、创新孵化等方面工作，实现各方协同创新、融合共赢。&lt;/p&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/RP5Jc4xITXKLBL&quot; img_width&#x3D;&quot;488&quot; img_height&#x3D;&quot;325&quot; alt&#x3D;&quot;5G智慧教育合作联盟成立&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p&gt;与会嘉宾代表共同启动联盟发布&lt;/p&gt;&lt;p&gt;参会专家王珠珠认为，发展“互联网+教育”是国之大计，民之所向。建设教育强国，办好人民满意教育，解决教育发展不平衡不充分的问题，让每个孩子通过教育获得美好人生均需要不断采用新技术。&lt;/p&gt;&lt;p&gt;联盟首届理事长、中国移动政企客户分公司副总经理方力称，中国移动通过丰富多彩的垂直行业应用引领5G发展，积极构建5G生态系统（5G+Ecology），提出了“让了解行业的伙伴打造产品、让接触客户的伙伴获得增值、让平台助力产品销售、让资源助力企业腾飞”的合作思路。中国移动作为联盟首届理事单位，将致力于推进联盟日常运行、深化联盟内部合作、加速优秀成果孵化、打造一个大规模、高活跃、有成效的产业合作平台。&lt;/p&gt;&lt;p&gt;中国移动还在会上发布了《5G+智慧教育白皮书》，与35家合作伙伴签署了联盟备忘录。北京师范大学互联网教育智能技术及应用国家工程实验室主任黄荣怀以“5G+”为手段发展智慧教育、促进教育公平为题做了专题讲座。好未来、戴尔、网龙三家合作伙伴代表也进行了主题分享,表示要紧密依托中国移动5G技术、渠道资源和平台能力更好地为教育行业赋能，与中国移动携手共绘5G智慧教育新蓝图。&lt;/p&gt;&lt;p&gt;中国移动5G产业数字化联盟体系是中国移动全方位推进5G发展，实施“5G+”计划，构建5G+ecology生态体系的具体举措之一。目前，5G产业数字化联盟已经在交通、能源、教育等领域打造了多个专业领域联盟。"
    import re
    # p = re.compile("(http|ftp|https):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?^=%&amp;/~\\+#])?") #  &quot;
    p = re.compile("(&quot;){1}(http|ftp|https)://[A-Za-z1-9.%-_*]{1,}/(([A-Za-z1-9.%-_*]{1,}/){0,}){0,}([A-Za-z1-9.%-_*]{0,});{1}")
    res = re.search(p, context)
    print(res)

