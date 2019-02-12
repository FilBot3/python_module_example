#!python

import setuptools

def readme():
  with open('README.md') as f:
    return f.read()

setuptools.setup(
  name = "python_module_example",
  version = "0.1.0",
  description = "An Example Python Module",
  long_description = readme(),
  classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7'
  ],
  keywords = 'example python module',
  url = "https://github.com/Predatorian3/python_module_example",
  author = "Phillip Dudley",
  author_email = "Predatorian3@gmail.com",
  license = "MIT",
  package_dir = {'': 'src'},
  packages = setuptools.find_namespace_packages(where = 'src'),
  include_package_data = True,
  zip_safe = False,
  test_suite = 'tests.python_module_example',
  scripts = [
    'exe/python_module_example'
  ]
)