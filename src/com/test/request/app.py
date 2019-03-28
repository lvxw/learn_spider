# -*- coding: UTF-8 -*-

import requests


def test_common_attributes():
    url = "https://www.baidu.com/"
    r = requests.get(url)
    print(r.status_code)            # 状态码
    print(r.encoding)               # 字符编码吗，header中content-type中的值
    print(r.apparent_encoding)      # 实际文档编码，更具文档分析出来的编码
    print(r.headers)                # response头
    print(r.text)                   # 服务器返回的文本
    print(r.content)                # 返回的内容的二进制
    print(r.cookies)                # 返回的cookies
    print(r.request.headers)        # 请求头
    print(r.request.url)            # 请求url


def test_common_method():
    url = "https://www.baidu.com/"
    r = requests.get(url)
    # 要么正取，返回200状态码，要么抛出异常
    r.raise_for_status()


def regular_code():
    url = "https://www.baidu.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except Exception as errorMsg:
        print("发生了异常："+errorMsg)
        return ""


test_common_attributes()
test_common_method()
regular_code()

