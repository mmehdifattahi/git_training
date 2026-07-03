import re


def is_valid_email(email: str) -> bool:
    """
    بررسی می‌کنه که آیا رشته‌ی ورودی یک ایمیل معتبره یا نه.
    """
    if not isinstance(email, str):
        return False

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))