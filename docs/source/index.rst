Distributing Python Modules, Generating Module setup.py.
=========================================================

.. toctree::
 :hidden:

 modules
 self


**dist_py_module** is toolset for generating setup.py for pyp.

Developed in python code: **100%**.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|GitHub issues| |Documentation Status| |GitHub contributors|

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/dist_py_module/badge/?version=latest
   :target: https://dist_py_module.readthedocs.io/projects/dist_py_module/en/latest/?badge=latest

Installation
-------------

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/dist_py_module/releases

To install **dist_py_module** type the following:

.. code-block:: bash

    tar xvzf dist_py_module-x.y.z.tar.gz
    cd dist_py_module-x.y.z/
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_data
    python setup.py install_egg_info

Dependencies
-------------

**dist_py_module** requires next modules and libraries:
    sh_util `https://github.com/vroncevic/sh_util <https://github.com/vroncevic/sh_util>`_

GENERATION FLOW OF PROJECT SETUP
----------------------------------

Base flow of generation process:

.. image:: https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup_flow.png

Tool structure
---------------

**dist_py_module** is based on Template mechanism:

.. image:: https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup.png

Code structure:

.. code-block:: bash

   .
   ├── bin/
   │   ├── dist_py_module.py
   │   ├── dist_py_module_run.py
   │   └── setup/
   │       ├── gen_setup.py
   │       ├── __init__.py
   │       ├── read_template.py
   │       └── write_template.py
   ├── conf/
   │   ├── dist_py_module.cfg
   │   ├── dist_py_module_util.cfg
   │   └── template/
   │       └── setup.template
   └── log/
        └── dist_py_module.log

Copyright and licence
-----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/dist_py_module <https://vroncevic.github.io/dist_py_module>`_

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

