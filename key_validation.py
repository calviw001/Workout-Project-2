def _is_int(test_key):
    try:
        assert test_key.isdigit()
        int(test_key)
        return True
    except (ValueError, AssertionError):
        return False


def _is_postive(an_int):
    return an_int > 0


def _check_length(an_int, upper_bound):
    return an_int < upper_bound


# Temporary main function to test private functions
def check_test_key(key, file_size):
    if _is_int(key):
        key = int(key)
        if _is_postive(key) and _check_length(key, file_size):
            return True
        else:
            return False
    else:
        return False
