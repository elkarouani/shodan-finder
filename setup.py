import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()
	
setuptools.setup(
     name='shodanfinder',  
     version='1.4.3',
     author="KDragon",
     author_email="elkarouani@gmail.com",
     description="Get an observation on any website on internet using Shodan",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/elkarouani/shodan-finder-demo",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
	 packages=['shodanfinder'],
	 include_package_data=True,
	 zip_safe=False,
	 install_requires=required
 )