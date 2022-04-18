Generate setup.py
------------------

☯️ **dist_py_module** is toolset for generation of setup.py.

Developed in 🐍 `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|Python package linting| |Python code checker| |Documentation Status|
|GitHub issues| |GitHub contributors|

.. |Python package linting| image:: https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_python_package_linting?style=flat&label=dist_py_module%20python%20package%20linting
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python_package_linting.yml

.. |Python code checker| image:: https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_python_code_checker?style=flat&label=dist_py_module%20python%20code%20checker
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python_code_checker.yml

.. |Documentation Status| image:: https://readthedocs.org/projects/dist-py-module/badge/?version=latest
   :target: https://dist-py-module.readthedocs.io/en/latest/?badge=latest

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/graphs/contributors

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|Build Python2 Package| |Build Python3 Package|

.. |Build Python2 Package| image:: https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_build_python2_package?style=flat&label=dist_py_module%20build%20python2%20package
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_build_python2_package.yml

.. |Build Python3 Package| image:: https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_build_python3_package?style=flat&label=dist_py_module%20build%20python3%20package
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_build_python3_package.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/dist_py_module/releases

To install 📦 **dist_py_module** type the following

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

.. |GitHub docker checker| image:: https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_docker_checker?style=flat&label=dist_py_module%20docker%20checker
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_docker_checker.yml

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
    │   ├── dist_py_module.cfg
    │   ├── dist_py_module.logo
    │   ├── dist_py_module_util.cfg
    │   ├── project.yaml
    │   └── template/
    │       ├── MANIFEST.template
    │       ├── pyproject.template
    │       ├── setup_package.template
    │       ├── setup.template
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
