import requests
from config.config import get_config
from common.logger import get_logger

# ===== 调试开关：True=走Fiddler代理抓包；False=正常直连（正式跑用False）=====
DEBUG_PROXY = False
FIDDLER_PROXY = "http://127.0.0.1:8888"


class ApiClient:
    def __init__(self,store):
        self.base_url=get_config('base_url')
        self.timeout=get_config('timeout')
        self.logger=get_logger()
        self.headers={"Content-Type": "application/json"}
        self.store = store

        # 调试模式才配代理；verify=False仅本地抓包用，跳过Fiddler自签证书校验
        if DEBUG_PROXY:
            self.proxies = {"http": FIDDLER_PROXY, "https": FIDDLER_PROXY}
            self.verify = False
        else:
            self.proxies = None
            self.verify = True

    def api_get(self,path,params=None):
        try:
            url=self.base_url+path
            print(f"【实际请求完整URL】：{url}")
            self.logger.info(f"url:{url}")
            resp=requests.get(url,params=params,timeout=self.timeout,proxies=self.proxies,verify=self.verify)
            self.logger.info(f"状态码:{resp.status_code}")
        except Exception as e:
            self.logger.error(f"GET请求异常{e}")
            raise e
        return resp

    def api_post(self,path,data=None,json=None):
        try:
            url=self.base_url+path
            print(f"【实际请求完整URL】：{url}")
            self.logger.info(f"url:{url}")
            resp=requests.post(url,data=data,timeout=self.timeout,json=json,proxies=self.proxies,verify=self.verify)
            self.logger.info(f"状态码:{resp.status_code}")
        except Exception as e:
            self.logger.error(f"POST请求异常{e}")
            raise e
        return resp

    def api_put(self,path,data=None,json=None):
        try:
            url=self.base_url+path
            print(f"【实际请求完整URL】：{url}")
            self.logger.info(f"url:{url}")
            resp=requests.put(url,data=data,timeout=self.timeout,json=json,proxies=self.proxies,verify=self.verify)
        except Exception as e:
            self.logger.error(f"PUT请求异常{e}")
            raise e
        return resp

    def api_delete(self,path):
        try:
            url=self.base_url+path
            self.logger.info(f"url:{url}")
            resp=requests.delete(url,timeout=self.timeout,proxies=self.proxies,verify=self.verify)
        except Exception as e:
            self.logger.error(f"DELETE请求异常{e}")
            raise e
        return resp