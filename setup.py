from setuptools import setup

setup(
   name='nfem',
   version='1.4',
   description='',
   author='ge73xip',
   author_email='ge73xip@mytum.de',
   url='https://github.com/ge73xip/nfem/tree/pipBranch/',
   packages=['nfem', 'nfem.visualization', 'nfem.tests'],
   install_requires=['numpy', 'matplotlib', 'pyqt5'],
)
