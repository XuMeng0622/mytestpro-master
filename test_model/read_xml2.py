# -*- coding:utf -*-

from xml.dom import minidom

if __name__ == '__main__':
    dom = minidom.parse('./config_file/get_data.xml')

    #获取根元素
    root = dom.documentElement
    # print(root.nodeName)
    # print(root.nodeValue)
    # print(root.nodeType)
    # print(root.ELEMENT_NODE)

    #获取标签名
    tagname_list = root.getElementsByTagName('id')
    print(tagname_list[1].tagName)

    #获取标签属性
    download_list = root.getElementsByTagName('download')
    path = download_list[1].getAttribute('path')
    print(path)

    #获取标签对之间的数据
    id1 = tagname_list[0].firstChild.data
    print(id1)





