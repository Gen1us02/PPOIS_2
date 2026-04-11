from setuptools import setup, find_packages

setup(
    name='robot_core',
    version='0.1.0',
    packages=find_packages(where='.', include=['source', 'source.*', 'exceptions', 'exceptions.*']),
    package_dir={'': '.'},
    install_requires=[],
    python_requires='>=3.8',
)