#!/bin/bash
#
# @brief   dist_py_module
# @version v3.1.1
# @date    Sun Jun 30 09:25:12 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 run_coverage.py
python3 ats_coverage.py -n dist_py_module
echo "Done"
