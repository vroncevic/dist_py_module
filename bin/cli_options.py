# encoding: utf-8
"""
cli_options - class CLI

Usage:
	from cli_options import CLI
	...

	app_cli = CLI(config)
	app_cli.process()

@date: Feb 23, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

import sys
from app.info import AppInfo
from setup.gen_setup import GenSetup
from app.option.option_parser import AppOptionParser

class CLI(AppOptionParser, AppInfo, GenSetup):
	"""
	Define class CLI with atribute(s) and method(s).
	Define options, process arguments and do operation.
	It defines:
		attribute:
			__OPS - tool options
		method:
			__init__ - create and initial instance
			process - procesing arguments and do operation
	"""

	__OPS = ["-g", "--gen", "-h", "--version"]

	def __init__(self, config):
		"""
		@summary: Basic Constructor
		@param config: configuration object (dictionary)
		"""
		AppInfo.__init__(self, config)
		AppOptionParser.__init__(
			self, "{0} {1}".format(
				AppInfo.get_version(self), AppInfo.get_build_date(self)
			),
			AppInfo.get_name(self), AppInfo.get_license(self)
		)
		AppOptionParser.add_option(
			self, CLI.__OPS[0], CLI.__OPS[1], dest="mod",
			help="Generate setup.py for module"
		)
		GenSetup.__init__(self)

	def process(self):
		"""
		@summary: Processing arguments from start and do operation
		@return: Success return true, else return false
		"""
		if len(sys.argv) > 1:
			op = sys.argv[1]
			if op not in CLI.__OPS:
				sys.argv.clear()
				sys.argv.append("-h")
		else:
			sys.argv.append("-h")
		opts, args = AppOptionParser.parse_args(self, sys.argv)
		if len(args) == 1 and opts.mod:
			status = GenSetup.gen_setup(self, "{0}".format(opts.mod))
			if status == True:
				print("Done")
			else:
				print("Failed to finish operation")

