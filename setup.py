from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'useTwitter',
    version = '0.1',
    description = "A class for using Twitter easily in order to help create bots for the social network.",
    author = 'João Costa',
    author_email = 'joaocosta_neto@hotmail.com',
    packages = ['useTwitter'],
    license = 'MIT',
    keywords = ['twitter', 'bot'],
    long_description=long_description,
    install_requires=[
          'requests',
          'json',
          'time'
      ],
    classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)