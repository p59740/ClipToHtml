import webbrowser
import subprocess
# write-html.py

f = open('/Users/yue/Documents/study/ClipToHtml/test.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

def getClipboardData():

    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)

    retcode = p.wait()

    data = p.stdout.read()

    #这里的data为bytes类型，之后需要转成utf-8操作

    return data

def setClipboardData(data):

    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)

    p.stdin.write(data)

    p.stdin.close()

    p.communicate()

txt = str(getClipboardData(),'utf-8')

# transfer the space and line
txt = txt.strip().replace('\r\n','<br>').replace('\r','<br>').replace('\n','<br>')

# print(txt)

f.writelines('<br>')
f.writelines('<div><span style = "color:#cab19D;font-size:66px;">')
f.writelines(txt)
f.writelines('</span></div>')
f.close()

webbrowser.get(using ='chrome').open('file:///Users/yue/Documents/study/ClipToHtml/test.html', 0)

