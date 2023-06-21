from setuptools import find_packages,setup
# this is to setup the package and many more 
from typing import List


# from this script we will run requirments.txt that will build env

# now get the requirememts from the file open it

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
name='M-health project',
developer=' Adarsh'.
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)


