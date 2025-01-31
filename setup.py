from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will retrun the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","") for req in requirements]

         if HYPEN_E_DOT in requirements:
              requirements.remove(HYPEN_E_DOT)

    return requirements     

setup
(
    name= 'mlproject',
    version='0.0.1',
    author='Susmitha'
    author_email='susmithabenny@gmail.com',
    packages=find_packages(),
    include_package_data=true,
    install_requires=get_requirements('requirements.txt')
)

from setuptools import setup, find_packages

setup(
    name='mlproject',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
)
