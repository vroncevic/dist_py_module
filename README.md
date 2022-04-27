<img align="right" src="https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/dist_py_module_logo.png" width="25%">

# Generate setup.py

☯️ **dist_py_module** is toolset for generation of setup.py.

Developed in 🐍 **[python](https://www.python.org/)** code.

[![codecov](https://codecov.io/gh/vroncevic/dist_py_module/branch/dev/graph/badge.svg?token=Y6VSNLJ45R)](https://codecov.io/gh/vroncevic/dist_py_module) [![circleci](https://circleci.com/gh/vroncevic/dist_py_module/tree/master.svg?style=svg)](https://circleci.com/gh/vroncevic/dist_py_module/tree/master)

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![dist_py_module python checker](https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_python_checker?style=flat&label=dist_py_module%20python%20checker)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python_checker.yml) [![dist_py_module package checker](https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_package_checker?style=flat&label=dist_py_module%20package%20checker)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of pyp setup](#generation-flow-of-pyp-setup)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![Development environment](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/debtux.png)

[![dist_py_module python2 build](https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_python2_build?style=flat&label=dist_py_module%20python2%20build)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python2_build.yml) [![dist_py_module python3 build](https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_python3_build?style=flat&label=dist_py_module%20python3%20build)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python3_build.yml)

Currently there are four ways to install framework
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python 📦 is located at **[pypi.org](https://pypi.org/project/dist-py-module/)**.

You can install by using pip

```bash
# python2
pip install dist-py-module
# python3
pip3 install dist-py-module
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/dist_py_module/releases)** download and extract release archive 📦.

To install **dist-py-module** 📦 run

```bash
tar xvzf dist-py-module-x.y.z.tar.gz
cd dist-py-module-x.y.z
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 -m build -s --no-isolation --wheel
pip2 install dist/dist-py-module-x.y.z-py2-none-any.whl
rm -f get-pip.py
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build -s --no-isolation --wheel
pip3 install dist/dist-py-module-x.y.z-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to release **[page](https://github.com/vroncevic/dist_py_module/releases/)** download and extract release archive 📦.

To install **dist_py_module** 📦 type the following

```bash
tar xvzf dist_py_module-x.y.z.tar.gz
cd dist_py_module-x.y.z/
# python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container 🚢.

[![dist_py_module docker checker](https://img.shields.io/github/workflow/status/vroncevic/dist_py_module/dist_py_module_docker_checker?style=flat&label=dist_py_module%20docker%20checker)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_docker_checker.yml)

### Dependencies

**dist_py_module** requires next modules and libraries

* [dist-py-module - Python App/Tool/Script Utilities](https://pypi.org/project/dist-py-module/)

### Generation flow of pyp setup

Base flow of generation process

![Setup generation flow](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup_flow.png)

### Tool structure

**dist_py_module** is based on OOP.

![Setup tool flow](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/python_setup.png)

🧰 Generator structure

```bash
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

5 directories, 15 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/dist-py-module/badge/?version=latest)](https://dist-py-module.readthedocs.io/en/latest/?badge=latest)

📗 More documentation and info at

* [dist_py_module.readthedocs.io](https://dist_py_module.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

🌎 🌍 🌏 [Contributing to codecipher](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/dist_py_module](https://vroncevic.github.io/dist_py_module)

**dist_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
