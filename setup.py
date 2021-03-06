#setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Cody_Reece_classes",  # the name that you will install via pip
    version="0.2",
    author="Cody Reece",
    author_email="codyreece323@gmail.com",
    description="a few functions for U3-Ass-1 mod 1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/Reece323/lambdata-reece323",
    # keywords="",
    packages=['my_lambdata_1']    #find_packages()  # ["my_lambdata_1"]
)
