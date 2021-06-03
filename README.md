# Disposable Email Domains

This module provides a set of known disposable email domains.

## Usage

The blocklist is a Python `set` containing all domains in the blocklist:

```python
>>> from disposable_email_domains import blocklist
>>> 'bearsarefuzzy.com' in blocklist
True
```

The domains are guaranteed to be fully lowercased and stripped of whitespace.

## Source

The source of this list is the [disposable-email-domains][1] project.

This module attempts to provide a mirror of that project as a Python module.

If you feel a domain should or shouldn't be on the blocklist, you are
encouraged to make a pull request against the [source repository][2]

[1]: https://github.com/disposable-email-domains/disposable-email-domains
[2]: https://github.com/disposable-email-domains/disposable-email-domains
