# Distributing Python Modules, generating Module setup.py

**dist_py_module** is toolset for generating setup.py for pyp.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/dist_py_module/workflows/Python%20package/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of pyp setup](#generation-flow-of-pyp-setup)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/dist_py_module/workflows/Install%20Python2%20Package%20dist_py_module/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/dist_py_module/workflows/Install%20Python3%20Package%20dist_py_module/badge.svg?branch=master)

Navigate to release [page](https://github.com/vroncevic/dist_py_module/releases/tag/v1.0) download and extract release archive.

Currently there are two ways to install tool:
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using setuptools

To install this set of modules type the following:
```
tar xvzf dist_py_module-x.y.z.tar.gz
cd dist_py_module-x.y.z/
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
```

##### Install using docker

You can use docker to load Dockerfile which contains all the commands
a user could call on the command line to assemble an image.

[![dist_py_module docker checker](https://github.com/vroncevic/dist_py_module/workflows/dist_py_module%20docker%20checker/badge.svg)](https://github.com/vroncevic/dist_py_module/actions?query=workflow%3A%22dist_py_module+docker+checker%22)

### Dependencies

This module requires these other modules and libraries:

* ats_utilities [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities)

### Generation flow of pyp setup

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup_flow.png)

### Tool structure

**dist_py_module** is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup.png)

Generator structure:

```
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
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/dist_py_module/badge/?version=latest)](https://dist_py_module.readthedocs.io/en/latest/?badge=latest)

More documentation and info at:

* [dist_py_module.readthedocs.io](https://dist_py_module.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/dist_py_module](https://vroncevic.github.io/dist_py_module)

**dist_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
