# coding=utf-8
import configparser
import subprocess
import logging 
import os

class comctrl(object):
	"""docstring for ClassName"""
	def __init__(self, control_dir=None, control_com='3'):
		self.control_dir = control_dir if control_dir else os.path.join(os.getcwd(), 'scduinoM.exe')
		self.control_com = control_com
		if not(os.path.isfile(self.control_dir)):	
			raise IOError('the path of the exe is not correct!')
	def poweroff(self):
		cp = configparser.ConfigParser()
		cp.read('box.cfg')
		compath = cp.get('CPE_CLI','compath')
		comport = cp.get('CPE_CLI','comport')
		cmd = '"' + compath + '" ' + comport + ' no pw'
		sub=subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
		sub.wait()
		stdout,stderr = sub.communicate()
		if stderr:
			raise IOError(stderr)
		return stdout

	def poweron(self):
		cp = configparser.ConfigParser()
		cp.read('box.cfg')
		compath = cp.get('CPE_CLI','compath')
		comport = cp.get('CPE_CLI','comport')
		cmd = '"' + compath + '" '+ comport + ' nc pw'
		sub=subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
		sub.wait()
		stdout,stderr = sub.communicate()
		if stderr:
			raise IOError(stderr)
		out = sub.stdout.decode('utf-8')
		info1 = "poweroff at %s s" %i
		return stdout

'''		
cp = configparser.ConfigParser() 
cp.read('box.cfg')
compath = cp.get('CPE_CLI','compath')
comport = cp.get('CPE_CLI','comport')

cmd = '"'+compath+'"'

sub=subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
sub.wait()
out = sub.stdout.read().decode('utf-8')
i = 100
info1 ="This is %sst time reboot" %i

logging.basicConfig(level=logging.INFO,filename='ping.log',format='[%(asctime)s] -%(message)s')
#logging.info(info1)
#logging.info(comport)
#logging.info(compath)
logging.info(out)
'''

if __name__=='__main__':
    print("this module is to control thr connected dut automaticlly")



