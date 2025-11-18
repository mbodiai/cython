# Cython annotation for Actions.py

Raw output: Actions.c

L1  ⚪  (score=0)
```python
"""
```
L2  ⚪  (score=0)
```python
Python Lexical Analyser
```
L3  ⚪  (score=0)
```python
```
L4  ⚪  (score=0)
```python
Actions for use in token specifications
```
L5  ⚪  (score=0)
```python
"""
```
L6  ⚪  (score=0)
```python
```
L7  ⚪  (score=0)
```python
class Action:
```
L8  ⚪  (score=0)
```python
    __slots__ = ()
```
L9  ⚪  (score=0)
```python
    def perform(self, token_stream, text):
```
L10  ⚪  (score=0)
```python
        pass  # abstract
```
L11  ⚪  (score=0)
```python
```
L12  ⚪  (score=0)
```python
    def __copy__(self):
```
L13  ⚪  (score=0)
```python
        return self  # immutable, no need to copy
```
L14  ⚪  (score=0)
```python
```
L15  ⚪  (score=0)
```python
    def __deepcopy__(self, memo):
```
L16  ⚪  (score=0)
```python
        return self  # immutable, no need to copy
```
L17  ⚪  (score=0)
```python
```
L18  ⚪  (score=0)
```python
```
L19  ⚪  (score=0)
```python
class Return(Action):
```
L20  ⚪  (score=0)
```python
    """
```
L21  ⚪  (score=0)
```python
    Internal Plex action which causes |value| to
```
L22  ⚪  (score=0)
```python
    be returned as the value of the associated token
```
L23  ⚪  (score=0)
```python
    """
```
L24  ⚪  (score=0)
```python
```
L25  ⚪  (score=0)
```python
    __slots__ = ("value",)
```
L26  ⚪  (score=0)
```python
```
L27  ⚪  (score=0)
```python
    def __init__(self, value):
```
L28  ⚪  (score=0)
```python
        self.value = value
```
L29  ⚪  (score=0)
```python
```
L30  ⚪  (score=0)
```python
    def perform(self, token_stream, text):
```
L31  ⚪  (score=0)
```python
        return self.value
```
L32  ⚪  (score=0)
```python
```
L33  ⚪  (score=0)
```python
    def __repr__(self):
```
L34  ⚪  (score=0)
```python
        return "Return(%r)" % self.value
```
L35  ⚪  (score=0)
```python
```
L36  ⚪  (score=0)
```python
```
L37  ⚪  (score=0)
```python
class Call(Action):
```
L38  ⚪  (score=0)
```python
    """
```
L39  ⚪  (score=0)
```python
    Internal Plex action which causes a function to be called.
```
L40  ⚪  (score=0)
```python
    """
```
L41  ⚪  (score=0)
```python
```
L42  ⚪  (score=0)
```python
    __slots__ = ("function",)
```
L43  ⚪  (score=0)
```python
```
L44  ⚪  (score=0)
```python
    def __init__(self, function):
```
L45  ⚪  (score=0)
```python
        self.function = function
```
L46  ⚪  (score=0)
```python
```
L47  ⚪  (score=0)
```python
    def perform(self, token_stream, text):
```
L48  ⚪  (score=0)
```python
        return self.function(token_stream, text)
```
L49  ⚪  (score=0)
```python
```
L50  ⚪  (score=0)
```python
    def __repr__(self):
```
L51  ⚪  (score=0)
```python
        return "Call(%s)" % self.function.__name__
```
L52  ⚪  (score=0)
```python
```
L53  ⚪  (score=0)
```python
```
L54  ⚪  (score=0)
```python
class Method(Action):
```
L55  ⚪  (score=0)
```python
    """
```
L56  ⚪  (score=0)
```python
    Plex action that calls a specific method on the token stream,
```
L57  ⚪  (score=0)
```python
    passing the matched text and any provided constant keyword arguments.
```
L58  ⚪  (score=0)
```python
    """
```
L59  ⚪  (score=0)
```python
```
L60  ⚪  (score=0)
```python
    __slots__ = ("name", "kwargs")
```
L61  ⚪  (score=0)
```python
```
L62  ⚪  (score=0)
```python
    def __init__(self, name, **kwargs):
```
L63  ⚪  (score=0)
```python
        self.name = name
```
L64  ⚪  (score=0)
```python
        self.kwargs = kwargs or None
```
L65  ⚪  (score=0)
```python
```
L66  ⚪  (score=0)
```python
    def perform(self, token_stream, text):
```
L67  ⚪  (score=0)
```python
        method = getattr(token_stream, self.name)
```
L68  ⚪  (score=0)
```python
        # self.kwargs is almost always unused => avoid call overhead
```
L69  ⚪  (score=0)
```python
        return method(text, **self.kwargs) if self.kwargs is not None else method(text)
```
L70  ⚪  (score=0)
```python
```
L71  ⚪  (score=0)
```python
    def __repr__(self):
```
L72  ⚪  (score=0)
```python
        kwargs = (
```
L73  ⚪  (score=0)
```python
            ', '.join(sorted(['%s=%r' % item for item in self.kwargs.items()]))
```
L74  ⚪  (score=0)
```python
            if self.kwargs is not None else '')
```
L75  ⚪  (score=0)
```python
        return "Method(%s%s%s)" % (self.name, ', ' if kwargs else '', kwargs)
```
L76  ⚪  (score=0)
```python
```
L77  ⚪  (score=0)
```python
```
L78  ⚪  (score=0)
```python
class Begin(Action):
```
L79  ⚪  (score=0)
```python
    """
```
L80  ⚪  (score=0)
```python
    Begin(state_name) is a Plex action which causes the Scanner to
```
L81  ⚪  (score=0)
```python
    enter the state |state_name|. See the docstring of Plex.Lexicon
```
L82  ⚪  (score=0)
```python
    for more information.
```
L83  ⚪  (score=0)
```python
    """
```
L84  ⚪  (score=0)
```python
```
L85  ⚪  (score=0)
```python
    __slots__ = ("state_name",)
```
L86  ⚪  (score=0)
```python
```
L87  ⚪  (score=0)
```python
    def __init__(self, state_name):
```
L88  ⚪  (score=0)
```python
        self.state_name = state_name
```
L89  ⚪  (score=0)
```python
```
L90  ⚪  (score=0)
```python
    def perform(self, token_stream, text):
```
L91  ⚪  (score=0)
```python
        token_stream.begin(self.state_name)
```
L92  ⚪  (score=0)
```python
```
L93  ⚪  (score=0)
```python
    def __repr__(self):
```
L94  ⚪  (score=0)
```python
        return "Begin(%s)" % self.state_name
```
L95  ⚪  (score=0)
```python
```
L96  ⚪  (score=0)
```python
```
L97  ⚪  (score=0)
```python
class Ignore(Action):
```
L98  ⚪  (score=0)
```python
    """
```
L99  ⚪  (score=0)
```python
    IGNORE is a Plex action which causes its associated token
```
L100  ⚪  (score=0)
```python
    to be ignored. See the docstring of Plex.Lexicon  for more
```
L101  ⚪  (score=0)
```python
    information.
```
L102  ⚪  (score=0)
```python
    """
```
L103  ⚪  (score=0)
```python
```
L104  ⚪  (score=0)
```python
    def perform(self, token_stream, text):
```
L105  ⚪  (score=0)
```python
        return None
```
L106  ⚪  (score=0)
```python
```
L107  ⚪  (score=0)
```python
    def __repr__(self):
```
L108  ⚪  (score=0)
```python
        return "IGNORE"
```
L109  ⚪  (score=0)
```python
```
L110  ⚪  (score=0)
```python
```
L111  ⚪  (score=0)
```python
IGNORE = Ignore()
```
L112  ⚪  (score=0)
```python
```
L113  ⚪  (score=0)
```python
```
L114  ⚪  (score=0)
```python
class Text(Action):
```
L115  ⚪  (score=0)
```python
    """
```
L116  ⚪  (score=0)
```python
    TEXT is a Plex action which causes the text of a token to
```
L117  ⚪  (score=0)
```python
    be returned as the value of the token. See the docstring of
```
L118  ⚪  (score=0)
```python
    Plex.Lexicon  for more information.
```
L119  ⚪  (score=0)
```python
    """
```
L120  ⚪  (score=0)
```python
```
L121  ⚪  (score=0)
```python
    def perform(self, token_stream, text):
```
L122  ⚪  (score=0)
```python
        return text
```
L123  ⚪  (score=0)
```python
```
L124  ⚪  (score=0)
```python
    def __repr__(self):
```
L125  ⚪  (score=0)
```python
        return "TEXT"
```
L126  ⚪  (score=0)
```python
```
L127  ⚪  (score=0)
```python
```
L128  ⚪  (score=0)
```python
TEXT = Text()
```
