from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in streaming_platform_admin/__init__.py
from streaming_platform_admin import __version__ as version

setup(
	name="streaming_platform_admin",
	version=version,
	description="App para administrar perfiles y cuentas de plataformas streaming o plataformas de servicios online",
	author="Akkalame Ereut",
	author_email="akkalameo.o@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
