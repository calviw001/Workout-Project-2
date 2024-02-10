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
def main():
    k = '11'
    u = 10
    if _is_int(k):
        k = int(k)
        print(_is_postive(k))
        print(_check_length(k,u))
    else:
        print("NO")


main()