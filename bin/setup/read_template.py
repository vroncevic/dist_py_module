# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from os.path import dirname, realpath

class ReadTemplate(object):
	"""
	Define class ReadTemplate with attribute(s) and method(s).
	Read a template file (setup.template) and return a content.
	It defines:
		attribute:
			__TEMPLATE - Template file path
			__template - Absolute template file path
		method:
			__init__ - Initial constructor
			read - Read a template and return a string representation
	"""

	__TEMPLATE = "/../../conf/template/setup.template"

	def __init__(self):
		current_dir = dirname(realpath(__file__))
		self.__template = "{0}{1}".format(current_dir, ReadTemplate.__TEMPLATE)

	def read(self):
		"""
		:return: Template content for setup module
		:rtype: str or NoneType
		"""
		try:
			template_file = open(self.__template, "r")
			setup_content = template_file.read()
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		else:
			template_file.close()
			return setup_content
		return None
