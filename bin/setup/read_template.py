# encoding: utf-8
"""
setup.read_template - class ReadTemplate

Usage:
	from setup.read_template import ReadTemplate

	template_reader = ReadTemplate()
	content_template = template_reader.read()
	if content_template != None:
		# operate with content

@date: Feb 24, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from os.path import dirname, realpath

class ReadTemplate:
	"""
	Define class ReadTemplate with atribute(s) and method(s).
	Read a template file (setup.template) and return a string representation.
	It defines:
		attribute:
			__TEMPLATE - template file path
			__template - absolute template file path
		method:
			__init__ - create and initial instance
			read - read a template and return a string representation
	"""

	__TEMPLATE = "/../../conf/template/setup.template"

	def __init__(self):
		"""
		@summary: Basic constructor (initial absolute template file path)
		"""
		cdir = dirname(realpath(__file__))
		self.__template = "{0}{1}".format(cdir, ReadTemplate.__TEMPLATE)

	def read(self):
		"""
		@summary: Read a template file and return a content
		@return: string text code
		"""
		try:
			tfile = open(self.__template, "r")
			setup_content = tfile.read()
			tfile.close()
			return setup_content
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
			return None

