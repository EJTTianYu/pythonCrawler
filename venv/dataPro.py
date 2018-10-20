import linecache
filePath=r'D:\pythonCrawler\scrapXML\news4.xml'

def get_line(file_path,line_number):
    return (linecache.getline(file_path,line_number).strip())

title_line=6
text_line=8
count=len(open(r'D:\pythonCrawler\scrapXML\news4.xml',encoding='utf-8').readlines())

while(text_line<count):
    print(get_line(filePath,title_line),get_line(filePath,text_line))
    title_line+=7
    text_line+=7
