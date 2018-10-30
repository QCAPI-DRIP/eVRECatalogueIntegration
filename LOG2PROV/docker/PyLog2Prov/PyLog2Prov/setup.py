from setuptools import setup, find_packages

setup (
       name='LOG2PROV',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['requests','six>=1.11.0','apache-log-parser>=1.7.0','provpy>=1.1.3','prov>=1.1.3','pika>=0.12.0'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='S. Koulouzis',
       author_email='',

       #summary = 'Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )