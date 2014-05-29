import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Facebook Test Accounts Manager",
    version="0.0.1",
    author="Johan Lorenzo",
    author_email="jlorenzo@mozilla.com",
    description="A simple manager for creating Test Account via the Facebook's GraphAPI",
    license="MPL2",
    keywords="facebook test accounts graphapi",
    url="https://github.com/JohanLorenzo/facebook-test-accounts-manager",
    packages=['facebook_test_accounts_manager'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ],
    install_requires=['requests'],
)
