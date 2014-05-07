from distutils.core import setup

setup(
    name='django-pymssql',
    version='0.0.0',
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    packages=['sqlserver_pymssql'],
    url='http://pypi.python.org/pypi/django-pymssql/',
    description='',
    long_description='',
    install_requires=[
        'Django >= 1.6',
        'django-mssql',
        'pymssql',
    ],
)
