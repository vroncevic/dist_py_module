# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from os import getcwd, chmod
from string import Template

class WriteTemplate(object):
	"""
	Define class WriteTemplate with attribute(s) and method(s).
	Write template content with parameters to a file setup.py.
	It defines:
		attribute:
			__SETUP_FILE - File name for setup file
		method:
			__init__ - Initial constructor
			write - Write a template content with parameters to a file setup.py
	"""

	__SETUP_FILE = "setup.py"

	def __init__(self):
		pass

	def write(self, setup_content, package_name):
		"""
		:param setup_content: Template content
		:type: str
		:param package_name: Parameter package name
		:type: str
		:return Boolean status
		:rtype: bool
		"""
		current_dir = getcwd()
		setup = "{0}/{1}".format(current_dir, WriteTemplate.__SETUP_FILE)
		package = {"pkg":"{0}".format(package_name)}
		try:
			template = Template(setup_content)
			setup_file = open(setup, "w")
			setup_file.write(template.substitute(package))
		except (IOError, KeyError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		else:
			setup_file.close()
			chmod(setup, 0o666)
			return True
		return False
