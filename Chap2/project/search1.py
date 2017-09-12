
import requests, json

record = []

def asking(typing):
    params= {'key':'sliiph0emwkrfagt','location':'typing','language':'zh-Hans','unit':'c'}
    params['location']= typing
    r = requests.get('https://api.seniverse.com/v3/weather/now.json',params)
    detail = r.text
    block = json.loads(detail)
    if 'status' in block.keys():
        print('请输入中国城市名，中文或拼音')
    else:
        wea_info = block['results'][0]['now']['text']
        temp = block['results'][0]['now']['temperature']
        appearing = temp + '℃ ,'+ wea_info
        print(appearing)
        wea_listing = typing + ',' + appearing
        record.append(wea_listing)

def help():
    print("""
          输入字母
          t:查询记录
          q:退出查询
          """)

def history():
    if record == []:
        print('还没输入正确的城市名哦')

    else:
        print(record)

def leaving():
    print('欢迎再来！')
    quit()

#def null():
    #print('好像不对哦，换个城市名试试')

def start():
    print('请输入中国城市查询当地天气,或者‘help’查询使用指南')

    while True:
        typing = input('>')

        if typing == 'help':
            help()

        elif typing == 'q':
            leaving()

        elif typing == 't':
            history()

        else:
            asking(typing)





start()
