from disposable_email_domains import blocklist


def test_blocklist_inclusion():
    assert 'spamcowboy.com' in blocklist


def test_blocklist_exclusion():
    assert 'spamcannon.com' not in blocklist
