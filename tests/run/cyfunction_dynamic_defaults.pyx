# mode: run
# tag: cyfunction, defaults, fastcall, closures

import time
import cython


def dynamic_default_arg(val=time.time()):
    """
    >>> first = dynamic_default_arg()
    >>> second = dynamic_default_arg()
    >>> first == second
    True
    >>> isinstance(first, float)
    True
    """
    return val


def args_kwargs_with_default(*args, marker=time.time(), **kwargs):
    """
    >>> stamp, received_args, received_kwargs = args_kwargs_with_default(1, 2, key='value')
    >>> isinstance(stamp, float)
    True
    >>> received_args
    (1, 2)
    >>> received_kwargs
    {'key': 'value'}
    >>> stamp == args_kwargs_with_default()[0]
    True
    """
    return marker, args, kwargs


def make_nested_closure(seed):
    created_at = time.time()
    counter = [seed]

    def inner(*args, x=counter.pop(), **kwargs):
        return x, args, kwargs, created_at

    return inner


def exercise_nested_closure(seed):
    """
    >>> nested = make_nested_closure(7)
    >>> default_call = nested()
    >>> default_call[:3]
    (7, (), {})
    >>> stamped = default_call[3]
    >>> result = nested('extra', note='ok')
    >>> result[:3]
    (7, ('extra',), {'note': 'ok'})
    >>> result[3] == stamped
    True
    """
    return make_nested_closure(seed)
