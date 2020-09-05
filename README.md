# Distributing Python Modules, Generating Module setup.py.

**dist_py_module** is toolset for generating setup.py for pyp.

Developed in python code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/dist_py_module/workflows/Python%20package/badge.svg?branch=master)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/issues)
 [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/graphs/contributors)

### TABLE OF CONTENTS

- [Installation](#installation)
    * [Install using setuptools](#install-using-setuptools)
    * [Install using Docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Generation flow of project setup](#generation-flow-of-project-setup)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

### INSTALLATION

Navigate to release [page](https://github.com/vroncevic/dist_py_module/releases/tag/v1.0) download and extract release archive.

Currently there are two ways to install tool:
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### INSTALL USING SETUPTOOLS

To install this set of modules type the following:
```
tar xvzf dist_py_module-x.y.z.tar.gz
cd dist_py_module-x.y.z/
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
```

##### INSTALL USING DOCKER

You can use docker to load Dockerfile which contains all the commands
a user could call on the command line to assemble an image.

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities)

### GENERATION FLOW OF PYP SETUP

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup_flow.png)

### TOOL STRUCTURE

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

### DOCS

[![Documentation Status](https://readthedocs.org/projects/dist_py_module/badge/?version=latest)](https://dist_py_module.readthedocs.io/en/latest/?badge=latest)

More documentation and info at:

* [dist_py_module.readthedocs.io](https://dist_py_module.readthedocs.io/en/latest/)

### COPYRIGHT AND LICENCE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/dist_py_module](https://vroncevic.github.io/dist_py_module)

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

