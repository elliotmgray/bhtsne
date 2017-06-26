from setuptools import setup, find_packages
import sys


if sys.version_info.major != 3:
    raise RuntimeError("bhtsne requires Python 3")

setup(
    name="bhtsne",
    description="Dimensionality Reduction technique",
    version="",
    author="Laurens van der Maaten",
    author_email="lvdmaaten@gmail.com",
    packages=find_packages(),
    package_data={
        '': ['*bhtsne*']
    },
    include_package_data=True,
    zip_safe=False,
    url="https://github.com/elliotmgray/bhtsne",
    license="LICENSE",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read()
)
