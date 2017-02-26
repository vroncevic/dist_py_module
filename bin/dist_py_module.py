# encoding: utf-8
"""
dist_py_module - class DistPyModule

Usage:
	from dist_py_module import DistPyModule

	tool = DistPyModule()
	tool.run()

@date: Feb 23, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from settings import Settings
from cli_options import CLI

class DistPyModule(object):
	"""
	Define class DistPyModule with atribute(s) and method(s).
	Load a settings, create a CL interface and run operation.
	It defines:
		attribute:
			__app_cli - Command line interface parser
		method:
			__init__ - Create and initial instance
			run - Run tool
	"""

	def __init__(self):
		"""
		@summary: Basic constructor
		"""
		config_reader = Settings()
		config = config_reader.get_configuration()
		if config != None:
			self.__app_cli = CLI(config)

	def run(self):
		"""
		@summary: Run command line interface
		"""
		self.__app_cli.process()

