import requests 

def get_alldate():

    url = "http://192.168.2.55:7900/mes/newAssemble/allData?selectedTimeQuantum=2018-07-23&status=1&choosedWo=2000802160"

    #Referer: http://192.168.2.55:7900/mes/newAssemble/index?startDate=2018-05-10&endDate=2018-07-23
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
               , "cookie": "mdaId=273ef7d03f83416ea33319c9acfb9555; JSESSIONID=F94628958F1B43A2FBC78C1023C890AC"
               , 'Referer': 'http://192.168.2.55:7900/mes/newAssemble/index?startDate=2018-05-10&endDate=2018-07-23' }
    cookie = {"cookie":"mdaId=273ef7d03f83416ea33319c9acfb9555; JSESSIONID=F94628958F1B43A2FBC78C1023C890AC"}
    r = requests.get(url=url,headers=headers)

    print(r.text)

get_alldate()    


'''Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: mdaId=273ef7d03f83416ea33319c9acfb9555; JSESSIONID=F94628958F1B43A2FBC78C1023C890AC
Host: 192.168.2.55:7900
Referer: http://192.168.2.55:7900/mes/newAssemble/index?startDate=2018-05-10&endDate=2018-07-23
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
X-Requested-With: XMLHttpRequest'''