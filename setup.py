from setuptools import setup, find_packages
from typing import List 

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    HYPEN_e_DOTv= '-e .'
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_e_DOTv in requirements:
            requirements.remove("HYPEN_e_DOTv")
            
    return requirements
            

setup(
    name = "Ml_project",
    version= "0.0.1",
    author= "Happy",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)