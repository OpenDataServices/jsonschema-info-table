# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = open('README.md').read()

# Sphinx >= 0.6 in not in requires, as it will be possible to use this without Sphinx.

requires = [
    'jsonref',
    'jsonpointer',
    'recommonmark',
]

setup(
    name='jsonschema-info-table',
    version='0.0.0',
    url='https://github.com/OpenDataServices/jsonschema-info-table',
    license='BSD',
    maintainer='Open Data Services Coop',
    maintainer_email='code@opendataservices.coop',
    description='Takes JSON Schema and presents human readable information about it as a table. ' +
                'Includes Sphinx extension.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['jsonschemainfotable'],
)
