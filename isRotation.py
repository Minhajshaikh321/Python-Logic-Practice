def is_rotation(s1,s2):
    """
    Check if s2 is a rotation of s1.
    Args:
    s1 (str): The original string.
    s2 (str): The string to check if it is a rotation of s1.
    Returns: bool: True if s2 is a rotation of s1, False otherwise.
    """
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

print(is_rotation("abcd","cdab"))  