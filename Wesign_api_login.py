import requests
import json
from hashlib import md5
import requests

url = "https://app.signit.cn/api/users/sessions"
username = input('username:')
userpassword = input('password:')
def login(url,username,userpassword):
    userpassword = md5(userpassword.encode(encoding='utf-8')).hexdigest()
    print(userpassword)
    payload = {"accountNumber": username, "password": userpassword, "verificationCode": "", "loginType": "WEB"}
    headers = {
        'origin': "https://app.signit.cn",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        'content-type': "application/json;charset=UTF-8",
        'accept': "application/json, text/plain, */*",
        'referer': "https://app.signit.cn/login",
        'authority': "app.signit.cn",
        # 'cookie': "__guid=205526723.913289625729413100.1561960794538.1711; Hm_lvt_f5679562352d7a484ab419804ee943ea=1561960795,1561964264,1561964437,1561965854; Hm_lvt_45d62509d76760907fbf2b0df666f17c=1561965856; Hm_lpvt_45d62509d76760907fbf2b0df666f17c=1561965856; SessionWsid=WSID_SESS_0000016bac6c83300242d7e5be900001; connectId=s%3AanR39-gjdOCmVsYlIBVUHCbzZtnON3xg.oVG3SFF0B9nNXlRwKbOKYswX3lrPO%2BItESUAlC8tgHs; SERVERID=76571cd95b653f33ad9b8979ba414216|1561969179|1561960788; monitor_count=34; Hm_lpvt_f5679562352d7a484ab419804ee943ea=1561969186,__guid=205526723.913289625729413100.1561960794538.1711; Hm_lvt_f5679562352d7a484ab419804ee943ea=1561960795,1561964264,1561964437,1561965854; Hm_lvt_45d62509d76760907fbf2b0df666f17c=1561965856; Hm_lpvt_45d62509d76760907fbf2b0df666f17c=1561965856; SessionWsid=WSID_SESS_0000016bac6c83300242d7e5be900001; connectId=s%3AanR39-gjdOCmVsYlIBVUHCbzZtnON3xg.oVG3SFF0B9nNXlRwKbOKYswX3lrPO%2BItESUAlC8tgHs; SERVERID=76571cd95b653f33ad9b8979ba414216|1561969179|1561960788; monitor_count=34; Hm_lpvt_f5679562352d7a484ab419804ee943ea=1561969186; connectId=s%3AanR39-gjdOCmVsYlIBVUHCbzZtnON3xg.oVG3SFF0B9nNXlRwKbOKYswX3lrPO%2BItESUAlC8tgHs",
        'Cache-Control': "no-cache",
        'Postman-Token': "f8592158-272b-4092-bef0-d541af78620a,9f0e3b32-1f22-4427-a7bb-a701c4c29c39",
        'Host': "app.signit.cn",
        'content-length': "117",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'X-Requested-Device': "12345"
        #X-Requested-Device加入可以暂时避免验证码问题
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

if __name__ == '__main__':
    login(url, username, userpassword)


