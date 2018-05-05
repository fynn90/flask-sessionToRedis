"""
Flask-SessionToRedis
-------------
Flask-SessionToRedis 在Flask中将session保存在redis中

`````

"""
from setuptools import setup


setup(
    name='Flask-SessionToRedis',
    version='0.0.1',
    url='https://github.com/fynn90/flask-sessionToRedis.git',
    license='BSD',
    author='deng fan',
    author_email='fynn.90@outlook.com',
    description='在Flask中将session保存在redis中',
    long_description=__doc__,
    packages=['flask_sessionToRedis'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.12'
    ],
    test_suite='test_session',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
