from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of packages
    in the requirements.
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

# -e . run automatically trigger setup.py.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlprojectfinal',
    version='0.0.1',
    author='shoaib',
    author_email='shoaibold1967@gmail.com',
    packages=find_packages(),
    #install_requires = ['numpy','pandas','matplotlib','seaborn']
    ## by function
    install_requires = get_requirements('requirements.txt')


)

# how many packages are in this projects.
# we build the src folder as a package 
# with __init__.py file.
# if we require 100 packages in a project right,
# it is not feasible to write something like this,
# so what we do is that usually here in this case,
# we make sure over here is create a function:
# that function give my path.

#after create the requirements.txt,
#>pip install -r requirements.txt

#so it build the genric structure itself quickly.


