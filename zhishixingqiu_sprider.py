from datetime import time
from urllib.parse import urlencode
import requests
import json

def get_json(count,end_time):
    data={
        "count": count,
        "end_time": end_time
    }
    url="https://api.zsxq.com/v1.8/groups/2421112121/topics?"+urlencode(data)

    # 头部信息，直接复制自己的
    headers = """
      authorization:XXXXXXXXXX
      User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400
          """
    headers = headers_to_dict(headers)
    response=requests.get(url,headers=headers)
    data=response.text
    while True:
        end_time=get_endtime(data)
        parse(data)
        get_json(20,end_time)
        time.sleep(1)


def parse(data):
# 以json格式存储到文件
    with open("zhishixingqiu.json", "a", encoding="utf-8") as f:
        f.write(data+"\n")



def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典类型
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers



def get_endtime(data):
    try:
        end_time=json.loads(data).get("resp_data").get("topics")[19].get("create_time")
        print(end_time)
        return end_time
    except IndexError :
        print("已经爬完了")
        return None




def read_json():
    with open("zhishixingqiu.json", 'r', encoding='utf-8') as f:
        try:
            while True:
                line = f.readline()
                if line:
                    r = json.loads(line)
                    d=r.get("succeeded")
                    print(d)

                else:
                    break
        except:
            f.close()


if __name__ =="__main__":
    get_json(20, "2018-01-05T17:35:07.366+0800")




