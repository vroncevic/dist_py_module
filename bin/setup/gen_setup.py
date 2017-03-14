# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from setup.read_template import ReadTemplate
from setup.write_template import WriteTemplate

class GenSetup(ReadTemplate, WriteTemplate):
	"""
	Define class GenSetup with attribute(s) and method(s).
	Generate module file setup.py by template and parameters.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			gen_setup - Generate module file setup.py
	"""

	def __init__(self):
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)

	def gen_setup(self, package_name):
		"""
		:param package_name: Parameter package name
		:return: Boolean status
		:rtype: bool
		"""
		status = False
		setup_content = self.read()
		if setup_content:
			status = self.write(setup_content, package_name)
		return status
