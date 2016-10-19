Disposable Email Domains
========================

This module provides a set of known disposable email domains.

Usage
-----

The blacklist is a Python ``set`` containing all domains in the blacklist:

::

    >>> from disposable_email_domains import blacklist
    >>> 'bearsarefuzzy.com' in blacklist
    True

The domains are guaranteed to be fully lowercased and stripped of whitespace.

Source
------

The source of this list is the `disposable-email-domains`_ project.

.. _disposable-email-domains: https://github.com/martenson/disposable-email-domains

This module attempts to provide a mirror of that project as a Python module.

If you feel a domain should or shouldn't be on the blacklist, you are
encouraged to make a pull request against the `source repository`_.

.. _source repository: https://github.com/martenson/disposable-email-domains
