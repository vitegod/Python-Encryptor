from setuptools import find_packages, setup

setup(
    name='aes_pyapp',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pycryptodome',
    ],
    entry_points={
        'console_scripts': [
            'aes_pyapp = aes_pyapp.main:main',
        ],
    },
)