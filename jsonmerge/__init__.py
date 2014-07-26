import numbers

class UnknownType(Exception):
    def __init__(self, type, instance, schema):
        self.type = type
        self.instance = instance
        self.schema = schema

def flatten(suitable_for_isinstance):
    """
    isinstance() can accept a bunch of really annoying different types:
        * a single type
        * a tuple of types
        * an arbitrary nested tree of tuples

    Return a flattened tuple of the given argument.

    """

    types = set()

    if not isinstance(suitable_for_isinstance, tuple):
        suitable_for_isinstance = (suitable_for_isinstance,)
    for thing in suitable_for_isinstance:
        if isinstance(thing, tuple):
            types.update(flatten(thing))
        else:
            types.add(thing)
    return tuple(types)


class Merger(object):

    _types = {
        "array" : list, "boolean" : bool, "integer" : (int, long),
        "null" : type(None), "number" : numbers.Number, "object" : dict,
        "string" : str,
    }

    def __init__(self, schema):
        self.schema = schema

    def is_type(self, instance, type):
        if type not in self._types:
            raise UnknownType(type, instance, self.schema)

        pytypes = self._types[type]

        # bool inherits from int, so ensure bools aren't reported as ints
        if isinstance(instance, bool):
            pytypes = _utils.flatten(pytypes)
            is_number = any(
                issubclass(pytype, numbers.Number) for pytype in pytypes
            )
            if is_number and bool not in pytypes:
                return False
        return isinstance(instance, pytypes)

    def merge(self, base, head):
        return "b"


def merge(base, head, schema):
    merger = Merger(schema)
    return merger.merge(base, head)
