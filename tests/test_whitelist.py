from disposable_email_domains import whitelist


def test_whitelist_inclusion():
    assert 'spamcannon.com' in whitelist


def test_whitelist_exclusion():
    assert 'spamcowboy.com' not in whitelist
