#!/usr/bin/env python

from setuptools import setup

setup(name='bpy_lambda',
      version='1.0',
      description='A compiled binary of Blender-as-a-Python-Module (bpy) for use in AWS Lambda',
      author='Benjamin Congdon',
      author_email='me@bcon.gdn',
      url='https://github.com/bcongdon/bpy_lambda',
      packages=['bpy_lambda'],
      include_package_data=True
      )
