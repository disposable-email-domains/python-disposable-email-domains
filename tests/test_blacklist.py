from disposable_email_domains import blacklist


def test_blacklist_inclusion():
    assert 'spamcowboy.com' in blacklist


def test_blacklist_exclusion():
    assert 'spamcannon.com' not in blacklist
