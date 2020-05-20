import requests,json
import urllib

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def save(page_start):
    # 0 20 40 60
    url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start="+str(page_start)
    res=requests.get(url,headers=header)
    json_data=json.loads(res.text)
    subjects=json_data.get('subjects')
    for m in subjects:
        title=m.get('title').replace("/","斜斜斜线")
        cover=m.get('cover')
        ext=cover[cover.rindex("."):]
        print(title,cover,ext)
        urllib.request.urlretrieve(cover , filename='./movies/%s'%(title+ext))

for i in range(17):
    save(20*i)

# save(20*17)
