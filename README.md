django-auditlog-compat
===============

This is a fork of [django-auditlog](https://github.com/jjkester/django-auditlog) that works with [django-jsonfield-compat](https://github.com/kbussell/django-jsonfield-compat), getting you rid of weird issues when your stock django JSONField data gets accidentaly converted to PHP-like strings, see https://github.com/jjkester/django-auditlog/issues/71.

Do not forget to add `USE_NATIVE_JSONFIELD = True` to your settings.py

Author
======

The fork is originaly created by [florencioq](https://github.com/florencioq/django-auditlog), i have just made it packagable.
