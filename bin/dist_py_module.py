# encoding: utf-8
"""
dist_py_module - class DistPyModule

Usage:
	from dist_py_module import DistPyModule

	tool = DistPyModule()
	tool.process()

@date: Feb 23, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

import sys
from app.base import Base
from setup.gen_setup import GenSetup
from os.path import dirname, realpath

class DistPyModule(Base, GenSetup):
	"""
	Define class DistPyModule with atribute(s) and method(s).
	Load a settings, create a CL interface and run operation(s).
	It defines:
		attribute:
			__CONFIG - Configuration file path
			__OPS -  Tool options (list)
		method:
			__init__ - Initial constructor
			process - Process and run tool option
	"""

	__CONFIG = "/../conf/dist_py_module.cfg"
	__OPS = ["-g", "--gen", "-h", "--version"]

	def __init__(self):
		"""
		@summary: Basic constructor
		"""
		cdir = dirname(realpath(__file__))
		base_config_file = "{0}{1}".format(cdir, DistPyModule.__CONFIG)
		Base.__init__(self, base_config_file)
		if self.get_tool_status():
			self.add_new_option(
				DistPyModule.__OPS[0], DistPyModule.__OPS[1], dest="mod",
				help="Generate setup.py module"
			)
			GenSetup.__init__(self)

	def process(self):
		"""
		@summary: Process and run tool option
		"""
		if self.get_tool_status():
			if len(sys.argv) > 1:
				op = sys.argv[1]
				if op not in DistPyModule.__OPS:
					sys.argv = []
					sys.argv.append("-h")
			else:
				sys.argv.append("-h")
			opts, args = self.parse_args(sys.argv)
			if len(args) == 1 and opts.mod:
				status = self.gen_setup("{0}".format(opts.mod))
				if status == True:
					print("Done!\n")
			else:
				print("Failed to process and run option!\n")
		else:
			print("Tool is not operational!\n")

