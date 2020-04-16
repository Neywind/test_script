# coding=utf-8
import time
import operator as op
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
import configparser
cp = configparser.ConfigParser() 
cp.read('box.cfg')					#导入cfg文档
url = cp.get('GUI','url')
logging.basicConfig(level=logging.INFO,filename='test.log',format='[%(asctime)s] -%(message)s')
for i in range(1,100):
	str1 = str(i)+'st time to upgrade'
	logging.info(str1)
	driver1 = webdriver.Chrome()		#配置浏览器控制脚本
	driver1.get(url)
	'''
	#修改登陆页面属性
	js1 = 'document.getElementById("login-middle")[0].setAttribute("display","block")'
	js2 = 'document.getElementById("login-middle")[0].setAttribute("visiblity","visible")'

	js3 = 'document.getElementById("TANGRAM__PSP_4__qrcode").setAttribute("display","none")'
	js4 = 'document.getElementById("TANGRAM__PSP_4__qrcode").setAttribute("visiblity","hidden")'
	driver1.execute_script(js3)
	driver1.execute_script(js4)

	driver1.execute_script(js1)
	driver1.execute_script(js2)
	'''
	username = cp.get('GUI','user')
	password = cp.get('GUI','pw')
	input = driver1.find_element_by_xpath('//*[@id="rightContent"]/div[2]/div[1]/input')
	input.send_keys(username)
	input = driver1.find_element_by_xpath('//*[@id="rightContent"]/div[2]/div[2]/input')
	input.send_keys(password)
	click1 = driver1.find_element_by_id('start').click()
	time.sleep(2)
	driver1.find_element_by_xpath('/html/body/div[1]/center/div/div/div/div[2]/center/table[2]/tbody/tr/td[3]/div').click()
	time.sleep(2)
	ver = driver1.find_element_by_id('sys_firmware_version').text
	logging.info('version is'+str(ver))
	time.sleep(2)
	uptime = driver1.find_element_by_id('sys_uptime').text
	logging.info('uptime is '+str(uptime))
	time.sleep(2)
	click1 = driver1.find_element_by_id('lang700035').click()
	time.sleep(2)
	click1 = driver1.find_element_by_id('lang905002').click()
	time.sleep(2)
	filepath1 = cp.get('FWFile','Path')+cp.get('FWFile','Testfw') #升级测试fw
	filepath2 = cp.get('FWFile','Path')+cp.get('FWFile','99fw') #升级99fw
	if (i%2) ==0:
		uploadfw = driver1.find_element_by_xpath('/html/body/div[1]/section/article/div/div[2]/div[3]/div[2]/div/form/input[3]').send_keys(filepath1)
	else:
		uploadfw = driver1.find_element_by_xpath('/html/body/div[1]/section/article/div/div[2]/div[3]/div[2]/div/form/input[3]').send_keys(filepath2)
	time.sleep(5)
	click1 = driver1.find_element_by_id('installUpdate').click()
	time.sleep(5)
	click1 = driver1.find_element_by_xpath('/html/body/div[1]/section/article/div/div[3]/div/div[2]/input').click()
	time.sleep(200)
	driver1.close()
	'''
click1 = driver1.find_element_by_id('switchAccountLogin').click()
time.sleep(3)
#driver1.refresh()
input = driver1.find_element_by_name('email')
input.send_keys(username)
input = driver1.find_element_by_name('password')
input.send_keys(password)
button = driver1.find_element_by_id('dologin').click()

logging.basicConfig(level=logging.INFO,filename='test.log',format='%(asctime)s-%(message)s')
logging.info(cp.get('GUI','user'))
logging.info(cp.get('GUI','pw'))

driver1.close()

for i in range(1,2):
	browser = webdriver.Chrome()
	url = 'http://www.baidu.com'
	browser.get(url)
	logging.basicConfig(level=logging.INFO,filename='system.log',format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	str1='Time %d start'%i 
	logging.info(str1)
	input = browser.find_element_by_name('wd')
	input.send_keys('selenium学习')
	input.send_keys(Keys.ENTER)
	time.sleep(3)
	input = browser.find_element_by_name('wd')
	input.clear()ss
	input.send_keys('bilibili')
	input.send_keys(Keys.ENTER)
	time.sleep(3)
	
	print(browser.current_url)
	print(browser.get_cookies())
	

	browser.close()
	str2='Time %d successfully'%i
	logging.info(str2)
'''
'''
logging.basicConfig(level=logging.INFO,filename='system.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
browser = webdriver.Chrome()
url = 'http://localhost'
browser.get(url)
input = browser.find_element_by_name('test')
browser.execute_script('arguments[0].value="Arimaican"',input)
driver1 = browser.find_element_by_name('button')
driver1.click()
alert1 = browser.switch_to.alert
getvalue1 = alert1.text
time.sleep(3)
alert1.accept()
time.sleep(3)
browser.close()
logging.info(getvalue1)
if(op.eq(getvalue1,'SC_1913')):
	print('error')
	logging.info('Error')
else:
	print('No error')
	logging.info('Success')
print(getvalue1)
'''