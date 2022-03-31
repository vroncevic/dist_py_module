Generate setup.py
------------------

**dist_py_module** is toolset for generation of setup.py.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/dist_py_module/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/dist_py_module/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/dist_py_module/badge/?version=latest
   :target: https://dist_py_module.readthedocs.io/projects/dist_py_module/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/dist_py_module/workflows/Install%20Python2%20Package%20dist_py_module/badge.svg
   :target: https://github.com/vroncevic/dist_py_module/workflows/Install%20Python2%20Package%20dist_py_module/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/dist_py_module/workflows/Install%20Python3%20Package%20dist_py_module/badge.svg
   :target: https://github.com/vroncevic/dist_py_module/workflows/Install%20Python3%20Package%20dist_py_module/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/dist_py_module/releases

To install **dist_py_module** type the following

.. code-block:: bash

    tar xvzf dist_py_module-x.y.z.tar.gz
    cd dist_py_module-x.y.z/
    # python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_data
    python setup.py install_egg_info
    # pyton3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_data
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton2
    pip install dist-py-module
    # pyton3
    pip3 install dist-py-module

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/dist_py_module/workflows/dist_py_module%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/dist_py_module/actions?query=workflow%3A%22dist_py_module+docker+checker%22

Dependencies
-------------

**dist_py_module** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Generation flow of project setup
---------------------------------

Base flow of generation process

.. image:: https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup_flow.png

Tool structure
---------------

**dist_py_module** is based on OOP.

.. image:: https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup.png

Code structure

.. code-block:: bash

    dist_py_module/
    ├── conf/
    │   ├── dist_py_module.logo
    │   ├── dist_py_module.cfg
    │   ├── dist_py_module_util.cfg
    │   ├── project.yaml
    │   └── template/
    │       ├── setup_package.template
    │       └── setup_tool.template
    ├── __init__.py
    ├── log/
    │   └── dist_py_module.log
    ├── pro/
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    └── run/
        └── dist_py_module_run.py

Copyright and licence
-----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/dist_py_module <https://vroncevic.github.io/dist_py_module>`_

**dist_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
