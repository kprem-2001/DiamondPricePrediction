from setuptools import setup, find_packages
from typing import List

hyphen = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements  = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if hyphen in requirements:
            requirements.remove(hyphen)
        
        return requirements
setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Prem",
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()    
) 