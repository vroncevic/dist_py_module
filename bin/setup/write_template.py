# encoding: utf-8
"""
setup.write_template - class WriteTemplate

Usage:
	from setup.write_template import WriteTemplate

	template_writter = WriteTemplate()
	# ...
	status = template_writter.write(setup_content, package_name)
	if status == True:
		# operation done

@date: Feb 24, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from os import getcwd, chmod
from string import Template

class WriteTemplate(object):
	"""
	Define class WriteTemplate with atribute(s) and method(s).
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
		"""
		@summary: Basic constructor
		"""
		pass

	def write(self, setup_content, package_name):
		"""
		@summary: Write template content with parameters to file setup.py
		@param setup_content: Template content
		@param package_name: Parameter package name
		@return: Success return true, else return false
		"""
		cdir = getcwd()
		setup_file = "{0}/{1}".format(cdir, WriteTemplate.__SETUP_FILE)
		package = {"pkg":"{0}".format(package_name)}
		try:
			template = Template(setup_content)
			sfile = open(setup_file, "w")
			sfile.write(template.substitute(package))
		except (IOError, KeyError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
			sfile.close()
			return False
		else:
			sfile.close()
			chmod(setup_file, 0o666)
			return True

