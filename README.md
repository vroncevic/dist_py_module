# Generate setup.py

<img align="right" src="https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/dist_py_module_logo.png" width="25%">

**dist_py_module** is toolset for generation of setup.py.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![dist_py_module python checker](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python_checker.yml/badge.svg)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python_checker.yml) [![dist_py_module package checker](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_package_checker.yml/badge.svg)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/dist_py_module.svg)](https://github.com/vroncevic/dist_py_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Code coverage](#code-coverage)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/debtux.png)

[![dist_py_module python3 build](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python3_build.yml/badge.svg)](https://github.com/vroncevic/dist_py_module/actions/workflows/dist_py_module_python3_build.yml)

Currently there are four ways to install framework
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/dist-py-module/)**.

You can install by using pip

```bash
# python3
pip3 install dist-py-module
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/dist_py_module/releases)** download and extract release archive.

To install **dist-py-module** run

```bash
tar xvzf dist-py-module-x.y.z.tar.gz
cd dist-py-module-x.y.z
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

Navigate to release **[page](https://github.com/vroncevic/dist_py_module/releases/)** download and extract release archive.

To install **dist_py_module** type the following

```bash
tar xvzf dist_py_module-x.y.z.tar.gz
cd dist_py_module-x.y.z/
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**dist_py_module** requires next modules and libraries

* [dist-py-module - Python App/Tool/Script Utilities](https://pypi.org/project/dist-py-module/)

### Tool structure

**dist_py_module** is based on OOP.

Generator structure

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
          ├── py.typed
          └── run/
              └── dist_py_module_run.py
    
    6 directories, 16 files
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `dist_py_module/__init__.py` | 70 | 14 | 80% |
| `dist_py_module/pro/__init__.py` | 81 | 3 | 96% |
| `dist_py_module/pro/read_template.py` | 45 | 2 | 96% |
| `dist_py_module/pro/write_template.py` | 54 | 4 | 93% |
| **Total** | 250 | 23 | 91% |

### Docs

[![Documentation Status](https://readthedocs.org/projects/dist-py-module/badge/?version=latest)](https://dist-py-module.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [dist_py_module.readthedocs.io](https://dist-py-module.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to codecipher](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/dist_py_module](https://vroncevic.github.io/dist_py_module)

**dist_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
