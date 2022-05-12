一、文件结构：
	Check_opensea_Item
		--Util_Tools.py   
		--Base_setting.py
		--check_result.py
二、文件解释：
	Util_Tools.py ：工具包，里面有封装超时时间等待元素定位和错误信息收集功能
	Base_setting.py：请求url地址和路径的基础配置文件
	check_result.py：检查脚本，有opensea中收藏Item的url获取功能和检查点击元数据刷新后的提醒信息"We've queued..."
	
三、设计思路：
	1、通过selenium的执行js滑动界面 "https://opensea.io/collection/catalog-lu-store"至每一个项目，然后点击项目做后续操作
	2、通过selenium的执行js循环滑动界面动态获取每一个项目，用url_list接收最终获取的数据；然后检查功能调用获取url_list并操作元素，来批量检查提示信息；
	3、基于2 本脚本实现一部分的Item获取url数据（通过界面获取数据时间较长，暂未测试出有接口来获取数据），直接调用数据来进行检查返回结果；
	4、由于脚本涉及界面元素较少，较好维护，暂不分层设计模式进行封装。