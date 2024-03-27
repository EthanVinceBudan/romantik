def opposite(index: int) -> int:
    """Returns the opposite side index from an adjacent tile given an input 
    side index
    """
    return (index + 3) % 6
