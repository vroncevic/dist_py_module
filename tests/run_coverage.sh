#!/bin/bash
#
# @brief   dist_py_module
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf fresh_new/ setup.py *.template *.cfg *. in *.toml
python3 -m coverage run -m --source=../dist_py_module unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
