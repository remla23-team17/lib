from setuptools import setup, find_packages

setup(
    name='remla23-team17-lib',
    version='1.0.0',
    author='remla23-team17',
    author_email='remyduijsens@gmail.com',
    description='A Python library for retrieving the version of a GitHub repository',
    url='https://github.com/remla23-team17/lib',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages()
)
