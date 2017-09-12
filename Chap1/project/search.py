
f = open('weather_info.txt', 'r')
list_file = f.readlines()

#print(list_file)
#print(list_file[0])

w_detail = {}

h_entry = []

for i in list_file:
    city = i.split(',')[0]
    wea_detail = i.split(',')[1].rstrip()

    w_detail[city] = wea_detail

def null_hints():
        print("换个别的城市试试")

def start():
    print("请输入中国城市查询当地天气,或者‘help’查询使用指南")


    while True:
        r = input(">")

        if r in w_detail.keys():
            print("~", w_detail[r])
            h_entry.append(r +'～'+ w_detail[r])


        elif r == 'help':
            print("""
                  h:查询记录
                  q:退出查询
                  """)

        elif r == 'h':
            for record in h_entry:
                print(record)

        elif r == 'q':
            quit()


        else:
            null_hints()

start()
