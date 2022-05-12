'''
@author:hxh
@file: check_result.py
@time:2022/5/11
'''

import traceback  # 异常捕获
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base_Setting import *
from Util_Tools import *
import pandas as pd

dr = webdriver.Chrome()
def open_url(url):
    dr.maximize_window()
    dr.get(url)  # 打开网页

def get_item_url():
    try:
        open_url(online_url)
        temp_height = 0
        url_list = []
        scrollTop = 700   #初始页面滑动值
        while True:
            js = f"var q=document.documentElement.scrollTop={scrollTop}"  # documentElement表示获取根节点元素
            dr.execute_script(js)
            for i in range(1,6):
                item_path = wait_until(dr, (By.XPATH, f'//*[@id="main"]/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div/div[{i}]/div/article/a'), maxwait=20).get_attribute('href')
                item_url = base_url+ item_path
                url_list.append(item_url)
            # 获取当前滚动条距离顶部的距离
            check_height = dr.execute_script(
                "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
            if check_height == temp_height:    # 如果两者相等说明到底了
                break
                dr.quit()
            scrollTop += 450     #滑动截界面间隔值，动态加载数据
    except Exception as e:
        exstr = traceback.format_exc()
        e_log(f"错误信息为：{e}\n详细错误：{exstr}\n")
    return list(set(url_list))

def check_results():
    # url_list= get_item_url()   #上述方法获取Item_url列表
    for i,ul in enumerate(tmp_list):   #使用部分url列表，已经获取到的数据，调试脚本可更换成 url_list
        try:
            staus_list = []
            open_url(ul)
            wait_until(dr, (By.XPATH, '//*[@id="main"]/div/div/div/div[1]/div/div[1]/div[2]/section[1]/div/div[2]/div/button[1]/div/i'),1,1).click()
            if ul == dr.current_url:
                staus_list.append("Clicked=您的程序已单击元数据")
            timer_text = wait_until(dr, (By.XPATH, '//*[@id="__next"]/div[2]/div/div'),1, 1).text
            if "We've queued" in timer_text.split("\n")[1]:
                staus_list.append("Queued=您的程序检测到文本“We's Queued…”")
            else:
                staus_list.append("Error=您的程序检测到一些错误")
            item_list.append((i+1,ul,staus_list))
        except Exception as e:
            e_log(f"错误信息为：{e}\n详细错误：{traceback.format_exc()}\n")
            staus_list.append("Error=您的程序检测到一些错误")
            item_list.append((i+1,ul,staus_list))
            continue
    df = pd.DataFrame(data = item_list, columns=['no','url','staus'])
    df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
if __name__ == '__main__':
    item_list = check_results()
    

