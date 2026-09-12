#!/bin/bash
#
# @brief   dist_py_module
# @version 3.1.4
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py dist_py_module
pylint dist_py_module > dist_py_module.report
echo "Done"
