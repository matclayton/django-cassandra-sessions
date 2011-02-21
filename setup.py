from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
django-cassandra-sessions
=========================

This is a session backend for Django that stores sessions in Cassandra,
using the pycassa library.  

Installing django-cassandra-sessions
------------------------------------

1. Either download the tarball and run ``python setup.py install``, or simply
   use easy install or pip like so ``easy_install django-cassandra-sessions``.


2. Set ``cassandra_sessions`` as your session engine, like so::

       SESSION_ENGINE = 'cassandra_sessions'


3. (optional) Add settings describing where to connect to Cassandra::

       CASSANDRA_HOSTS = ['127.0.0.1:9160',]
       CASSANDRA_SESSIONS_KEYSPACE = 'Keyspace1'
       CASSANDRA_SESSIONS_COLUMN_FAMILY = 'Standard1'
"""
 
setup(
    name='django-cassandra-sessions',
    version=version,
    description="This is a session backend for Django that stores sessions in Cassandra,
using the pycassa library.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='cassandra,session,django',
    author='Mat Clayton',
    author_email='mat@wakari.co.uk',
    url='http://github.com/matclayton/django-cassandra-sessions/tree/master',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools', 'pycassa',],
    include_package_data=True,
    setup_requires=['setuptools_git'],
)