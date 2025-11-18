# Cython annotation for Visitor.py

Raw output: Visitor.c

L1  ⚪  (score=0)
```python
# cython: infer_types=True
```
L2  ⚪  (score=0)
```python
```
L3  ⚪  (score=0)
```python
#
```
L4  ⚪  (score=0)
```python
#   Tree visitor and transform framework
```
L5  ⚪  (score=0)
```python
#
```
L6  ⚪  (score=0)
```python
```
L7  ⚪  (score=0)
```python
```
L8  ⚪  (score=0)
```python
import inspect
```
L9  ⚪  (score=0)
```python
import sys
```
L10  ⚪  (score=0)
```python
from collections.abc import Callable
```
L11  ⚪  (score=0)
```python
from typing import TYPE_CHECKING, Any
```
L12  ⚪  (score=0)
```python
```
L13  ⚪  (score=0)
```python
import cython
```
L14  ⚪  (score=0)
```python
```
L15  ⚪  (score=0)
```python
from . import Builtin, DebugFlags, Errors, ExprNodes, Future, Nodes, TypeSlots
```
L16  ⚪  (score=0)
```python
```
L17  ⚪  (score=0)
```python
_PRINTABLE= cython.declare(tuple, (bytes, str, int, float, complex))
```
L18  ⚪  (score=0)
```python
```
L19  ⚪  (score=0)
```python
if TYPE_CHECKING:
```
L20  ⚪  (score=0)
```python
    from .CythonScope import CythonScope as Scope
```
L21  ⚪  (score=0)
```python
    from .Nodes import Node
```
L22  ⚪  (score=0)
```python
```
L23  ⚪  (score=0)
```python
class TreeVisitor:
```
L24  ⚪  (score=0)
```python
    """Base class for writing visitors for a Cython tree, contains utilities for recursing such trees using visitors.
```
L25  ⚪  (score=0)
```python
```
L26  ⚪  (score=0)
```python
    Each node is expected to have a child_attrs iterable containing the names of attributes
```
L27  ⚪  (score=0)
```python
    containing child nodes or lists of child nodes. Lists are not considered
```
L28  ⚪  (score=0)
```python
    part of the tree structure (i.e. contained nodes are considered direct
```
L29  ⚪  (score=0)
```python
    children of the parent node).
```
L30  ⚪  (score=0)
```python
```
L31  ⚪  (score=0)
```python
    visit_children visits each of the children of a given node (see the visit_children
```
L32  ⚪  (score=0)
```python
    documentation). When recursing the tree using visit_children, an attribute
```
L33  ⚪  (score=0)
```python
    access_path is maintained which gives information about the current location
```
L34  ⚪  (score=0)
```python
    in the tree as a stack of tuples: (parent_node, attrname, index), representing
```
L35  ⚪  (score=0)
```python
    the node, attribute and optional list index that was taken in each step in the path to
```
L36  ⚪  (score=0)
```python
    the current node.
```
L37  ⚪  (score=0)
```python
```
L38  ⚪  (score=0)
```python
    Example:
```
L39  ⚪  (score=0)
```python
    >>> class SampleNode(object):
```
L40  ⚪  (score=0)
```python
    ...     child_attrs = ["head", "body"]
```
L41  ⚪  (score=0)
```python
    ...     def __init__(self, value, head=None, body=None):
```
L42  ⚪  (score=0)
```python
    ...         self.value = value
```
L43  ⚪  (score=0)
```python
    ...         self.head = head
```
L44  ⚪  (score=0)
```python
    ...         self.body = body
```
L45  ⚪  (score=0)
```python
    ...     def __repr__(self): return "SampleNode(%s)" % self.value
```
L46  ⚪  (score=0)
```python
    ...
```
L47  ⚪  (score=0)
```python
    >>> tree = SampleNode(0, SampleNode(1), [SampleNode(2), SampleNode(3)])
```
L48  ⚪  (score=0)
```python
    >>> class MyVisitor(TreeVisitor):
```
L49  ⚪  (score=0)
```python
    ...     def visit_SampleNode(self, node):
```
L50  ⚪  (score=0)
```python
    ...         print("in %s %s" % (node.value, self.access_path))
```
L51  ⚪  (score=0)
```python
    ...         self.visitchildren(node)
```
L52  ⚪  (score=0)
```python
    ...         print("out %s" % node.value)
```
L53  ⚪  (score=0)
```python
    ...
```
L54  ⚪  (score=0)
```python
    >>> MyVisitor().visit(tree)
```
L55  ⚪  (score=0)
```python
    in 0 []
```
L56  ⚪  (score=0)
```python
    in 1 [(SampleNode(0), 'head', None)]
```
L57  ⚪  (score=0)
```python
    out 1
```
L58  ⚪  (score=0)
```python
    in 2 [(SampleNode(0), 'body', 0)]
```
L59  ⚪  (score=0)
```python
    out 2
```
L60  ⚪  (score=0)
```python
    in 3 [(SampleNode(0), 'body', 1)]
```
L61  ⚪  (score=0)
```python
    out 3
```
L62  ⚪  (score=0)
```python
    out 0
```
L63  ⚪  (score=0)
```python
    """
```
L64  ⚪  (score=0)
```python
    dispatch_table: dict[type, Callable[[Any], Any]]
```
L65  ⚪  (score=0)
```python
    access_path: list[tuple[Any, str, Any]]
```
L66  ⚪  (score=0)
```python
    def __init__(self):
```
L67  ⚪  (score=0)
```python
        super().__init__()
```
L68  ⚪  (score=0)
```python
        self.dispatch_table = {}
```
L69  ⚪  (score=0)
```python
        self.access_path = []
```
L70  ⚪  (score=0)
```python
```
L71  ⚪  (score=0)
```python
    def dump_node(self, node):
```
L72  ⚪  (score=0)
```python
        ignored = list(node.child_attrs or []) + [
```
L73  ⚪  (score=0)
```python
            'child_attrs', 'pos', 'gil_message', 'cpp_message', 'subexprs']
```
L74  ⚪  (score=0)
```python
        values = []
```
L75  ⚪  (score=0)
```python
        pos = getattr(node, 'pos', None)
```
L76  ⚪  (score=0)
```python
        if pos:
```
L77  ⚪  (score=0)
```python
            source = pos[0]
```
L78  ⚪  (score=0)
```python
            if source:
```
L79  ⚪  (score=0)
```python
                import os.path
```
L80  ⚪  (score=0)
```python
                source = os.path.basename(source.get_description())
```
L81  ⚪  (score=0)
```python
            values.append('%s:%s:%s' % (source, pos[1], pos[2]))
```
L82  ⚪  (score=0)
```python
        attribute_names = dir(node)
```
L83  ⚪  (score=0)
```python
        for attr in attribute_names:
```
L84  ⚪  (score=0)
```python
            if attr in ignored:
```
L85  ⚪  (score=0)
```python
                continue
```
L86  ⚪  (score=0)
```python
            if attr.startswith('_') or attr.endswith('_'):
```
L87  ⚪  (score=0)
```python
                continue
```
L88  ⚪  (score=0)
```python
            try:
```
L89  ⚪  (score=0)
```python
                value = getattr(node, attr)
```
L90  ⚪  (score=0)
```python
            except AttributeError:
```
L91  ⚪  (score=0)
```python
                continue
```
L92  ⚪  (score=0)
```python
            if value is None or value == 0:
```
L93  ⚪  (score=0)
```python
                continue
```
L94  ⚪  (score=0)
```python
            elif isinstance(value, list):
```
L95  ⚪  (score=0)
```python
                value = '[...]/%d' % len(value)
```
L96  ⚪  (score=0)
```python
            elif not isinstance(value, _PRINTABLE):
```
L97  ⚪  (score=0)
```python
                continue
```
L98  ⚪  (score=0)
```python
            else:
```
L99  ⚪  (score=0)
```python
                value = repr(value)
```
L100  ⚪  (score=0)
```python
            values.append('%s = %s' % (attr, value))
```
L101  ⚪  (score=0)
```python
        return '%s(%s)' % (node.__class__.__name__, ',\n    '.join(values))
```
L102  ⚪  (score=0)
```python
```
L103  ⚪  (score=0)
```python
    def _find_node_path(self, stacktrace):
```
L104  ⚪  (score=0)
```python
        import os.path
```
L105  ⚪  (score=0)
```python
        last_traceback = stacktrace
```
L106  ⚪  (score=0)
```python
        nodes = []
```
L107  ⚪  (score=0)
```python
        while hasattr(stacktrace, 'tb_frame'):
```
L108  ⚪  (score=0)
```python
            frame = stacktrace.tb_frame
```
L109  ⚪  (score=0)
```python
            node = frame.f_locals.get('self')
```
L110  ⚪  (score=0)
```python
            if isinstance(node, Nodes.Node):
```
L111  ⚪  (score=0)
```python
                code = frame.f_code
```
L112  ⚪  (score=0)
```python
                method_name = code.co_name
```
L113  ⚪  (score=0)
```python
                pos = (os.path.basename(code.co_filename),
```
L114  ⚪  (score=0)
```python
                       frame.f_lineno)
```
L115  ⚪  (score=0)
```python
                nodes.append((node, method_name, pos))
```
L116  ⚪  (score=0)
```python
                last_traceback = stacktrace
```
L117  ⚪  (score=0)
```python
            stacktrace = stacktrace.tb_next
```
L118  ⚪  (score=0)
```python
        return (last_traceback, nodes)
```
L119  ⚪  (score=0)
```python
```
L120  ⚪  (score=0)
```python
    def _raise_compiler_error(self, child, e):
```
L121  ⚪  (score=0)
```python
        trace = ['']
```
L122  ⚪  (score=0)
```python
        for parent, attribute, index in self.access_path:
```
L123  ⚪  (score=0)
```python
            node = getattr(parent, attribute)
```
L124  ⚪  (score=0)
```python
            if index is None:
```
L125  ⚪  (score=0)
```python
                index = ''
```
L126  ⚪  (score=0)
```python
            else:
```
L127  ⚪  (score=0)
```python
                node = node[index]
```
L128  ⚪  (score=0)
```python
                index = f'[{index}]'
```
L129  ⚪  (score=0)
```python
            trace.append(f'{parent.__class__.__name__}.{attribute}{index} = {self.dump_node(node)}')
```
L130  ⚪  (score=0)
```python
        stacktrace, called_nodes = self._find_node_path(sys.exc_info()[2])
```
L131  ⚪  (score=0)
```python
        last_node = child
```
L132  ⚪  (score=0)
```python
        for node, method_name, pos in called_nodes:
```
L133  ⚪  (score=0)
```python
            last_node = node
```
L134  ⚪  (score=0)
```python
            trace.append(f"File '{pos[0]}', line {pos[1]}, in {method_name}: {self.dump_node(node)}")
```
L135  ⚪  (score=0)
```python
        raise Errors.CompilerCrash(
```
L136  ⚪  (score=0)
```python
            getattr(last_node, 'pos', None), self.__class__.__name__,
```
L137  ⚪  (score=0)
```python
            '\n'.join(trace), e, stacktrace)
```
L138  ⚪  (score=0)
```python
```
L139  ⚪  (score=0)
```python
    @cython.final
```
L140  ⚪  (score=0)
```python
    def find_handler(self, obj):
```
L141  ⚪  (score=0)
```python
        # to resolve, try entire hierarchy
```
L142  ⚪  (score=0)
```python
        cls = type(obj)
```
L143  ⚪  (score=0)
```python
        mro = inspect.getmro(cls)
```
L144  ⚪  (score=0)
```python
        for mro_cls in mro:
```
L145  ⚪  (score=0)
```python
            handler_method = getattr(self, "visit_" + mro_cls.__name__, None)
```
L146  ⚪  (score=0)
```python
            if handler_method is not None:
```
L147  ⚪  (score=0)
```python
                return handler_method
```
L148  ⚪  (score=0)
```python
```
L149  ⚪  (score=0)
```python
        print(type(self), cls)
```
L150  ⚪  (score=0)
```python
        if self.access_path:
```
L151  ⚪  (score=0)
```python
            print(self.access_path)
```
L152  ⚪  (score=0)
```python
            print(self.access_path[-1][0].pos)
```
L153  ⚪  (score=0)
```python
            print(self.access_path[-1][0].__dict__)
```
L154  ⚪  (score=0)
```python
        raise RuntimeError(f"Visitor {self!r} does not accept object: {obj}")
```
L155  ⚪  (score=0)
```python
```
L156  ⚪  (score=0)
```python
    def visit(self, obj):
```
L157  ⚪  (score=0)
```python
        # generic def entry point for calls from Python subclasses
```
L158  ⚪  (score=0)
```python
        return self._visit(obj)
```
L159  ⚪  (score=0)
```python
```
L160  ⚪  (score=0)
```python
    @cython.final
```
L161  ⚪  (score=0)
```python
    def _visit(self, obj):
```
L162  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L163  ⚪  (score=0)
```python
        try:
```
L164  ⚪  (score=0)
```python
            try:
```
L165  ⚪  (score=0)
```python
                handler_method = self.dispatch_table[type(obj)]
```
L166  ⚪  (score=0)
```python
            except KeyError:
```
L167  ⚪  (score=0)
```python
                handler_method = self.find_handler(obj)
```
L168  ⚪  (score=0)
```python
                self.dispatch_table[type(obj)] = handler_method
```
L169  ⚪  (score=0)
```python
            return handler_method(obj)
```
L170  ⚪  (score=0)
```python
        except Errors.CompileError:
```
L171  ⚪  (score=0)
```python
            raise
```
L172  ⚪  (score=0)
```python
        except Errors.AbortError:
```
L173  ⚪  (score=0)
```python
            raise
```
L174  ⚪  (score=0)
```python
        except Exception as e:
```
L175  ⚪  (score=0)
```python
            if DebugFlags.debug_no_exception_intercept:
```
L176  ⚪  (score=0)
```python
                raise
```
L177  ⚪  (score=0)
```python
            self._raise_compiler_error(obj, e)
```
L178  ⚪  (score=0)
```python
```
L179  ⚪  (score=0)
```python
    @cython.final
```
L180  ⚪  (score=0)
```python
    def _visitchild(self, child, parent, attrname, idx):
```
L181  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L182  ⚪  (score=0)
```python
        self.access_path.append((parent, attrname, idx))
```
L183  ⚪  (score=0)
```python
        result = self._visit(child)
```
L184  ⚪  (score=0)
```python
        self.access_path.pop()
```
L185  ⚪  (score=0)
```python
        return result
```
L186  ⚪  (score=0)
```python
```
L187  ⚪  (score=0)
```python
    def visitchildren(self, parent, attrs=None, exclude=None):
```
L188  ⚪  (score=0)
```python
        # generic def entry point for calls from Python subclasses
```
L189  ⚪  (score=0)
```python
        return self._visitchildren(parent, attrs, exclude)
```
L190  ⚪  (score=0)
```python
```
L191  ⚪  (score=0)
```python
    @cython.final
```
L192  ⚪  (score=0)
```python
    def _visitchildren(self, parent, attrs, exclude):
```
L193  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L194  ⚪  (score=0)
```python
        """
```
L195  ⚪  (score=0)
```python
        Visits the children of the given parent. If parent is None, returns
```
L196  ⚪  (score=0)
```python
        immediately (returning None).
```
L197  ⚪  (score=0)
```python
```
L198  ⚪  (score=0)
```python
        The return value is a dictionary giving the results for each
```
L199  ⚪  (score=0)
```python
        child (mapping the attribute name to either the return value
```
L200  ⚪  (score=0)
```python
        or a list of return values (in the case of multiple children
```
L201  ⚪  (score=0)
```python
        in an attribute)).
```
L202  ⚪  (score=0)
```python
        """
```
L203  ⚪  (score=0)
```python
        idx: cython.Py_ssize_t
```
L204  ⚪  (score=0)
```python
```
L205  ⚪  (score=0)
```python
        if parent is None: 
```
L206  ⚪  (score=0)
```python
            return None
```
L207  ⚪  (score=0)
```python
        result = {}
```
L208  ⚪  (score=0)
```python
        for attr in parent.child_attrs:
```
L209  ⚪  (score=0)
```python
            if attrs is not None and attr not in attrs: continue
```
L210  ⚪  (score=0)
```python
            if exclude is not None and attr in exclude: continue
```
L211  ⚪  (score=0)
```python
            child = getattr(parent, attr)
```
L212  ⚪  (score=0)
```python
            if child is not None:
```
L213  ⚪  (score=0)
```python
                if type(child) is list:
```
L214  ⚪  (score=0)
```python
                    childretval = [self._visitchild(x, parent, attr, idx) for idx, x in enumerate(child)]
```
L215  ⚪  (score=0)
```python
                else:
```
L216  ⚪  (score=0)
```python
                    childretval = self._visitchild(child, parent, attr, None)
```
L217  ⚪  (score=0)
```python
                    assert not isinstance(childretval, list), 'Cannot insert list here: %s in %r' % (attr, parent)
```
L218  ⚪  (score=0)
```python
                result[attr] = childretval
```
L219  ⚪  (score=0)
```python
        return result
```
L220  ⚪  (score=0)
```python
```
L221  ⚪  (score=0)
```python
```
L222  ⚪  (score=0)
```python
class VisitorTransform(TreeVisitor):
```
L223  ⚪  (score=0)
```python
    """
```
L224  ⚪  (score=0)
```python
    A tree transform is a base class for visitors that wants to do stream
```
L225  ⚪  (score=0)
```python
    processing of the structure (rather than attributes etc.) of a tree.
```
L226  ⚪  (score=0)
```python
```
L227  ⚪  (score=0)
```python
    It implements __call__ to simply visit the argument node.
```
L228  ⚪  (score=0)
```python
```
L229  ⚪  (score=0)
```python
    It requires the visitor methods to return the nodes which should take
```
L230  ⚪  (score=0)
```python
    the place of the visited node in the result tree (which can be the same
```
L231  ⚪  (score=0)
```python
    or one or more replacement). Specifically, if the return value from
```
L232  ⚪  (score=0)
```python
    a visitor method is:
```
L233  ⚪  (score=0)
```python
```
L234  ⚪  (score=0)
```python
    - [] or None; the visited node will be removed (set to None if an attribute and
```
L235  ⚪  (score=0)
```python
    removed if in a list)
```
L236  ⚪  (score=0)
```python
    - A single node; the visited node will be replaced by the returned node.
```
L237  ⚪  (score=0)
```python
    - A list of nodes; the visited nodes will be replaced by all the nodes in the
```
L238  ⚪  (score=0)
```python
    list. This will only work if the node was already a member of a list; if it
```
L239  ⚪  (score=0)
```python
    was not, an exception will be raised. (Typically you want to ensure that you
```
L240  ⚪  (score=0)
```python
    are within a StatListNode or similar before doing this.)
```
L241  ⚪  (score=0)
```python
    """
```
L242  ⚪  (score=0)
```python
    def visitchildren(self, parent, attrs=None, exclude=None):
```
L243  ⚪  (score=0)
```python
        # generic def entry point for calls from Python subclasses
```
L244  ⚪  (score=0)
```python
        return self._process_children(parent, attrs, exclude)
```
L245  ⚪  (score=0)
```python
```
L246  ⚪  (score=0)
```python
    @cython.final
```
L247  ⚪  (score=0)
```python
    def _process_children(self, parent, attrs=None, exclude=None):
```
L248  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L249  ⚪  (score=0)
```python
        result = self._visitchildren(parent, attrs, exclude)
```
L250  ⚪  (score=0)
```python
        for attr, newnode in result.items():
```
L251  ⚪  (score=0)
```python
            if type(newnode) is list:
```
L252  ⚪  (score=0)
```python
                newnode = self._flatten_list(newnode)
```
L253  ⚪  (score=0)
```python
            setattr(parent, attr, newnode)
```
L254  ⚪  (score=0)
```python
        return result
```
L255  ⚪  (score=0)
```python
```
L256  ⚪  (score=0)
```python
    @cython.final
```
L257  ⚪  (score=0)
```python
    def _flatten_list(self, orig_list):
```
L258  ⚪  (score=0)
```python
        # Flatten the list one level and remove any None
```
L259  ⚪  (score=0)
```python
        newlist = []
```
L260  ⚪  (score=0)
```python
        for x in orig_list:
```
L261  ⚪  (score=0)
```python
            if x is not None:
```
L262  ⚪  (score=0)
```python
                if type(x) is list:
```
L263  ⚪  (score=0)
```python
                    newlist.extend(x)
```
L264  ⚪  (score=0)
```python
                else:
```
L265  ⚪  (score=0)
```python
                    newlist.append(x)
```
L266  ⚪  (score=0)
```python
        return newlist
```
L267  ⚪  (score=0)
```python
```
L268  ⚪  (score=0)
```python
    def visitchild(self, parent, attr, idx=0):
```
L269  ⚪  (score=0)
```python
        # Helper to visit specific children from Python subclasses
```
L270  ⚪  (score=0)
```python
        child = getattr(parent, attr)
```
L271  ⚪  (score=0)
```python
        if child is not None:
```
L272  ⚪  (score=0)
```python
            node = self._visitchild(child, parent, attr, idx)
```
L273  ⚪  (score=0)
```python
            if node is not child:
```
L274  ⚪  (score=0)
```python
                setattr(parent, attr, node)
```
L275  ⚪  (score=0)
```python
            child = node
```
L276  ⚪  (score=0)
```python
        return child
```
L277  ⚪  (score=0)
```python
```
L278  ⚪  (score=0)
```python
    def recurse_to_children(self, node):
```
L279  ⚪  (score=0)
```python
        self._process_children(node)
```
L280  ⚪  (score=0)
```python
        return node
```
L281  ⚪  (score=0)
```python
```
L282  ⚪  (score=0)
```python
    def __call__(self, root):
```
L283  ⚪  (score=0)
```python
        return self._visit(root)
```
L284  ⚪  (score=0)
```python
```
L285  ⚪  (score=0)
```python
```
L286  ⚪  (score=0)
```python
class CythonTransform(VisitorTransform):
```
L287  ⚪  (score=0)
```python
    """Certain common conventions and utilities for Cython transforms.
```
L288  ⚪  (score=0)
```python
```
L289  ⚪  (score=0)
```python
     - Sets up the context of the pipeline in self.context
```
L290  ⚪  (score=0)
```python
     - Tracks directives in effect in self.current_directives
```
L291  ⚪  (score=0)
```python
    """
```
L292  ⚪  (score=0)
```python
    def __init__(self, context):
```
L293  ⚪  (score=0)
```python
        super().__init__()
```
L294  ⚪  (score=0)
```python
        self.context = context
```
L295  ⚪  (score=0)
```python
```
L296  ⚪  (score=0)
```python
    def __call__(self, node):
```
L297  ⚪  (score=0)
```python
        from . import Directives
```
L298  ⚪  (score=0)
```python
        from .ModuleNode import ModuleNode
```
L299  ⚪  (score=0)
```python
        if isinstance(node, ModuleNode):
```
L300  ⚪  (score=0)
```python
            directives = node.directives
```
L301  ⚪  (score=0)
```python
            if directives is None:
```
L302  ⚪  (score=0)
```python
                directives = Directives.DIRECTIVE_DEFAULTS.copy()
```
L303  ⚪  (score=0)
```python
            elif not isinstance(directives, Directives.Directives):
```
L304  ⚪  (score=0)
```python
                normalized = Directives.Directives()
```
L305  ⚪  (score=0)
```python
                normalized.update(directives)
```
L306  ⚪  (score=0)
```python
                directives = normalized
```
L307  ⚪  (score=0)
```python
            node.directives = directives
```
L308  ⚪  (score=0)
```python
            self.current_directives = directives
```
L309  ⚪  (score=0)
```python
        return super().__call__(node)
```
L310  ⚪  (score=0)
```python
```
L311  ⚪  (score=0)
```python
    def visit_CompilerDirectivesNode(self, node):
```
L312  ⚪  (score=0)
```python
        old = self.current_directives
```
L313  ⚪  (score=0)
```python
        self.current_directives = node.directives
```
L314  ⚪  (score=0)
```python
        self._process_children(node)
```
L315  ⚪  (score=0)
```python
        self.current_directives = old
```
L316  ⚪  (score=0)
```python
        return node
```
L317  ⚪  (score=0)
```python
```
L318  ⚪  (score=0)
```python
    def visit_Node(self, node):
```
L319  ⚪  (score=0)
```python
        self._process_children(node)
```
L320  ⚪  (score=0)
```python
        return node
```
L321  ⚪  (score=0)
```python
```
L322  ⚪  (score=0)
```python
```
L323  ⚪  (score=0)
```python
class ScopeTrackingTransform(CythonTransform):
```
L324  ⚪  (score=0)
```python
    # Keeps track of type of scopes
```
L325  ⚪  (score=0)
```python
    #scope_type: can be either of 'module', 'function', 'cclass', 'pyclass', 'struct'
```
L326  ⚪  (score=0)
```python
    #scope_node: the node that owns the current scope
```
L327  ⚪  (score=0)
```python
```
L328  ⚪  (score=0)
```python
    def visit_ModuleNode(self, node):
```
L329  ⚪  (score=0)
```python
        self.scope_type = 'module'
```
L330  ⚪  (score=0)
```python
        self.scope_node = node
```
L331  ⚪  (score=0)
```python
        self._process_children(node)
```
L332  ⚪  (score=0)
```python
        return node
```
L333  ⚪  (score=0)
```python
```
L334  ⚪  (score=0)
```python
    def visit_scope(self, node, scope_type):
```
L335  ⚪  (score=0)
```python
        prev = self.scope_type, self.scope_node
```
L336  ⚪  (score=0)
```python
        self.scope_type = scope_type
```
L337  ⚪  (score=0)
```python
        self.scope_node = node
```
L338  ⚪  (score=0)
```python
        self._process_children(node)
```
L339  ⚪  (score=0)
```python
        self.scope_type, self.scope_node = prev
```
L340  ⚪  (score=0)
```python
        return node
```
L341  ⚪  (score=0)
```python
```
L342  ⚪  (score=0)
```python
    def visit_CClassDefNode(self, node):
```
L343  ⚪  (score=0)
```python
        return self.visit_scope(node, 'cclass')
```
L344  ⚪  (score=0)
```python
```
L345  ⚪  (score=0)
```python
    def visit_PyClassDefNode(self, node):
```
L346  ⚪  (score=0)
```python
        return self.visit_scope(node, 'pyclass')
```
L347  ⚪  (score=0)
```python
```
L348  ⚪  (score=0)
```python
    def visit_FuncDefNode(self, node):
```
L349  ⚪  (score=0)
```python
        return self.visit_scope(node, 'function')
```
L350  ⚪  (score=0)
```python
```
L351  ⚪  (score=0)
```python
    def visit_CStructOrUnionDefNode(self, node):
```
L352  ⚪  (score=0)
```python
        return self.visit_scope(node, 'struct')
```
L353  ⚪  (score=0)
```python
```
L354  ⚪  (score=0)
```python
```
L355  ⚪  (score=0)
```python
class EnvTransform(CythonTransform):
```
L356  ⚪  (score=0)
```python
    """This transformation keeps a stack of the environments."""
```
L357  ⚪  (score=0)
```python
    def __call__(self, root):
```
L358  ⚪  (score=0)
```python
        self.env_stack: list[tuple[Node, Scope]] = []
```
L359  ⚪  (score=0)
```python
        self.enter_scope(root, root.scope)
```
L360  ⚪  (score=0)
```python
        return super().__call__(root)
```
L361  ⚪  (score=0)
```python
```
L362  ⚪  (score=0)
```python
    def current_env(self):
```
L363  ⚪  (score=0)
```python
        return self.env_stack[-1][1]
```
L364  ⚪  (score=0)
```python
```
L365  ⚪  (score=0)
```python
    def current_scope_node(self):
```
L366  ⚪  (score=0)
```python
        return self.env_stack[-1][0]
```
L367  ⚪  (score=0)
```python
```
L368  ⚪  (score=0)
```python
    def global_scope(self):
```
L369  ⚪  (score=0)
```python
        return self.current_env().global_scope()
```
L370  ⚪  (score=0)
```python
```
L371  ⚪  (score=0)
```python
    def enter_scope(self, node:"Node", scope:"Scope"):
```
L372  ⚪  (score=0)
```python
        self.env_stack.append((node, scope))
```
L373  ⚪  (score=0)
```python
```
L374  ⚪  (score=0)
```python
    def exit_scope(self):
```
L375  ⚪  (score=0)
```python
        self.env_stack.pop()
```
L376  ⚪  (score=0)
```python
```
L377  ⚪  (score=0)
```python
    def visit_FuncDefNode(self, node):
```
L378  ⚪  (score=0)
```python
        self.visit_func_outer_attrs(node)
```
L379  ⚪  (score=0)
```python
        self.enter_scope(node, node.local_scope)
```
L380  ⚪  (score=0)
```python
        self.visitchildren(node, attrs=None, exclude=node.outer_attrs)
```
L381  ⚪  (score=0)
```python
        self.exit_scope()
```
L382  ⚪  (score=0)
```python
        return node
```
L383  ⚪  (score=0)
```python
```
L384  ⚪  (score=0)
```python
    def visit_func_outer_attrs(self, node):
```
L385  ⚪  (score=0)
```python
        self.visitchildren(node, attrs=node.outer_attrs)
```
L386  ⚪  (score=0)
```python
```
L387  ⚪  (score=0)
```python
    def visit_GeneratorBodyDefNode(self, node):
```
L388  ⚪  (score=0)
```python
        self._process_children(node)
```
L389  ⚪  (score=0)
```python
        return node
```
L390  ⚪  (score=0)
```python
```
L391  ⚪  (score=0)
```python
    def visit_ClassDefNode(self, node):
```
L392  ⚪  (score=0)
```python
        self.enter_scope(node, node.scope)
```
L393  ⚪  (score=0)
```python
        self._process_children(node)
```
L394  ⚪  (score=0)
```python
        self.exit_scope()
```
L395  ⚪  (score=0)
```python
        return node
```
L396  ⚪  (score=0)
```python
```
L397  ⚪  (score=0)
```python
    def visit_CStructOrUnionDefNode(self, node):
```
L398  ⚪  (score=0)
```python
        self.enter_scope(node, node.scope)
```
L399  ⚪  (score=0)
```python
        self._process_children(node)
```
L400  ⚪  (score=0)
```python
        self.exit_scope()
```
L401  ⚪  (score=0)
```python
        return node
```
L402  ⚪  (score=0)
```python
```
L403  ⚪  (score=0)
```python
    def visit_ScopedExprNode(self, node):
```
L404  ⚪  (score=0)
```python
        if node.expr_scope:
```
L405  ⚪  (score=0)
```python
            self.enter_scope(node, node.expr_scope)
```
L406  ⚪  (score=0)
```python
            self._process_children(node)
```
L407  ⚪  (score=0)
```python
            self.exit_scope()
```
L408  ⚪  (score=0)
```python
        else:
```
L409  ⚪  (score=0)
```python
            self._process_children(node)
```
L410  ⚪  (score=0)
```python
        return node
```
L411  ⚪  (score=0)
```python
```
L412  ⚪  (score=0)
```python
    def visit_CArgDeclNode(self, node):
```
L413  ⚪  (score=0)
```python
        # default arguments are evaluated in the outer scope
```
L414  ⚪  (score=0)
```python
        if node.default:
```
L415  ⚪  (score=0)
```python
            attrs = [attr for attr in node.child_attrs if attr != 'default']
```
L416  ⚪  (score=0)
```python
            self._process_children(node, attrs)
```
L417  ⚪  (score=0)
```python
            self.enter_scope(node, self.current_env().outer_scope)
```
L418  ⚪  (score=0)
```python
            self.visitchildren(node, ('default',))
```
L419  ⚪  (score=0)
```python
            self.exit_scope()
```
L420  ⚪  (score=0)
```python
        else:
```
L421  ⚪  (score=0)
```python
            self._process_children(node)
```
L422  ⚪  (score=0)
```python
        return node
```
L423  ⚪  (score=0)
```python
```
L424  ⚪  (score=0)
```python
```
L425  ⚪  (score=0)
```python
class NodeRefCleanupMixin:
```
L426  ⚪  (score=0)
```python
    """Clean up references to nodes that were replaced.
```
L427  ⚪  (score=0)
```python
```
L428  ⚪  (score=0)
```python
    NOTE: this implementation assumes that the replacement is
```
L429  ⚪  (score=0)
```python
    done first, before hitting any further references during
```
L430  ⚪  (score=0)
```python
    normal tree traversal.  This needs to be arranged by calling
```
L431  ⚪  (score=0)
```python
    "self.visitchildren()" at a proper place in the transform
```
L432  ⚪  (score=0)
```python
    and by ordering the "child_attrs" of nodes appropriately.
```
L433  ⚪  (score=0)
```python
    """
```
L434  ⚪  (score=0)
```python
    def __init__(self, *args):
```
L435  ⚪  (score=0)
```python
        super().__init__(*args)
```
L436  ⚪  (score=0)
```python
        self._replacements = {}
```
L437  ⚪  (score=0)
```python
```
L438  ⚪  (score=0)
```python
    def visit_CloneNode(self, node):
```
L439  ⚪  (score=0)
```python
        arg = node.arg
```
L440  ⚪  (score=0)
```python
        if arg not in self._replacements:
```
L441  ⚪  (score=0)
```python
            self.visitchildren(arg)
```
L442  ⚪  (score=0)
```python
        node.arg = self._replacements.get(arg, arg)
```
L443  ⚪  (score=0)
```python
        return node
```
L444  ⚪  (score=0)
```python
```
L445  ⚪  (score=0)
```python
    def visit_ResultRefNode(self, node):
```
L446  ⚪  (score=0)
```python
        expr = node.expression
```
L447  ⚪  (score=0)
```python
        if expr is None or expr not in self._replacements:
```
L448  ⚪  (score=0)
```python
            self.visitchildren(node)
```
L449  ⚪  (score=0)
```python
            expr = node.expression
```
L450  ⚪  (score=0)
```python
        if expr is not None:
```
L451  ⚪  (score=0)
```python
            node.expression = self._replacements.get(expr, expr)
```
L452  ⚪  (score=0)
```python
        return node
```
L453  ⚪  (score=0)
```python
```
L454  ⚪  (score=0)
```python
    def replace(self, node, replacement):
```
L455  ⚪  (score=0)
```python
        self._replacements[node] = replacement
```
L456  ⚪  (score=0)
```python
        return replacement
```
L457  ⚪  (score=0)
```python
```
L458  ⚪  (score=0)
```python
```
L459  ⚪  (score=0)
```python
find_special_method_for_binary_operator = {
```
L460  ⚪  (score=0)
```python
    '<':  '__lt__',
```
L461  ⚪  (score=0)
```python
    '<=': '__le__',
```
L462  ⚪  (score=0)
```python
    '==': '__eq__',
```
L463  ⚪  (score=0)
```python
    '!=': '__ne__',
```
L464  ⚪  (score=0)
```python
    '>=': '__ge__',
```
L465  ⚪  (score=0)
```python
    '>':  '__gt__',
```
L466  ⚪  (score=0)
```python
    '+':  '__add__',
```
L467  ⚪  (score=0)
```python
    '&':  '__and__',
```
L468  ⚪  (score=0)
```python
    '/':  '__div__',
```
L469  ⚪  (score=0)
```python
    '//': '__floordiv__',
```
L470  ⚪  (score=0)
```python
    '<<': '__lshift__',
```
L471  ⚪  (score=0)
```python
    '%':  '__mod__',
```
L472  ⚪  (score=0)
```python
    '*':  '__mul__',
```
L473  ⚪  (score=0)
```python
    '|':  '__or__',
```
L474  ⚪  (score=0)
```python
    '**': '__pow__',
```
L475  ⚪  (score=0)
```python
    '>>': '__rshift__',
```
L476  ⚪  (score=0)
```python
    '-':  '__sub__',
```
L477  ⚪  (score=0)
```python
    '^':  '__xor__',
```
L478  ⚪  (score=0)
```python
    'in': '__contains__',
```
L479  ⚪  (score=0)
```python
}.get
```
L480  ⚪  (score=0)
```python
```
L481  ⚪  (score=0)
```python
```
L482  ⚪  (score=0)
```python
find_special_method_for_unary_operator = {
```
L483  ⚪  (score=0)
```python
    'not': '__not__',
```
L484  ⚪  (score=0)
```python
    '~':   '__inv__',
```
L485  ⚪  (score=0)
```python
    '-':   '__neg__',
```
L486  ⚪  (score=0)
```python
    '+':   '__pos__',
```
L487  ⚪  (score=0)
```python
}.get
```
L488  ⚪  (score=0)
```python
```
L489  ⚪  (score=0)
```python
```
L490  ⚪  (score=0)
```python
class MethodDispatcherTransform(EnvTransform):
```
L491  ⚪  (score=0)
```python
    """
```
L492  ⚪  (score=0)
```python
    Base class for transformations that want to intercept on specific
```
L493  ⚪  (score=0)
```python
    builtin functions or methods of builtin types, including special
```
L494  ⚪  (score=0)
```python
    methods triggered by Python operators.  Must run after declaration
```
L495  ⚪  (score=0)
```python
    analysis when entries were assigned.
```
L496  ⚪  (score=0)
```python
```
L497  ⚪  (score=0)
```python
    Naming pattern for handler methods is as follows:
```
L498  ⚪  (score=0)
```python
```
L499  ⚪  (score=0)
```python
    * builtin functions: _handle_(general|simple|any)_function_NAME
```
L500  ⚪  (score=0)
```python
```
L501  ⚪  (score=0)
```python
    * builtin methods: _handle_(general|simple|any)_method_TYPENAME_METHODNAME
```
L502  ⚪  (score=0)
```python
    """
```
L503  ⚪  (score=0)
```python
    # only visit call nodes and Python operations
```
L504  ⚪  (score=0)
```python
    def visit_GeneralCallNode(self, node):
```
L505  ⚪  (score=0)
```python
        self._process_children(node)
```
L506  ⚪  (score=0)
```python
        function = node.function
```
L507  ⚪  (score=0)
```python
        if not function.type.is_pyobject:
```
L508  ⚪  (score=0)
```python
            return node
```
L509  ⚪  (score=0)
```python
        arg_tuple = node.positional_args
```
L510  ⚪  (score=0)
```python
        if not isinstance(arg_tuple, ExprNodes.TupleNode):
```
L511  ⚪  (score=0)
```python
            return node
```
L512  ⚪  (score=0)
```python
        keyword_args = node.keyword_args
```
L513  ⚪  (score=0)
```python
        if keyword_args and not isinstance(keyword_args, ExprNodes.DictNode):
```
L514  ⚪  (score=0)
```python
            # can't handle **kwargs
```
L515  ⚪  (score=0)
```python
            return node
```
L516  ⚪  (score=0)
```python
        args = arg_tuple.args
```
L517  ⚪  (score=0)
```python
        return self._dispatch_to_handler(node, function, args, keyword_args)
```
L518  ⚪  (score=0)
```python
```
L519  ⚪  (score=0)
```python
    def visit_SimpleCallNode(self, node):
```
L520  ⚪  (score=0)
```python
        self._process_children(node)
```
L521  ⚪  (score=0)
```python
        function = node.function
```
L522  ⚪  (score=0)
```python
        if function.type.is_pyobject:
```
L523  ⚪  (score=0)
```python
            arg_tuple = node.arg_tuple
```
L524  ⚪  (score=0)
```python
            if not isinstance(arg_tuple, ExprNodes.TupleNode):
```
L525  ⚪  (score=0)
```python
                return node
```
L526  ⚪  (score=0)
```python
            args = arg_tuple.args
```
L527  ⚪  (score=0)
```python
        else:
```
L528  ⚪  (score=0)
```python
            args = node.args
```
L529  ⚪  (score=0)
```python
        return self._dispatch_to_handler(node, function, args, None)
```
L530  ⚪  (score=0)
```python
```
L531  ⚪  (score=0)
```python
    def visit_PrimaryCmpNode(self, node):
```
L532  ⚪  (score=0)
```python
        if node.cascade:
```
L533  ⚪  (score=0)
```python
            # not currently handled below
```
L534  ⚪  (score=0)
```python
            self._process_children(node)
```
L535  ⚪  (score=0)
```python
            return node
```
L536  ⚪  (score=0)
```python
        return self._visit_binop_node(node)
```
L537  ⚪  (score=0)
```python
```
L538  ⚪  (score=0)
```python
    def visit_BinopNode(self, node):
```
L539  ⚪  (score=0)
```python
        return self._visit_binop_node(node)
```
L540  ⚪  (score=0)
```python
```
L541  ⚪  (score=0)
```python
    def _visit_binop_node(self, node):
```
L542  ⚪  (score=0)
```python
        self._process_children(node)
```
L543  ⚪  (score=0)
```python
        # FIXME: could special case 'not_in'
```
L544  ⚪  (score=0)
```python
        special_method_name = find_special_method_for_binary_operator(node.operator)
```
L545  ⚪  (score=0)
```python
        if special_method_name:
```
L546  ⚪  (score=0)
```python
            operand1, operand2 = node.operand1, node.operand2
```
L547  ⚪  (score=0)
```python
            if special_method_name == '__contains__':
```
L548  ⚪  (score=0)
```python
                operand1, operand2 = operand2, operand1
```
L549  ⚪  (score=0)
```python
            elif special_method_name == '__div__' and Future.division in self.current_env().context.future_directives:
```
L550  ⚪  (score=0)
```python
                    special_method_name = '__truediv__'
```
L551  ⚪  (score=0)
```python
            obj_type = operand1.type
```
L552  ⚪  (score=0)
```python
            type_name = obj_type.name if obj_type.is_builtin_type else "object" # safety measure
```
L553  ⚪  (score=0)
```python
            node = self._dispatch_to_method_handler(
```
L554  ⚪  (score=0)
```python
                special_method_name, None, False, type_name,
```
L555  ⚪  (score=0)
```python
                node, None, [operand1, operand2], None)
```
L556  ⚪  (score=0)
```python
        return node
```
L557  ⚪  (score=0)
```python
```
L558  ⚪  (score=0)
```python
    def visit_UnopNode(self, node):
```
L559  ⚪  (score=0)
```python
        self._process_children(node)
```
L560  ⚪  (score=0)
```python
        special_method_name = find_special_method_for_unary_operator(node.operator)
```
L561  ⚪  (score=0)
```python
        if special_method_name:
```
L562  ⚪  (score=0)
```python
            operand = node.operand
```
L563  ⚪  (score=0)
```python
            obj_type = operand.type
```
L564  ⚪  (score=0)
```python
            type_name = obj_type.name if obj_type.is_builtin_type else "object" # safety measure
```
L565  ⚪  (score=0)
```python
            node = self._dispatch_to_method_handler(
```
L566  ⚪  (score=0)
```python
                special_method_name, None, False, type_name,
```
L567  ⚪  (score=0)
```python
                node, None, [operand], None)
```
L568  ⚪  (score=0)
```python
        return node
```
L569  ⚪  (score=0)
```python
```
L570  ⚪  (score=0)
```python
    ### dispatch to specific handlers
```
L571  ⚪  (score=0)
```python
```
L572  ⚪  (score=0)
```python
    def _find_handler(self, match_name, has_kwargs):
```
L573  ⚪  (score=0)
```python
        if not match_name.isascii():
```
L574  ⚪  (score=0)
```python
            # Classes with unicode names won't have specific handlers.
```
L575  ⚪  (score=0)
```python
            return None
```
L576  ⚪  (score=0)
```python
```
L577  ⚪  (score=0)
```python
        call_type = 'general' if has_kwargs else 'simple'
```
L578  ⚪  (score=0)
```python
        handler = getattr(self, f'_handle_{call_type}_{match_name}', None)
```
L579  ⚪  (score=0)
```python
        if handler is None:
```
L580  ⚪  (score=0)
```python
            handler = getattr(self, f'_handle_any_{match_name}', None)
```
L581  ⚪  (score=0)
```python
        return handler
```
L582  ⚪  (score=0)
```python
```
L583  ⚪  (score=0)
```python
    def _delegate_to_assigned_value(self, node, function, arg_list, kwargs):
```
L584  ⚪  (score=0)
```python
        assignment = function.cf_state[0]
```
L585  ⚪  (score=0)
```python
        value = assignment.rhs
```
L586  ⚪  (score=0)
```python
        if value.is_name:
```
L587  ⚪  (score=0)
```python
            if not value.entry or len(value.entry.cf_assignments) > 1:
```
L588  ⚪  (score=0)
```python
                # the variable might have been reassigned => play safe
```
L589  ⚪  (score=0)
```python
                return node
```
L590  ⚪  (score=0)
```python
        elif value.is_attribute and value.obj.is_name:
```
L591  ⚪  (score=0)
```python
            if not value.obj.entry or len(value.obj.entry.cf_assignments) > 1:
```
L592  ⚪  (score=0)
```python
                # the underlying variable might have been reassigned => play safe
```
L593  ⚪  (score=0)
```python
                return node
```
L594  ⚪  (score=0)
```python
        else:
```
L595  ⚪  (score=0)
```python
            return node
```
L596  ⚪  (score=0)
```python
        return self._dispatch_to_handler(
```
L597  ⚪  (score=0)
```python
            node, value, arg_list, kwargs)
```
L598  ⚪  (score=0)
```python
```
L599  ⚪  (score=0)
```python
    def _dispatch_to_handler(self, node, function, arg_list, kwargs):
```
L600  ⚪  (score=0)
```python
        if function.is_name:
```
L601  ⚪  (score=0)
```python
            # we only consider functions that are either builtin
```
L602  ⚪  (score=0)
```python
            # Python functions or builtins that were already replaced
```
L603  ⚪  (score=0)
```python
            # into a C function call (defined in the builtin scope)
```
L604  ⚪  (score=0)
```python
            if not function.entry:
```
L605  ⚪  (score=0)
```python
                return node
```
L606  ⚪  (score=0)
```python
            entry = function.entry
```
L607  ⚪  (score=0)
```python
            is_builtin = (
```
L608  ⚪  (score=0)
```python
                entry.is_builtin or
```
L609  ⚪  (score=0)
```python
                entry is self.current_env().builtin_scope().lookup_here(function.name))
```
L610  ⚪  (score=0)
```python
            if not is_builtin:
```
L611  ⚪  (score=0)
```python
                if function.cf_state and function.cf_state.is_single:
```
L612  ⚪  (score=0)
```python
                    # we know the value of the variable
```
L613  ⚪  (score=0)
```python
                    # => see if it's usable instead
```
L614  ⚪  (score=0)
```python
                    return self._delegate_to_assigned_value(
```
L615  ⚪  (score=0)
```python
                        node, function, arg_list, kwargs)
```
L616  ⚪  (score=0)
```python
                if arg_list and entry.is_cmethod and entry.scope and entry.scope.parent_type.is_builtin_type:
```
L617  ⚪  (score=0)
```python
                    if entry.scope.parent_type is arg_list[0].type:
```
L618  ⚪  (score=0)
```python
                        # Optimised (unbound) method of a builtin type => try to "de-optimise".
```
L619  ⚪  (score=0)
```python
                        return self._dispatch_to_method_handler(
```
L620  ⚪  (score=0)
```python
                            entry.name, self_arg=None, is_unbound_method=True,
```
L621  ⚪  (score=0)
```python
                            type_name=entry.scope.parent_type.name,
```
L622  ⚪  (score=0)
```python
                            node=node, function=function, arg_list=arg_list, kwargs=kwargs)
```
L623  ⚪  (score=0)
```python
                return node
```
L624  ⚪  (score=0)
```python
            function_handler = self._find_handler(
```
L625  ⚪  (score=0)
```python
                f"function_{function.name}", kwargs)
```
L626  ⚪  (score=0)
```python
            if function_handler is None:
```
L627  ⚪  (score=0)
```python
                return self._handle_function(node, function.name, function, arg_list, kwargs)
```
L628  ⚪  (score=0)
```python
            if kwargs:
```
L629  ⚪  (score=0)
```python
                return function_handler(node, function, arg_list, kwargs)
```
L630  ⚪  (score=0)
```python
```
L631  ⚪  (score=0)
```python
            return function_handler(node, function, arg_list)
```
L632  ⚪  (score=0)
```python
        if function.is_attribute:
```
L633  ⚪  (score=0)
```python
            attr_name = function.attribute
```
L634  ⚪  (score=0)
```python
            if function.type.is_pyobject:
```
L635  ⚪  (score=0)
```python
                self_arg = function.obj
```
L636  ⚪  (score=0)
```python
            elif node.self and function.entry:
```
L637  ⚪  (score=0)
```python
                entry = function.entry.as_variable
```
L638  ⚪  (score=0)
```python
                if not entry or not entry.is_builtin:
```
L639  ⚪  (score=0)
```python
                    return node
```
L640  ⚪  (score=0)
```python
                # C implementation of a Python builtin method - see if we find further matches
```
L641  ⚪  (score=0)
```python
                self_arg = node.self
```
L642  ⚪  (score=0)
```python
                arg_list = arg_list[1:]  # drop CloneNode of self argument
```
L643  ⚪  (score=0)
```python
            else:
```
L644  ⚪  (score=0)
```python
                return node
```
L645  ⚪  (score=0)
```python
            obj_type = self_arg.type
```
L646  ⚪  (score=0)
```python
            is_unbound_method = False
```
L647  ⚪  (score=0)
```python
            if obj_type.is_builtin_type:
```
L648  ⚪  (score=0)
```python
                if obj_type is Builtin.type_type and self_arg.is_name and arg_list and arg_list[0].type.is_pyobject:
```
L649  ⚪  (score=0)
```python
                    # calling an unbound method like 'list.append(L,x)'
```
L650  ⚪  (score=0)
```python
                    # (ignoring 'type.mro()' here ...)
```
L651  ⚪  (score=0)
```python
                    type_name = self_arg.name
```
L652  ⚪  (score=0)
```python
                    self_arg = None
```
L653  ⚪  (score=0)
```python
                    is_unbound_method = True
```
L654  ⚪  (score=0)
```python
                else:
```
L655  ⚪  (score=0)
```python
                    type_name = obj_type.name
```
L656  ⚪  (score=0)
```python
                if type_name == 'str':
```
L657  ⚪  (score=0)
```python
                    # We traditionally used the type name 'unicode' for 'str' dispatch methods.
```
L658  ⚪  (score=0)
```python
                    type_name = 'unicode'
```
L659  ⚪  (score=0)
```python
            else:
```
L660  ⚪  (score=0)
```python
                type_name = "object"  # safety measure
```
L661  ⚪  (score=0)
```python
            return self._dispatch_to_method_handler(
```
L662  ⚪  (score=0)
```python
                attr_name, self_arg, is_unbound_method, type_name,
```
L663  ⚪  (score=0)
```python
                node, function, arg_list, kwargs)
```
L664  ⚪  (score=0)
```python
```
L665  ⚪  (score=0)
```python
        return node
```
L666  ⚪  (score=0)
```python
```
L667  ⚪  (score=0)
```python
    def _dispatch_to_method_handler(self, attr_name, self_arg,
```
L668  ⚪  (score=0)
```python
                                    is_unbound_method, type_name,
```
L669  ⚪  (score=0)
```python
                                    node, function, arg_list, kwargs):
```
L670  ⚪  (score=0)
```python
        method_handler = self._find_handler(
```
L671  ⚪  (score=0)
```python
            f"method_{type_name}_{attr_name}", kwargs)
```
L672  ⚪  (score=0)
```python
        if method_handler is None:
```
L673  ⚪  (score=0)
```python
            if (attr_name in TypeSlots.special_method_names
```
L674  ⚪  (score=0)
```python
                    or attr_name in ['__new__', '__class__']):
```
L675  ⚪  (score=0)
```python
                method_handler = self._find_handler(
```
L676  ⚪  (score=0)
```python
                    f"slot{attr_name}", kwargs)
```
L677  ⚪  (score=0)
```python
            if method_handler is None:
```
L678  ⚪  (score=0)
```python
                return self._handle_method(
```
L679  ⚪  (score=0)
```python
                    node, type_name, attr_name, function,
```
L680  ⚪  (score=0)
```python
                    arg_list, is_unbound_method, kwargs)
```
L681  ⚪  (score=0)
```python
        if self_arg is not None:
```
L682  ⚪  (score=0)
```python
            arg_list = [self_arg] + list(arg_list)
```
L683  ⚪  (score=0)
```python
        if kwargs:
```
L684  ⚪  (score=0)
```python
            result = method_handler(
```
L685  ⚪  (score=0)
```python
                node, function, arg_list, is_unbound_method, kwargs)
```
L686  ⚪  (score=0)
```python
        else:
```
L687  ⚪  (score=0)
```python
            result = method_handler(
```
L688  ⚪  (score=0)
```python
                node, function, arg_list, is_unbound_method)
```
L689  ⚪  (score=0)
```python
        return result
```
L690  ⚪  (score=0)
```python
```
L691  ⚪  (score=0)
```python
    def _handle_function(self, node, function_name, function, arg_list, kwargs):
```
L692  ⚪  (score=0)
```python
        """Fallback handler"""
```
L693  ⚪  (score=0)
```python
        return node
```
L694  ⚪  (score=0)
```python
```
L695  ⚪  (score=0)
```python
    def _handle_method(self, node, type_name, attr_name, function,
```
L696  ⚪  (score=0)
```python
                       arg_list, is_unbound_method, kwargs):
```
L697  ⚪  (score=0)
```python
        """Fallback handler"""
```
L698  ⚪  (score=0)
```python
        return node
```
L699  ⚪  (score=0)
```python
```
L700  ⚪  (score=0)
```python
```
L701  ⚪  (score=0)
```python
class RecursiveNodeReplacer(VisitorTransform):
```
L702  ⚪  (score=0)
```python
    """
```
L703  ⚪  (score=0)
```python
    Recursively replace all occurrences of a node in a subtree by
```
L704  ⚪  (score=0)
```python
    another node.
```
L705  ⚪  (score=0)
```python
    """
```
L706  ⚪  (score=0)
```python
    def __init__(self, orig_node, new_node):
```
L707  ⚪  (score=0)
```python
        super().__init__()
```
L708  ⚪  (score=0)
```python
        self.orig_node, self.new_node = orig_node, new_node
```
L709  ⚪  (score=0)
```python
```
L710  ⚪  (score=0)
```python
    def visit_CloneNode(self, node):
```
L711  ⚪  (score=0)
```python
        if node is self.orig_node:
```
L712  ⚪  (score=0)
```python
            return self.new_node
```
L713  ⚪  (score=0)
```python
        if node.arg is self.orig_node:
```
L714  ⚪  (score=0)
```python
            node.arg = self.new_node
```
L715  ⚪  (score=0)
```python
        return node
```
L716  ⚪  (score=0)
```python
```
L717  ⚪  (score=0)
```python
    def visit_Node(self, node):
```
L718  ⚪  (score=0)
```python
        self._process_children(node)
```
L719  ⚪  (score=0)
```python
        if node is self.orig_node:
```
L720  ⚪  (score=0)
```python
            return self.new_node
```
L721  ⚪  (score=0)
```python
        else:
```
L722  ⚪  (score=0)
```python
            return node
```
L723  ⚪  (score=0)
```python
```
L724  ⚪  (score=0)
```python
def recursively_replace_node(tree, old_node, new_node):
```
L725  ⚪  (score=0)
```python
    replace_in = RecursiveNodeReplacer(old_node, new_node)
```
L726  ⚪  (score=0)
```python
    replace_in(tree)
```
L727  ⚪  (score=0)
```python
```
L728  ⚪  (score=0)
```python
```
L729  ⚪  (score=0)
```python
class NodeFinder(TreeVisitor):
```
L730  ⚪  (score=0)
```python
    """
```
L731  ⚪  (score=0)
```python
    Find out if a node appears in a subtree.
```
L732  ⚪  (score=0)
```python
    """
```
L733  ⚪  (score=0)
```python
    def __init__(self, node):
```
L734  ⚪  (score=0)
```python
        super().__init__()
```
L735  ⚪  (score=0)
```python
        self.node = node
```
L736  ⚪  (score=0)
```python
        self.found = False
```
L737  ⚪  (score=0)
```python
```
L738  ⚪  (score=0)
```python
    def visit_Node(self, node):
```
L739  ⚪  (score=0)
```python
        if self.found:
```
L740  ⚪  (score=0)
```python
            pass  # short-circuit
```
L741  ⚪  (score=0)
```python
        elif node is self.node:
```
L742  ⚪  (score=0)
```python
            self.found = True
```
L743  ⚪  (score=0)
```python
        else:
```
L744  ⚪  (score=0)
```python
            self._visitchildren(node, None, None)
```
L745  ⚪  (score=0)
```python
```
L746  ⚪  (score=0)
```python
def tree_contains(tree, node):
```
L747  ⚪  (score=0)
```python
    finder = NodeFinder(node)
```
L748  ⚪  (score=0)
```python
    finder.visit(tree)
```
L749  ⚪  (score=0)
```python
    return finder.found
```
L750  ⚪  (score=0)
```python
```
L751  ⚪  (score=0)
```python
```
L752  ⚪  (score=0)
```python
# Utils
```
L753  ⚪  (score=0)
```python
def replace_node(ptr, value):
```
L754  ⚪  (score=0)
```python
    """Replaces a node. ptr is of the form used on the access path stack
```
L755  ⚪  (score=0)
```python
    (parent, attrname, listidx|None)
```
L756  ⚪  (score=0)
```python
    """
```
L757  ⚪  (score=0)
```python
    parent, attrname, listidx = ptr
```
L758  ⚪  (score=0)
```python
    if listidx is None:
```
L759  ⚪  (score=0)
```python
        setattr(parent, attrname, value)
```
L760  ⚪  (score=0)
```python
    else:
```
L761  ⚪  (score=0)
```python
        getattr(parent, attrname)[listidx] = value
```
L762  ⚪  (score=0)
```python
```
L763  ⚪  (score=0)
```python
```
L764  ⚪  (score=0)
```python
class PrintTree(TreeVisitor):
```
L765  ⚪  (score=0)
```python
    """Prints a representation of the tree to standard output.
```
L766  ⚪  (score=0)
```python
    Subclass and override repr_of to provide more information
```
L767  ⚪  (score=0)
```python
    about nodes. """
```
L768  ⚪  (score=0)
```python
    def __init__(self, start=None, end=None):
```
L769  ⚪  (score=0)
```python
        TreeVisitor.__init__(self)
```
L770  ⚪  (score=0)
```python
        self._indent = ""
```
L771  ⚪  (score=0)
```python
        if start is not None or end is not None:
```
L772  ⚪  (score=0)
```python
            self._line_range = (start or 0, end or 2**30)
```
L773  ⚪  (score=0)
```python
        else:
```
L774  ⚪  (score=0)
```python
            self._line_range = None
```
L775  ⚪  (score=0)
```python
```
L776  ⚪  (score=0)
```python
    def indent(self):
```
L777  ⚪  (score=0)
```python
        self._indent += "  "
```
L778  ⚪  (score=0)
```python
```
L779  ⚪  (score=0)
```python
    def unindent(self):
```
L780  ⚪  (score=0)
```python
        self._indent = self._indent[:-2]
```
L781  ⚪  (score=0)
```python
```
L782  ⚪  (score=0)
```python
    def __call__(self, tree, phase=None):
```
L783  ⚪  (score=0)
```python
        print("Parse tree dump at phase '%s'" % phase)
```
L784  ⚪  (score=0)
```python
        self.visit(tree)
```
L785  ⚪  (score=0)
```python
        return tree
```
L786  ⚪  (score=0)
```python
```
L787  ⚪  (score=0)
```python
    # Don't do anything about process_list, the defaults gives
```
L788  ⚪  (score=0)
```python
    # nice-looking name[idx] nodes which will visually appear
```
L789  ⚪  (score=0)
```python
    # under the parent-node, not displaying the list itself in
```
L790  ⚪  (score=0)
```python
    # the hierarchy.
```
L791  ⚪  (score=0)
```python
    def visit_Node(self, node):
```
L792  ⚪  (score=0)
```python
        self._print_node(node)
```
L793  ⚪  (score=0)
```python
        self.indent()
```
L794  ⚪  (score=0)
```python
        self.visitchildren(node)
```
L795  ⚪  (score=0)
```python
        self.unindent()
```
L796  ⚪  (score=0)
```python
        return node
```
L797  ⚪  (score=0)
```python
```
L798  ⚪  (score=0)
```python
    def visit_CloneNode(self, node):
```
L799  ⚪  (score=0)
```python
        self._print_node(node)
```
L800  ⚪  (score=0)
```python
        self.indent()
```
L801  ⚪  (score=0)
```python
        line = node.pos[1]
```
L802  ⚪  (score=0)
```python
        if self._line_range is None or self._line_range[0] <= line <= self._line_range[1]:
```
L803  ⚪  (score=0)
```python
            print("%s- %s: %s" % (self._indent, 'arg', self.repr_of(node.arg)))
```
L804  ⚪  (score=0)
```python
        self.indent()
```
L805  ⚪  (score=0)
```python
        self.visitchildren(node.arg)
```
L806  ⚪  (score=0)
```python
        self.unindent()
```
L807  ⚪  (score=0)
```python
        self.unindent()
```
L808  ⚪  (score=0)
```python
        return node
```
L809  ⚪  (score=0)
```python
```
L810  ⚪  (score=0)
```python
    def _print_node(self, node):
```
L811  ⚪  (score=0)
```python
        line = node.pos[1]
```
L812  ⚪  (score=0)
```python
        if self._line_range is None or self._line_range[0] <= line <= self._line_range[1]:
```
L813  ⚪  (score=0)
```python
            if len(self.access_path) == 0:
```
L814  ⚪  (score=0)
```python
                name = "(root)"
```
L815  ⚪  (score=0)
```python
            else:
```
L816  ⚪  (score=0)
```python
                parent, attr, idx = self.access_path[-1]
```
L817  ⚪  (score=0)
```python
                if idx is not None:
```
L818  ⚪  (score=0)
```python
                    name = "%s[%d]" % (attr, idx)
```
L819  ⚪  (score=0)
```python
                else:
```
L820  ⚪  (score=0)
```python
                    name = attr
```
L821  ⚪  (score=0)
```python
            print("%s- %s: %s" % (self._indent, name, self.repr_of(node)))
```
L822  ⚪  (score=0)
```python
```
L823  ⚪  (score=0)
```python
    def repr_of(self, node):
```
L824  ⚪  (score=0)
```python
        if node is None:
```
L825  ⚪  (score=0)
```python
            return "(none)"
```
L826  ⚪  (score=0)
```python
        else:
```
L827  ⚪  (score=0)
```python
            result = node.__class__.__name__
```
L828  ⚪  (score=0)
```python
            if isinstance(node, ExprNodes.NameNode):
```
L829  ⚪  (score=0)
```python
                result += "(type=%s, name=\"%s\")" % (repr(node.type), node.name)
```
L830  ⚪  (score=0)
```python
            elif isinstance(node, Nodes.DefNode):
```
L831  ⚪  (score=0)
```python
                result += "(name=\"%s\")" % node.name
```
L832  ⚪  (score=0)
```python
            elif isinstance(node, Nodes.CFuncDefNode):
```
L833  ⚪  (score=0)
```python
                result += "(name=\"%s\", type=\"%s\")" % (
```
L834  ⚪  (score=0)
```python
                    node.declared_name(), getattr(node, "type", None))
```
L835  ⚪  (score=0)
```python
            elif isinstance(node, ExprNodes.AttributeNode):
```
L836  ⚪  (score=0)
```python
                result += "(type=%s, attribute=\"%s\")" % (repr(node.type), node.attribute)
```
L837  ⚪  (score=0)
```python
            elif isinstance(node, (ExprNodes.ConstNode, ExprNodes.PyConstNode)):
```
L838  ⚪  (score=0)
```python
                result += "(type=%s, value=%r)" % (repr(node.type), node.value)
```
L839  ⚪  (score=0)
```python
            elif isinstance(node, ExprNodes.ExprNode):
```
L840  ⚪  (score=0)
```python
                t = node.type
```
L841  ⚪  (score=0)
```python
                result += "(type=%s)" % repr(t)
```
L842  ⚪  (score=0)
```python
            elif node.pos:
```
L843  ⚪  (score=0)
```python
                pos = node.pos
```
L844  ⚪  (score=0)
```python
                path = pos[0].get_description()
```
L845  ⚪  (score=0)
```python
                if '/' in path:
```
L846  ⚪  (score=0)
```python
                    path = path.split('/')[-1]
```
L847  ⚪  (score=0)
```python
                if '\\' in path:
```
L848  ⚪  (score=0)
```python
                    path = path.split('\\')[-1]
```
L849  ⚪  (score=0)
```python
                result += "(pos=(%s:%s:%s))" % (path, pos[1], pos[2])
```
L850  ⚪  (score=0)
```python
```
L851  ⚪  (score=0)
```python
            return result
```
L852  ⚪  (score=0)
```python
```
L853  ⚪  (score=0)
```python
if __name__ == "__main__":
```
L854  ⚪  (score=0)
```python
    import doctest
```
L855  ⚪  (score=0)
```python
    doctest.testmod()
```
