# Distributing Python Modules, Generate Module setup.py.

dist_py_module is toolset for generating setup.py for pyp.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

### INSTALLATION

To install this set of modules type the following:

```
cp -R ~/dist_py_module/bin/   /root/scripts/dist_py_module/ver.1.0/
cp -R ~/dist_py_module/conf/  /root/scripts/dist_py_module/ver.1.0/
cp -R ~/dist_py_module/log/   /root/scripts/dist_py_module/ver.1.0/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### GENERATION FLOW OF PYP SETUP

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/python-tool-docs/python_setup_flow.png)

### TOOL STRUCTURE

dist_py_module is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/dist_py_module/dev/python-tool-docs/python_setup.png)

Generator structure:

```
.
├── bin
│   ├── dist_py_module.py
│   ├── dist_py_module_run.py
│   └── setup
│       ├── gen_setup.py
│       ├── __init__.py
│       ├── read_template.py
│       └── write_template.py
├── conf
│   ├── dist_py_module.cfg
│   ├── dist_py_module_util.cfg
│   └── template
│       └── setup.template
└── log
    └── dist_py_module.log
```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by https://vroncevic.github.io/dist_py_module

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

