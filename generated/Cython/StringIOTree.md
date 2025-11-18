# Cython annotation for StringIOTree.py

Raw output: StringIOTree.c

L1  ⚪  (score=0)
```python
r"""
```
L2  ⚪  (score=0)
```python
Implements a buffer with insertion points. When you know you need to
```
L3  ⚪  (score=0)
```python
"get back" to a place and write more later, simply call insertion_point()
```
L4  ⚪  (score=0)
```python
at that spot and get a new StringIOTree object that is "left behind".
```
L5  ⚪  (score=0)
```python
```
L6  ⚪  (score=0)
```python
EXAMPLE:
```
L7  ⚪  (score=0)
```python
```
L8  ⚪  (score=0)
```python
>>> a = StringIOTree()
```
L9  ⚪  (score=0)
```python
>>> _= a.write('first\n')
```
L10  ⚪  (score=0)
```python
>>> b = a.insertion_point()
```
L11  ⚪  (score=0)
```python
>>> _= a.write('third\n')
```
L12  ⚪  (score=0)
```python
>>> _= b.write('second\n')
```
L13  ⚪  (score=0)
```python
>>> a.getvalue().split()
```
L14  ⚪  (score=0)
```python
['first', 'second', 'third']
```
L15  ⚪  (score=0)
```python
```
L16  ⚪  (score=0)
```python
>>> c = b.insertion_point()
```
L17  ⚪  (score=0)
```python
>>> d = c.insertion_point()
```
L18  ⚪  (score=0)
```python
>>> _= d.write('alpha\n')
```
L19  ⚪  (score=0)
```python
>>> _= b.write('gamma\n')
```
L20  ⚪  (score=0)
```python
>>> _= c.write('beta\n')
```
L21  ⚪  (score=0)
```python
>>> b.getvalue().split()
```
L22  ⚪  (score=0)
```python
['second', 'alpha', 'beta', 'gamma']
```
L23  ⚪  (score=0)
```python
```
L24  ⚪  (score=0)
```python
>>> try: from cStringIO import StringIO
```
L25  ⚪  (score=0)
```python
... except ImportError: from io import StringIO
```
L26  ⚪  (score=0)
```python
```
L27  ⚪  (score=0)
```python
>>> i = StringIOTree()
```
L28  ⚪  (score=0)
```python
>>> d.insert(i)
```
L29  ⚪  (score=0)
```python
>>> _= i.write('inserted\n')
```
L30  ⚪  (score=0)
```python
>>> out = StringIO()
```
L31  ⚪  (score=0)
```python
>>> a.copyto(out)
```
L32  ⚪  (score=0)
```python
>>> out.getvalue().split()
```
L33  ⚪  (score=0)
```python
['first', 'second', 'alpha', 'inserted', 'beta', 'gamma', 'third']
```
L34  ⚪  (score=0)
```python
"""
```
L35  ⚪  (score=0)
```python
```
L36  ⚪  (score=0)
```python
```
L37  ⚪  (score=0)
```python
from io import StringIO
```
L38  ⚪  (score=0)
```python
```
L39  ⚪  (score=0)
```python
```
L40  ⚪  (score=0)
```python
class StringIOTree:
```
L41  ⚪  (score=0)
```python
    """
```
L42  ⚪  (score=0)
```python
    See module docs.
```
L43  ⚪  (score=0)
```python
    """
```
L44  ⚪  (score=0)
```python
```
L45  ⚪  (score=0)
```python
    def __init__(self, stream=None):
```
L46  ⚪  (score=0)
```python
        self.prepended_children = []
```
L47  ⚪  (score=0)
```python
        if stream is None:
```
L48  ⚪  (score=0)
```python
            stream = StringIO()
```
L49  ⚪  (score=0)
```python
        self.stream = stream
```
L50  ⚪  (score=0)
```python
        self.write = stream.write
```
L51  ⚪  (score=0)
```python
        self.markers = []
```
L52  ⚪  (score=0)
```python
```
L53  ⚪  (score=0)
```python
    def empty(self):
```
L54  ⚪  (score=0)
```python
        if self.stream.tell():
```
L55  ⚪  (score=0)
```python
            return False
```
L56  ⚪  (score=0)
```python
        return all([child.empty() for child in self.prepended_children]) if self.prepended_children else True
```
L57  ⚪  (score=0)
```python
```
L58  ⚪  (score=0)
```python
    def getvalue(self):
```
L59  ⚪  (score=0)
```python
        content = []
```
L60  ⚪  (score=0)
```python
        self._collect_in(content)
```
L61  ⚪  (score=0)
```python
        return "".join(content)
```
L62  ⚪  (score=0)
```python
```
L63  ⚪  (score=0)
```python
    def _collect_in(self, target_list):
```
L64  ⚪  (score=0)
```python
        x: StringIOTree
```
L65  ⚪  (score=0)
```python
        for x in self.prepended_children:
```
L66  ⚪  (score=0)
```python
            x._collect_in(target_list)
```
L67  ⚪  (score=0)
```python
        stream_content = self.stream.getvalue()
```
L68  ⚪  (score=0)
```python
        if stream_content:
```
L69  ⚪  (score=0)
```python
            target_list.append(stream_content)
```
L70  ⚪  (score=0)
```python
```
L71  ⚪  (score=0)
```python
    def copyto(self, target):
```
L72  ⚪  (score=0)
```python
        """Potentially cheaper than getvalue as no string concatenation
```
L73  ⚪  (score=0)
```python
        needs to happen."""
```
L74  ⚪  (score=0)
```python
        child: StringIOTree
```
L75  ⚪  (score=0)
```python
        for child in self.prepended_children:
```
L76  ⚪  (score=0)
```python
            child.copyto(target)
```
L77  ⚪  (score=0)
```python
        stream_content = self.stream.getvalue()
```
L78  ⚪  (score=0)
```python
        if stream_content:
```
L79  ⚪  (score=0)
```python
            target.write(stream_content)
```
L80  ⚪  (score=0)
```python
```
L81  ⚪  (score=0)
```python
    def commit(self):
```
L82  ⚪  (score=0)
```python
        # Save what we have written until now so that the buffer
```
L83  ⚪  (score=0)
```python
        # itself is empty -- this makes it ready for insertion
```
L84  ⚪  (score=0)
```python
        if self.stream.tell():
```
L85  ⚪  (score=0)
```python
            self.prepended_children.append(StringIOTree(self.stream))
```
L86  ⚪  (score=0)
```python
            self.prepended_children[-1].markers = self.markers
```
L87  ⚪  (score=0)
```python
            self.markers = []
```
L88  ⚪  (score=0)
```python
            self.stream = StringIO()
```
L89  ⚪  (score=0)
```python
            self.write = self.stream.write
```
L90  ⚪  (score=0)
```python
```
L91  ⚪  (score=0)
```python
    def reset(self):
```
L92  ⚪  (score=0)
```python
        self.prepended_children = []
```
L93  ⚪  (score=0)
```python
        self.markers = []
```
L94  ⚪  (score=0)
```python
        self.stream = StringIO()
```
L95  ⚪  (score=0)
```python
        self.write = self.stream.write
```
L96  ⚪  (score=0)
```python
```
L97  ⚪  (score=0)
```python
    def insert(self, iotree):
```
L98  ⚪  (score=0)
```python
        """
```
L99  ⚪  (score=0)
```python
        Insert a StringIOTree (and all of its contents) at this location.
```
L100  ⚪  (score=0)
```python
        Further writing to self appears after what is inserted.
```
L101  ⚪  (score=0)
```python
        """
```
L102  ⚪  (score=0)
```python
        self.commit()
```
L103  ⚪  (score=0)
```python
        self.prepended_children.append(iotree)
```
L104  ⚪  (score=0)
```python
```
L105  ⚪  (score=0)
```python
    def insertion_point(self):
```
L106  ⚪  (score=0)
```python
        """
```
L107  ⚪  (score=0)
```python
        Returns a new StringIOTree, which is left behind at the current position
```
L108  ⚪  (score=0)
```python
        (it what is written to the result will appear right before whatever is
```
L109  ⚪  (score=0)
```python
        next written to self).
```
L110  ⚪  (score=0)
```python
```
L111  ⚪  (score=0)
```python
        Calling getvalue() or copyto() on the result will only return the
```
L112  ⚪  (score=0)
```python
        contents written to it.
```
L113  ⚪  (score=0)
```python
        """
```
L114  ⚪  (score=0)
```python
        # Save what we have written until now
```
L115  ⚪  (score=0)
```python
        # This is so that getvalue on the result doesn't include it.
```
L116  ⚪  (score=0)
```python
        self.commit()
```
L117  ⚪  (score=0)
```python
        # Construct the new forked object to return
```
L118  ⚪  (score=0)
```python
        other = StringIOTree()
```
L119  ⚪  (score=0)
```python
        self.prepended_children.append(other)
```
L120  ⚪  (score=0)
```python
        return other
```
L121  ⚪  (score=0)
```python
```
L122  ⚪  (score=0)
```python
    def allmarkers(self):
```
L123  ⚪  (score=0)
```python
        c: StringIOTree
```
L124  ⚪  (score=0)
```python
        children = self.prepended_children
```
L125  ⚪  (score=0)
```python
        return [m for c in children for m in c.allmarkers()] + self.markers
```
L126  ⚪  (score=0)
```python
```
L127  ⚪  (score=0)
```python
    """
```
L128  ⚪  (score=0)
```python
    # Print the result of allmarkers in a nice human-readable form. Use it only for debugging.
```
L129  ⚪  (score=0)
```python
    # Prints e.g.
```
L130  ⚪  (score=0)
```python
    # /path/to/source.pyx:
```
L131  ⚪  (score=0)
```python
    #     cython line 2 maps to 3299-3343
```
L132  ⚪  (score=0)
```python
    #     cython line 4 maps to 2236-2245  2306  3188-3201
```
L133  ⚪  (score=0)
```python
    # /path/to/othersource.pyx:
```
L134  ⚪  (score=0)
```python
    #     cython line 3 maps to 1234-1270
```
L135  ⚪  (score=0)
```python
    # ...
```
L136  ⚪  (score=0)
```python
    # Note: In the example above, 3343 maps to line 2, 3344 does not.
```
L137  ⚪  (score=0)
```python
    def print_hr_allmarkers(self):
```
L138  ⚪  (score=0)
```python
        from collections import defaultdict
```
L139  ⚪  (score=0)
```python
        markers = self.allmarkers()
```
L140  ⚪  (score=0)
```python
        totmap = defaultdict(lambda: defaultdict(list))
```
L141  ⚪  (score=0)
```python
        for c_lineno, (cython_desc, cython_lineno) in enumerate(markers):
```
L142  ⚪  (score=0)
```python
            if cython_lineno > 0 and cython_desc.filename is not None:
```
L143  ⚪  (score=0)
```python
                totmap[cython_desc.filename][cython_lineno].append(c_lineno + 1)
```
L144  ⚪  (score=0)
```python
        reprstr = ""
```
L145  ⚪  (score=0)
```python
        if totmap == 0:
```
L146  ⚪  (score=0)
```python
            reprstr += "allmarkers is empty\n"
```
L147  ⚪  (score=0)
```python
        try:
```
L148  ⚪  (score=0)
```python
            sorted(totmap.items())
```
L149  ⚪  (score=0)
```python
        except:
```
L150  ⚪  (score=0)
```python
            print(totmap)
```
L151  ⚪  (score=0)
```python
            print(totmap.items())
```
L152  ⚪  (score=0)
```python
        for cython_path, filemap in sorted(totmap.items()):
```
L153  ⚪  (score=0)
```python
            reprstr += cython_path + ":\n"
```
L154  ⚪  (score=0)
```python
            for cython_lineno, c_linenos in sorted(filemap.items()):
```
L155  ⚪  (score=0)
```python
                reprstr += "\tcython line " + str(cython_lineno) + " maps to "
```
L156  ⚪  (score=0)
```python
                i = 0
```
L157  ⚪  (score=0)
```python
                while i < len(c_linenos):
```
L158  ⚪  (score=0)
```python
                    reprstr += str(c_linenos[i])
```
L159  ⚪  (score=0)
```python
                    flag = False
```
L160  ⚪  (score=0)
```python
                    while i+1 < len(c_linenos) and c_linenos[i+1] == c_linenos[i]+1:
```
L161  ⚪  (score=0)
```python
                        i += 1
```
L162  ⚪  (score=0)
```python
                        flag = True
```
L163  ⚪  (score=0)
```python
                    if flag:
```
L164  ⚪  (score=0)
```python
                        reprstr += "-" + str(c_linenos[i]) + " "
```
L165  ⚪  (score=0)
```python
                    i += 1
```
L166  ⚪  (score=0)
```python
                reprstr += "\n"
```
L167  ⚪  (score=0)
```python
```
L168  ⚪  (score=0)
```python
        import sys
```
L169  ⚪  (score=0)
```python
        sys.stdout.write(reprstr)
```
L170  ⚪  (score=0)
```python
    """
```
