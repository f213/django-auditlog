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
        'django-jsonfield-compat-with-django30@git+https://github.com/f213/django-jsonfield-compat.git@3db0052fe7f9f0342a58ae7d5f009f5547c36ced',
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
