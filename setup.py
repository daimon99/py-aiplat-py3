# encoding=utf8
from setuptools import setup
from py_aiplat_py3 import __version__

version = __version__

long_description = '腾讯ai的python3版本'

EXCLUDE_FROM_PACKAGES = []

setup(name="py-aiplat-py3",
      version=version,
      url='https://github.com/daimon99/py-aiplat-py3',
      license='MIT License',
      author="Daimon",
      author_email="daijian1@qq.com",
      description=long_description,
      long_description=long_description,
      packages=['py_aiplat_py3'],
      package_dir={'py_aiplat_py3': 'py_aiplat_py3'},
      include_package_data=True,
      zip_safe=False,
      platforms='Programming Language :: Python :: 3',
      install_requires=[
      ]
      )