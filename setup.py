import os

import setuptools

# Avoid polluting the .tar.gz with ._* files under Mac OS X
os.putenv('COPYFILE_DISABLE', 'true')

# Prevent distutils from complaining that a standard file wasn't found
README = os.path.join(os.path.dirname(__file__), 'README')
if not os.path.exists(README):
    os.symlink(README + '.rst', README)

description = ('Django database backend for Microsoft SQL Server '
               'that works on non-Windows systems.')

with open(README) as f:
    long_description = '\n\n'.join(f.read().split('\n\n')[1:])

setuptools.setup(
    name='django-pymssql',
    version='1.7.0',
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    url='https://github.com/aaugustin/django-pymssql',
    description=description,
    long_description=long_description,
    download_url='http://pypi.python.org/pypi/django-pymssql',
    packages=[
        'sqlserver_pymssql',
    ],
    install_requires=[
        'Django',
        'django-mssql',
        'pymssql',
    ],
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
    platforms='all',
    license='BSD',
)
