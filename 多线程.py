
import concurrent.futures,urllib.request as dw
import requests,re,bs4,time
from contextlib import closing
#import serial

ok = bytes([160,1,1,162])
no = bytes([160,1,0,161]) 
ser = serial.Serial("COM2",9600,timeout=5)
url = 'https://alpha.wallhaven.cc/random?page=2'

headers = {'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

URLS = [] 

URLS_JPG = []

class ProgressBar(object):
    def __init__(self, title, count=0.0, run_status=None, fin_status=None, total=100.0, unit='', sep='/', chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "[%s] %s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total  #欲下载文件大小
        self.count = count
        self.chunk_size = chunk_size #区块下载大小
        self.status = run_status or "" #下载开始提示
        self.fin_status = fin_status or " " * len(self.status) #下载完成提示
        self.unit = unit  #下载单位
        self.seq = sep #分割字符

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (self.title, self.status, self.count/self.chunk_size, self.unit, self.seq, self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r" #光标移动至开头
        #ser.write(no)
        if self.count >= self.total:
            end_str = '\n' 
            self.status = status or self.fin_status
            #ser.write(ok)

            
        """
        没搞懂 print(end="")的用法
        ,在eric中打印的东西看不到
        ,在window控制台下单条语句刷新并不添加新的行
        """  
        # print(,end="")的用法,可能会出现打印看不到的情况
        print(self.__get_info(), end=end_str, )

def load_url(url, timeout):
    with requests.get(url=url, headers=headers, timeout=timeout) as conn:
        return conn.text

def get_all_urls(url): 

    url_text = load_url(url,60)

    rjie = bs4.BeautifulSoup(url_text,'lxml')

    url_all = rjie.find_all('a',"preview")

    for uurl in url_all:
        URLS.append(uurl['href'])
        print(uurl['href'])


def get_jpg_url():

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    #print(future_to_url)
	    #print(future_to_url)
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
        #time.sleep(2)
            try:
                data = future.result()
                rjie = bs4.BeautifulSoup(data,'lxml')
                url_all = rjie.find('img',id="wallpaper")
                url_a = url_all.get('src')
                
                url_jpg = "https:" + url_a
                URLS_JPG.append(url_jpg)
                print(url_jpg)

            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                pass
                #print('%r page is %d bytes' % (url, len(data)))

if __name__ == '__main__':
    get_all_urls(url)
    get_jpg_url()
    for url in URLS_JPG:
        name_a = url[48:]
        path_jpg = r'F:\壁纸\{}'.format(name_a)
        print(path_jpg)
        with closing(requests.get(url, stream=True)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
     
            print(f'文件大小 {content_size/1024} KB', response.status_code ,  )
            progress = ProgressBar("razorback"
                    , total=content_size
                    , unit="KB"
                    , chunk_size=chunk_size
                    , run_status="正在下载"
                    , fin_status="下载完成")
            # chunk_size = chunk_size < content_size and chunk_size or content_size
            with open(path_jpg, "wb") as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        progress.refresh(count=len(data))
                    
            print('下载完成', )
       