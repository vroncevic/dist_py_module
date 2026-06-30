Generate setup.py
------------------

**dist_py_module** is toolset for generation of setup.py.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|python package checker| |python checker| |documentation status|
|github issues| |github contributors|

.. |python package checker| image:: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python_checker.yml

.. |python checker| image:: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_package.yml

.. |documentation status| image:: https://readthedocs.org/projects/dist-py-module/badge/?version=latest
   :target: https://dist-py-module.readthedocs.io/en/latest/?badge=latest

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg
   :target: https://github.com/vroncevic/dist_py_module/graphs/contributors

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|build python3 package|

.. |build python3 package| image:: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/dist_py_module/releases

To install **dist_py_module** type the following

.. code-block:: bash

    tar xvzf dist_py_module-x.y.z.tar.gz
    cd dist_py_module-x.y.z/
    # pyton3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_data
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install dist-py-module

Dependencies
-------------

**dist_py_module** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**dist_py_module** is based on OOP.

Code structure

.. code-block:: bash

    dist_py_module/
         ├── application/
         │   ├── __init__.py
         │   ├── service.py
         │   └── service_bundle.py
         ├── dist_py_module_bundle.py
         ├── domain/
         │   ├── __init__.py
         │   ├── models.py
         │   └── ports/
         │       ├── ifile_gen.py
         │       ├── ifile_writer.py
         │       ├── __init__.py
         │       └── itemplate_provider.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli.py
         │   ├── cli_bundle.py
         │   ├── config/
         │   │   ├── dist_py_module.cfg
         │   │   └── dist_py_module.logo
         │   ├── file_writer.py
         │   ├── gen_setup_command.py
         │   ├── icli.py
         │   ├── icli_command.py
         │   ├── __init__.py
         │   ├── template_provider.py
         │   └── templates/
         │       └── setup.template
         └── __init__.py
     7 directories, 23 files

Usage
-----

Install package

.. code-block:: bash

    pip3 install dist_py_module

Prepare main entry point by downloading `main.py`_.

.. _main.py: https://raw.githubusercontent.com/vroncevic/dist_py_module/master/main.py

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/dist_py_module/master/main.py

Running tool for creating new distributing py module

.. code-block:: bash

    mkdir -p demo/mytool/

    python3 main.py setup --package-name "dist_py_module" --version "3.1.0" --description "Package for distributing Python packages." --author "Vladimir Roncevic" --email "elektron.ronca@gmail.com" --github "vroncevic" --license "GNU General Public License (GPL)" --with-readme "True"

Copyright and licence
-----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2017 - 2026 by `vroncevic.github.io/dist_py_module <https://vroncevic.github.io/dist_py_module>`_

**dist_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
