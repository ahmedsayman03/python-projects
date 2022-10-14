class A(B, C, D):
    """
    attribute search:
    A
    B
    B2 (B2 is base class of B)
    B3
    not F (Parent class of B, that C and D share, e.g. Object - all classes extend object, object class parent base class)
    C
    C2
    not F
    D
    not F

    F parent shared blass for B C and D. This is called a diamond relationship.
    Dynamic ordering solves this problem and doesn't repeat checking a same class that is a parent of multiple
    inherited classes.
    """
