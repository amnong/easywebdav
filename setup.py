import os
import functools
from setuptools import setup, find_packages

_IN_PACKAGE_DIR = functools.partial(os.path.join, "easywebdav")

with open(_IN_PACKAGE_DIR("__version__.py")) as version_file:
    exec(version_file.read())

setup(name="easywebdav",
      classifiers = [
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 2.7",
          ],
      description="A straight-forward WebDAV client, implemented using Requests",
      license="ISC",
      author="Amnon Grossman",
      author_email="emesh1@gmail.com",
      url="http://github.com/amnong/easywebdav",
      version=__version__,
      packages=find_packages(exclude=["tests"]),
      data_files = [],
      install_requires=[
          "requests",
          ],
      scripts=[],
      )
