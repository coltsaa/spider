import requests,re,json,pandas

head = requests.get('https://comment.bilibili.com/rolldate,3724723')
data = list(map(lambda ll:json.loads(head.text)[ll]['timestamp'],range(len(json.loads(head.text)))))
data.reverse()
url = list(map(lambda jj:'https://comment.bilibili.com/dmroll,'+jj+',3724723',data))
for ff in url:
    html = requests.get(ff)
    ren = re.compile(r'<d p=".*?">(.*?)</d>', re.S)
    print(re.findall(ren,html.text))
