'''
@author:hxh
@file: Util_Tools.py
@time:2022/5/11
'''
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait as wwait
from selenium.webdriver.support import expected_conditions as EC


# 等待设置
def wait_until(bc, locator, timemore=0.5, type=1, maxwait=30):
    '''bc=driver,类似locator=(By.ID,'kw'),type{1:visible,2:clickable,3:frame switch}'''

    wait = wwait(bc, maxwait, 0.2)

    # 等待页面元素可见，返回该页面元素
    if type == 1:
        ret = wait.until(EC.visibility_of_element_located(locator))
        if timemore > 0:
            sleep(timemore)
        return ret

    # 等待页面元素可点击，返回该元素
    elif type == 2:
        ret = wait.until(EC.element_to_be_clickable(locator))
        if timemore > 0:
            sleep(timemore)
        return ret

    # 通过定位frame 切换到这个frame
    elif type == 3:
        ret = wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        if timemore > 0:
            sleep(timemore)
        return ret
    # 等待页面元素可见，返回该页面元素列表
    if type == 4:
        ret = wait.until(EC.visibility_of_any_elements_located(locator))
        if timemore > 0:
            sleep(timemore)
        return ret


# 日志记录信息
def e_log(info):
    now_time = time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time()))
    print(now_time + ":" + info)
    with open("error_msg.txt", "a", encoding='utf-8') as f:
        f.write(now_time + ":" + info)

