# -*- coding: utf-8 -*-
import logging
import telnetlib
import time
import sys
import configparser
tn = telnetlib.Telnet()

class upgrade(object):
	"""docstring for upgrade"""
	def __init__(self, arg):
		super(upgrade, self).__init__()
		self.arg = arg
		