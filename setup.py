from __future__ import unicode_literals

import codecs
import os.path

import setuptools

root_dir = os.path.abspath(os.path.dirname(__file__))

description = ("Django database backend for Microsoft SQL Server "
               "that works on non-Windows systems.")

with codecs.open(os.path.join(root_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='django-pymssql',
    version='1.7.1',
    description=description,
    long_description=long_description,
    url='https://github.com/aaugustin/django-pymssql',
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=[
        'sqlserver_pymssql',
    ],
    install_requires=[
        'Django',
        'django-mssql',
        'pymssql',
    ],
)
