import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'r') as f:
    requirements = f.readlines()

setup(name='omlet_common',
      version='0.1.0',
      author='rapsealk',
      author_email='piono623@naver.com',
      package=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=requirements)
