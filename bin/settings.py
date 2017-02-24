# encoding: utf-8
"""
settings - class Settings

Usage:
	from settings import Settings

	config_reader = Settings()
	info = config_reader.get_configuration()
	if info != None:
		# use configuration
	else:
		# exit from App/Tool/Script

@date: Feb 23, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.cfg.cfg2object import Cfg2Object
from os.path import dirname, realpath

class Settings(Cfg2Object):
	"""
	Define class Settings with atribute(s) and method(s).
	Loading a settings from a configuration file.
	It defines:
		attribute:
			__CONFIG - postfix part of configuration file path
		method:
			__init__ - create and initial instance
	"""

	__CONFIG = "/../conf/dist_py_module.cfg"

	def __init__(self):
		cdir = dirname(realpath(__file__))
		cfg = "{0}{1}".format(cdir, Settings.__CONFIG)
		Cfg2Object.__init__(self, cfg)

