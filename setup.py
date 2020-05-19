from distutils.core import setup

setup(
    name='django-auditlog-compat',
    version='0.5.3',
    packages=['auditlog', 'auditlog.migrations', 'auditlog.management', 'auditlog.management.commands'],
    package_dir={'': 'src'},
    url='https://github.com/f213/django-auditlog-compat',
    license='MIT',
    author='Jan-Jelle Kester',
    description='Audit log app for Django (local fork with compatible jsonfield)',
    install_requires=[
        'django-jsonfield==1.4.0',
        'python-dateutil>=2.8.0',
        'django-jsonfield-compat@git+https://github.com/f213/django-jsonfield-compat.git@b1f1955077041fe9f14eb32be7bbcc6a7525e366',
    ],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
