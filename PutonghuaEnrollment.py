import json
import requests
import logging
import requests.packages.urllib3
import time
import threading


def enroll(cookie, post_data):
    url = 'http://202.114.50.130/Examination/pthkssqSave.do'
    header = {
        'Connection': 'keep-alive',
        'Content-Length': '163',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://202.114.50.130',
        'Referer': 'http://202.114.50.130/Examination/login.do?msg=VHyDOX5O769dnH%2By8UhcV5xsh%2BS%2BMqhxcu24BfqJGTF6VhzkiYe1qbDzB9km7aS5cMEFhNfGmw76%0AcSIv%2Bpl728lU7Sdb5%2BCZWpOnR9%2BVXoNoZjphjaGsQi9VgQOCmxxcu3Ih2DtFWPWsRTJQeswdCcGW%0AL8ItlN0EWqE2KJidcwU%3D%0A%23A9EBWsAf95M9DnKfnAJiZEQhXFqZ1oxBmzl%2BclW03BwYq06HSXd%2FJ78CLBoLr3vgQcUoKlf4Ura%2F%0AewmEex71z%2Bx9hO8wSHRgXWOuzkncs2AnexGDuxZvpBReMyFTxS9E8k9sF0jf5MDbQdkFYBEc4heo%0AFFYiNktJYqgEr%2BNEJ1k%3D%0A%23eFzhEGONce6rPR7oMcQPG%2FGWFFZSmHP5PTx%2BzPHa5n%2Bfy7at902%2FCq%2F5duRON5oFeiFF8NLbWvZO%0A9Cd2hAarlo9nx%2FyoYdj7PONmZ3IIjgVkeboxhMIpSfCtud1uCO2oEPNFTj89qPiT06SXxTBNueig%0A0YvWOz4sK3TMdoZuU7I%3D%0A%23a3178IZlZ23wAhDySnzIgNNAj1%2BPsE9KV4NsR4sLHJSYrvxsRs5kRskk334xnxj1l8e8huHYdibG%0AuQ8fGbVSya8T3DbqSsKrm15svfIBUcM7AMMxhR2TxTdDsZRFTb7%2B5nRsZRutbH1gnFyyaFEW9xq7%0AMwi%2B0%2BaVd0IH3T%2FTvlg%3D%0A%23gfg8mQAefIcvhAvi3RguorIhoJ09YXFAWz13xb20muIEXBQIXHjsWJ%2FEYeoyX0WXNvSNQpUFub%2B1%0ABqgiDwO9Q982JzkBcOQb9l%2FZZneCbNoLu3aJKwX9V2gaerhV3ZsoOxMRd%2B%2FB%2FxftZn0WDcFef7SR%0AbVkDxXaQ69TnaH5nJT4%3D%0A%23',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
        'Cookie': cookie,
        'Host': '202.114.50.130',
    }
    rp = requests.post(url, headers=header, data=post_data, verify=False, timeout=(1, 1))
    rp_response = rp.text
    print(str(rp_response))
    logging.info(str(rp_response))


def run_enroll(cookie, post_data):
    while True:
        try:
            enroll(cookie, post_data)
        except BaseException as e:
            print(e)
            logging.warning(e)


class EnrollThread(threading.Thread):
    def __init__(self, cookie, post_data):
        threading.Thread.__init__(self)
        self.cookie = cookie
        self.post_data = post_data

    def run(self):
        run_enroll(cookie, post_data)


if __name__ == '__main__':
    # 在浏览器network中从post请求中抓到,遵循以下格式
    post_data = 'temp=true&sqkeys=&xnxq=2020-2021-1&pthkey=&xh=&xm=&sfzh=&lxdh='
    # 可以直接用EditCookie插件获取cookie，也可报名一次从post请求中获取
    cookie = 'JSESSIONID='
    # 线程数
    thread_count = 16

    logging.basicConfig(filename='enrolling_log.log', level=logging.INFO)
    requests.packages.urllib3.disable_warnings()
    for i in range(thread_count):
        thread = EnrollThread(cookie, post_data)
        thread.start()
