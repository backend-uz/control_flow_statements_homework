def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a < 0:
        a -= 2
        return a
    if a > 0:
        a += 1
        return a
    if a == 0:
        return 10
print(main(-5))