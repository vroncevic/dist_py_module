# Copyright 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:10
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
 tree \
 htop \
 wget \
 unzip \
 ca-certificates \
 openssl \
 python \
 python-pip \
 python-wheel \
 libyaml-dev
 
RUN pip install --upgrade setuptools
RUN wget https://github.com/vroncevic/ats_utilities/archive/v1.0.3.zip
RUN unzip v1.0.3.zip
RUN find /ats_utilities-1.0.3/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN cd /ats_utilities-1.0.3/ && pip install -r requirements.txt
RUN cd /ats_utilities-1.0.3/ && python setup.py install_lib && python setup.py install_egg_info
RUN rm -rf /ats_utilities-1.0.3/ v1.0.3.zip
RUN mkdir /dist_py_module/
COPY dist_py_module /dist_py_module/
COPY requirements.txt /
COPY setup.py /
RUN pip install -r requirements.txt
RUN rm -f requirements.txt
RUN find /dist_py_module/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN python setup.py install_lib && python setup.py install_data && python setup.py install_egg_info
RUN rm -rf /dist_py_module/
RUN rm -f setup.py
RUN chmod -R 755 /usr/local/lib/python2.7/dist-packages/dist_py_module/
RUN tree /usr/local/lib/python2.7/dist-packages/dist_py_module/
RUN ln -s /usr/bin/dist_py_module_run.py /usr/bin/dist_py_module
