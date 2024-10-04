from setuptools import setup, find_packages

setup(
    name='pynitor',
    version='0.2.0',
    description='A simple application to monitor the health of multiple applications and send notifications to Discord.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Saad Mrabet',
    author_email='saad.mrabet@kubicbits.com',
    url='https://github.com/na0495/pynitor',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    package_data={
        '': ['assets/*.webp'], 
    },
    entry_points={
        'console_scripts': [
            'pynitor=app.monitor:main',  # Entry point for the command line
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)