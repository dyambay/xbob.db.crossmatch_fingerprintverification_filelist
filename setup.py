#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# David Yambay <yambayda@gmail.com>
# Apr 11 2014 18:12

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='xbob.db.crossmatch_fingerprintverification_filelist',
    version='1.3.5a0',
    description='Verification File List Database Access API for Bob',
    url='https://github.com/dyambay/xbob.db.crossmatch_fingerprintverification_filelist',
    license='GPLv3',
    author='David Yambay',
    author_email='yambayda@gmail.com',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'bob',  # base signal proc./machine learning library
    ],

    namespace_packages = [
      'xbob',
      'xbob.db',
      ],

    entry_points={

      # declare database to bob
      'bob.db': [
        'crossmatch_fingerprintverification_filelist = xbob.db.crossmatch_fingerprintverification_filelist:Interface',
        ],

      # declare tests to bob
      'bob.test': [
        'crossmatch_fingerprintverification_filelist = xbob.db.crossmatch_fingerprintverification_filelist.test:VerificationFilelistTest',
        ],

      },

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
      ],
)
