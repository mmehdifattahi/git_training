from src.utils.validator import is_valid_email


def test_valid_email():
    assert is_valid_email("test@example.com") is True


def test_valid_email_with_subdomain():
    assert is_valid_email("user@mail.example.co.uk") is True


def test_invalid_email_no_at_sign():
    assert is_valid_email("testexample.com") is False


def test_invalid_email_no_domain():
    assert is_valid_email("main@") is False


def test_invalid_email_no_username():
    assert is_valid_email("@example.com") is False


def test_invalid_email_empty_string():
    assert is_valid_email("") is False


def test_invalid_email_none_input():
    assert is_valid_email(None) is False


def test_invalid_email_no_tld():
    assert is_valid_email("test@example") is False