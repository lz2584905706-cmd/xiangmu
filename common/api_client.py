import requests
from config.config import get_config
from common.logger import get_logger


class ApiClient:
    def __init__(self,store):
        self.base_url=get_config('base_url')
        self.timeout=get_config('timeout')
        self.logger=get_logger()
        self.headers={
        "Content-Type": "application/json"
    }
        self.store = store

    def api_get(self,path,params=None):
        try:
            url=self.base_url+path
            print(f"【实际请求完整URL】：{url}")
            self.logger.info(f"url:{url}")
            resp=requests.get(url,timeout=self.timeout)
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
            resp=requests.post(url,data=data,timeout=self.timeout,json=json)
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
            resp=requests.put(url,data=data,timeout=self.timeout,json=json)
        except Exception as e:
            self.logger.error(f"PUT请求异常{e}")
            raise e
        return resp

    def api_delete(self,path):
        try:
            url=self.base_url+path
            self.logger.info(f"url:{url}")
            resp=requests.delete(url,timeout=self.timeout)
        except Exception as e:
            self.logger.error(f"DELETE请求异常{e}")
            raise e
        return resp

