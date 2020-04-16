import configparser
import subprocess
import logging 
import os

logging.basicConfig(level=logging.INFO,filename='ping.log',format='[%(asctime)s] -%(message)s')
class ping(object):
	"""durl,timeouttring for ping"""
	def __init__(self, url='www.baidu.com'):
		self.url = url

	def test(self):
		cmd = 'ping.exe ' + self.url
		sub = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
		sub.wait()
		stdout,stderr = sub.communicate()
		if stderr:
			raise IOError(stderr)
		return stdout.decode('utf-8')

if __name__ == '__main__':
	t = ping('www.sina.com')
	str1 = t.test()
	print(str1)