import time
import operator as op
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import subprocess
import logging
import configparser

class longrun(object):
	"""docstring for longrun"""
	def __init__(self, url,user,pwd,num):
		super(longrun, self).__init__()
		self.url = url
		self.user = user
		self.pwd = pwd
		self.num = num
	def open(self):
		web = webdriver.Chrome()
		web.get(self.url)
		input = web.find_element_by_xpath('//*[@id="rightContent"]/div[2]/div[1]/input')
		input.send_keys(self.user)
		input = web.find_element_by_xpath('//*[@id="rightContent"]/div[2]/div[2]/input')
		input.send_keys(self.pwd)
		click1 = web.find_element_by_id('start').click()
		time.sleep(2)
		self.ver = web.find_element_by_id('sys_firmware_version').text
		time.sleep(2)
		self.uptime = web.find_element_by_id('sys_uptime').text
		time.sleep(2)


	def upgrade(self):
		self.open()
		click1 = web.find_element_by_id('lang700035').click()
		time.sleep(2)
		click1 = web.find_element_by_id('lang905002').click()
		time.sleep(2)
		filepath1 = cp.get('FWFile','Path')+cp.get('FWFile','Testfw') #升级测试fw
		filepath2 = cp.get('FWFile','Path')+cp.get('FWFile','99fw') #升级99fw
		filearr = [filepath2,filepath1]
		uploadfw = web.find_element_by_xpath('/html/body/div[1]/section/article/div/div[2]/div[3]/div[2]/div/form/input[3]').send_keys(filearr[i%2])
		time.sleep(5)
		click1 = web.find_element_by_id('installUpdate').click()
		time.sleep(5)
		click1 = web.find_element_by_xpath('/html/body/div[1]/section/article/div/div[3]/div/div[2]/input').click()
		time.sleep(200)
		web.close()




	def reboot(self):
		self.open()
		



if __name__ == '__main__':
	a = longrun('http://www.baidu.com','admin','admin','1')
	a.upgrade()
