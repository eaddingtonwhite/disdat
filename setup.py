#
# Copyright 2015, 2016  Human Longevity, Inc.
#
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
#
from setuptools import setup, find_packages
import os


def find_version():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'disdat','VERSION')) as version_file:
        version = version_file.read().strip()
    return version

setup(
    name='disdat',
    version=find_version(),
    description='DisDat: bundled data science',
    author='Ken Yocum',
    author_email='kyocum@gmail.com',
    url='https://github.com/disdat',

    # Choose your license
    license='Apache License, version 2.0',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Data Scientists and Developers',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Natural Language :: English',
    ],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['tests*',
                                    'infrastructure.aws',
                                    'infrastructure.kubernetes',
                                    'infrastructure.tests*']),

    # Include non-python files found in each package in the install, if in your MANIFEST.in
    include_package_data=True,

    # If any package contains other resource files, include them here.
    # We copy config/disdat so 'dsdt init' still runs from an installed
    # .egg.  This package_data only works if you're not using "sdist"
    # Otherwise only MANIFEST.in actually works, and then only if include_package_data=True
    package_data={
        '': ['*.json'],
        'disdat': [
            'config/disdat/*',
            'VERSION',
        ],
        'infrastructure': [
            'Dockerfiles/hyperframe_def/*'
            'dockerizer/Makefile',
            'dockerizer/Dockerfiles/*',
            'dockerizer/bin/*.py',
            'dockerizer/kickstart/bin/*',
            'dockerizer/kickstart/etc/*',
        ],
    },

    exclude_package_data={
        'disdat': [
            'dockerizer/kickstart/bin/*.pyc',
        ]
    },

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed.

    install_requires=['python-dateutil<2.7', # python-dateutil<2.7.0,>=2.1 is required by set(['botocore']), 2.7 broke things on March 12, 2018
                      'boto3',
                      'boto3-session-cache',
                      'termcolor',
                      'docker',
                      'pyodbc',
                      'luigi>=2.5.0',
                      'pandas==0.20.3', # 0.21.0 causes pyinstaller built binary to crap out
                      'enum34>=',
                      'sqlalchemy>=',
                      'protobuf>='
                      ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e '.[dev, rel]'
    extras_require={
        'dev': [
            'pytest',
            'ipython<6.0',
            'mock',
            'nose',
            'pylint',
            'coverage'
        ],
        'rel': [
            'wheel',
            'sphinx',
            'sphinx_rtd_theme',
            'pyinstaller'
        ]
    },

    entry_points={
        'console_scripts': [
            'dsdt = disdat.dsdt:main',
        ]
    },

)
