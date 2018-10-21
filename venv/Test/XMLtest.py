import xml.dom.minidom

doc=xml.dom.minidom.Document()
root=doc.createElement('News')
doc.appendChild(root)

managerList = [{'name' : 'joy',  'age' : 27, 'sex' : '女'},
               {'name' : 'tom', 'age' : 30, 'sex' : '男'},
               {'name' : 'ruby', 'age' : 29, 'sex' : '女'}
]
print(type(managerList))
for i in managerList:
    nodeTopic=doc.createElement('Topic')
    nodeTopic.appendChild(doc.createTextNode('sports'))
    nodeLink=doc.createElement('Link')
    nodeLink.appendChild(doc.createTextNode('baidu.com'))
    nodeTime=doc.createElement('Time')
    nodeTime.appendChild(doc.createTextNode('10-17'))
    nodeTitle=doc.createElement('Title')
    nodeTitle.appendChild(doc.createTextNode(str(i['name'])))
    nodeText=doc.createElement('Text')
    nodeText.appendChild(doc.createElement(str(i['age'])))
    root.appendChild(nodeTopic)
    root.appendChild(nodeLink)
    root.appendChild(nodeTime)
    root.appendChild(nodeTitle)
    root.appendChild(nodeText)
fp=open('/Users/tianyu/news.xml','w')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding="utf-8")

