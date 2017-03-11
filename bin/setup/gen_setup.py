# encoding: utf-8
"""
setup.gen_setup - class GenSetup

Usage:
	from setup.gen_setup import GenSetup

	generator = GenSetup()
	status = generator.gen_setup("configuration")
	if status:
		# operation done

@date: Feb 23, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from setup.read_template import ReadTemplate
from setup.write_template import WriteTemplate

class GenSetup(ReadTemplate, WriteTemplate):
	"""
	Define class GenSetup with atribute(s) and method(s).
	Generate module file setup.py by template and parameters.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			gen_setup - Generate module file setup.py
	"""

	def __init__(self):
		"""
		@summary: Basic constructor
		"""
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)

	def gen_setup(self, package_name):
		"""
		@summary: Generate setup.py by template and parameters
		@param package_name: Parameter package name
		@return: Success return true, else return false
		"""
		status = False
		setup_content = self.read()
		if setup_content != None:
			status = self.write(setup_content, package_name)
		return status

