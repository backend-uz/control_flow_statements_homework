def main(a):
    """
    If the number is positive, increase it to 1, else leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a>=0:
        b = a + 1
        return b

    if a<=0:
        return a
        
    
print(main(-9))