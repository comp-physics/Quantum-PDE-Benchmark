# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Install library to site-packages
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='qpde-benchmark',
    version='0.0.1',
    author='Zhixin(Jack) Song',
    author_email='zsong300@gatech.edu',
    description='Benchmark quantum solutions to solve PDE.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    packages=[],
    install_requires=['scipy', 'networkx>=2.5', 'matplotlib', 'interval', 'tqdm'],
    python_requires='>=3.6, <4',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    project_urls={
        'Documentation': '',
        'Source': '',
        'Tracker': ''},)
