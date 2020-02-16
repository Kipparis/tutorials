#!python3
# encoding: utf-8

from pprint import pprint

before = ['Nonmetals',
        '    Hydrogen',
        '    Carbon',
        '    Nitrogen',
        '    Oxygen',
        'Inner Transitionals',
        '    Lanthanides',
        '        Cerium',
        '        Europium',
        '    Actinides',
        '        Uranium',
        '        Curium',
        '        Plutonium',
        'Alkali Metals',
        '    Lithium',
        '    Sodium',
        '    Potassium'
        ]


def indented_list_sort(indented_list, indent="    "):
    KEY, ITEM, CHILDREN = range(3)

    def add_entry(level, key, item, children):
        if level == 0:
            children.append((key, item, []))
        else:
            add_entry(level - 1, key, item, children[-1][CHILDREN])

    def update_indented_list(entry):
        indented_list.append(entry[ITEM])
        for subentry in sorted(entry[CHILDREN]):
            update_indented_list(subentry)

    entries = []
    for item in indented_list:
        level = 0
        i = 0
        while item.startswith(indent, i):
            i += len(indent)
            level += 1
        key = item.strip().lower()
        add_entry(level, key, item, entries)


    indented_list = []
    for entry in sorted(entries):
        update_indented_list(entry)
    return(indented_list)

after = indented_list_sort(before)

@positive_result
def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

def positive_result(function):
    @functools.wraps
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() result isn't >= 0"
        return result
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__

@logged
def discounted_price(price, percentage, make_integer=False):
    result = price * ((100 - percentage) / 100)
    if not (0 < result <= price):
        raise ValueError("invalid price")
    return result if not make_integer else int(round(result))

if __debug__:
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.path.join(
        tempfile.g ettempdir(), "logged.log"))
    logger.addhandler(handler)

    def logged(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            log = "called: " + function.__name__ + "("
            log += ", ".join(["{0!r}".format(a) for a in args] +
                ["{0!s}={1!r}".format(k, v) for k, v in
                    kwargs.items()])
            result = excxeption = None
            try:
                result = function(*args, **kvargs)
                return result
            except Exception as err:
                exception = err
            finally:
                log += ((" -> " + str(result) if exception is None else 
                ") {0}: {1}".format(type(exception), exception)))
                logger.debug(log)
                if exception is not None:
                    raise exception
        return wrapper
else:
    def logged(function):
        return function
    
class Point:
    
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Product:

    __slots__ = ("__name", "_description", "__price")

    name_as_xml = XmlShadow("name")
    description_as_xml = XmlShadow("description")

    def __init__(self, name, description< price):
        self.__name = name
        self.description = description
        self.price = price

class XmlShadow:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __get__(self, instance, owner=None):
        return xml.sax.saxutils.escape(getattr(instance, self.attribute_name))
