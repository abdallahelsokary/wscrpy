from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='wscrpy',
  version='0.0.1',
  description='web scraping library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abdallah Elsokary',
  author_email='abdallahelsokary@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='web scraping', 
  packages=find_packages(),
  install_requires=['beautifulsoup4'] 
)