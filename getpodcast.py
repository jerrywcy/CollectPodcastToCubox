import feedparser
import json
import os

def send(item):
    dic={}
    dic["type"]="url"
    dic["content"]=item.enclosures[0].href
    dic["title"]=item.title
    dic["description"]=item.summary
    dic["tags"]=["#podcast"]
    dic["folder"]="Podcast"
    apilink="https://cubox.pro/c/api/save/1lazyzxmbzofp6"
    command="curl -X POST -H 'Content-Type: application/json' -d '"+json.dumps(dic)+"' "+apilink
    print(command)
    os.system(command)

d={}
with open("./data.txt","r") as f:
    j=f.read()
    d=json.loads(j)
for i in d:
    feed=feedparser.parse(i)
    cur=0
    while cur<len(feed.entries) and feed.entries[cur]!=d[i]:
        send(feed.entries[cur])
        cur+=1
    d[i]=feed.entries[0].id
with open("./data.txt","w") as f:
    f.write(json.dumps(d))
