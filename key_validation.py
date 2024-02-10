def __is_int(test_key):
    try:
        assert test_key.isdigit()
        int(test_key)
        return True
    except (ValueError, AssertionError):
        return False

