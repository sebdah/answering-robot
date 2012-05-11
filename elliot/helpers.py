"""
Various helpers
"""

def list_make_unique(seq, idfun = None):
    """
    Ensure a list is unique
    
    Preserves the order
    """
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    
    return result