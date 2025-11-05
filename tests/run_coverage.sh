#!/bin/bash
#
# @brief   dist_py_module
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov dist_py_module_coverage.xml dist_py_module_coverage.json .coverage
rm -rf fresh_new/ setup.py *.template *.cfg *. in *.toml
python3 -m coverage run -m --source=../dist_py_module unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o dist_py_module_coverage.xml 
python3 -m coverage json -o dist_py_module_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n dist_py_module
rm htmlcov/.gitignore
echo "Done"