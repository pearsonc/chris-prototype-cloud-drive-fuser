
from setuptools import setup, find_packages
import sys, os

setup(name='CloudDrive',
    version='0.1.0',
    description="Uses Fuse to bind cloud drive services to unix based filesystems.",
    long_description="Uses Fuse to bind cloud drive services to unix based filesystems.",
    classifiers=[],
    keywords='',
    author='Chris Pearson',
    author_email='chris@pearsonnet.co.uk',
    url='https://github.com/pearsonc/prototype-cloud-drive-fuser.git',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        CloudDrive = CloudDrive.cli.main:main
    """,
    namespace_packages=[],
    )
