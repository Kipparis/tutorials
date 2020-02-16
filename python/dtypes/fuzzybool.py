class FuzzyBoolAlt:
    def __init__(self, value=0.0):
        self.__value = value if 0.0 <= value <= 1 else 0.0
        

    # same as ~
    def __invert__(self):
        return FuzzyBool(1.0 - self.__value)
    
    # and, &
    def __and__(self, other):
        return FuzzyBool(min(self.__value, other.__value))
    
    # &=
    def __iand__(self, other):
        self.__value = min(self.__value, other.__value)
        return self
     
    # or, |
    def __or__(self, other):
        return FuzzyBool(max(self.__value, other.__value))
    
    # |=
    def __ior__(self, other):
        self.__value = max(self.__value, other.__value)
        return self
    
    def __repr__(self): # will work correctly for subclasses
        return("{0}({1})".format(self.__class__.__name__, self.__value))
    
    def __str__(self):
        return str(self.__value)
    
    def __bool__(self):
        return self.__value > 0.5

    def __int__(self):
        return round(self.__value)
    
    def __float__(self):
        return self.__value
    
    def __lt__(self, other):
        return self.__value < other.__value
    
    # Becouse == reimplemented we have to reimplement hash
    def __eq__(self, other):
        return self.__value == other.__value
    
    def __hash__(self):
        return hash(id(self))
    
    def __format__(self, format_spec):
        return format(self.__value, format_spec)
    
    @staticmethod
    def conjunction(*fuzzies):
        return FuzzyBoolAlt(min([float(x) for x in fuzzies]))
    

class FuzzyBool(float):

    def __new__(cls, value=0.0):
        return super().__new__(cls, value if 0.0 <= value <= 1.0 else 0.0)
    
    def __invert__(self):
        return FuzzyBool(1 - float(self))
    
    def __and__(self, other):
        return FuzzyBool(min(self, other))
    
    def __iand__(self, other):
        self = FuzzyBool(min(self, other))
        return self
     
    def __or__(self, other):
        return FuzzyBool(max(self, other))
    
    def __ior__(self, other):
        self = FuzzyBool(max(self, other))
        return self
    
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, super().__repr__()))
    
    def __bool__(self):
        return float(self) > 0.5

    def __int__(self):
        return round(self)
    
    def __add__(self, other):
        # raise NotImplementedError()
        raise TypeError("unsupported operand type(s) for +: "
                "'{0}' and '{1}'".format(self.__class__.__name__, other.__class__.__name__))
                
    def __neg__(self):
        raise TypeError("unsupported operand type for unary -: '{0}'".format(
            self.__class__.__name__))
        
    def __eq__(self, other):
        return NotImplemented
