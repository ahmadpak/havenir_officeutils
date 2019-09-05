# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in havenir_officeutils/__init__.py
from havenir_officeutils import __version__ as version

setup(
	name='havenir_officeutils',
	version=version,
	description='Doctypes for inhancing day to day reporting',
	author='Havenir',
	author_email='info@havenir.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
