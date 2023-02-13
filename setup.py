from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pr/__init__.py
from pr import __version__ as version

setup(
	name="pr",
	version=version,
	description="PR",
	author="Hammad",
	author_email="hammadsrca@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
