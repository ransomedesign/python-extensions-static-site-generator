# In this module, we'll build a basic event system. There will be two ways to
# fire an event: one that calls a callback and one that captures the result of a
# callback. We'll store these callbacks in a dictionary.

_callbacks = {}


def register(hook, order=0):
    """This is a decorator function for registering hooks."""
    def register_callback(func):
        """The register_callback function is responsible for adding 
        default key value pairs to the _callbacks dictionary."""

        _callbacks.setdefault(hook, {}).setdefault(order, []).append(func)
        # Note that the passed function is returned without being called.
        return func

    return register_callback


def event(hook, *args):
    """Call the callback for the named event/hook"""

    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            func(*args)
