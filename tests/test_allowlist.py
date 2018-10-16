from disposable_email_domains import allowlist


def test_allowlist_inclusion():
    assert 'spamcannon.com' in allowlist


def test_allowlist_exclusion():
    assert 'spamcowboy.com' not in allowlist
