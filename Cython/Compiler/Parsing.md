# Cython annotation for Parsing.py

Raw output: Parsing.c

L1  ⚪  (score=0)
```python
# cython: auto_cpdef=True, infer_types=True, py2_import=True
```
L2  ⚪  (score=0)
```python
#
```
L3  ⚪  (score=0)
```python
#   Parser
```
L4  ⚪  (score=0)
```python
#
```
L5  ⚪  (score=0)
```python
```
L6  ⚪  (score=0)
```python
```
L7  ⚪  (score=0)
```python
# This should be done automatically
```
L8  ⚪  (score=0)
```python
```
L9  ⚪  (score=0)
```python
import cython
```
L10  ⚪  (score=0)
```python
import dataclasses
```
L11  ⚪  (score=0)
```python
cython.declare(Nodes=object, ExprNodes=object, EncodedString=object,
```
L12  ⚪  (score=0)
```python
               bytes_literal=object, StringEncoding=object,
```
L13  ⚪  (score=0)
```python
               FileSourceDescriptor=object, lookup_unicodechar=object,
```
L14  ⚪  (score=0)
```python
               Future=object, Options=object, error=object, warning=object,
```
L15  ⚪  (score=0)
```python
               Builtin=object, ModuleNode=object, Utils=object, _unicode=object, _bytes=object,
```
L16  ⚪  (score=0)
```python
               re=object, _parse_escape_sequences=object, _parse_escape_sequences_raw=object,
```
L17  ⚪  (score=0)
```python
               partial=object, reduce=object,
```
L18  ⚪  (score=0)
```python
               _CDEF_MODIFIERS=tuple, COMMON_BINOP_MISTAKES=dict)
```
L19  ⚪  (score=0)
```python
```
L20  ⚪  (score=0)
```python
from io import StringIO
```
L21  ⚪  (score=0)
```python
import re
```
L22  ⚪  (score=0)
```python
from unicodedata import lookup as lookup_unicodechar
```
L23  ⚪  (score=0)
```python
from functools import partial, reduce
```
L24  ⚪  (score=0)
```python
from typing import Any, Optional
```
L25  ⚪  (score=0)
```python
```
L26  ⚪  (score=0)
```python
from .Scanning import PyrexScanner, FileSourceDescriptor, tentatively_scan
```
L27  ⚪  (score=0)
```python
from . import Nodes
```
L28  ⚪  (score=0)
```python
from . import ExprNodes
```
L29  ⚪  (score=0)
```python
from . import MatchCaseNodes
```
L30  ⚪  (score=0)
```python
from . import Builtin
```
L31  ⚪  (score=0)
```python
from . import StringEncoding
```
L32  ⚪  (score=0)
```python
from .StringEncoding import EncodedString, bytes_literal
```
L33  ⚪  (score=0)
```python
from .ModuleNode import ModuleNode
```
L34  ⚪  (score=0)
```python
from .Errors import error, warning
```
L35  ⚪  (score=0)
```python
from . import Future
```
L36  ⚪  (score=0)
```python
from . import Directives
```
L37  ⚪  (score=0)
```python
```
L38  ⚪  (score=0)
```python
```
L39  ⚪  (score=0)
```python
_CDEF_MODIFIERS = ('inline', 'nogil', 'api')
```
L40  ⚪  (score=0)
```python
statement_terminators = cython.declare(frozenset, frozenset((
```
L41  ⚪  (score=0)
```python
    ';', 'NEWLINE', 'EOF')))
```
L42  ⚪  (score=0)
```python
@dataclasses.dataclass
```
L43  ⚪  (score=0)
```python
class Ctx:
```
L44  ⚪  (score=0)
```python
    #  Parsing context
```
L45  ⚪  (score=0)
```python
    level: str = 'other'
```
L46  ⚪  (score=0)
```python
    visibility: str = 'private'
```
L47  ⚪  (score=0)
```python
    cdef_flag: bool | int = False
```
L48  ⚪  (score=0)
```python
    typedef_flag = False
```
L49  ⚪  (score=0)
```python
    api: bool    = False
```
L50  ⚪  (score=0)
```python
    overridable: bool | int = False
```
L51  ⚪  (score=0)
```python
    nogil: bool | int = False
```
L52  ⚪  (score=0)
```python
    namespace: str | None = None
```
L53  ⚪  (score=0)
```python
    templates: list[str] | None = None
```
L54  ⚪  (score=0)
```python
    allow_struct_enum_decorator: bool = False
```
L55  ⚪  (score=0)
```python
    modifiers: Any = None
```
L56  ⚪  (score=0)
```python
```
L57  ⚪  (score=0)
```python
```
L58  ⚪  (score=0)
```python
    __call__ = clone = dataclasses.replace
```
L59  ⚪  (score=0)
```python
```
L60  ⚪  (score=0)
```python
```
L61  ⚪  (score=0)
```python
```
L62  ⚪  (score=0)
```python
```
L63  ⚪  (score=0)
```python
@cython.cfunc
```
L64  ⚪  (score=0)
```python
def p_ident(s: PyrexScanner, message="Expected an identifier"):
```
L65  ⚪  (score=0)
```python
    if s.sy == 'IDENT':
```
L66  ⚪  (score=0)
```python
        name = s.context.intern_ustring(s.systring)
```
L67  ⚪  (score=0)
```python
        s.next()
```
L68  ⚪  (score=0)
```python
        return name
```
L69  ⚪  (score=0)
```python
    else:
```
L70  ⚪  (score=0)
```python
        s.error(message)
```
L71  ⚪  (score=0)
```python
```
L72  ⚪  (score=0)
```python
```
L73  ⚪  (score=0)
```python
@cython.cfunc
```
L74  ⚪  (score=0)
```python
def p_ident_list(s: PyrexScanner):
```
L75  ⚪  (score=0)
```python
    names = []
```
L76  ⚪  (score=0)
```python
    while s.sy == 'IDENT':
```
L77  ⚪  (score=0)
```python
        names.append(s.context.intern_ustring(s.systring))
```
L78  ⚪  (score=0)
```python
        s.next()
```
L79  ⚪  (score=0)
```python
        if s.sy != ',':
```
L80  ⚪  (score=0)
```python
            break
```
L81  ⚪  (score=0)
```python
        s.next()
```
L82  ⚪  (score=0)
```python
    return names
```
L83  ⚪  (score=0)
```python
```
L84  ⚪  (score=0)
```python
#------------------------------------------
```
L85  ⚪  (score=0)
```python
#
```
L86  ⚪  (score=0)
```python
#   Expressions
```
L87  ⚪  (score=0)
```python
#
```
L88  ⚪  (score=0)
```python
#------------------------------------------
```
L89  ⚪  (score=0)
```python
```
L90  ⚪  (score=0)
```python
@cython.cfunc
```
L91  ⚪  (score=0)
```python
def p_binop_operator(s: PyrexScanner) -> tuple:
```
L92  ⚪  (score=0)
```python
    pos = s.position()
```
L93  ⚪  (score=0)
```python
    op = s.sy
```
L94  ⚪  (score=0)
```python
    s.next()
```
L95  ⚪  (score=0)
```python
    return op, pos
```
L96  ⚪  (score=0)
```python
```
L97  ⚪  (score=0)
```python
```
L98  ⚪  (score=0)
```python
# signature is currently overridden in pxd file
```
L99  ⚪  (score=0)
```python
def p_binop_expr(s: "PyrexScanner", ops, p_sub_expr):
```
L100  ⚪  (score=0)
```python
    n1 = p_sub_expr(s)
```
L101  ⚪  (score=0)
```python
    while s.sy in ops:
```
L102  ⚪  (score=0)
```python
        op, pos = p_binop_operator(s)
```
L103  ⚪  (score=0)
```python
        n2 = p_sub_expr(s)
```
L104  ⚪  (score=0)
```python
        n1 = ExprNodes.binop_node(pos, op, n1, n2)
```
L105  ⚪  (score=0)
```python
        if op == '/':
```
L106  ⚪  (score=0)
```python
            if Future.division in s.context.future_directives:
```
L107  ⚪  (score=0)
```python
                n1.truedivision = True
```
L108  ⚪  (score=0)
```python
            else:
```
L109  ⚪  (score=0)
```python
                n1.truedivision = None  # unknown
```
L110  ⚪  (score=0)
```python
    return n1
```
L111  ⚪  (score=0)
```python
```
L112  ⚪  (score=0)
```python
```
L113  ⚪  (score=0)
```python
#lambdef: 'lambda' [varargslist] ':' test
```
L114  ⚪  (score=0)
```python
```
L115  ⚪  (score=0)
```python
@cython.cfunc
```
L116  ⚪  (score=0)
```python
def p_lambdef(s: PyrexScanner):
```
L117  ⚪  (score=0)
```python
    # s.sy == 'lambda'
```
L118  ⚪  (score=0)
```python
    pos = s.position()
```
L119  ⚪  (score=0)
```python
    s.next()
```
L120  ⚪  (score=0)
```python
    if s.sy == ':':
```
L121  ⚪  (score=0)
```python
        args = []
```
L122  ⚪  (score=0)
```python
        star_arg = starstar_arg = None
```
L123  ⚪  (score=0)
```python
    else:
```
L124  ⚪  (score=0)
```python
        args, star_arg, starstar_arg = p_varargslist(
```
L125  ⚪  (score=0)
```python
            s, terminator=':', annotated=False)
```
L126  ⚪  (score=0)
```python
    s.expect(':')
```
L127  ⚪  (score=0)
```python
    expr = p_test(s)
```
L128  ⚪  (score=0)
```python
    return ExprNodes.LambdaNode(
```
L129  ⚪  (score=0)
```python
        pos, args = args,
```
L130  ⚪  (score=0)
```python
        star_arg = star_arg, starstar_arg = starstar_arg,
```
L131  ⚪  (score=0)
```python
        result_expr = expr)
```
L132  ⚪  (score=0)
```python
```
L133  ⚪  (score=0)
```python
```
L134  ⚪  (score=0)
```python
#test: or_test ['if' or_test 'else' test] | lambdef
```
L135  ⚪  (score=0)
```python
```
L136  ⚪  (score=0)
```python
@cython.cfunc
```
L137  ⚪  (score=0)
```python
def p_test(s: PyrexScanner):
```
L138  ⚪  (score=0)
```python
    # The check for a following ':=' is only for error reporting purposes.
```
L139  ⚪  (score=0)
```python
    # It simply changes a
```
L140  ⚪  (score=0)
```python
    #   expected ')', found ':='
```
L141  ⚪  (score=0)
```python
    # message into something a bit more descriptive.
```
L142  ⚪  (score=0)
```python
    # It is close to what the PEG parser does in CPython, where an expression has
```
L143  ⚪  (score=0)
```python
    # a lookahead assertion that it isn't followed by ':='
```
L144  ⚪  (score=0)
```python
    expr = p_test_allow_walrus_after(s)
```
L145  ⚪  (score=0)
```python
    if s.sy == ':=':
```
L146  ⚪  (score=0)
```python
        s.error("invalid syntax: assignment expression not allowed in this context")
```
L147  ⚪  (score=0)
```python
    return expr
```
L148  ⚪  (score=0)
```python
```
L149  ⚪  (score=0)
```python
```
L150  ⚪  (score=0)
```python
@cython.cfunc
```
L151  ⚪  (score=0)
```python
def p_test_allow_walrus_after(s: PyrexScanner):
```
L152  ⚪  (score=0)
```python
    if s.sy == 'lambda':
```
L153  ⚪  (score=0)
```python
        return p_lambdef(s)
```
L154  ⚪  (score=0)
```python
    pos = s.position()
```
L155  ⚪  (score=0)
```python
    expr = p_or_test(s)
```
L156  ⚪  (score=0)
```python
    if s.sy == 'if':
```
L157  ⚪  (score=0)
```python
        s.next()
```
L158  ⚪  (score=0)
```python
        test = p_or_test(s)
```
L159  ⚪  (score=0)
```python
        s.expect('else')
```
L160  ⚪  (score=0)
```python
        other = p_test(s)
```
L161  ⚪  (score=0)
```python
        return ExprNodes.CondExprNode(pos, test=test, true_val=expr, false_val=other)
```
L162  ⚪  (score=0)
```python
    else:
```
L163  ⚪  (score=0)
```python
        return expr
```
L164  ⚪  (score=0)
```python
```
L165  ⚪  (score=0)
```python
```
L166  ⚪  (score=0)
```python
@cython.cfunc
```
L167  ⚪  (score=0)
```python
def p_namedexpr_test(s: PyrexScanner):
```
L168  ⚪  (score=0)
```python
    # defined in the LL parser as
```
L169  ⚪  (score=0)
```python
    #  namedexpr_test: test [':=' test]
```
L170  ⚪  (score=0)
```python
    # The requirement that the LHS is a name is not enforced in the grammar.
```
L171  ⚪  (score=0)
```python
    # For comparison the PEG parser does:
```
L172  ⚪  (score=0)
```python
    #  1. look for "name :=", if found it's definitely a named expression
```
L173  ⚪  (score=0)
```python
    #     so look for expression
```
L174  ⚪  (score=0)
```python
    #  2. Otherwise, look for expression
```
L175  ⚪  (score=0)
```python
    lhs = p_test_allow_walrus_after(s)
```
L176  ⚪  (score=0)
```python
    if s.sy == ':=':
```
L177  ⚪  (score=0)
```python
        position = s.position()
```
L178  ⚪  (score=0)
```python
        if not lhs.is_name:
```
L179  ⚪  (score=0)
```python
            s.error("Left-hand side of assignment expression must be an identifier", fatal=False)
```
L180  ⚪  (score=0)
```python
        s.next()
```
L181  ⚪  (score=0)
```python
        rhs = p_test(s)
```
L182  ⚪  (score=0)
```python
        return ExprNodes.AssignmentExpressionNode(position, lhs=lhs, rhs=rhs)
```
L183  ⚪  (score=0)
```python
    return lhs
```
L184  ⚪  (score=0)
```python
```
L185  ⚪  (score=0)
```python
```
L186  ⚪  (score=0)
```python
#or_test: and_test ('or' and_test)*
```
L187  ⚪  (score=0)
```python
```
L188  ⚪  (score=0)
```python
COMMON_BINOP_MISTAKES = {'||': 'or', '&&': 'and'}
```
L189  ⚪  (score=0)
```python
```
L190  ⚪  (score=0)
```python
@cython.cfunc
```
L191  ⚪  (score=0)
```python
def p_or_test(s: PyrexScanner):
```
L192  ⚪  (score=0)
```python
    return p_rassoc_binop_expr(s, 'or', p_and_test)
```
L193  ⚪  (score=0)
```python
```
L194  ⚪  (score=0)
```python
```
L195  ⚪  (score=0)
```python
# signature is currently overridden in pxd file
```
L196  ⚪  (score=0)
```python
def p_rassoc_binop_expr(s: "PyrexScanner", op, p_subexpr):
```
L197  ⚪  (score=0)
```python
    n1 = p_subexpr(s)
```
L198  ⚪  (score=0)
```python
    if s.sy == op:
```
L199  ⚪  (score=0)
```python
        pos = s.position()
```
L200  ⚪  (score=0)
```python
        op = s.sy
```
L201  ⚪  (score=0)
```python
        s.next()
```
L202  ⚪  (score=0)
```python
        n2 = p_rassoc_binop_expr(s, op, p_subexpr)
```
L203  ⚪  (score=0)
```python
        n1 = ExprNodes.binop_node(pos, op, n1, n2)
```
L204  ⚪  (score=0)
```python
    elif s.sy in COMMON_BINOP_MISTAKES and COMMON_BINOP_MISTAKES[s.sy] == op:
```
L205  ⚪  (score=0)
```python
        # Only report this for the current operator since we pass through here twice for 'and' and 'or'.
```
L206  ⚪  (score=0)
```python
        warning(s.position(),
```
L207  ⚪  (score=0)
```python
                "Found the C operator '%s', did you mean the Python operator '%s'?" % (s.sy, op),
```
L208  ⚪  (score=0)
```python
                level=1)
```
L209  ⚪  (score=0)
```python
    return n1
```
L210  ⚪  (score=0)
```python
```
L211  ⚪  (score=0)
```python
```
L212  ⚪  (score=0)
```python
#and_test: not_test ('and' not_test)*
```
L213  ⚪  (score=0)
```python
```
L214  ⚪  (score=0)
```python
@cython.cfunc
```
L215  ⚪  (score=0)
```python
def p_and_test(s: PyrexScanner):
```
L216  ⚪  (score=0)
```python
    #return p_binop_expr(s, ('and',), p_not_test)
```
L217  ⚪  (score=0)
```python
    return p_rassoc_binop_expr(s, 'and', p_not_test)
```
L218  ⚪  (score=0)
```python
```
L219  ⚪  (score=0)
```python
```
L220  ⚪  (score=0)
```python
#not_test: 'not' not_test | comparison
```
L221  ⚪  (score=0)
```python
```
L222  ⚪  (score=0)
```python
@cython.cfunc
```
L223  ⚪  (score=0)
```python
def p_not_test(s: PyrexScanner):
```
L224  ⚪  (score=0)
```python
    if s.sy == 'not':
```
L225  ⚪  (score=0)
```python
        pos = s.position()
```
L226  ⚪  (score=0)
```python
        s.next()
```
L227  ⚪  (score=0)
```python
        return ExprNodes.NotNode(pos, operand = p_not_test(s))
```
L228  ⚪  (score=0)
```python
    else:
```
L229  ⚪  (score=0)
```python
        return p_comparison(s)
```
L230  ⚪  (score=0)
```python
```
L231  ⚪  (score=0)
```python
```
L232  ⚪  (score=0)
```python
#comparison: expr (comp_op expr)*
```
L233  ⚪  (score=0)
```python
#comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'
```
L234  ⚪  (score=0)
```python
```
L235  ⚪  (score=0)
```python
@cython.cfunc
```
L236  ⚪  (score=0)
```python
def p_comparison(s: PyrexScanner):
```
L237  ⚪  (score=0)
```python
    n1 = p_starred_expr(s)
```
L238  ⚪  (score=0)
```python
    if s.sy in comparison_ops:
```
L239  ⚪  (score=0)
```python
        pos = s.position()
```
L240  ⚪  (score=0)
```python
        op = p_cmp_op(s)
```
L241  ⚪  (score=0)
```python
        n2 = p_starred_expr(s)
```
L242  ⚪  (score=0)
```python
        n1 = ExprNodes.PrimaryCmpNode(pos,
```
L243  ⚪  (score=0)
```python
            operator = op, operand1 = n1, operand2 = n2)
```
L244  ⚪  (score=0)
```python
        if s.sy in comparison_ops:
```
L245  ⚪  (score=0)
```python
            n1.cascade = p_cascaded_cmp(s)
```
L246  ⚪  (score=0)
```python
    return n1
```
L247  ⚪  (score=0)
```python
```
L248  ⚪  (score=0)
```python
```
L249  ⚪  (score=0)
```python
@cython.cfunc
```
L250  ⚪  (score=0)
```python
def p_test_or_starred_expr(s: PyrexScanner):
```
L251  ⚪  (score=0)
```python
    if s.sy == '*':
```
L252  ⚪  (score=0)
```python
        return p_starred_expr(s)
```
L253  ⚪  (score=0)
```python
    else:
```
L254  ⚪  (score=0)
```python
        return p_test(s)
```
L255  ⚪  (score=0)
```python
```
L256  ⚪  (score=0)
```python
```
L257  ⚪  (score=0)
```python
@cython.cfunc
```
L258  ⚪  (score=0)
```python
def p_namedexpr_test_or_starred_expr(s: PyrexScanner):
```
L259  ⚪  (score=0)
```python
    if s.sy == '*':
```
L260  ⚪  (score=0)
```python
        return p_starred_expr(s)
```
L261  ⚪  (score=0)
```python
    else:
```
L262  ⚪  (score=0)
```python
        return p_namedexpr_test(s)
```
L263  ⚪  (score=0)
```python
```
L264  ⚪  (score=0)
```python
```
L265  ⚪  (score=0)
```python
@cython.cfunc
```
L266  ⚪  (score=0)
```python
def p_starred_expr(s: PyrexScanner):
```
L267  ⚪  (score=0)
```python
    pos = s.position()
```
L268  ⚪  (score=0)
```python
    if s.sy == '*':
```
L269  ⚪  (score=0)
```python
        starred = True
```
L270  ⚪  (score=0)
```python
        s.next()
```
L271  ⚪  (score=0)
```python
    else:
```
L272  ⚪  (score=0)
```python
        starred = False
```
L273  ⚪  (score=0)
```python
    expr = p_bit_expr(s)
```
L274  ⚪  (score=0)
```python
    if starred:
```
L275  ⚪  (score=0)
```python
        expr = ExprNodes.StarredUnpackingNode(pos, expr)
```
L276  ⚪  (score=0)
```python
    return expr
```
L277  ⚪  (score=0)
```python
```
L278  ⚪  (score=0)
```python
```
L279  ⚪  (score=0)
```python
@cython.cfunc
```
L280  ⚪  (score=0)
```python
def p_cascaded_cmp(s: PyrexScanner):
```
L281  ⚪  (score=0)
```python
    pos = s.position()
```
L282  ⚪  (score=0)
```python
    op = p_cmp_op(s)
```
L283  ⚪  (score=0)
```python
    n2 = p_starred_expr(s)
```
L284  ⚪  (score=0)
```python
    result = ExprNodes.CascadedCmpNode(pos,
```
L285  ⚪  (score=0)
```python
        operator = op, operand2 = n2)
```
L286  ⚪  (score=0)
```python
    if s.sy in comparison_ops:
```
L287  ⚪  (score=0)
```python
        result.cascade = p_cascaded_cmp(s)
```
L288  ⚪  (score=0)
```python
    return result
```
L289  ⚪  (score=0)
```python
```
L290  ⚪  (score=0)
```python
```
L291  ⚪  (score=0)
```python
@cython.cfunc
```
L292  ⚪  (score=0)
```python
def p_cmp_op(s: PyrexScanner):
```
L293  ⚪  (score=0)
```python
    if s.sy == 'not':
```
L294  ⚪  (score=0)
```python
        s.next()
```
L295  ⚪  (score=0)
```python
        s.expect('in')
```
L296  ⚪  (score=0)
```python
        op = 'not_in'
```
L297  ⚪  (score=0)
```python
    elif s.sy == 'is':
```
L298  ⚪  (score=0)
```python
        s.next()
```
L299  ⚪  (score=0)
```python
        if s.sy == 'not':
```
L300  ⚪  (score=0)
```python
            s.next()
```
L301  ⚪  (score=0)
```python
            op = 'is_not'
```
L302  ⚪  (score=0)
```python
        else:
```
L303  ⚪  (score=0)
```python
            op = 'is'
```
L304  ⚪  (score=0)
```python
    else:
```
L305  ⚪  (score=0)
```python
        op = s.sy
```
L306  ⚪  (score=0)
```python
        s.next()
```
L307  ⚪  (score=0)
```python
    if op == '<>':
```
L308  ⚪  (score=0)
```python
        op = '!='
```
L309  ⚪  (score=0)
```python
    return op
```
L310  ⚪  (score=0)
```python
```
L311  ⚪  (score=0)
```python
```
L312  ⚪  (score=0)
```python
comparison_ops = cython.declare(frozenset, frozenset((
```
L313  ⚪  (score=0)
```python
    '<', '>', '==', '>=', '<=', '<>', '!=',
```
L314  ⚪  (score=0)
```python
    'in', 'is', 'not'
```
L315  ⚪  (score=0)
```python
)))
```
L316  ⚪  (score=0)
```python
```
L317  ⚪  (score=0)
```python
```
L318  ⚪  (score=0)
```python
#expr: xor_expr ('|' xor_expr)*
```
L319  ⚪  (score=0)
```python
```
L320  ⚪  (score=0)
```python
@cython.cfunc
```
L321  ⚪  (score=0)
```python
def p_bit_expr(s: PyrexScanner):
```
L322  ⚪  (score=0)
```python
    return p_binop_expr(s, ('|',), p_xor_expr)
```
L323  ⚪  (score=0)
```python
```
L324  ⚪  (score=0)
```python
```
L325  ⚪  (score=0)
```python
#xor_expr: and_expr ('^' and_expr)*
```
L326  ⚪  (score=0)
```python
```
L327  ⚪  (score=0)
```python
@cython.cfunc
```
L328  ⚪  (score=0)
```python
def p_xor_expr(s: PyrexScanner):
```
L329  ⚪  (score=0)
```python
    return p_binop_expr(s, ('^',), p_and_expr)
```
L330  ⚪  (score=0)
```python
```
L331  ⚪  (score=0)
```python
```
L332  ⚪  (score=0)
```python
#and_expr: shift_expr ('&' shift_expr)*
```
L333  ⚪  (score=0)
```python
```
L334  ⚪  (score=0)
```python
@cython.cfunc
```
L335  ⚪  (score=0)
```python
def p_and_expr(s: PyrexScanner):
```
L336  ⚪  (score=0)
```python
    return p_binop_expr(s, ('&',), p_shift_expr)
```
L337  ⚪  (score=0)
```python
```
L338  ⚪  (score=0)
```python
```
L339  ⚪  (score=0)
```python
#shift_expr: arith_expr (('<<'|'>>') arith_expr)*
```
L340  ⚪  (score=0)
```python
```
L341  ⚪  (score=0)
```python
@cython.cfunc
```
L342  ⚪  (score=0)
```python
def p_shift_expr(s: PyrexScanner):
```
L343  ⚪  (score=0)
```python
    return p_binop_expr(s, ('<<', '>>'), p_arith_expr)
```
L344  ⚪  (score=0)
```python
```
L345  ⚪  (score=0)
```python
```
L346  ⚪  (score=0)
```python
#arith_expr: term (('+'|'-') term)*
```
L347  ⚪  (score=0)
```python
```
L348  ⚪  (score=0)
```python
@cython.cfunc
```
L349  ⚪  (score=0)
```python
def p_arith_expr(s: PyrexScanner):
```
L350  ⚪  (score=0)
```python
    return p_binop_expr(s, ('+', '-'), p_term)
```
L351  ⚪  (score=0)
```python
```
L352  ⚪  (score=0)
```python
```
L353  ⚪  (score=0)
```python
#term: factor (('*'|'@'|'/'|'%'|'//') factor)*
```
L354  ⚪  (score=0)
```python
```
L355  ⚪  (score=0)
```python
@cython.cfunc
```
L356  ⚪  (score=0)
```python
def p_term(s: PyrexScanner):
```
L357  ⚪  (score=0)
```python
    return p_binop_expr(s, ('*', '@', '/', '%', '//'), p_factor)
```
L358  ⚪  (score=0)
```python
```
L359  ⚪  (score=0)
```python
```
L360  ⚪  (score=0)
```python
#factor: ('+'|'-'|'~'|'&'|typecast|sizeof) factor | power
```
L361  ⚪  (score=0)
```python
```
L362  ⚪  (score=0)
```python
@cython.cfunc
```
L363  ⚪  (score=0)
```python
def p_factor(s: PyrexScanner):
```
L364  ⚪  (score=0)
```python
    # little indirection for C-ification purposes
```
L365  ⚪  (score=0)
```python
    return _p_factor(s)
```
L366  ⚪  (score=0)
```python
```
L367  ⚪  (score=0)
```python
```
L368  ⚪  (score=0)
```python
@cython.cfunc
```
L369  ⚪  (score=0)
```python
def _p_factor(s: PyrexScanner):
```
L370  ⚪  (score=0)
```python
    sy = s.sy
```
L371  ⚪  (score=0)
```python
    if sy in ('+', '-', '~'):
```
L372  ⚪  (score=0)
```python
        op = s.sy
```
L373  ⚪  (score=0)
```python
        pos = s.position()
```
L374  ⚪  (score=0)
```python
        s.next()
```
L375  ⚪  (score=0)
```python
        return ExprNodes.unop_node(pos, op, p_factor(s))
```
L376  ⚪  (score=0)
```python
    elif not s.in_python_file:
```
L377  ⚪  (score=0)
```python
        if sy == '&':
```
L378  ⚪  (score=0)
```python
            pos = s.position()
```
L379  ⚪  (score=0)
```python
            s.next()
```
L380  ⚪  (score=0)
```python
            arg = p_factor(s)
```
L381  ⚪  (score=0)
```python
            return ExprNodes.AmpersandNode(pos, operand = arg)
```
L382  ⚪  (score=0)
```python
        elif sy == "<":
```
L383  ⚪  (score=0)
```python
            return p_typecast(s)
```
L384  ⚪  (score=0)
```python
        elif sy == 'IDENT' and s.systring == "sizeof":
```
L385  ⚪  (score=0)
```python
            return p_sizeof(s)
```
L386  ⚪  (score=0)
```python
    return p_power(s)
```
L387  ⚪  (score=0)
```python
```
L388  ⚪  (score=0)
```python
```
L389  ⚪  (score=0)
```python
@cython.cfunc
```
L390  ⚪  (score=0)
```python
def p_typecast(s: PyrexScanner):
```
L391  ⚪  (score=0)
```python
    # s.sy == "<"
```
L392  ⚪  (score=0)
```python
    pos = s.position()
```
L393  ⚪  (score=0)
```python
    s.next()
```
L394  ⚪  (score=0)
```python
    base_type = p_c_base_type(s)
```
L395  ⚪  (score=0)
```python
    is_memslice = isinstance(base_type, Nodes.MemoryViewSliceTypeNode)
```
L396  ⚪  (score=0)
```python
    is_other_unnamed_type = isinstance(base_type, (
```
L397  ⚪  (score=0)
```python
        Nodes.TemplatedTypeNode,
```
L398  ⚪  (score=0)
```python
        Nodes.CConstOrVolatileTypeNode,
```
L399  ⚪  (score=0)
```python
        Nodes.CTupleBaseTypeNode,
```
L400  ⚪  (score=0)
```python
    ))
```
L401  ⚪  (score=0)
```python
    if not (is_memslice or is_other_unnamed_type) and base_type.name is None:
```
L402  ⚪  (score=0)
```python
        s.error("Unknown type")
```
L403  ⚪  (score=0)
```python
    declarator = p_c_declarator(s, empty=True)
```
L404  ⚪  (score=0)
```python
    if s.sy == '?':
```
L405  ⚪  (score=0)
```python
        s.next()
```
L406  ⚪  (score=0)
```python
        typecheck = True
```
L407  ⚪  (score=0)
```python
    else:
```
L408  ⚪  (score=0)
```python
        typecheck = False
```
L409  ⚪  (score=0)
```python
    s.expect(">")
```
L410  ⚪  (score=0)
```python
    operand = p_factor(s)
```
L411  ⚪  (score=0)
```python
    if is_memslice:
```
L412  ⚪  (score=0)
```python
        return ExprNodes.CythonArrayNode(pos, base_type_node=base_type, operand=operand)
```
L413  ⚪  (score=0)
```python
```
L414  ⚪  (score=0)
```python
    return ExprNodes.TypecastNode(pos,
```
L415  ⚪  (score=0)
```python
        base_type = base_type,
```
L416  ⚪  (score=0)
```python
        declarator = declarator,
```
L417  ⚪  (score=0)
```python
        operand = operand,
```
L418  ⚪  (score=0)
```python
        typecheck = typecheck)
```
L419  ⚪  (score=0)
```python
```
L420  ⚪  (score=0)
```python
```
L421  ⚪  (score=0)
```python
@cython.cfunc
```
L422  ⚪  (score=0)
```python
def p_sizeof(s: PyrexScanner):
```
L423  ⚪  (score=0)
```python
    # s.sy == ident "sizeof"
```
L424  ⚪  (score=0)
```python
    pos = s.position()
```
L425  ⚪  (score=0)
```python
    s.next()
```
L426  ⚪  (score=0)
```python
    s.expect('(')
```
L427  ⚪  (score=0)
```python
    # Here we decide if we are looking at an expression or type
```
L428  ⚪  (score=0)
```python
    # If it is actually a type, but parsable as an expression,
```
L429  ⚪  (score=0)
```python
    # we treat it as an expression here.
```
L430  ⚪  (score=0)
```python
    if looking_at_expr(s):
```
L431  ⚪  (score=0)
```python
        operand = p_test(s)
```
L432  ⚪  (score=0)
```python
        node = ExprNodes.SizeofVarNode(pos, operand = operand)
```
L433  ⚪  (score=0)
```python
    else:
```
L434  ⚪  (score=0)
```python
        base_type = p_c_base_type(s)
```
L435  ⚪  (score=0)
```python
        declarator = p_c_declarator(s, empty=True)
```
L436  ⚪  (score=0)
```python
        node = ExprNodes.SizeofTypeNode(pos,
```
L437  ⚪  (score=0)
```python
            base_type = base_type, declarator = declarator)
```
L438  ⚪  (score=0)
```python
    s.expect(')')
```
L439  ⚪  (score=0)
```python
    return node
```
L440  ⚪  (score=0)
```python
```
L441  ⚪  (score=0)
```python
```
L442  ⚪  (score=0)
```python
@cython.cfunc
```
L443  ⚪  (score=0)
```python
def p_yield_expression(s: PyrexScanner, statement_terminators: frozenset = statement_terminators):
```
L444  ⚪  (score=0)
```python
    # s.sy == "yield"
```
L445  ⚪  (score=0)
```python
    pos = s.position()
```
L446  ⚪  (score=0)
```python
    s.next()
```
L447  ⚪  (score=0)
```python
    is_yield_from = False
```
L448  ⚪  (score=0)
```python
    if s.sy == 'from':
```
L449  ⚪  (score=0)
```python
        is_yield_from = True
```
L450  ⚪  (score=0)
```python
        s.next()
```
L451  ⚪  (score=0)
```python
    if s.sy != ')' and s.sy not in statement_terminators:
```
L452  ⚪  (score=0)
```python
        # "yield from" does not support implicit tuples, but "yield" does ("yield 1,2")
```
L453  ⚪  (score=0)
```python
        arg = p_test(s) if is_yield_from else p_testlist(s)
```
L454  ⚪  (score=0)
```python
    else:
```
L455  ⚪  (score=0)
```python
        if is_yield_from:
```
L456  ⚪  (score=0)
```python
            s.error("'yield from' requires a source argument",
```
L457  ⚪  (score=0)
```python
                    pos=pos, fatal=False)
```
L458  ⚪  (score=0)
```python
        arg = None
```
L459  ⚪  (score=0)
```python
    if is_yield_from:
```
L460  ⚪  (score=0)
```python
        return ExprNodes.YieldFromExprNode(pos, arg=arg)
```
L461  ⚪  (score=0)
```python
    else:
```
L462  ⚪  (score=0)
```python
        return ExprNodes.YieldExprNode(pos, arg=arg)
```
L463  ⚪  (score=0)
```python
```
L464  ⚪  (score=0)
```python
```
L465  ⚪  (score=0)
```python
@cython.cfunc
```
L466  ⚪  (score=0)
```python
def p_yield_statement(s: PyrexScanner):
```
L467  ⚪  (score=0)
```python
    # s.sy == "yield"
```
L468  ⚪  (score=0)
```python
    yield_expr = p_yield_expression(s)
```
L469  ⚪  (score=0)
```python
    return Nodes.ExprStatNode(yield_expr.pos, expr=yield_expr)
```
L470  ⚪  (score=0)
```python
```
L471  ⚪  (score=0)
```python
```
L472  ⚪  (score=0)
```python
@cython.cfunc
```
L473  ⚪  (score=0)
```python
def p_async_statement(s: PyrexScanner, ctx, decorators):
```
L474  ⚪  (score=0)
```python
    # s.sy >> 'async' ...
```
L475  ⚪  (score=0)
```python
    if s.sy == 'def':
```
L476  ⚪  (score=0)
```python
        # 'async def' statements aren't allowed in pxd files
```
L477  ⚪  (score=0)
```python
        if 'pxd' in ctx.level:
```
L478  ⚪  (score=0)
```python
            s.error('def statement not allowed here')
```
L479  ⚪  (score=0)
```python
        s.level = ctx.level
```
L480  ⚪  (score=0)
```python
        return p_def_statement(s, decorators, is_async_def=True)
```
L481  ⚪  (score=0)
```python
    elif decorators:
```
L482  ⚪  (score=0)
```python
        s.error("Decorators can only be followed by functions or classes")
```
L483  ⚪  (score=0)
```python
    elif s.sy == 'for':
```
L484  ⚪  (score=0)
```python
        return p_for_statement(s, is_async=True)
```
L485  ⚪  (score=0)
```python
    elif s.sy == 'with':
```
L486  ⚪  (score=0)
```python
        s.next()
```
L487  ⚪  (score=0)
```python
        return p_with_items(s, is_async=True)
```
L488  ⚪  (score=0)
```python
    else:
```
L489  ⚪  (score=0)
```python
        s.error("expected one of 'def', 'for', 'with' after 'async'")
```
L490  ⚪  (score=0)
```python
```
L491  ⚪  (score=0)
```python
```
L492  ⚪  (score=0)
```python
#power: atom_expr ('**' factor)*
```
L493  ⚪  (score=0)
```python
#atom_expr: ['await'] atom trailer*
```
L494  ⚪  (score=0)
```python
```
L495  ⚪  (score=0)
```python
@cython.cfunc
```
L496  ⚪  (score=0)
```python
def p_power(s: PyrexScanner):
```
L497  ⚪  (score=0)
```python
    if s.systring == 'new' and s.peek()[0] == 'IDENT':
```
L498  ⚪  (score=0)
```python
        return p_new_expr(s)
```
L499  ⚪  (score=0)
```python
    await_pos = None
```
L500  ⚪  (score=0)
```python
    if s.sy == 'await':
```
L501  ⚪  (score=0)
```python
        await_pos = s.position()
```
L502  ⚪  (score=0)
```python
        s.next()
```
L503  ⚪  (score=0)
```python
    n1 = p_atom(s)
```
L504  ⚪  (score=0)
```python
    while s.sy in ('(', '[', '.'):
```
L505  ⚪  (score=0)
```python
        n1 = p_trailer(s, n1)
```
L506  ⚪  (score=0)
```python
    if await_pos:
```
L507  ⚪  (score=0)
```python
        n1 = ExprNodes.AwaitExprNode(await_pos, arg=n1)
```
L508  ⚪  (score=0)
```python
    if s.sy == '**':
```
L509  ⚪  (score=0)
```python
        pos = s.position()
```
L510  ⚪  (score=0)
```python
        s.next()
```
L511  ⚪  (score=0)
```python
        n2 = p_factor(s)
```
L512  ⚪  (score=0)
```python
        n1 = ExprNodes.binop_node(pos, '**', n1, n2)
```
L513  ⚪  (score=0)
```python
    return n1
```
L514  ⚪  (score=0)
```python
```
L515  ⚪  (score=0)
```python
```
L516  ⚪  (score=0)
```python
@cython.cfunc
```
L517  ⚪  (score=0)
```python
def p_new_expr(s: PyrexScanner):
```
L518  ⚪  (score=0)
```python
    # s.systring == 'new'.
```
L519  ⚪  (score=0)
```python
    pos = s.position()
```
L520  ⚪  (score=0)
```python
    s.next()
```
L521  ⚪  (score=0)
```python
    cppclass = p_c_base_type(s)
```
L522  ⚪  (score=0)
```python
    return p_call(s, ExprNodes.NewExprNode(pos, cppclass = cppclass))
```
L523  ⚪  (score=0)
```python
```
L524  ⚪  (score=0)
```python
```
L525  ⚪  (score=0)
```python
#trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME
```
L526  ⚪  (score=0)
```python
```
L527  ⚪  (score=0)
```python
@cython.cfunc
```
L528  ⚪  (score=0)
```python
def p_trailer(s: PyrexScanner, node1):
```
L529  ⚪  (score=0)
```python
    pos = s.position()
```
L530  ⚪  (score=0)
```python
    if s.sy == '(':
```
L531  ⚪  (score=0)
```python
        return p_call(s, node1)
```
L532  ⚪  (score=0)
```python
    elif s.sy == '[':
```
L533  ⚪  (score=0)
```python
        return p_index(s, node1)
```
L534  ⚪  (score=0)
```python
    else:  # s.sy == '.'
```
L535  ⚪  (score=0)
```python
        s.next()
```
L536  ⚪  (score=0)
```python
        name = p_ident(s)
```
L537  ⚪  (score=0)
```python
        return ExprNodes.AttributeNode(pos,
```
L538  ⚪  (score=0)
```python
            obj=node1, attribute=name)
```
L539  ⚪  (score=0)
```python
```
L540  ⚪  (score=0)
```python
```
L541  ⚪  (score=0)
```python
# arglist:  argument (',' argument)* [',']
```
L542  ⚪  (score=0)
```python
# argument: [test '='] test       # Really [keyword '='] test
```
L543  ⚪  (score=0)
```python
```
L544  ⚪  (score=0)
```python
# since PEP 448:
```
L545  ⚪  (score=0)
```python
# argument: ( test [comp_for] |
```
L546  ⚪  (score=0)
```python
#             test '=' test |
```
L547  ⚪  (score=0)
```python
#             '**' expr |
```
L548  ⚪  (score=0)
```python
#             star_expr )
```
L549  ⚪  (score=0)
```python
```
L550  ⚪  (score=0)
```python
@cython.cfunc
```
L551  ⚪  (score=0)
```python
def p_call_parse_args(s: PyrexScanner, allow_genexp: cython.bint = True):
```
L552  ⚪  (score=0)
```python
    # s.sy == '('
```
L553  ⚪  (score=0)
```python
    s.next()
```
L554  ⚪  (score=0)
```python
    positional_args = []
```
L555  ⚪  (score=0)
```python
    keyword_args = []
```
L556  ⚪  (score=0)
```python
    starstar_seen = False
```
L557  ⚪  (score=0)
```python
    last_was_tuple_unpack = False
```
L558  ⚪  (score=0)
```python
    while s.sy != ')':
```
L559  ⚪  (score=0)
```python
        if s.sy == '*':
```
L560  ⚪  (score=0)
```python
            if starstar_seen:
```
L561  ⚪  (score=0)
```python
                s.error("Non-keyword arg following keyword arg", pos=s.position())
```
L562  ⚪  (score=0)
```python
            s.next()
```
L563  ⚪  (score=0)
```python
            positional_args.append(p_test(s))
```
L564  ⚪  (score=0)
```python
            last_was_tuple_unpack = True
```
L565  ⚪  (score=0)
```python
        elif s.sy == '**':
```
L566  ⚪  (score=0)
```python
            s.next()
```
L567  ⚪  (score=0)
```python
            keyword_args.append(p_test(s))
```
L568  ⚪  (score=0)
```python
            starstar_seen = True
```
L569  ⚪  (score=0)
```python
        else:
```
L570  ⚪  (score=0)
```python
            arg = p_namedexpr_test(s)
```
L571  ⚪  (score=0)
```python
            if s.sy == '=':
```
L572  ⚪  (score=0)
```python
                s.next()
```
L573  ⚪  (score=0)
```python
                if not arg.is_name:
```
L574  ⚪  (score=0)
```python
                    s.error("Expected an identifier before '='",
```
L575  ⚪  (score=0)
```python
                            pos=arg.pos)
```
L576  ⚪  (score=0)
```python
                encoded_name = s.context.intern_ustring(arg.name)
```
L577  ⚪  (score=0)
```python
                keyword = ExprNodes.IdentifierStringNode(
```
L578  ⚪  (score=0)
```python
                    arg.pos, value=encoded_name)
```
L579  ⚪  (score=0)
```python
                arg = p_test(s)
```
L580  ⚪  (score=0)
```python
                keyword_args.append((keyword, arg))
```
L581  ⚪  (score=0)
```python
            else:
```
L582  ⚪  (score=0)
```python
                if keyword_args:
```
L583  ⚪  (score=0)
```python
                    s.error("Non-keyword arg following keyword arg", pos=arg.pos)
```
L584  ⚪  (score=0)
```python
                if positional_args and not last_was_tuple_unpack:
```
L585  ⚪  (score=0)
```python
                    positional_args[len(positional_args) - 1].append(arg)
```
L586  ⚪  (score=0)
```python
                else:
```
L587  ⚪  (score=0)
```python
                    positional_args.append([arg])
```
L588  ⚪  (score=0)
```python
                last_was_tuple_unpack = False
```
L589  ⚪  (score=0)
```python
        if s.sy != ',':
```
L590  ⚪  (score=0)
```python
            break
```
L591  ⚪  (score=0)
```python
        s.next()
```
L592  ⚪  (score=0)
```python
```
L593  ⚪  (score=0)
```python
    if s.sy in ('for', 'async') and allow_genexp:
```
L594  ⚪  (score=0)
```python
        if not keyword_args and not last_was_tuple_unpack:
```
L595  ⚪  (score=0)
```python
            if len(positional_args) == 1 and len(positional_args[0]) == 1:
```
L596  ⚪  (score=0)
```python
                positional_args = [[p_genexp(s, positional_args[0][0])]]
```
L597  ⚪  (score=0)
```python
    s.expect(')')
```
L598  ⚪  (score=0)
```python
    return positional_args or [[]], keyword_args
```
L599  ⚪  (score=0)
```python
```
L600  ⚪  (score=0)
```python
```
L601  ⚪  (score=0)
```python
@cython.cfunc
```
L602  ⚪  (score=0)
```python
def p_call_build_packed_args(pos, positional_args, keyword_args) -> tuple:
```
L603  ⚪  (score=0)
```python
    keyword_dict = None
```
L604  ⚪  (score=0)
```python
```
L605  ⚪  (score=0)
```python
    subtuples = [
```
L606  ⚪  (score=0)
```python
        ExprNodes.TupleNode(pos, args=arg) if isinstance(arg, list) else ExprNodes.AsTupleNode(pos, arg=arg)
```
L607  ⚪  (score=0)
```python
        for arg in positional_args
```
L608  ⚪  (score=0)
```python
    ]
```
L609  ⚪  (score=0)
```python
    # TODO: implement a faster way to join tuples than creating each one and adding them
```
L610  ⚪  (score=0)
```python
    arg_tuple = reduce(partial(ExprNodes.binop_node, pos, '+'), subtuples)
```
L611  ⚪  (score=0)
```python
```
L612  ⚪  (score=0)
```python
    if keyword_args:
```
L613  ⚪  (score=0)
```python
        kwargs = []
```
L614  ⚪  (score=0)
```python
        dict_items = []
```
L615  ⚪  (score=0)
```python
        for item in keyword_args:
```
L616  ⚪  (score=0)
```python
            if isinstance(item, tuple):
```
L617  ⚪  (score=0)
```python
                key, value = item
```
L618  ⚪  (score=0)
```python
                dict_items.append(ExprNodes.DictItemNode(pos=key.pos, key=key, value=value))
```
L619  ⚪  (score=0)
```python
            elif item.is_dict_literal:
```
L620  ⚪  (score=0)
```python
                # unpack "**{a:b}" directly
```
L621  ⚪  (score=0)
```python
                dict_items.extend(item.key_value_pairs)
```
L622  ⚪  (score=0)
```python
            else:
```
L623  ⚪  (score=0)
```python
                if dict_items:
```
L624  ⚪  (score=0)
```python
                    kwargs.append(ExprNodes.DictNode(
```
L625  ⚪  (score=0)
```python
                        dict_items[0].pos, key_value_pairs=dict_items, reject_duplicates=True))
```
L626  ⚪  (score=0)
```python
                    dict_items = []
```
L627  ⚪  (score=0)
```python
                kwargs.append(item)
```
L628  ⚪  (score=0)
```python
```
L629  ⚪  (score=0)
```python
        if dict_items:
```
L630  ⚪  (score=0)
```python
            kwargs.append(ExprNodes.DictNode(
```
L631  ⚪  (score=0)
```python
                dict_items[0].pos, key_value_pairs=dict_items, reject_duplicates=True))
```
L632  ⚪  (score=0)
```python
```
L633  ⚪  (score=0)
```python
        if kwargs:
```
L634  ⚪  (score=0)
```python
            if len(kwargs) == 1 and kwargs[0].is_dict_literal:
```
L635  ⚪  (score=0)
```python
                # only simple keyword arguments found -> one dict
```
L636  ⚪  (score=0)
```python
                keyword_dict = kwargs[0]
```
L637  ⚪  (score=0)
```python
            else:
```
L638  ⚪  (score=0)
```python
                # at least one **kwargs
```
L639  ⚪  (score=0)
```python
                keyword_dict = ExprNodes.MergedDictNode(pos, keyword_args=kwargs)
```
L640  ⚪  (score=0)
```python
```
L641  ⚪  (score=0)
```python
    return arg_tuple, keyword_dict
```
L642  ⚪  (score=0)
```python
```
L643  ⚪  (score=0)
```python
```
L644  ⚪  (score=0)
```python
@cython.cfunc
```
L645  ⚪  (score=0)
```python
def p_call(s: PyrexScanner, function):
```
L646  ⚪  (score=0)
```python
    # s.sy == '('
```
L647  ⚪  (score=0)
```python
    pos = s.position()
```
L648  ⚪  (score=0)
```python
    positional_args, keyword_args = p_call_parse_args(s)
```
L649  ⚪  (score=0)
```python
```
L650  ⚪  (score=0)
```python
    if not keyword_args and len(positional_args) == 1 and isinstance(positional_args[0], list):
```
L651  ⚪  (score=0)
```python
        return ExprNodes.SimpleCallNode(pos, function=function, args=positional_args[0])
```
L652  ⚪  (score=0)
```python
    else:
```
L653  ⚪  (score=0)
```python
        arg_tuple, keyword_dict = p_call_build_packed_args(pos, positional_args, keyword_args)
```
L654  ⚪  (score=0)
```python
        return ExprNodes.GeneralCallNode(
```
L655  ⚪  (score=0)
```python
            pos, function=function, positional_args=arg_tuple, keyword_args=keyword_dict)
```
L656  ⚪  (score=0)
```python
```
L657  ⚪  (score=0)
```python
```
L658  ⚪  (score=0)
```python
#lambdef: 'lambda' [varargslist] ':' test
```
L659  ⚪  (score=0)
```python
```
L660  ⚪  (score=0)
```python
#subscriptlist: subscript (',' subscript)* [',']
```
L661  ⚪  (score=0)
```python
```
L662  ⚪  (score=0)
```python
@cython.cfunc
```
L663  ⚪  (score=0)
```python
def p_index(s: PyrexScanner, base):
```
L664  ⚪  (score=0)
```python
    # s.sy == '['
```
L665  ⚪  (score=0)
```python
    pos = s.position()
```
L666  ⚪  (score=0)
```python
    s.next()
```
L667  ⚪  (score=0)
```python
    subscripts, is_single_value = p_subscript_list(s)
```
L668  ⚪  (score=0)
```python
    if is_single_value and len(subscripts[0]) == 2:
```
L669  ⚪  (score=0)
```python
        start, stop = subscripts[0]
```
L670  ⚪  (score=0)
```python
        result = ExprNodes.SliceIndexNode(pos,
```
L671  ⚪  (score=0)
```python
            base = base, start = start, stop = stop)
```
L672  ⚪  (score=0)
```python
    else:
```
L673  ⚪  (score=0)
```python
        indexes = make_slice_nodes(pos, subscripts)
```
L674  ⚪  (score=0)
```python
        if is_single_value:
```
L675  ⚪  (score=0)
```python
            index = indexes[0]
```
L676  ⚪  (score=0)
```python
        else:
```
L677  ⚪  (score=0)
```python
            index = ExprNodes.TupleNode(pos, args = indexes)
```
L678  ⚪  (score=0)
```python
        result = ExprNodes.IndexNode(pos,
```
L679  ⚪  (score=0)
```python
            base = base, index = index)
```
L680  ⚪  (score=0)
```python
    s.expect(']')
```
L681  ⚪  (score=0)
```python
    return result
```
L682  ⚪  (score=0)
```python
```
L683  ⚪  (score=0)
```python
```
L684  ⚪  (score=0)
```python
@cython.cfunc
```
L685  ⚪  (score=0)
```python
def p_subscript_list(s: PyrexScanner) -> tuple:
```
L686  ⚪  (score=0)
```python
    is_single_value = True
```
L687  ⚪  (score=0)
```python
    items = [p_subscript(s)]
```
L688  ⚪  (score=0)
```python
    while s.sy == ',':
```
L689  ⚪  (score=0)
```python
        is_single_value = False
```
L690  ⚪  (score=0)
```python
        s.next()
```
L691  ⚪  (score=0)
```python
        if s.sy == ']':
```
L692  ⚪  (score=0)
```python
            break
```
L693  ⚪  (score=0)
```python
        items.append(p_subscript(s))
```
L694  ⚪  (score=0)
```python
    return items, is_single_value
```
L695  ⚪  (score=0)
```python
```
L696  ⚪  (score=0)
```python
```
L697  ⚪  (score=0)
```python
#subscript: '.' '.' '.' | test | [test] ':' [test] [':' [test]]
```
L698  ⚪  (score=0)
```python
```
L699  ⚪  (score=0)
```python
@cython.cfunc
```
L700  ⚪  (score=0)
```python
def p_subscript(s: PyrexScanner):
```
L701  ⚪  (score=0)
```python
    # Parse a subscript and return a list of
```
L702  ⚪  (score=0)
```python
    # 1, 2 or 3 ExprNodes, depending on how
```
L703  ⚪  (score=0)
```python
    # many slice elements were encountered.
```
L704  ⚪  (score=0)
```python
    start = p_slice_element(s, (':',))
```
L705  ⚪  (score=0)
```python
    if s.sy != ':':
```
L706  ⚪  (score=0)
```python
        return [start]
```
L707  ⚪  (score=0)
```python
    s.next()
```
L708  ⚪  (score=0)
```python
    stop = p_slice_element(s, (':', ',', ']'))
```
L709  ⚪  (score=0)
```python
    if s.sy != ':':
```
L710  ⚪  (score=0)
```python
        return [start, stop]
```
L711  ⚪  (score=0)
```python
    s.next()
```
L712  ⚪  (score=0)
```python
    step = p_slice_element(s, (':', ',', ']'))
```
L713  ⚪  (score=0)
```python
    return [start, stop, step]
```
L714  ⚪  (score=0)
```python
```
L715  ⚪  (score=0)
```python
```
L716  ⚪  (score=0)
```python
@cython.cfunc
```
L717  ⚪  (score=0)
```python
def p_slice_element(s: PyrexScanner, follow_set):
```
L718  ⚪  (score=0)
```python
    # Simple expression which may be missing iff
```
L719  ⚪  (score=0)
```python
    # it is followed by something in follow_set.
```
L720  ⚪  (score=0)
```python
    if s.sy not in follow_set:
```
L721  ⚪  (score=0)
```python
        return p_test(s)
```
L722  ⚪  (score=0)
```python
    else:
```
L723  ⚪  (score=0)
```python
        return None
```
L724  ⚪  (score=0)
```python
```
L725  ⚪  (score=0)
```python
```
L726  ⚪  (score=0)
```python
@cython.cfunc
```
L727  ⚪  (score=0)
```python
def expect_ellipsis(s: PyrexScanner):
```
L728  ⚪  (score=0)
```python
    s.expect('...')
```
L729  ⚪  (score=0)
```python
```
L730  ⚪  (score=0)
```python
```
L731  ⚪  (score=0)
```python
@cython.cfunc
```
L732  ⚪  (score=0)
```python
def make_slice_nodes(pos, subscripts):
```
L733  ⚪  (score=0)
```python
    # Convert a list of subscripts as returned
```
L734  ⚪  (score=0)
```python
    # by p_subscript_list into a list of ExprNodes,
```
L735  ⚪  (score=0)
```python
    # creating SliceNodes for elements with 2 or
```
L736  ⚪  (score=0)
```python
    # more components.
```
L737  ⚪  (score=0)
```python
    result = []
```
L738  ⚪  (score=0)
```python
    for subscript in subscripts:
```
L739  ⚪  (score=0)
```python
        if len(subscript) == 1:
```
L740  ⚪  (score=0)
```python
            result.append(subscript[0])
```
L741  ⚪  (score=0)
```python
        else:
```
L742  ⚪  (score=0)
```python
            result.append(make_slice_node(pos, *subscript))
```
L743  ⚪  (score=0)
```python
    return result
```
L744  ⚪  (score=0)
```python
```
L745  ⚪  (score=0)
```python
```
L746  ⚪  (score=0)
```python
@cython.ccall
```
L747  ⚪  (score=0)
```python
def make_slice_node(pos, start, stop = None, step = None):
```
L748  ⚪  (score=0)
```python
    if not start:
```
L749  ⚪  (score=0)
```python
        start = ExprNodes.NoneNode(pos)
```
L750  ⚪  (score=0)
```python
    if not stop:
```
L751  ⚪  (score=0)
```python
        stop = ExprNodes.NoneNode(pos)
```
L752  ⚪  (score=0)
```python
    if not step:
```
L753  ⚪  (score=0)
```python
        step = ExprNodes.NoneNode(pos)
```
L754  ⚪  (score=0)
```python
    return ExprNodes.SliceNode(pos,
```
L755  ⚪  (score=0)
```python
        start = start, stop = stop, step = step)
```
L756  ⚪  (score=0)
```python
```
L757  ⚪  (score=0)
```python
```
L758  ⚪  (score=0)
```python
#atom: '(' [yield_expr|testlist_comp] ')' | '[' [listmaker] ']' | '{' [dict_or_set_maker] '}' | '`' testlist '`' | NAME | NUMBER | STRING+
```
L759  ⚪  (score=0)
```python
```
L760  ⚪  (score=0)
```python
@cython.cfunc
```
L761  ⚪  (score=0)
```python
def p_atom(s: PyrexScanner):
```
L762  ⚪  (score=0)
```python
    pos = s.position()
```
L763  ⚪  (score=0)
```python
    sy = s.sy
```
L764  ⚪  (score=0)
```python
    if sy == '(':
```
L765  ⚪  (score=0)
```python
        s.next()
```
L766  ⚪  (score=0)
```python
        if s.sy == ')':
```
L767  ⚪  (score=0)
```python
            result = ExprNodes.TupleNode(pos, args = [])
```
L768  ⚪  (score=0)
```python
        elif s.sy == 'yield':
```
L769  ⚪  (score=0)
```python
            result = p_yield_expression(s)
```
L770  ⚪  (score=0)
```python
        else:
```
L771  ⚪  (score=0)
```python
            result = p_testlist_comp(s)
```
L772  ⚪  (score=0)
```python
        s.expect(')')
```
L773  ⚪  (score=0)
```python
        return result
```
L774  ⚪  (score=0)
```python
    elif sy == '[':
```
L775  ⚪  (score=0)
```python
        return p_list_maker(s)
```
L776  ⚪  (score=0)
```python
    elif sy == '{':
```
L777  ⚪  (score=0)
```python
        return p_dict_or_set_maker(s)
```
L778  ⚪  (score=0)
```python
    elif sy == '`':
```
L779  ⚪  (score=0)
```python
        return p_backquote_expr(s)
```
L780  ⚪  (score=0)
```python
    elif sy == '...':
```
L781  ⚪  (score=0)
```python
        expect_ellipsis(s)
```
L782  ⚪  (score=0)
```python
        return ExprNodes.EllipsisNode(pos)
```
L783  ⚪  (score=0)
```python
    elif sy == 'INT':
```
L784  ⚪  (score=0)
```python
        return p_int_literal(s)
```
L785  ⚪  (score=0)
```python
    elif sy == 'FLOAT':
```
L786  ⚪  (score=0)
```python
        value = s.systring
```
L787  ⚪  (score=0)
```python
        s.next()
```
L788  ⚪  (score=0)
```python
        return ExprNodes.FloatNode(pos, value = value)
```
L789  ⚪  (score=0)
```python
    elif sy == 'IMAG':
```
L790  ⚪  (score=0)
```python
        sy_imag = s.systring
```
L791  ⚪  (score=0)
```python
        value = sy_imag[:len(sy_imag) - 1]
```
L792  ⚪  (score=0)
```python
        s.next()
```
L793  ⚪  (score=0)
```python
        return ExprNodes.ImagNode(pos, value = value)
```
L794  ⚪  (score=0)
```python
    elif sy == 'BEGIN_STRING' or sy == 'BEGIN_FT_STRING':
```
L795  ⚪  (score=0)
```python
        return p_atom_string(s)
```
L796  ⚪  (score=0)
```python
    elif sy == 'IDENT':
```
L797  ⚪  (score=0)
```python
        result = p_atom_ident_constants(s)
```
L798  ⚪  (score=0)
```python
        if result is None:
```
L799  ⚪  (score=0)
```python
            result = p_name(s, s.systring)
```
L800  ⚪  (score=0)
```python
            s.next()
```
L801  ⚪  (score=0)
```python
        return result
```
L802  ⚪  (score=0)
```python
    else:
```
L803  ⚪  (score=0)
```python
        s.error("Expected an identifier or literal")
```
L804  ⚪  (score=0)
```python
```
L805  ⚪  (score=0)
```python
```
L806  ⚪  (score=0)
```python
@cython.cfunc
```
L807  ⚪  (score=0)
```python
def p_atom_string(s: PyrexScanner):
```
L808  ⚪  (score=0)
```python
    # s.sy == 'BEGIN_STRING' or s.sy == 'BEGIN_FT_STRING'
```
L809  ⚪  (score=0)
```python
    pos = s.position()
```
L810  ⚪  (score=0)
```python
    kind, bytes_value, unicode_value = p_cat_string_literal(s)
```
L811  ⚪  (score=0)
```python
    if not kind:
```
L812  ⚪  (score=0)
```python
        return ExprNodes.UnicodeNode(pos, value=unicode_value, bytes_value=bytes_value)
```
L813  ⚪  (score=0)
```python
    kind_char: cython.Py_UCS4 = kind
```
L814  ⚪  (score=0)
```python
    if kind_char == 'c':
```
L815  ⚪  (score=0)
```python
        return ExprNodes.CharNode(pos, value=bytes_value)
```
L816  ⚪  (score=0)
```python
    elif kind_char == 'u':
```
L817  ⚪  (score=0)
```python
        return ExprNodes.UnicodeNode(pos, value=unicode_value, bytes_value=bytes_value)
```
L818  ⚪  (score=0)
```python
    elif kind_char == 'b':
```
L819  ⚪  (score=0)
```python
        return ExprNodes.BytesNode(pos, value=bytes_value)
```
L820  ⚪  (score=0)
```python
    elif kind_char == 'f':
```
L821  ⚪  (score=0)
```python
        return ExprNodes.JoinedStrNode(pos, values=unicode_value)
```
L822  ⚪  (score=0)
```python
    elif kind_char == 't':
```
L823  ⚪  (score=0)
```python
        # TODO
```
L824  ⚪  (score=0)
```python
        return ExprNodes.TemplateStringNode(pos, values=unicode_value)
```
L825  ⚪  (score=0)
```python
    else:
```
L826  ⚪  (score=0)
```python
        # This is actually prevented by the scanner (Lexicon.py).
```
L827  ⚪  (score=0)
```python
        s.error(f"invalid string kind '{kind}'")
```
L828  ⚪  (score=0)
```python
```
L829  ⚪  (score=0)
```python
```
L830  ⚪  (score=0)
```python
@cython.cfunc
```
L831  ⚪  (score=0)
```python
def p_atom_ident_constants(s: PyrexScanner):
```
L832  ⚪  (score=0)
```python
    """
```
L833  ⚪  (score=0)
```python
    Returns None if it isn't a special-cased named constant.
```
L834  ⚪  (score=0)
```python
    Only calls s.next() if it successfully matches a named constant.
```
L835  ⚪  (score=0)
```python
    """
```
L836  ⚪  (score=0)
```python
    # s.sy == 'IDENT'
```
L837  ⚪  (score=0)
```python
    pos = s.position()
```
L838  ⚪  (score=0)
```python
    name = s.systring
```
L839  ⚪  (score=0)
```python
    if name == "None":
```
L840  ⚪  (score=0)
```python
        result = ExprNodes.NoneNode(pos)
```
L841  ⚪  (score=0)
```python
    elif name == "True":
```
L842  ⚪  (score=0)
```python
        result = ExprNodes.BoolNode(pos, value=True)
```
L843  ⚪  (score=0)
```python
    elif name == "False":
```
L844  ⚪  (score=0)
```python
        result = ExprNodes.BoolNode(pos, value=False)
```
L845  ⚪  (score=0)
```python
    elif name == "NULL" and not s.in_python_file:
```
L846  ⚪  (score=0)
```python
        result = ExprNodes.NullNode(pos)
```
L847  ⚪  (score=0)
```python
    else:
```
L848  ⚪  (score=0)
```python
        return None
```
L849  ⚪  (score=0)
```python
    s.next()
```
L850  ⚪  (score=0)
```python
    return result
```
L851  ⚪  (score=0)
```python
```
L852  ⚪  (score=0)
```python
```
L853  ⚪  (score=0)
```python
@cython.cfunc
```
L854  ⚪  (score=0)
```python
def p_int_literal(s: PyrexScanner):
```
L855  ⚪  (score=0)
```python
    pos = s.position()
```
L856  ⚪  (score=0)
```python
    value: str = cython.cast(str, s.systring)
```
L857  ⚪  (score=0)
```python
    s.next()
```
L858  ⚪  (score=0)
```python
    unsigned = ""
```
L859  ⚪  (score=0)
```python
    longness = ""
```
L860  ⚪  (score=0)
```python
    while value[len(value) - 1] in "UuLl":
```
L861  ⚪  (score=0)
```python
        if value[len(value) - 1] in "Ll":
```
L862  ⚪  (score=0)
```python
            longness += "L"
```
L863  ⚪  (score=0)
```python
        else:
```
L864  ⚪  (score=0)
```python
            unsigned += "U"
```
L865  ⚪  (score=0)
```python
        value = value[:len(value) - 1]
```
L866  ⚪  (score=0)
```python
    # '3L' is ambiguous in Py2 but not in Py3.  '3U' and '3LL' are
```
L867  ⚪  (score=0)
```python
    # illegal in Py2 Python files.  All suffixes are illegal in Py3
```
L868  ⚪  (score=0)
```python
    # Python files.
```
L869  ⚪  (score=0)
```python
    is_c_literal = None
```
L870  ⚪  (score=0)
```python
    if unsigned:
```
L871  ⚪  (score=0)
```python
        is_c_literal = True
```
L872  ⚪  (score=0)
```python
    elif longness:
```
L873  ⚪  (score=0)
```python
        if longness == 'LL' or s.context.language_level >= 3:
```
L874  ⚪  (score=0)
```python
            is_c_literal = True
```
L875  ⚪  (score=0)
```python
    if s.in_python_file:
```
L876  ⚪  (score=0)
```python
        if is_c_literal:
```
L877  ⚪  (score=0)
```python
            error(pos, "illegal integer literal syntax in Python source file")
```
L878  ⚪  (score=0)
```python
        is_c_literal = False
```
L879  ⚪  (score=0)
```python
    return ExprNodes.IntNode(pos,
```
L880  ⚪  (score=0)
```python
                             is_c_literal = is_c_literal,
```
L881  ⚪  (score=0)
```python
                             value = value,
```
L882  ⚪  (score=0)
```python
                             unsigned = unsigned,
```
L883  ⚪  (score=0)
```python
                             longness = longness)
```
L884  ⚪  (score=0)
```python
```
L885  ⚪  (score=0)
```python
```
L886  ⚪  (score=0)
```python
@cython.cfunc
```
L887  ⚪  (score=0)
```python
def p_name(s: PyrexScanner, name):
```
L888  ⚪  (score=0)
```python
    pos = s.position()
```
L889  ⚪  (score=0)
```python
    if not s.compile_time_expr and name in s.compile_time_env:
```
L890  ⚪  (score=0)
```python
        value = s.compile_time_env.lookup_here(name)
```
L891  ⚪  (score=0)
```python
        node = wrap_compile_time_constant(pos, value)
```
L892  ⚪  (score=0)
```python
        if node is not None:
```
L893  ⚪  (score=0)
```python
            return node
```
L894  ⚪  (score=0)
```python
    return ExprNodes.NameNode(pos, name=name)
```
L895  ⚪  (score=0)
```python
```
L896  ⚪  (score=0)
```python
```
L897  ⚪  (score=0)
```python
@cython.cfunc
```
L898  ⚪  (score=0)
```python
def wrap_compile_time_constant(pos, value):
```
L899  ⚪  (score=0)
```python
    if value is None:
```
L900  ⚪  (score=0)
```python
        return ExprNodes.NoneNode(pos)
```
L901  ⚪  (score=0)
```python
    elif value is Ellipsis:
```
L902  ⚪  (score=0)
```python
        return ExprNodes.EllipsisNode(pos)
```
L903  ⚪  (score=0)
```python
    elif isinstance(value, bool):
```
L904  ⚪  (score=0)
```python
        return ExprNodes.BoolNode(pos, value=value)
```
L905  ⚪  (score=0)
```python
    elif isinstance(value, int):
```
L906  ⚪  (score=0)
```python
        return ExprNodes.IntNode(pos, value=repr(value), constant_result=value)
```
L907  ⚪  (score=0)
```python
    elif isinstance(value, float):
```
L908  ⚪  (score=0)
```python
        return ExprNodes.FloatNode(pos, value=repr(value), constant_result=value)
```
L909  ⚪  (score=0)
```python
    elif isinstance(value, complex):
```
L910  ⚪  (score=0)
```python
        node = ExprNodes.ImagNode(pos, value=repr(value.imag), constant_result=complex(0.0, value.imag))
```
L911  ⚪  (score=0)
```python
        if value.real:
```
L912  ⚪  (score=0)
```python
            # FIXME: should we care about -0.0 ?
```
L913  ⚪  (score=0)
```python
            # probably not worth using the '-' operator for negative imag values
```
L914  ⚪  (score=0)
```python
            node = ExprNodes.binop_node(
```
L915  ⚪  (score=0)
```python
                pos, '+', ExprNodes.FloatNode(pos, value=repr(value.real), constant_result=value.real), node,
```
L916  ⚪  (score=0)
```python
                constant_result=value)
```
L917  ⚪  (score=0)
```python
        return node
```
L918  ⚪  (score=0)
```python
    elif isinstance(value, str):
```
L919  ⚪  (score=0)
```python
        return ExprNodes.UnicodeNode(pos, value=EncodedString(value))
```
L920  ⚪  (score=0)
```python
    elif isinstance(value, bytes):
```
L921  ⚪  (score=0)
```python
        bvalue = bytes_literal(value, 'ascii')  # actually: unknown encoding, but BytesLiteral requires one
```
L922  ⚪  (score=0)
```python
        return ExprNodes.BytesNode(pos, value=bvalue, constant_result=value)
```
L923  ⚪  (score=0)
```python
    elif isinstance(value, tuple):
```
L924  ⚪  (score=0)
```python
        args = [wrap_compile_time_constant(pos, arg) for arg in value]
```
L925  ⚪  (score=0)
```python
        if None in args:
```
L926  ⚪  (score=0)
```python
            # error already reported
```
L927  ⚪  (score=0)
```python
            return None
```
L928  ⚪  (score=0)
```python
        return ExprNodes.TupleNode(pos, args=args)
```
L929  ⚪  (score=0)
```python
```
L930  ⚪  (score=0)
```python
    error(pos, "Invalid type for compile-time constant: %r (type %s)"
```
L931  ⚪  (score=0)
```python
               % (value, value.__class__.__name__))
```
L932  ⚪  (score=0)
```python
    return None
```
L933  ⚪  (score=0)
```python
```
L934  ⚪  (score=0)
```python
```
L935  ⚪  (score=0)
```python
@cython.cfunc
```
L936  ⚪  (score=0)
```python
def p_cat_string_literal(s: PyrexScanner) -> tuple:
```
L937  ⚪  (score=0)
```python
    # A sequence of one or more adjacent string literals.
```
L938  ⚪  (score=0)
```python
    # Returns (kind, bytes_value, unicode_value)
```
L939  ⚪  (score=0)
```python
    # where kind in ('b', 'c', 'u', 'f', 't', '')
```
L940  ⚪  (score=0)
```python
    pos = s.position()
```
L941  ⚪  (score=0)
```python
    kind, bytes_value, unicode_value = p_string_literal(s)
```
L942  ⚪  (score=0)
```python
    if kind == 'c' or (s.sy != 'BEGIN_STRING' and s.sy != 'BEGIN_FT_STRING'):
```
L943  ⚪  (score=0)
```python
        return kind, bytes_value, unicode_value
```
L944  ⚪  (score=0)
```python
    bstrings, ustrings, positions = [bytes_value], [unicode_value], [pos]
```
L945  ⚪  (score=0)
```python
    bytes_value = unicode_value = None
```
L946  ⚪  (score=0)
```python
    while s.sy == 'BEGIN_STRING' or s.sy == 'BEGIN_FT_STRING':
```
L947  ⚪  (score=0)
```python
        pos = s.position()
```
L948  ⚪  (score=0)
```python
        next_kind, next_bytes_value, next_unicode_value = p_string_literal(s)
```
L949  ⚪  (score=0)
```python
        if next_kind == 'c':
```
L950  ⚪  (score=0)
```python
            error(pos, "Cannot concatenate char literal with another string or char literal")
```
L951  ⚪  (score=0)
```python
            continue
```
L952  ⚪  (score=0)
```python
        elif next_kind != kind:
```
L953  ⚪  (score=0)
```python
            # concatenating f strings and normal strings is allowed and leads to an f string
```
L954  ⚪  (score=0)
```python
            if {kind, next_kind} in ({'f', 'u'}, {'f', ''}):
```
L955  ⚪  (score=0)
```python
                kind = 'f'
```
L956  ⚪  (score=0)
```python
            elif kind == 't' or next_kind == 't':
```
L957  ⚪  (score=0)
```python
                error(pos, "cannot mix t-string literals with string or bytes literals")
```
L958  ⚪  (score=0)
```python
                continue
```
L959  ⚪  (score=0)
```python
            else:
```
L960  ⚪  (score=0)
```python
                error(pos, "Cannot mix string literals of different types, expected %s'', got %s''" % (
```
L961  ⚪  (score=0)
```python
                    kind, next_kind))
```
L962  ⚪  (score=0)
```python
                continue
```
L963  ⚪  (score=0)
```python
        bstrings.append(next_bytes_value)
```
L964  ⚪  (score=0)
```python
        ustrings.append(next_unicode_value)
```
L965  ⚪  (score=0)
```python
        positions.append(pos)
```
L966  ⚪  (score=0)
```python
    # join and rewrap the partial literals
```
L967  ⚪  (score=0)
```python
    if kind in ('b', 'c', '') or kind == 'u' and None not in bstrings:
```
L968  ⚪  (score=0)
```python
        # Py3 enforced unicode literals are parsed as bytes/unicode combination
```
L969  ⚪  (score=0)
```python
        bytes_value = bytes_literal(b''.join(bstrings), s.source_encoding)
```
L970  ⚪  (score=0)
```python
    if kind in ('u', ''):
```
L971  ⚪  (score=0)
```python
        unicode_value = EncodedString(''.join([u for u in ustrings if u is not None]))
```
L972  ⚪  (score=0)
```python
    if kind == 'f':
```
L973  ⚪  (score=0)
```python
        unicode_value = []
```
L974  ⚪  (score=0)
```python
        for u, pos in zip(ustrings, positions, strict=False):
```
L975  ⚪  (score=0)
```python
            if isinstance(u, list):
```
L976  ⚪  (score=0)
```python
                unicode_value += u
```
L977  ⚪  (score=0)
```python
            else:
```
L978  ⚪  (score=0)
```python
                # non-f-string concatenated into the f-string
```
L979  ⚪  (score=0)
```python
                unicode_value.append(ExprNodes.UnicodeNode(pos, value=EncodedString(u)))
```
L980  ⚪  (score=0)
```python
    if kind == 't':
```
L981  ⚪  (score=0)
```python
        unicode_value = []
```
L982  ⚪  (score=0)
```python
        for u in ustrings:
```
L983  ⚪  (score=0)
```python
            unicode_value.extend(u)
```
L984  ⚪  (score=0)
```python
    return kind, bytes_value, unicode_value
```
L985  ⚪  (score=0)
```python
```
L986  ⚪  (score=0)
```python
```
L987  ⚪  (score=0)
```python
@cython.cfunc
```
L988  ⚪  (score=0)
```python
def p_opt_string_literal(s: PyrexScanner, required_type: str = 'u'):
```
L989  ⚪  (score=0)
```python
    if s.sy != 'BEGIN_STRING':
```
L990  ⚪  (score=0)
```python
        return None
```
L991  ⚪  (score=0)
```python
    pos = s.position()
```
L992  ⚪  (score=0)
```python
    kind, bytes_value, unicode_value = p_string_literal(s, required_type)
```
L993  ⚪  (score=0)
```python
    if required_type == 'u':
```
L994  ⚪  (score=0)
```python
        if kind == 'f':
```
L995  ⚪  (score=0)
```python
            s.error("f-string not allowed here", pos)
```
L996  ⚪  (score=0)
```python
        return unicode_value
```
L997  ⚪  (score=0)
```python
    elif required_type == 'b':
```
L998  ⚪  (score=0)
```python
        return bytes_value
```
L999  ⚪  (score=0)
```python
    else:
```
L1000  ⚪  (score=0)
```python
        s.error("internal parser configuration error")
```
L1001  ⚪  (score=0)
```python
```
L1002  ⚪  (score=0)
```python
```
L1003  ⚪  (score=0)
```python
@cython.cfunc
```
L1004  ⚪  (score=0)
```python
def check_for_non_ascii_characters(string) -> cython.bint:
```
L1005  ⚪  (score=0)
```python
    s = cython.cast(str, string)  # EncodedString
```
L1006  ⚪  (score=0)
```python
    for c in s:
```
L1007  ⚪  (score=0)
```python
        if c >= '\x80':
```
L1008  ⚪  (score=0)
```python
            return True
```
L1009  ⚪  (score=0)
```python
    return False
```
L1010  ⚪  (score=0)
```python
```
L1011  ⚪  (score=0)
```python
```
L1012  ⚪  (score=0)
```python
@cython.cfunc
```
L1013  ⚪  (score=0)
```python
def p_string_literal_shared_read(
```
L1014  ⚪  (score=0)
```python
        s: PyrexScanner, pos, chars, kind,
```
L1015  ⚪  (score=0)
```python
        is_raw: cython.bint):
```
L1016  ⚪  (score=0)
```python
    """
```
L1017  ⚪  (score=0)
```python
    Returns a string of non-escaped characters (if handled) or none.
```
L1018  ⚪  (score=0)
```python
    If passed an escape sequence returns an empty string.
```
L1019  ⚪  (score=0)
```python
    """
```
L1020  ⚪  (score=0)
```python
    sy = s.sy
```
L1021  ⚪  (score=0)
```python
    systr = s.systring
```
L1022  ⚪  (score=0)
```python
    result = systr
```
L1023  ⚪  (score=0)
```python
    is_python3_source: cython.bint = s.context.language_level >= 3
```
L1024  ⚪  (score=0)
```python
    # print "p_string_literal: sy =", sy, repr(s.systring) ###
```
L1025  ⚪  (score=0)
```python
    if sy == 'CHARS':
```
L1026  ⚪  (score=0)
```python
        chars.append(systr)
```
L1027  ⚪  (score=0)
```python
    elif sy == 'ESCAPE':
```
L1028  ⚪  (score=0)
```python
        # in Py2, 'ur' raw unicode strings resolve unicode escapes but nothing else
```
L1029  ⚪  (score=0)
```python
        if is_raw and (is_python3_source or kind != 'u' or len(systr) < 2 or systr[1] not in 'Uu'):
```
L1030  ⚪  (score=0)
```python
            chars.append(systr)
```
L1031  ⚪  (score=0)
```python
        else:
```
L1032  ⚪  (score=0)
```python
            result = ""
```
L1033  ⚪  (score=0)
```python
            _append_escape_sequence(kind, chars, systr, s)
```
L1034  ⚪  (score=0)
```python
    elif sy == 'NEWLINE':
```
L1035  ⚪  (score=0)
```python
        chars.append('\n')
```
L1036  ⚪  (score=0)
```python
    elif sy == 'EOF':
```
L1037  ⚪  (score=0)
```python
        s.error("Unclosed string literal", pos=pos)
```
L1038  ⚪  (score=0)
```python
    else:
```
L1039  ⚪  (score=0)
```python
        return None
```
L1040  ⚪  (score=0)
```python
    return result
```
L1041  ⚪  (score=0)
```python
```
L1042  ⚪  (score=0)
```python
@cython.cfunc
```
L1043  ⚪  (score=0)
```python
def _validate_kind_string(pos, systring: str):
```
L1044  ⚪  (score=0)
```python
    kind_string = systring.rstrip('"\'').lower()
```
L1045  ⚪  (score=0)
```python
    if len(kind_string) <= 1 or (len(kind_string) == 2 and kind_string in "rbrurfrtr"):
```
L1046  ⚪  (score=0)
```python
        return kind_string
```
L1047  ⚪  (score=0)
```python
    # Otherwise an error of some sort
```
L1048  ⚪  (score=0)
```python
    unique_string_prefixes = set(kind_string)
```
L1049  ⚪  (score=0)
```python
    if len(unique_string_prefixes) != len(kind_string):
```
L1050  ⚪  (score=0)
```python
        error(pos, 'Duplicate string prefix character')
```
L1051  ⚪  (score=0)
```python
    unique_string_prefixes.discard('r')
```
L1052  ⚪  (score=0)
```python
    unique_string_prefixes = sorted(unique_string_prefixes)
```
L1053  ⚪  (score=0)
```python
    if len(unique_string_prefixes) >= 2:
```
L1054  ⚪  (score=0)
```python
        error(pos, f'String prefixes {unique_string_prefixes[0]} and {unique_string_prefixes[1]} cannot be combined')
```
L1055  ⚪  (score=0)
```python
    else:
```
L1056  ⚪  (score=0)
```python
        error(pos, f'Invalid string prefix {kind_string}')
```
L1057  ⚪  (score=0)
```python
    return ''
```
L1058  ⚪  (score=0)
```python
```
L1059  ⚪  (score=0)
```python
@cython.cfunc
```
L1060  ⚪  (score=0)
```python
def p_string_literal(s: PyrexScanner, kind_override=None) -> tuple:
```
L1061  ⚪  (score=0)
```python
    # A single string or char literal.  Returns (kind, bvalue, uvalue)
```
L1062  ⚪  (score=0)
```python
    # where kind in ('b', 'c', 'u', 'f', '').  The 'bvalue' is the source
```
L1063  ⚪  (score=0)
```python
    # code byte sequence of the string literal, 'uvalue' is the
```
L1064  ⚪  (score=0)
```python
    # decoded Unicode string.  Either of the two may be None depending
```
L1065  ⚪  (score=0)
```python
    # on the 'kind' of string, only unprefixed strings have both
```
L1066  ⚪  (score=0)
```python
    # representations. In f-strings, the uvalue is a list of the Unicode
```
L1067  ⚪  (score=0)
```python
    # strings and f-string expressions that make up the f-string.
```
L1068  ⚪  (score=0)
```python
    # s.sy == 'BEGIN_STRING' or s.sy == 'BEGIN_FT_STRING'
```
L1069  ⚪  (score=0)
```python
    if s.sy == 'BEGIN_FT_STRING':
```
L1070  ⚪  (score=0)
```python
        assert kind_override is None
```
L1071  ⚪  (score=0)
```python
        return p_ft_string_literal(s)
```
L1072  ⚪  (score=0)
```python
    pos = s.position()
```
L1073  ⚪  (score=0)
```python
    is_python3_source: cython.bint = s.context.language_level >= 3
```
L1074  ⚪  (score=0)
```python
    has_non_ascii_literal_characters = False
```
L1075  ⚪  (score=0)
```python
    kind_string = _validate_kind_string(pos, s.systring)
```
L1076  ⚪  (score=0)
```python
```
L1077  ⚪  (score=0)
```python
    is_raw: cython.bint = 'r' in kind_string
```
L1078  ⚪  (score=0)
```python
```
L1079  ⚪  (score=0)
```python
    if 'c' in kind_string:
```
L1080  ⚪  (score=0)
```python
        # this should never happen, since the lexer does not allow combining c
```
L1081  ⚪  (score=0)
```python
        # with other prefix characters
```
L1082  ⚪  (score=0)
```python
        if len(kind_string) != 1:
```
L1083  ⚪  (score=0)
```python
            error(pos, 'Invalid string prefix for character literal')
```
L1084  ⚪  (score=0)
```python
        kind = 'c'
```
L1085  ⚪  (score=0)
```python
    elif 'b' in kind_string:
```
L1086  ⚪  (score=0)
```python
        kind = 'b'
```
L1087  ⚪  (score=0)
```python
    elif 'u' in kind_string:
```
L1088  ⚪  (score=0)
```python
        kind = 'u'
```
L1089  ⚪  (score=0)
```python
    else:
```
L1090  ⚪  (score=0)
```python
        kind = ''
```
L1091  ⚪  (score=0)
```python
```
L1092  ⚪  (score=0)
```python
    if kind == '' and kind_override is None and Future.unicode_literals in s.context.future_directives:
```
L1093  ⚪  (score=0)
```python
        chars = StringEncoding.StrLiteralBuilder(s.source_encoding)
```
L1094  ⚪  (score=0)
```python
        kind = 'u'
```
L1095  ⚪  (score=0)
```python
    else:
```
L1096  ⚪  (score=0)
```python
        if kind_override is not None and kind_override in 'ub':
```
L1097  ⚪  (score=0)
```python
            kind = kind_override
```
L1098  ⚪  (score=0)
```python
        if kind in ('u', 'f'):  # f-strings are scanned exactly like Unicode literals, but are parsed further later
```
L1099  ⚪  (score=0)
```python
            chars = StringEncoding.UnicodeLiteralBuilder()
```
L1100  ⚪  (score=0)
```python
        elif kind == '':
```
L1101  ⚪  (score=0)
```python
            chars = StringEncoding.StrLiteralBuilder(s.source_encoding)
```
L1102  ⚪  (score=0)
```python
        else:
```
L1103  ⚪  (score=0)
```python
            chars = StringEncoding.BytesLiteralBuilder(s.source_encoding)
```
L1104  ⚪  (score=0)
```python
```
L1105  ⚪  (score=0)
```python
    while 1:
```
L1106  ⚪  (score=0)
```python
        s.next()
```
L1107  ⚪  (score=0)
```python
        handled_chars = p_string_literal_shared_read(
```
L1108  ⚪  (score=0)
```python
            s, pos, chars, kind,
```
L1109  ⚪  (score=0)
```python
            is_raw=is_raw)
```
L1110  ⚪  (score=0)
```python
        if handled_chars is not None:
```
L1111  ⚪  (score=0)
```python
            if (not has_non_ascii_literal_characters and
```
L1112  ⚪  (score=0)
```python
                    is_python3_source and Future.unicode_literals in s.context.future_directives):
```
L1113  ⚪  (score=0)
```python
                has_non_ascii_literal_characters = check_for_non_ascii_characters(handled_chars)
```
L1114  ⚪  (score=0)
```python
            continue
```
L1115  ⚪  (score=0)
```python
        if s.sy == 'END_STRING':
```
L1116  ⚪  (score=0)
```python
            break
```
L1117  ⚪  (score=0)
```python
        else:
```
L1118  ⚪  (score=0)
```python
            s.error("Unexpected token %r:%r in string literal" % (
```
L1119  ⚪  (score=0)
```python
                s.sy, s.systring))
```
L1120  ⚪  (score=0)
```python
```
L1121  ⚪  (score=0)
```python
    if kind == 'c':
```
L1122  ⚪  (score=0)
```python
        unicode_value = None
```
L1123  ⚪  (score=0)
```python
        bytes_value = chars.getchar()
```
L1124  ⚪  (score=0)
```python
        if len(bytes_value) != 1:
```
L1125  ⚪  (score=0)
```python
            error(pos, "invalid character literal: %r" % bytes_value)
```
L1126  ⚪  (score=0)
```python
    else:
```
L1127  ⚪  (score=0)
```python
        bytes_value, unicode_value = chars.getstrings()
```
L1128  ⚪  (score=0)
```python
        if (has_non_ascii_literal_characters
```
L1129  ⚪  (score=0)
```python
                and is_python3_source and Future.unicode_literals in s.context.future_directives):
```
L1130  ⚪  (score=0)
```python
            # Python 3 forbids literal non-ASCII characters in byte strings
```
L1131  ⚪  (score=0)
```python
            if kind == 'b':
```
L1132  ⚪  (score=0)
```python
                s.error("bytes can only contain ASCII literal characters.", pos=pos)
```
L1133  ⚪  (score=0)
```python
            bytes_value = None
```
L1134  ⚪  (score=0)
```python
    s.next()
```
L1135  ⚪  (score=0)
```python
    return (kind, bytes_value, unicode_value)
```
L1136  ⚪  (score=0)
```python
```
L1137  ⚪  (score=0)
```python
```
L1138  ⚪  (score=0)
```python
@cython.cfunc
```
L1139  ⚪  (score=0)
```python
def p_read_ft_string_expression(s: PyrexScanner):
```
L1140  ⚪  (score=0)
```python
    strings = []
```
L1141  ⚪  (score=0)
```python
    while True:
```
L1142  ⚪  (score=0)
```python
        s.next()
```
L1143  ⚪  (score=0)
```python
        sy = s.sy
```
L1144  ⚪  (score=0)
```python
        if sy in ["END_FT_STRING_EXPR",
```
L1145  ⚪  (score=0)
```python
                    # probably an error, but handle it elsewhere
```
L1146  ⚪  (score=0)
```python
                   "EOF", None]:
```
L1147  ⚪  (score=0)
```python
            if sy == "END_FT_STRING_EXPR":
```
L1148  ⚪  (score=0)
```python
                s.next()
```
L1149  ⚪  (score=0)
```python
            return ''.join(strings)
```
L1150  ⚪  (score=0)
```python
        strings.append(s.systring)
```
L1151  ⚪  (score=0)
```python
```
L1152  ⚪  (score=0)
```python
```
L1153  ⚪  (score=0)
```python
@cython.cfunc
```
L1154  ⚪  (score=0)
```python
def p_ft_string_replacement_field(s: PyrexScanner,
```
L1155  ⚪  (score=0)
```python
                                is_raw: cython.bint, is_single_quoted: cython.bint,
```
L1156  ⚪  (score=0)
```python
                                tf_string_kind: cython.Py_UCS4):
```
L1157  ⚪  (score=0)
```python
    result = []
```
L1158  ⚪  (score=0)
```python
    conversion_char = format_spec = expr = None
```
L1159  ⚪  (score=0)
```python
    t_string_expression = None
```
L1160  ⚪  (score=0)
```python
    self_documenting = False
```
L1161  ⚪  (score=0)
```python
```
L1162  ⚪  (score=0)
```python
    bracket_pos = s.position()
```
L1163  ⚪  (score=0)
```python
    expr_pos = (bracket_pos[0], bracket_pos[1], bracket_pos[2]+1)
```
L1164  ⚪  (score=0)
```python
    expr_string = p_read_ft_string_expression(s)
```
L1165  ⚪  (score=0)
```python
    if not expr_string.strip():
```
L1166  ⚪  (score=0)
```python
        error(bracket_pos,
```
L1167  ⚪  (score=0)
```python
              f"empty expression not allowed in {tf_string_kind}-string")
```
L1168  ⚪  (score=0)
```python
        result = []
```
L1169  ⚪  (score=0)
```python
    else:
```
L1170  ⚪  (score=0)
```python
        original_scanner = s
```
L1171  ⚪  (score=0)
```python
        s = PyrexScanner(
```
L1172  ⚪  (score=0)
```python
            StringIO(expr_string),
```
L1173  ⚪  (score=0)
```python
            bracket_pos[0],
```
L1174  ⚪  (score=0)
```python
            parent_scanner=s,
```
L1175  ⚪  (score=0)
```python
            source_encoding=s.source_encoding,
```
L1176  ⚪  (score=0)
```python
            initial_pos=expr_pos
```
L1177  ⚪  (score=0)
```python
        )
```
L1178  ⚪  (score=0)
```python
        s.bracket_nesting_level += 1
```
L1179  ⚪  (score=0)
```python
        if s.sy == "INDENT":
```
L1180  ⚪  (score=0)
```python
            s.next()
```
L1181  ⚪  (score=0)
```python
        if s.sy == 'yield':
```
L1182  ⚪  (score=0)
```python
            expr = p_yield_expression(
```
L1183  ⚪  (score=0)
```python
                s,
```
L1184  ⚪  (score=0)
```python
                statement_terminators=statement_terminators | {':', '}', '!'})
```
L1185  ⚪  (score=0)
```python
        else:
```
L1186  ⚪  (score=0)
```python
            expr = p_testlist_star_expr(s)
```
L1187  ⚪  (score=0)
```python
```
L1188  ⚪  (score=0)
```python
        if s.sy == "=":
```
L1189  ⚪  (score=0)
```python
            self_documenting = True
```
L1190  ⚪  (score=0)
```python
            s.next()
```
L1191  ⚪  (score=0)
```python
```
L1192  ⚪  (score=0)
```python
        if s.sy == "!":
```
L1193  ⚪  (score=0)
```python
            # format conversion
```
L1194  ⚪  (score=0)
```python
            previous_pos = s.position()
```
L1195  ⚪  (score=0)
```python
            s.next()
```
L1196  ⚪  (score=0)
```python
            conversion_char = s.systring
```
L1197  ⚪  (score=0)
```python
            # validate the conversion char
```
L1198  ⚪  (score=0)
```python
            if conversion_char in ['}', ':', '']:
```
L1199  ⚪  (score=0)
```python
                error(s.position(), "missing conversion character")
```
L1200  ⚪  (score=0)
```python
            elif not ExprNodes.FormattedValueNode.find_conversion_func(conversion_char):
```
L1201  ⚪  (score=0)
```python
                error(s.position(), "invalid conversion character '%s'" % conversion_char)
```
L1202  ⚪  (score=0)
```python
                s.next()
```
L1203  ⚪  (score=0)
```python
            elif s.position()[2] != (previous_pos[2] + 1):
```
L1204  ⚪  (score=0)
```python
                error(s.position(), "f-string: conversion type must come right after the exclamation mark")
```
L1205  ⚪  (score=0)
```python
                s.next()
```
L1206  ⚪  (score=0)
```python
            else:
```
L1207  ⚪  (score=0)
```python
                s.next()
```
L1208  ⚪  (score=0)
```python
```
L1209  ⚪  (score=0)
```python
        if self_documenting or tf_string_kind == 't':
```
L1210  ⚪  (score=0)
```python
            if conversion_char is not None:
```
L1211  ⚪  (score=0)
```python
                expr_string, _ = expr_string.rsplit('!', 1)
```
L1212  ⚪  (score=0)
```python
            if tf_string_kind == 't':
```
L1213  ⚪  (score=0)
```python
                t_string_expression = ExprNodes.UnicodeNode(
```
L1214  ⚪  (score=0)
```python
                    pos=expr_pos,
```
L1215  ⚪  (score=0)
```python
                    value=StringEncoding.EncodedString(expr_string.rstrip().rstrip('=').rstrip())
```
L1216  ⚪  (score=0)
```python
                )
```
L1217  ⚪  (score=0)
```python
            if self_documenting:
```
L1218  ⚪  (score=0)
```python
                result.append(
```
L1219  ⚪  (score=0)
```python
                    ExprNodes.UnicodeNode(
```
L1220  ⚪  (score=0)
```python
                        pos=expr_pos,
```
L1221  ⚪  (score=0)
```python
                        value=StringEncoding.EncodedString(expr_string)
```
L1222  ⚪  (score=0)
```python
                    )
```
L1223  ⚪  (score=0)
```python
                )
```
L1224  ⚪  (score=0)
```python
```
L1225  ⚪  (score=0)
```python
        # Validate that the expression string has actually ended
```
L1226  ⚪  (score=0)
```python
        while s.sy == "NEWLINE" or s.sy == "DEDENT":
```
L1227  ⚪  (score=0)
```python
            s.next()
```
L1228  ⚪  (score=0)
```python
        if s.sy != "EOF":
```
L1229  ⚪  (score=0)
```python
            error(
```
L1230  ⚪  (score=0)
```python
                s.position(),
```
L1231  ⚪  (score=0)
```python
                f"Unexpected characters after {tf_string_kind}-string expression: {s.systring}")
```
L1232  ⚪  (score=0)
```python
```
L1233  ⚪  (score=0)
```python
        s = original_scanner
```
L1234  ⚪  (score=0)
```python
```
L1235  ⚪  (score=0)
```python
    if s.sy == ":":
```
L1236  ⚪  (score=0)
```python
        # full format spec
```
L1237  ⚪  (score=0)
```python
        pos = s.position()
```
L1238  ⚪  (score=0)
```python
        # Contents of format spec are handled closer to an f-string than a t-string
```
L1239  ⚪  (score=0)
```python
        # (even for t-strings).
```
L1240  ⚪  (score=0)
```python
        format_spec_contents = p_ft_string_middles(s, is_raw, is_single_quoted, is_format_string=True, tf_string_kind='f')
```
L1241  ⚪  (score=0)
```python
        format_spec = ExprNodes.JoinedStrNode(
```
L1242  ⚪  (score=0)
```python
            pos,
```
L1243  ⚪  (score=0)
```python
            values=format_spec_contents
```
L1244  ⚪  (score=0)
```python
        )
```
L1245  ⚪  (score=0)
```python
    if self_documenting and conversion_char is None and format_spec is None:
```
L1246  ⚪  (score=0)
```python
        conversion_char = 'r'
```
L1247  ⚪  (score=0)
```python
```
L1248  ⚪  (score=0)
```python
    if conversion_char is not None:
```
L1249  ⚪  (score=0)
```python
        conversion_char = StringEncoding.EncodedString(conversion_char)
```
L1250  ⚪  (score=0)
```python
    if tf_string_kind == 't':
```
L1251  ⚪  (score=0)
```python
        result.append(ExprNodes.TStringInterpolationNode(
```
L1252  ⚪  (score=0)
```python
            bracket_pos, value=expr, conversion_char=conversion_char,
```
L1253  ⚪  (score=0)
```python
            format_spec=format_spec, expression_str=t_string_expression
```
L1254  ⚪  (score=0)
```python
        ))
```
L1255  ⚪  (score=0)
```python
    else:
```
L1256  ⚪  (score=0)
```python
        result.append(ExprNodes.FormattedValueNode(
```
L1257  ⚪  (score=0)
```python
            bracket_pos, value=expr, conversion_char=conversion_char,
```
L1258  ⚪  (score=0)
```python
            format_spec=format_spec
```
L1259  ⚪  (score=0)
```python
        ))
```
L1260  ⚪  (score=0)
```python
    return result
```
L1261  ⚪  (score=0)
```python
```
L1262  ⚪  (score=0)
```python
@cython.cfunc
```
L1263  ⚪  (score=0)
```python
def p_ft_string_middles(s: PyrexScanner,
```
L1264  ⚪  (score=0)
```python
                        is_raw: cython.bint, is_single_quoted: cython.bint,
```
L1265  ⚪  (score=0)
```python
                        is_format_string: cython.bint,
```
L1266  ⚪  (score=0)
```python
                        tf_string_kind: cython.Py_UCS4):
```
L1267  ⚪  (score=0)
```python
    middles: list = []
```
L1268  ⚪  (score=0)
```python
    builder = StringEncoding.UnicodeLiteralBuilder()
```
L1269  ⚪  (score=0)
```python
    pos = s.position()
```
L1270  ⚪  (score=0)
```python
    while True:
```
L1271  ⚪  (score=0)
```python
        s.next()
```
L1272  ⚪  (score=0)
```python
        sy = s.sy
```
L1273  ⚪  (score=0)
```python
```
L1274  ⚪  (score=0)
```python
        handled_chars = p_string_literal_shared_read(
```
L1275  ⚪  (score=0)
```python
            s, pos, builder, "u",
```
L1276  ⚪  (score=0)
```python
            is_raw=is_raw)
```
L1277  ⚪  (score=0)
```python
        if handled_chars is not None:
```
L1278  ⚪  (score=0)
```python
            continue
```
L1279  ⚪  (score=0)
```python
```
L1280  ⚪  (score=0)
```python
        if builder.chars:
```
L1281  ⚪  (score=0)
```python
            middles.append(ExprNodes.UnicodeNode(pos, value=builder.getstring()))
```
L1282  ⚪  (score=0)
```python
            builder = StringEncoding.UnicodeLiteralBuilder()
```
L1283  ⚪  (score=0)
```python
        if sy == "{":
```
L1284  ⚪  (score=0)
```python
            fields = p_ft_string_replacement_field(
```
L1285  ⚪  (score=0)
```python
                s, is_raw, is_single_quoted, tf_string_kind=tf_string_kind)
```
L1286  ⚪  (score=0)
```python
            middles.extend(fields)
```
L1287  ⚪  (score=0)
```python
            if not s.sy == '}':
```
L1288  ⚪  (score=0)
```python
                s.expected('}')
```
L1289  ⚪  (score=0)
```python
            continue
```
L1290  ⚪  (score=0)
```python
        elif sy == "END_FT_STRING":
```
L1291  ⚪  (score=0)
```python
            break
```
L1292  ⚪  (score=0)
```python
        elif s.sy == '}':
```
L1293  ⚪  (score=0)
```python
            if is_format_string:
```
L1294  ⚪  (score=0)
```python
                break
```
L1295  ⚪  (score=0)
```python
            # otherwise it's an error, but the scanner has reported it
```
L1296  ⚪  (score=0)
```python
        else:
```
L1297  ⚪  (score=0)
```python
            error(
```
L1298  ⚪  (score=0)
```python
                s.position(),
```
L1299  ⚪  (score=0)
```python
                "Unexpected token %r:%r in %s-string literal" % (
```
L1300  ⚪  (score=0)
```python
                s.sy, s.systring, tf_string_kind))
```
L1301  ⚪  (score=0)
```python
    return middles
```
L1302  ⚪  (score=0)
```python
```
L1303  ⚪  (score=0)
```python
@cython.cfunc
```
L1304  ⚪  (score=0)
```python
def p_ft_string_literal(s: PyrexScanner):
```
L1305  ⚪  (score=0)
```python
    # s.sy == BEGIN_FT_STRING
```
L1306  ⚪  (score=0)
```python
    kind_string = _validate_kind_string(s.position(), s.systring)
```
L1307  ⚪  (score=0)
```python
    tf_string_kind: cython.Py_UCS4 = 't' if 't' in kind_string else 'f'
```
L1308  ⚪  (score=0)
```python
    is_raw: cython.bint = 'r' in kind_string
```
L1309  ⚪  (score=0)
```python
    quotes = s.systring.lstrip("rRbBuUfFtT")
```
L1310  ⚪  (score=0)
```python
    is_single_quoted: cython.bint = len(quotes) != 3
```
L1311  ⚪  (score=0)
```python
    middles = p_ft_string_middles(s, is_raw, is_single_quoted, is_format_string=False, tf_string_kind=tf_string_kind)
```
L1312  ⚪  (score=0)
```python
    if s.sy != "END_FT_STRING":
```
L1313  ⚪  (score=0)
```python
        s.expected(quotes)
```
L1314  ⚪  (score=0)
```python
    s.next()
```
L1315  ⚪  (score=0)
```python
    return tf_string_kind, None, middles
```
L1316  ⚪  (score=0)
```python
```
L1317  ⚪  (score=0)
```python
```
L1318  ⚪  (score=0)
```python
@cython.cfunc
```
L1319  ⚪  (score=0)
```python
def _append_escape_sequence(kind, builder, escape_sequence: str, s: PyrexScanner):
```
L1320  ⚪  (score=0)
```python
    if len(escape_sequence) < 2:
```
L1321  ⚪  (score=0)
```python
        builder.append("\\")  # invalid escape sequence, warned earlier
```
L1322  ⚪  (score=0)
```python
        return
```
L1323  ⚪  (score=0)
```python
    c = escape_sequence[1]
```
L1324  ⚪  (score=0)
```python
    if c in "01234567":
```
L1325  ⚪  (score=0)
```python
        builder.append_charval(int(escape_sequence[1:], 8))
```
L1326  ⚪  (score=0)
```python
    elif c in "'\"\\":
```
L1327  ⚪  (score=0)
```python
        builder.append(c)
```
L1328  ⚪  (score=0)
```python
    elif c in "abfnrtv":
```
L1329  ⚪  (score=0)
```python
        builder.append(StringEncoding.char_from_escape_sequence(escape_sequence))
```
L1330  ⚪  (score=0)
```python
    elif c == '\n':
```
L1331  ⚪  (score=0)
```python
        pass  # line continuation
```
L1332  ⚪  (score=0)
```python
    elif c == 'x':  # \xXX
```
L1333  ⚪  (score=0)
```python
        if len(escape_sequence) == 4:
```
L1334  ⚪  (score=0)
```python
            builder.append_charval(int(escape_sequence[2:], 16))
```
L1335  ⚪  (score=0)
```python
        else:
```
L1336  ⚪  (score=0)
```python
            s.error("Invalid hex escape '%s'" % escape_sequence, fatal=False)
```
L1337  ⚪  (score=0)
```python
    elif c in 'NUu' and kind in ('u', 'f', ''):  # \uxxxx, \Uxxxxxxxx, \N{...}
```
L1338  ⚪  (score=0)
```python
        chrval = -1
```
L1339  ⚪  (score=0)
```python
        if c == 'N':
```
L1340  ⚪  (score=0)
```python
            uchar = None
```
L1341  ⚪  (score=0)
```python
            try:
```
L1342  ⚪  (score=0)
```python
                name_slice = escape_sequence[3:len(escape_sequence) - 1]
```
L1343  ⚪  (score=0)
```python
                uchar = lookup_unicodechar(name_slice)
```
L1344  ⚪  (score=0)
```python
                chrval = ord(uchar)
```
L1345  ⚪  (score=0)
```python
            except KeyError:
```
L1346  ⚪  (score=0)
```python
                s.error("Unknown Unicode character name %s" %
```
L1347  ⚪  (score=0)
```python
                        repr(name_slice).lstrip('u'), fatal=False)
```
L1348  ⚪  (score=0)
```python
        elif len(escape_sequence) in (6, 10):
```
L1349  ⚪  (score=0)
```python
            chrval = int(escape_sequence[2:], 16)
```
L1350  ⚪  (score=0)
```python
            if chrval > 1114111:  # sys.maxunicode:
```
L1351  ⚪  (score=0)
```python
                s.error("Invalid unicode escape '%s'" % escape_sequence)
```
L1352  ⚪  (score=0)
```python
                chrval = -1
```
L1353  ⚪  (score=0)
```python
        else:
```
L1354  ⚪  (score=0)
```python
            s.error("Invalid unicode escape '%s'" % escape_sequence, fatal=False)
```
L1355  ⚪  (score=0)
```python
        if chrval >= 0:
```
L1356  ⚪  (score=0)
```python
            builder.append_uescape(chrval, escape_sequence)
```
L1357  ⚪  (score=0)
```python
    else:
```
L1358  ⚪  (score=0)
```python
        builder.append(escape_sequence)
```
L1359  ⚪  (score=0)
```python
```
L1360  ⚪  (score=0)
```python
```
L1361  ⚪  (score=0)
```python
# since PEP 448:
```
L1362  ⚪  (score=0)
```python
# list_display  ::=     "[" [listmaker] "]"
```
L1363  ⚪  (score=0)
```python
# listmaker     ::=     (named_test|star_expr) ( comp_for | (',' (named_test|star_expr))* [','] )
```
L1364  ⚪  (score=0)
```python
# comp_iter     ::=     comp_for | comp_if
```
L1365  ⚪  (score=0)
```python
# comp_for      ::=     ["async"] "for" expression_list "in" testlist [comp_iter]
```
L1366  ⚪  (score=0)
```python
# comp_if       ::=     "if" test [comp_iter]
```
L1367  ⚪  (score=0)
```python
```
L1368  ⚪  (score=0)
```python
@cython.cfunc
```
L1369  ⚪  (score=0)
```python
def p_list_maker(s: PyrexScanner):
```
L1370  ⚪  (score=0)
```python
    # s.sy == '['
```
L1371  ⚪  (score=0)
```python
    pos = s.position()
```
L1372  ⚪  (score=0)
```python
    s.next()
```
L1373  ⚪  (score=0)
```python
    if s.sy == ']':
```
L1374  ⚪  (score=0)
```python
        s.expect(']')
```
L1375  ⚪  (score=0)
```python
        return ExprNodes.ListNode(pos, args=[])
```
L1376  ⚪  (score=0)
```python
```
L1377  ⚪  (score=0)
```python
    expr = p_namedexpr_test_or_starred_expr(s)
```
L1378  ⚪  (score=0)
```python
    if s.sy in ('for', 'async'):
```
L1379  ⚪  (score=0)
```python
        if expr.is_starred:
```
L1380  ⚪  (score=0)
```python
            s.error("iterable unpacking cannot be used in comprehension")
```
L1381  ⚪  (score=0)
```python
        append = ExprNodes.ComprehensionAppendNode(pos, expr=expr)
```
L1382  ⚪  (score=0)
```python
        loop = p_comp_for(s, append)
```
L1383  ⚪  (score=0)
```python
        s.expect(']')
```
L1384  ⚪  (score=0)
```python
        return ExprNodes.ComprehensionNode(
```
L1385  ⚪  (score=0)
```python
            pos, loop=loop, append=append, type=Builtin.list_type,
```
L1386  ⚪  (score=0)
```python
            # list comprehensions leak their loop variable in Py2
```
L1387  ⚪  (score=0)
```python
            has_local_scope=s.context.language_level >= 3)
```
L1388  ⚪  (score=0)
```python
```
L1389  ⚪  (score=0)
```python
    # (merged) list literal
```
L1390  ⚪  (score=0)
```python
    if s.sy == ',':
```
L1391  ⚪  (score=0)
```python
        s.next()
```
L1392  ⚪  (score=0)
```python
        exprs = p_namedexpr_test_or_starred_expr_list(s, expr)
```
L1393  ⚪  (score=0)
```python
    else:
```
L1394  ⚪  (score=0)
```python
        exprs = [expr]
```
L1395  ⚪  (score=0)
```python
    s.expect(']')
```
L1396  ⚪  (score=0)
```python
    return ExprNodes.ListNode(pos, args=exprs)
```
L1397  ⚪  (score=0)
```python
```
L1398  ⚪  (score=0)
```python
```
L1399  ⚪  (score=0)
```python
@cython.cfunc
```
L1400  ⚪  (score=0)
```python
def p_comp_iter(s: PyrexScanner, body):
```
L1401  ⚪  (score=0)
```python
    if s.sy in ('for', 'async'):
```
L1402  ⚪  (score=0)
```python
        return p_comp_for(s, body)
```
L1403  ⚪  (score=0)
```python
    elif s.sy == 'if':
```
L1404  ⚪  (score=0)
```python
        return p_comp_if(s, body)
```
L1405  ⚪  (score=0)
```python
    else:
```
L1406  ⚪  (score=0)
```python
        # insert the 'append' operation into the loop
```
L1407  ⚪  (score=0)
```python
        return body
```
L1408  ⚪  (score=0)
```python
```
L1409  ⚪  (score=0)
```python
```
L1410  ⚪  (score=0)
```python
@cython.cfunc
```
L1411  ⚪  (score=0)
```python
def p_comp_for(s: PyrexScanner, body):
```
L1412  ⚪  (score=0)
```python
    pos = s.position()
```
L1413  ⚪  (score=0)
```python
    # [async] for ...
```
L1414  ⚪  (score=0)
```python
    is_async = False
```
L1415  ⚪  (score=0)
```python
    if s.sy == 'async':
```
L1416  ⚪  (score=0)
```python
        is_async = True
```
L1417  ⚪  (score=0)
```python
        s.next()
```
L1418  ⚪  (score=0)
```python
```
L1419  ⚪  (score=0)
```python
    # s.sy == 'for'
```
L1420  ⚪  (score=0)
```python
    s.expect('for')
```
L1421  ⚪  (score=0)
```python
    kw = p_for_bounds(s, allow_testlist=False, is_async=is_async)
```
L1422  ⚪  (score=0)
```python
    kw.update(else_clause=None, body=p_comp_iter(s, body), is_async=is_async)
```
L1423  ⚪  (score=0)
```python
    return Nodes.ForStatNode(pos, **kw)
```
L1424  ⚪  (score=0)
```python
```
L1425  ⚪  (score=0)
```python
```
L1426  ⚪  (score=0)
```python
@cython.cfunc
```
L1427  ⚪  (score=0)
```python
def p_comp_if(s: PyrexScanner, body):
```
L1428  ⚪  (score=0)
```python
    # s.sy == 'if'
```
L1429  ⚪  (score=0)
```python
    pos = s.position()
```
L1430  ⚪  (score=0)
```python
    s.next()
```
L1431  ⚪  (score=0)
```python
    # Note that Python 3.9+ is actually more restrictive here and Cython now follows
```
L1432  ⚪  (score=0)
```python
    # the Python 3.9+ behaviour: https://github.com/python/cpython/issues/86014
```
L1433  ⚪  (score=0)
```python
    # On Python <3.9 `[i for i in range(10) if lambda: i if True else 1]` was disallowed
```
L1434  ⚪  (score=0)
```python
    # but `[i for i in range(10) if lambda: i]` was allowed.
```
L1435  ⚪  (score=0)
```python
    # On Python >=3.9 they're both disallowed.
```
L1436  ⚪  (score=0)
```python
    test = p_or_test(s)
```
L1437  ⚪  (score=0)
```python
    return Nodes.IfStatNode(pos,
```
L1438  ⚪  (score=0)
```python
        if_clauses = [Nodes.IfClauseNode(pos, condition = test,
```
L1439  ⚪  (score=0)
```python
                                         body = p_comp_iter(s, body))],
```
L1440  ⚪  (score=0)
```python
        else_clause = None )
```
L1441  ⚪  (score=0)
```python
```
L1442  ⚪  (score=0)
```python
```
L1443  ⚪  (score=0)
```python
# since PEP 448:
```
L1444  ⚪  (score=0)
```python
#dictorsetmaker: ( ((test ':' test | '**' expr)
```
L1445  ⚪  (score=0)
```python
#                   (comp_for | (',' (test ':' test | '**' expr))* [','])) |
```
L1446  ⚪  (score=0)
```python
#                  ((test | star_expr)
```
L1447  ⚪  (score=0)
```python
#                   (comp_for | (',' (test | star_expr))* [','])) )
```
L1448  ⚪  (score=0)
```python
```
L1449  ⚪  (score=0)
```python
@cython.cfunc
```
L1450  ⚪  (score=0)
```python
def p_dict_or_set_maker(s: PyrexScanner):
```
L1451  ⚪  (score=0)
```python
    # s.sy == '{'
```
L1452  ⚪  (score=0)
```python
    pos = s.position()
```
L1453  ⚪  (score=0)
```python
    s.next()
```
L1454  ⚪  (score=0)
```python
    if s.sy == '}':
```
L1455  ⚪  (score=0)
```python
        s.next()
```
L1456  ⚪  (score=0)
```python
        return ExprNodes.DictNode(pos, key_value_pairs=[])
```
L1457  ⚪  (score=0)
```python
```
L1458  ⚪  (score=0)
```python
    parts = []
```
L1459  ⚪  (score=0)
```python
    target_type: cython.int = 0
```
L1460  ⚪  (score=0)
```python
    last_was_simple_item = False
```
L1461  ⚪  (score=0)
```python
    while True:
```
L1462  ⚪  (score=0)
```python
        if s.sy in ('*', '**'):
```
L1463  ⚪  (score=0)
```python
            # merged set/dict literal
```
L1464  ⚪  (score=0)
```python
            if target_type == 0:
```
L1465  ⚪  (score=0)
```python
                target_type = 1 if s.sy == '*' else 2  # 'stars'
```
L1466  ⚪  (score=0)
```python
            elif target_type != len(s.sy):
```
L1467  ⚪  (score=0)
```python
                s.error("unexpected %sitem found in %s literal" % (
```
L1468  ⚪  (score=0)
```python
                    s.sy, 'set' if target_type == 1 else 'dict'))
```
L1469  ⚪  (score=0)
```python
            s.next()
```
L1470  ⚪  (score=0)
```python
            if s.sy == '*':
```
L1471  ⚪  (score=0)
```python
                s.error("expected expression, found '*'")
```
L1472  ⚪  (score=0)
```python
            item = p_starred_expr(s)
```
L1473  ⚪  (score=0)
```python
            parts.append(item)
```
L1474  ⚪  (score=0)
```python
            last_was_simple_item = False
```
L1475  ⚪  (score=0)
```python
        else:
```
L1476  ⚪  (score=0)
```python
            item = p_test(s)
```
L1477  ⚪  (score=0)
```python
            if target_type == 0:
```
L1478  ⚪  (score=0)
```python
                target_type = 2 if s.sy == ':' else 1  # dict vs. set
```
L1479  ⚪  (score=0)
```python
            if target_type == 2:
```
L1480  ⚪  (score=0)
```python
                # dict literal
```
L1481  ⚪  (score=0)
```python
                s.expect(':')
```
L1482  ⚪  (score=0)
```python
                key = item
```
L1483  ⚪  (score=0)
```python
                value = p_test(s)
```
L1484  ⚪  (score=0)
```python
                item = ExprNodes.DictItemNode(key.pos, key=key, value=value)
```
L1485  ⚪  (score=0)
```python
            if last_was_simple_item:
```
L1486  ⚪  (score=0)
```python
                parts[len(parts) - 1].append(item)
```
L1487  ⚪  (score=0)
```python
            else:
```
L1488  ⚪  (score=0)
```python
                parts.append([item])
```
L1489  ⚪  (score=0)
```python
                last_was_simple_item = True
```
L1490  ⚪  (score=0)
```python
```
L1491  ⚪  (score=0)
```python
        if s.sy == ',':
```
L1492  ⚪  (score=0)
```python
            s.next()
```
L1493  ⚪  (score=0)
```python
            if s.sy == '}':
```
L1494  ⚪  (score=0)
```python
                break
```
L1495  ⚪  (score=0)
```python
        else:
```
L1496  ⚪  (score=0)
```python
            break
```
L1497  ⚪  (score=0)
```python
```
L1498  ⚪  (score=0)
```python
    if s.sy in ('for', 'async'):
```
L1499  ⚪  (score=0)
```python
        # dict/set comprehension
```
L1500  ⚪  (score=0)
```python
        if len(parts) == 1 and isinstance(parts[0], list) and len(parts[0]) == 1:
```
L1501  ⚪  (score=0)
```python
            item = parts[0][0]
```
L1502  ⚪  (score=0)
```python
            if target_type == 2:
```
L1503  ⚪  (score=0)
```python
                assert isinstance(item, ExprNodes.DictItemNode), type(item)
```
L1504  ⚪  (score=0)
```python
                comprehension_type = Builtin.dict_type
```
L1505  ⚪  (score=0)
```python
                append = ExprNodes.DictComprehensionAppendNode(
```
L1506  ⚪  (score=0)
```python
                    item.pos, key_expr=item.key, value_expr=item.value)
```
L1507  ⚪  (score=0)
```python
            else:
```
L1508  ⚪  (score=0)
```python
                comprehension_type = Builtin.set_type
```
L1509  ⚪  (score=0)
```python
                append = ExprNodes.ComprehensionAppendNode(item.pos, expr=item)
```
L1510  ⚪  (score=0)
```python
            loop = p_comp_for(s, append)
```
L1511  ⚪  (score=0)
```python
            s.expect('}')
```
L1512  ⚪  (score=0)
```python
            return ExprNodes.ComprehensionNode(pos, loop=loop, append=append, type=comprehension_type)
```
L1513  ⚪  (score=0)
```python
        else:
```
L1514  ⚪  (score=0)
```python
            # syntax error, try to find a good error message
```
L1515  ⚪  (score=0)
```python
            if len(parts) == 1 and not isinstance(parts[0], list):
```
L1516  ⚪  (score=0)
```python
                s.error("iterable unpacking cannot be used in comprehension")
```
L1517  ⚪  (score=0)
```python
            else:
```
L1518  ⚪  (score=0)
```python
                # e.g. "{1,2,3 for ..."
```
L1519  ⚪  (score=0)
```python
                s.expect('}')
```
L1520  ⚪  (score=0)
```python
            return ExprNodes.DictNode(pos, key_value_pairs=[])
```
L1521  ⚪  (score=0)
```python
```
L1522  ⚪  (score=0)
```python
    s.expect('}')
```
L1523  ⚪  (score=0)
```python
    if target_type == 1:
```
L1524  ⚪  (score=0)
```python
        # (merged) set literal
```
L1525  ⚪  (score=0)
```python
        items = []
```
L1526  ⚪  (score=0)
```python
        set_items = []
```
L1527  ⚪  (score=0)
```python
        for part in parts:
```
L1528  ⚪  (score=0)
```python
            if isinstance(part, list):
```
L1529  ⚪  (score=0)
```python
                set_items.extend(part)
```
L1530  ⚪  (score=0)
```python
            else:
```
L1531  ⚪  (score=0)
```python
                if set_items:
```
L1532  ⚪  (score=0)
```python
                    items.append(ExprNodes.SetNode(set_items[0].pos, args=set_items))
```
L1533  ⚪  (score=0)
```python
                    set_items = []
```
L1534  ⚪  (score=0)
```python
                items.append(part)
```
L1535  ⚪  (score=0)
```python
        if set_items:
```
L1536  ⚪  (score=0)
```python
            items.append(ExprNodes.SetNode(set_items[0].pos, args=set_items))
```
L1537  ⚪  (score=0)
```python
        if len(items) == 1 and items[0].is_set_literal:
```
L1538  ⚪  (score=0)
```python
            return items[0]
```
L1539  ⚪  (score=0)
```python
        return ExprNodes.MergedSequenceNode(pos, args=items, type=Builtin.set_type)
```
L1540  ⚪  (score=0)
```python
    else:
```
L1541  ⚪  (score=0)
```python
        # (merged) dict literal
```
L1542  ⚪  (score=0)
```python
        items = []
```
L1543  ⚪  (score=0)
```python
        dict_items = []
```
L1544  ⚪  (score=0)
```python
        for part in parts:
```
L1545  ⚪  (score=0)
```python
            if isinstance(part, list):
```
L1546  ⚪  (score=0)
```python
                dict_items.extend(part)
```
L1547  ⚪  (score=0)
```python
            else:
```
L1548  ⚪  (score=0)
```python
                if dict_items:
```
L1549  ⚪  (score=0)
```python
                    items.append(ExprNodes.DictNode(dict_items[0].pos, key_value_pairs=dict_items))
```
L1550  ⚪  (score=0)
```python
                    dict_items = []
```
L1551  ⚪  (score=0)
```python
                items.append(part)
```
L1552  ⚪  (score=0)
```python
        if dict_items:
```
L1553  ⚪  (score=0)
```python
            items.append(ExprNodes.DictNode(dict_items[0].pos, key_value_pairs=dict_items))
```
L1554  ⚪  (score=0)
```python
        if len(items) == 1 and items[0].is_dict_literal:
```
L1555  ⚪  (score=0)
```python
            return items[0]
```
L1556  ⚪  (score=0)
```python
        return ExprNodes.MergedDictNode(pos, keyword_args=items, reject_duplicates=False)
```
L1557  ⚪  (score=0)
```python
```
L1558  ⚪  (score=0)
```python
```
L1559  ⚪  (score=0)
```python
# NOTE: no longer in Py3 :)
```
L1560  ⚪  (score=0)
```python
@cython.cfunc
```
L1561  ⚪  (score=0)
```python
def p_backquote_expr(s: PyrexScanner):
```
L1562  ⚪  (score=0)
```python
    # s.sy == '`'
```
L1563  ⚪  (score=0)
```python
    pos = s.position()
```
L1564  ⚪  (score=0)
```python
    s.next()
```
L1565  ⚪  (score=0)
```python
    args = [p_test(s)]
```
L1566  ⚪  (score=0)
```python
    while s.sy == ',':
```
L1567  ⚪  (score=0)
```python
        s.next()
```
L1568  ⚪  (score=0)
```python
        args.append(p_test(s))
```
L1569  ⚪  (score=0)
```python
    s.expect('`')
```
L1570  ⚪  (score=0)
```python
    if len(args) == 1:
```
L1571  ⚪  (score=0)
```python
        arg = args[0]
```
L1572  ⚪  (score=0)
```python
    else:
```
L1573  ⚪  (score=0)
```python
        arg = ExprNodes.TupleNode(pos, args = args)
```
L1574  ⚪  (score=0)
```python
    return ExprNodes.BackquoteNode(pos, arg = arg)
```
L1575  ⚪  (score=0)
```python
```
L1576  ⚪  (score=0)
```python
```
L1577  ⚪  (score=0)
```python
@cython.cfunc
```
L1578  ⚪  (score=0)
```python
def p_simple_expr_list(s: PyrexScanner, expr=None) -> list:
```
L1579  ⚪  (score=0)
```python
    exprs: list = [expr] if expr is not None else []
```
L1580  ⚪  (score=0)
```python
    while s.sy not in expr_terminators:
```
L1581  ⚪  (score=0)
```python
        exprs.append( p_test(s) )
```
L1582  ⚪  (score=0)
```python
        if s.sy != ',':
```
L1583  ⚪  (score=0)
```python
            break
```
L1584  ⚪  (score=0)
```python
        s.next()
```
L1585  ⚪  (score=0)
```python
    return exprs
```
L1586  ⚪  (score=0)
```python
```
L1587  ⚪  (score=0)
```python
```
L1588  ⚪  (score=0)
```python
@cython.cfunc
```
L1589  ⚪  (score=0)
```python
def p_test_or_starred_expr_list(s: PyrexScanner, expr=None) -> list:
```
L1590  ⚪  (score=0)
```python
    exprs: list = [expr] if expr is not None else []
```
L1591  ⚪  (score=0)
```python
    while s.sy not in expr_terminators:
```
L1592  ⚪  (score=0)
```python
        exprs.append(p_test_or_starred_expr(s))
```
L1593  ⚪  (score=0)
```python
        if s.sy != ',':
```
L1594  ⚪  (score=0)
```python
            break
```
L1595  ⚪  (score=0)
```python
        s.next()
```
L1596  ⚪  (score=0)
```python
    return exprs
```
L1597  ⚪  (score=0)
```python
```
L1598  ⚪  (score=0)
```python
```
L1599  ⚪  (score=0)
```python
@cython.cfunc
```
L1600  ⚪  (score=0)
```python
def p_namedexpr_test_or_starred_expr_list(s: PyrexScanner, expr=None) -> list:
```
L1601  ⚪  (score=0)
```python
    exprs: list = [expr] if expr is not None else []
```
L1602  ⚪  (score=0)
```python
    while s.sy not in expr_terminators:
```
L1603  ⚪  (score=0)
```python
        exprs.append(p_namedexpr_test_or_starred_expr(s))
```
L1604  ⚪  (score=0)
```python
        if s.sy != ',':
```
L1605  ⚪  (score=0)
```python
            break
```
L1606  ⚪  (score=0)
```python
        s.next()
```
L1607  ⚪  (score=0)
```python
    return exprs
```
L1608  ⚪  (score=0)
```python
```
L1609  ⚪  (score=0)
```python
```
L1610  ⚪  (score=0)
```python
#testlist: test (',' test)* [',']
```
L1611  ⚪  (score=0)
```python
```
L1612  ⚪  (score=0)
```python
@cython.cfunc
```
L1613  ⚪  (score=0)
```python
def p_testlist(s: PyrexScanner):
```
L1614  ⚪  (score=0)
```python
    pos = s.position()
```
L1615  ⚪  (score=0)
```python
    expr = p_test(s)
```
L1616  ⚪  (score=0)
```python
    if s.sy == ',':
```
L1617  ⚪  (score=0)
```python
        s.next()
```
L1618  ⚪  (score=0)
```python
        exprs = p_simple_expr_list(s, expr)
```
L1619  ⚪  (score=0)
```python
        return ExprNodes.TupleNode(pos, args = exprs)
```
L1620  ⚪  (score=0)
```python
    else:
```
L1621  ⚪  (score=0)
```python
        return expr
```
L1622  ⚪  (score=0)
```python
```
L1623  ⚪  (score=0)
```python
```
L1624  ⚪  (score=0)
```python
# testlist_star_expr: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )
```
L1625  ⚪  (score=0)
```python
```
L1626  ⚪  (score=0)
```python
@cython.cfunc
```
L1627  ⚪  (score=0)
```python
def p_testlist_star_expr(s: PyrexScanner):
```
L1628  ⚪  (score=0)
```python
    pos = s.position()
```
L1629  ⚪  (score=0)
```python
    expr = p_test_or_starred_expr(s)
```
L1630  ⚪  (score=0)
```python
    if s.sy == ',':
```
L1631  ⚪  (score=0)
```python
        s.next()
```
L1632  ⚪  (score=0)
```python
        exprs = p_test_or_starred_expr_list(s, expr)
```
L1633  ⚪  (score=0)
```python
        return ExprNodes.TupleNode(pos, args = exprs)
```
L1634  ⚪  (score=0)
```python
    else:
```
L1635  ⚪  (score=0)
```python
        return expr
```
L1636  ⚪  (score=0)
```python
```
L1637  ⚪  (score=0)
```python
```
L1638  ⚪  (score=0)
```python
# testlist_comp: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )
```
L1639  ⚪  (score=0)
```python
```
L1640  ⚪  (score=0)
```python
@cython.cfunc
```
L1641  ⚪  (score=0)
```python
def p_testlist_comp(s: PyrexScanner):
```
L1642  ⚪  (score=0)
```python
    pos = s.position()
```
L1643  ⚪  (score=0)
```python
    expr = p_namedexpr_test_or_starred_expr(s)
```
L1644  ⚪  (score=0)
```python
    if s.sy == ',':
```
L1645  ⚪  (score=0)
```python
        s.next()
```
L1646  ⚪  (score=0)
```python
        exprs = p_namedexpr_test_or_starred_expr_list(s, expr)
```
L1647  ⚪  (score=0)
```python
        return ExprNodes.TupleNode(pos, args = exprs)
```
L1648  ⚪  (score=0)
```python
    elif s.sy in ('for', 'async'):
```
L1649  ⚪  (score=0)
```python
        return p_genexp(s, expr)
```
L1650  ⚪  (score=0)
```python
    else:
```
L1651  ⚪  (score=0)
```python
        return expr
```
L1652  ⚪  (score=0)
```python
```
L1653  ⚪  (score=0)
```python
```
L1654  ⚪  (score=0)
```python
@cython.cfunc
```
L1655  ⚪  (score=0)
```python
def p_genexp(s: PyrexScanner, expr):
```
L1656  ⚪  (score=0)
```python
    # s.sy == 'async' | 'for'
```
L1657  ⚪  (score=0)
```python
    loop = p_comp_for(s, Nodes.ExprStatNode(
```
L1658  ⚪  (score=0)
```python
        expr.pos, expr = ExprNodes.YieldExprNode(expr.pos, arg=expr)))
```
L1659  ⚪  (score=0)
```python
    return ExprNodes.GeneratorExpressionNode(expr.pos, loop=loop)
```
L1660  ⚪  (score=0)
```python
```
L1661  ⚪  (score=0)
```python
```
L1662  ⚪  (score=0)
```python
expr_terminators = cython.declare(frozenset, frozenset((
```
L1663  ⚪  (score=0)
```python
    ')', ']', '}', ':', '=', 'NEWLINE', 'EOF')))
```
L1664  ⚪  (score=0)
```python
```
L1665  ⚪  (score=0)
```python
```
L1666  ⚪  (score=0)
```python
#-------------------------------------------------------
```
L1667  ⚪  (score=0)
```python
#
```
L1668  ⚪  (score=0)
```python
#   Statements
```
L1669  ⚪  (score=0)
```python
#
```
L1670  ⚪  (score=0)
```python
#-------------------------------------------------------
```
L1671  ⚪  (score=0)
```python
```
L1672  ⚪  (score=0)
```python
@cython.cfunc
```
L1673  ⚪  (score=0)
```python
def p_global_statement(s: PyrexScanner):
```
L1674  ⚪  (score=0)
```python
    # assume s.sy == 'global'
```
L1675  ⚪  (score=0)
```python
    pos = s.position()
```
L1676  ⚪  (score=0)
```python
    s.next()
```
L1677  ⚪  (score=0)
```python
    names = p_ident_list(s)
```
L1678  ⚪  (score=0)
```python
    return Nodes.GlobalNode(pos, names = names)
```
L1679  ⚪  (score=0)
```python
```
L1680  ⚪  (score=0)
```python
```
L1681  ⚪  (score=0)
```python
@cython.cfunc
```
L1682  ⚪  (score=0)
```python
def p_nonlocal_statement(s: PyrexScanner):
```
L1683  ⚪  (score=0)
```python
    pos = s.position()
```
L1684  ⚪  (score=0)
```python
    s.next()
```
L1685  ⚪  (score=0)
```python
    names = p_ident_list(s)
```
L1686  ⚪  (score=0)
```python
    return Nodes.NonlocalNode(pos, names = names)
```
L1687  ⚪  (score=0)
```python
```
L1688  ⚪  (score=0)
```python
```
L1689  ⚪  (score=0)
```python
@cython.cfunc
```
L1690  ⚪  (score=0)
```python
def p_expression_or_assignment(s: PyrexScanner):
```
L1691  ⚪  (score=0)
```python
    expr = p_testlist_star_expr(s)
```
L1692  ⚪  (score=0)
```python
    has_annotation = False
```
L1693  ⚪  (score=0)
```python
    if s.sy == ':' and (expr.is_name or expr.is_subscript or expr.is_attribute):
```
L1694  ⚪  (score=0)
```python
        has_annotation = True
```
L1695  ⚪  (score=0)
```python
        s.next()
```
L1696  ⚪  (score=0)
```python
        expr.annotation = p_annotation(s)
```
L1697  ⚪  (score=0)
```python
```
L1698  ⚪  (score=0)
```python
    if s.sy == '=' and expr.is_starred:
```
L1699  ⚪  (score=0)
```python
        # This is a common enough error to make when learning Cython to let
```
L1700  ⚪  (score=0)
```python
        # it fail as early as possible and give a very clear error message.
```
L1701  ⚪  (score=0)
```python
        s.error("a starred assignment target must be in a list or tuple"
```
L1702  ⚪  (score=0)
```python
                " - maybe you meant to use an index assignment: var[0] = ...",
```
L1703  ⚪  (score=0)
```python
                pos=expr.pos)
```
L1704  ⚪  (score=0)
```python
```
L1705  ⚪  (score=0)
```python
    expr_list = [expr]
```
L1706  ⚪  (score=0)
```python
    while s.sy == '=':
```
L1707  ⚪  (score=0)
```python
        s.next()
```
L1708  ⚪  (score=0)
```python
        if s.sy == 'yield':
```
L1709  ⚪  (score=0)
```python
            expr = p_yield_expression(s)
```
L1710  ⚪  (score=0)
```python
        else:
```
L1711  ⚪  (score=0)
```python
            expr = p_testlist_star_expr(s)
```
L1712  ⚪  (score=0)
```python
        expr_list.append(expr)
```
L1713  ⚪  (score=0)
```python
    if len(expr_list) == 1:
```
L1714  ⚪  (score=0)
```python
        if re.match(r"([-+*/%^&|]|<<|>>|\*\*|//|@)=", s.sy):
```
L1715  ⚪  (score=0)
```python
            lhs = expr_list[0]
```
L1716  ⚪  (score=0)
```python
            if isinstance(lhs, ExprNodes.SliceIndexNode):
```
L1717  ⚪  (score=0)
```python
                # implementation requires IndexNode
```
L1718  ⚪  (score=0)
```python
                lhs = ExprNodes.IndexNode(
```
L1719  ⚪  (score=0)
```python
                    lhs.pos,
```
L1720  ⚪  (score=0)
```python
                    base=lhs.base,
```
L1721  ⚪  (score=0)
```python
                    index=make_slice_node(lhs.pos, lhs.start, lhs.stop))
```
L1722  ⚪  (score=0)
```python
            elif not isinstance(lhs, (ExprNodes.AttributeNode, ExprNodes.IndexNode, ExprNodes.NameNode)):
```
L1723  ⚪  (score=0)
```python
                error(lhs.pos, "Illegal operand for inplace operation.")
```
L1724  ⚪  (score=0)
```python
            op_text = s.sy
```
L1725  ⚪  (score=0)
```python
            operator = op_text[:len(op_text) - 1]
```
L1726  ⚪  (score=0)
```python
            s.next()
```
L1727  ⚪  (score=0)
```python
            if s.sy == 'yield':
```
L1728  ⚪  (score=0)
```python
                rhs = p_yield_expression(s)
```
L1729  ⚪  (score=0)
```python
            else:
```
L1730  ⚪  (score=0)
```python
                rhs = p_testlist(s)
```
L1731  ⚪  (score=0)
```python
            return Nodes.InPlaceAssignmentNode(lhs.pos, operator=operator, lhs=lhs, rhs=rhs)
```
L1732  ⚪  (score=0)
```python
        expr = expr_list[0]
```
L1733  ⚪  (score=0)
```python
        return Nodes.ExprStatNode(expr.pos, expr=expr)
```
L1734  ⚪  (score=0)
```python
```
L1735  ⚪  (score=0)
```python
    rhs = expr_list[len(expr_list) - 1]
```
L1736  ⚪  (score=0)
```python
    if len(expr_list) == 2:
```
L1737  ⚪  (score=0)
```python
        return Nodes.SingleAssignmentNode(rhs.pos, lhs=expr_list[0], rhs=rhs, first=has_annotation)
```
L1738  ⚪  (score=0)
```python
    else:
```
L1739  ⚪  (score=0)
```python
        return Nodes.CascadedAssignmentNode(rhs.pos, lhs_list=expr_list[:len(expr_list) - 1], rhs=rhs)
```
L1740  ⚪  (score=0)
```python
```
L1741  ⚪  (score=0)
```python
```
L1742  ⚪  (score=0)
```python
@cython.cfunc
```
L1743  ⚪  (score=0)
```python
def p_print_statement(s: PyrexScanner):
```
L1744  ⚪  (score=0)
```python
    # s.sy == 'print'
```
L1745  ⚪  (score=0)
```python
    pos = s.position()
```
L1746  ⚪  (score=0)
```python
    ends_with_comma: cython.bint = False
```
L1747  ⚪  (score=0)
```python
    s.next()
```
L1748  ⚪  (score=0)
```python
    if s.sy == '>>':
```
L1749  ⚪  (score=0)
```python
        s.next()
```
L1750  ⚪  (score=0)
```python
        stream = p_test(s)
```
L1751  ⚪  (score=0)
```python
        if s.sy == ',':
```
L1752  ⚪  (score=0)
```python
            s.next()
```
L1753  ⚪  (score=0)
```python
            ends_with_comma = s.sy in ('NEWLINE', 'EOF')
```
L1754  ⚪  (score=0)
```python
    else:
```
L1755  ⚪  (score=0)
```python
        stream = None
```
L1756  ⚪  (score=0)
```python
    args = []
```
L1757  ⚪  (score=0)
```python
    if s.sy not in ('NEWLINE', 'EOF'):
```
L1758  ⚪  (score=0)
```python
        args.append(p_test(s))
```
L1759  ⚪  (score=0)
```python
        while s.sy == ',':
```
L1760  ⚪  (score=0)
```python
            s.next()
```
L1761  ⚪  (score=0)
```python
            if s.sy in ('NEWLINE', 'EOF'):
```
L1762  ⚪  (score=0)
```python
                ends_with_comma = True
```
L1763  ⚪  (score=0)
```python
                break
```
L1764  ⚪  (score=0)
```python
            args.append(p_test(s))
```
L1765  ⚪  (score=0)
```python
    arg_tuple = ExprNodes.TupleNode(pos, args=args)
```
L1766  ⚪  (score=0)
```python
    return Nodes.PrintStatNode(pos,
```
L1767  ⚪  (score=0)
```python
        arg_tuple=arg_tuple, stream=stream,
```
L1768  ⚪  (score=0)
```python
        append_newline=not ends_with_comma)
```
L1769  ⚪  (score=0)
```python
```
L1770  ⚪  (score=0)
```python
```
L1771  ⚪  (score=0)
```python
@cython.cfunc
```
L1772  ⚪  (score=0)
```python
def p_exec_statement(s: PyrexScanner):
```
L1773  ⚪  (score=0)
```python
    # s.sy == 'exec'
```
L1774  ⚪  (score=0)
```python
    pos = s.position()
```
L1775  ⚪  (score=0)
```python
    s.next()
```
L1776  ⚪  (score=0)
```python
    code = p_bit_expr(s)
```
L1777  ⚪  (score=0)
```python
    if isinstance(code, ExprNodes.TupleNode):
```
L1778  ⚪  (score=0)
```python
        # Py3 compatibility syntax
```
L1779  ⚪  (score=0)
```python
        tuple_variant = True
```
L1780  ⚪  (score=0)
```python
        args = code.args
```
L1781  ⚪  (score=0)
```python
        if len(args) not in (2, 3):
```
L1782  ⚪  (score=0)
```python
            s.error("expected tuple of length 2 or 3, got length %d" % len(args),
```
L1783  ⚪  (score=0)
```python
                    pos=pos, fatal=False)
```
L1784  ⚪  (score=0)
```python
            args = [code]
```
L1785  ⚪  (score=0)
```python
    else:
```
L1786  ⚪  (score=0)
```python
        tuple_variant = False
```
L1787  ⚪  (score=0)
```python
        args = [code]
```
L1788  ⚪  (score=0)
```python
    if s.sy == 'in':
```
L1789  ⚪  (score=0)
```python
        if tuple_variant:
```
L1790  ⚪  (score=0)
```python
            s.error("tuple variant of exec does not support additional 'in' arguments",
```
L1791  ⚪  (score=0)
```python
                    fatal=False)
```
L1792  ⚪  (score=0)
```python
        s.next()
```
L1793  ⚪  (score=0)
```python
        args.append(p_test(s))
```
L1794  ⚪  (score=0)
```python
        if s.sy == ',':
```
L1795  ⚪  (score=0)
```python
            s.next()
```
L1796  ⚪  (score=0)
```python
            args.append(p_test(s))
```
L1797  ⚪  (score=0)
```python
    return Nodes.ExecStatNode(pos, args=args)
```
L1798  ⚪  (score=0)
```python
```
L1799  ⚪  (score=0)
```python
```
L1800  ⚪  (score=0)
```python
@cython.cfunc
```
L1801  ⚪  (score=0)
```python
def p_del_statement(s: PyrexScanner):
```
L1802  ⚪  (score=0)
```python
    # s.sy == 'del'
```
L1803  ⚪  (score=0)
```python
    pos = s.position()
```
L1804  ⚪  (score=0)
```python
    s.next()
```
L1805  ⚪  (score=0)
```python
    # FIXME: 'exprlist' in Python
```
L1806  ⚪  (score=0)
```python
    args = p_simple_expr_list(s)
```
L1807  ⚪  (score=0)
```python
    return Nodes.DelStatNode(pos, args = args)
```
L1808  ⚪  (score=0)
```python
```
L1809  ⚪  (score=0)
```python
```
L1810  ⚪  (score=0)
```python
@cython.cfunc
```
L1811  ⚪  (score=0)
```python
def p_pass_statement(s: PyrexScanner, with_newline: cython.bint = False):
```
L1812  ⚪  (score=0)
```python
    pos = s.position()
```
L1813  ⚪  (score=0)
```python
    s.expect('pass')
```
L1814  ⚪  (score=0)
```python
    if with_newline:
```
L1815  ⚪  (score=0)
```python
        s.expect_newline("Expected a newline", ignore_semicolon=True)
```
L1816  ⚪  (score=0)
```python
    return Nodes.PassStatNode(pos)
```
L1817  ⚪  (score=0)
```python
```
L1818  ⚪  (score=0)
```python
```
L1819  ⚪  (score=0)
```python
@cython.cfunc
```
L1820  ⚪  (score=0)
```python
def p_break_statement(s: PyrexScanner):
```
L1821  ⚪  (score=0)
```python
    # s.sy == 'break'
```
L1822  ⚪  (score=0)
```python
    pos = s.position()
```
L1823  ⚪  (score=0)
```python
    s.next()
```
L1824  ⚪  (score=0)
```python
    return Nodes.BreakStatNode(pos)
```
L1825  ⚪  (score=0)
```python
```
L1826  ⚪  (score=0)
```python
```
L1827  ⚪  (score=0)
```python
@cython.cfunc
```
L1828  ⚪  (score=0)
```python
def p_continue_statement(s: PyrexScanner):
```
L1829  ⚪  (score=0)
```python
    # s.sy == 'continue'
```
L1830  ⚪  (score=0)
```python
    pos = s.position()
```
L1831  ⚪  (score=0)
```python
    s.next()
```
L1832  ⚪  (score=0)
```python
    return Nodes.ContinueStatNode(pos)
```
L1833  ⚪  (score=0)
```python
```
L1834  ⚪  (score=0)
```python
```
L1835  ⚪  (score=0)
```python
@cython.cfunc
```
L1836  ⚪  (score=0)
```python
def p_return_statement(s: PyrexScanner):
```
L1837  ⚪  (score=0)
```python
    # s.sy == 'return'
```
L1838  ⚪  (score=0)
```python
    pos = s.position()
```
L1839  ⚪  (score=0)
```python
    s.next()
```
L1840  ⚪  (score=0)
```python
    if s.sy not in statement_terminators:
```
L1841  ⚪  (score=0)
```python
        value = p_testlist(s)
```
L1842  ⚪  (score=0)
```python
    else:
```
L1843  ⚪  (score=0)
```python
        value = None
```
L1844  ⚪  (score=0)
```python
    return Nodes.ReturnStatNode(pos, value = value)
```
L1845  ⚪  (score=0)
```python
```
L1846  ⚪  (score=0)
```python
```
L1847  ⚪  (score=0)
```python
@cython.cfunc
```
L1848  ⚪  (score=0)
```python
def p_raise_statement(s: PyrexScanner):
```
L1849  ⚪  (score=0)
```python
    # s.sy == 'raise'
```
L1850  ⚪  (score=0)
```python
    pos = s.position()
```
L1851  ⚪  (score=0)
```python
    s.next()
```
L1852  ⚪  (score=0)
```python
    exc_type = None
```
L1853  ⚪  (score=0)
```python
    exc_value = None
```
L1854  ⚪  (score=0)
```python
    exc_tb = None
```
L1855  ⚪  (score=0)
```python
    cause = None
```
L1856  ⚪  (score=0)
```python
    if s.sy not in statement_terminators:
```
L1857  ⚪  (score=0)
```python
        exc_type = p_test(s)
```
L1858  ⚪  (score=0)
```python
        if s.sy == ',':
```
L1859  ⚪  (score=0)
```python
            s.next()
```
L1860  ⚪  (score=0)
```python
            exc_value = p_test(s)
```
L1861  ⚪  (score=0)
```python
            if s.sy == ',':
```
L1862  ⚪  (score=0)
```python
                s.next()
```
L1863  ⚪  (score=0)
```python
                exc_tb = p_test(s)
```
L1864  ⚪  (score=0)
```python
        elif s.sy == 'from':
```
L1865  ⚪  (score=0)
```python
            s.next()
```
L1866  ⚪  (score=0)
```python
            cause = p_test(s)
```
L1867  ⚪  (score=0)
```python
    if exc_type or exc_value or exc_tb:
```
L1868  ⚪  (score=0)
```python
        return Nodes.RaiseStatNode(pos,
```
L1869  ⚪  (score=0)
```python
            exc_type = exc_type,
```
L1870  ⚪  (score=0)
```python
            exc_value = exc_value,
```
L1871  ⚪  (score=0)
```python
            exc_tb = exc_tb,
```
L1872  ⚪  (score=0)
```python
            cause = cause)
```
L1873  ⚪  (score=0)
```python
    else:
```
L1874  ⚪  (score=0)
```python
        return Nodes.ReraiseStatNode(pos)
```
L1875  ⚪  (score=0)
```python
```
L1876  ⚪  (score=0)
```python
```
L1877  ⚪  (score=0)
```python
@cython.cfunc
```
L1878  ⚪  (score=0)
```python
def p_import_statement(s: PyrexScanner):
```
L1879  ⚪  (score=0)
```python
    # s.sy in ('import', 'cimport')
```
L1880  ⚪  (score=0)
```python
    pos = s.position()
```
L1881  ⚪  (score=0)
```python
    kind = s.sy
```
L1882  ⚪  (score=0)
```python
    s.next()
```
L1883  ⚪  (score=0)
```python
    items = [p_dotted_name(s, as_allowed=True)]
```
L1884  ⚪  (score=0)
```python
    while s.sy == ',':
```
L1885  ⚪  (score=0)
```python
        s.next()
```
L1886  ⚪  (score=0)
```python
        items.append(p_dotted_name(s, as_allowed=True))
```
L1887  ⚪  (score=0)
```python
    stats = []
```
L1888  ⚪  (score=0)
```python
    is_absolute = Future.absolute_import in s.context.future_directives
```
L1889  ⚪  (score=0)
```python
    for pos, target_name, dotted_name, as_name in items:
```
L1890  ⚪  (score=0)
```python
        if kind == 'cimport':
```
L1891  ⚪  (score=0)
```python
            stat = Nodes.CImportStatNode(
```
L1892  ⚪  (score=0)
```python
                pos,
```
L1893  ⚪  (score=0)
```python
                module_name=dotted_name,
```
L1894  ⚪  (score=0)
```python
                as_name=as_name,
```
L1895  ⚪  (score=0)
```python
                is_absolute=is_absolute)
```
L1896  ⚪  (score=0)
```python
        else:
```
L1897  ⚪  (score=0)
```python
            stat = Nodes.SingleAssignmentNode(
```
L1898  ⚪  (score=0)
```python
                pos,
```
L1899  ⚪  (score=0)
```python
                lhs=ExprNodes.NameNode(pos, name=as_name or target_name),
```
L1900  ⚪  (score=0)
```python
                rhs=ExprNodes.ImportNode(
```
L1901  ⚪  (score=0)
```python
                    pos,
```
L1902  ⚪  (score=0)
```python
                    module_name=ExprNodes.IdentifierStringNode(pos, value=dotted_name),
```
L1903  ⚪  (score=0)
```python
                    is_import_as_name=bool(as_name),
```
L1904  ⚪  (score=0)
```python
                    level=0 if is_absolute else None,
```
L1905  ⚪  (score=0)
```python
                    imported_names=None))
```
L1906  ⚪  (score=0)
```python
        stats.append(stat)
```
L1907  ⚪  (score=0)
```python
    return Nodes.StatListNode(pos, stats=stats)
```
L1908  ⚪  (score=0)
```python
```
L1909  ⚪  (score=0)
```python
```
L1910  ⚪  (score=0)
```python
@cython.cfunc
```
L1911  ⚪  (score=0)
```python
def p_from_import_statement(s: PyrexScanner, first_statement: cython.bint = 0):
```
L1912  ⚪  (score=0)
```python
    # s.sy == 'from'
```
L1913  ⚪  (score=0)
```python
    pos = s.position()
```
L1914  ⚪  (score=0)
```python
    s.next()
```
L1915  ⚪  (score=0)
```python
    if s.sy in ('.', '...'):
```
L1916  ⚪  (score=0)
```python
        # count relative import level
```
L1917  ⚪  (score=0)
```python
        level = 0
```
L1918  ⚪  (score=0)
```python
        while s.sy in ('.', '...'):
```
L1919  ⚪  (score=0)
```python
            level += len(s.sy)
```
L1920  ⚪  (score=0)
```python
            s.next()
```
L1921  ⚪  (score=0)
```python
    else:
```
L1922  ⚪  (score=0)
```python
        level = None
```
L1923  ⚪  (score=0)
```python
    if level is not None and s.sy in ('import', 'cimport'):
```
L1924  ⚪  (score=0)
```python
        # we are dealing with "from .. import foo, bar"
```
L1925  ⚪  (score=0)
```python
        dotted_name_pos, dotted_name = s.position(), s.context.intern_ustring('')
```
L1926  ⚪  (score=0)
```python
    else:
```
L1927  ⚪  (score=0)
```python
        if level is None and Future.absolute_import in s.context.future_directives:
```
L1928  ⚪  (score=0)
```python
            level = 0
```
L1929  ⚪  (score=0)
```python
        (dotted_name_pos, _, dotted_name, _) = p_dotted_name(s, as_allowed=False)
```
L1930  ⚪  (score=0)
```python
    if s.sy not in ('import', 'cimport'):
```
L1931  ⚪  (score=0)
```python
        s.error("Expected 'import' or 'cimport'")
```
L1932  ⚪  (score=0)
```python
    kind = s.sy
```
L1933  ⚪  (score=0)
```python
    s.next()
```
L1934  ⚪  (score=0)
```python
```
L1935  ⚪  (score=0)
```python
    is_cimport = kind == 'cimport'
```
L1936  ⚪  (score=0)
```python
    is_parenthesized = False
```
L1937  ⚪  (score=0)
```python
    if s.sy == '*':
```
L1938  ⚪  (score=0)
```python
        imported_names = [(s.position(), s.context.intern_ustring("*"), None)]
```
L1939  ⚪  (score=0)
```python
        s.next()
```
L1940  ⚪  (score=0)
```python
    else:
```
L1941  ⚪  (score=0)
```python
        if s.sy == '(':
```
L1942  ⚪  (score=0)
```python
            is_parenthesized = True
```
L1943  ⚪  (score=0)
```python
            s.next()
```
L1944  ⚪  (score=0)
```python
        imported_names = [p_imported_name(s)]
```
L1945  ⚪  (score=0)
```python
    while s.sy == ',':
```
L1946  ⚪  (score=0)
```python
        s.next()
```
L1947  ⚪  (score=0)
```python
        if is_parenthesized and s.sy == ')':
```
L1948  ⚪  (score=0)
```python
            break
```
L1949  ⚪  (score=0)
```python
        imported_names.append(p_imported_name(s))
```
L1950  ⚪  (score=0)
```python
    if is_parenthesized:
```
L1951  ⚪  (score=0)
```python
        s.expect(')')
```
L1952  ⚪  (score=0)
```python
    if dotted_name == '__future__':
```
L1953  ⚪  (score=0)
```python
        if not first_statement:
```
L1954  ⚪  (score=0)
```python
            s.error("from __future__ imports must occur at the beginning of the file")
```
L1955  ⚪  (score=0)
```python
        elif level:
```
L1956  ⚪  (score=0)
```python
            s.error("invalid syntax")
```
L1957  ⚪  (score=0)
```python
        else:
```
L1958  ⚪  (score=0)
```python
            for (name_pos, name, as_name) in imported_names:
```
L1959  ⚪  (score=0)
```python
                if name == "braces":
```
L1960  ⚪  (score=0)
```python
                    s.error("not a chance", name_pos)
```
L1961  ⚪  (score=0)
```python
                    break
```
L1962  ⚪  (score=0)
```python
                try:
```
L1963  ⚪  (score=0)
```python
                    directive = getattr(Future, name)
```
L1964  ⚪  (score=0)
```python
                except AttributeError:
```
L1965  ⚪  (score=0)
```python
                    s.error("future feature %s is not defined" % name, name_pos)
```
L1966  ⚪  (score=0)
```python
                    break
```
L1967  ⚪  (score=0)
```python
                s.context.future_directives.add(directive)
```
L1968  ⚪  (score=0)
```python
        return Nodes.PassStatNode(pos)
```
L1969  ⚪  (score=0)
```python
    elif is_cimport:
```
L1970  ⚪  (score=0)
```python
        return Nodes.FromCImportStatNode(
```
L1971  ⚪  (score=0)
```python
            pos, module_name=dotted_name,
```
L1972  ⚪  (score=0)
```python
            relative_level=level,
```
L1973  ⚪  (score=0)
```python
            imported_names=imported_names)
```
L1974  ⚪  (score=0)
```python
    else:
```
L1975  ⚪  (score=0)
```python
        imported_name_strings = []
```
L1976  ⚪  (score=0)
```python
        items = []
```
L1977  ⚪  (score=0)
```python
        for (name_pos, name, as_name) in imported_names:
```
L1978  ⚪  (score=0)
```python
            imported_name_strings.append(
```
L1979  ⚪  (score=0)
```python
                ExprNodes.IdentifierStringNode(name_pos, value=name))
```
L1980  ⚪  (score=0)
```python
            items.append(
```
L1981  ⚪  (score=0)
```python
                (name, ExprNodes.NameNode(name_pos, name=as_name or name)))
```
L1982  ⚪  (score=0)
```python
        return Nodes.FromImportStatNode(pos,
```
L1983  ⚪  (score=0)
```python
            module = ExprNodes.ImportNode(dotted_name_pos,
```
L1984  ⚪  (score=0)
```python
                module_name = ExprNodes.IdentifierStringNode(pos, value = dotted_name),
```
L1985  ⚪  (score=0)
```python
                is_import_as_name = False,
```
L1986  ⚪  (score=0)
```python
                level = level,
```
L1987  ⚪  (score=0)
```python
                imported_names = imported_name_strings),
```
L1988  ⚪  (score=0)
```python
            items = items)
```
L1989  ⚪  (score=0)
```python
```
L1990  ⚪  (score=0)
```python
```
L1991  ⚪  (score=0)
```python
@cython.cfunc
```
L1992  ⚪  (score=0)
```python
def p_imported_name(s: PyrexScanner):
```
L1993  ⚪  (score=0)
```python
    pos = s.position()
```
L1994  ⚪  (score=0)
```python
    name = p_ident(s)
```
L1995  ⚪  (score=0)
```python
    as_name = p_as_name(s)
```
L1996  ⚪  (score=0)
```python
    return (pos, name, as_name)
```
L1997  ⚪  (score=0)
```python
```
L1998  ⚪  (score=0)
```python
```
L1999  ⚪  (score=0)
```python
@cython.cfunc
```
L2000  ⚪  (score=0)
```python
def p_dotted_name(s: PyrexScanner, as_allowed: cython.bint) -> tuple:
```
L2001  ⚪  (score=0)
```python
    pos = s.position()
```
L2002  ⚪  (score=0)
```python
    target_name = p_ident(s)
```
L2003  ⚪  (score=0)
```python
    as_name = None
```
L2004  ⚪  (score=0)
```python
    names = [target_name]
```
L2005  ⚪  (score=0)
```python
    while s.sy == '.':
```
L2006  ⚪  (score=0)
```python
        s.next()
```
L2007  ⚪  (score=0)
```python
        names.append(p_ident(s))
```
L2008  ⚪  (score=0)
```python
    if as_allowed:
```
L2009  ⚪  (score=0)
```python
        as_name = p_as_name(s)
```
L2010  ⚪  (score=0)
```python
    return (pos, target_name, s.context.intern_ustring('.'.join(names)), as_name)
```
L2011  ⚪  (score=0)
```python
```
L2012  ⚪  (score=0)
```python
```
L2013  ⚪  (score=0)
```python
@cython.cfunc
```
L2014  ⚪  (score=0)
```python
def p_as_name(s: PyrexScanner):
```
L2015  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == 'as':
```
L2016  ⚪  (score=0)
```python
        s.next()
```
L2017  ⚪  (score=0)
```python
        return p_ident(s)
```
L2018  ⚪  (score=0)
```python
    else:
```
L2019  ⚪  (score=0)
```python
        return None
```
L2020  ⚪  (score=0)
```python
```
L2021  ⚪  (score=0)
```python
```
L2022  ⚪  (score=0)
```python
@cython.cfunc
```
L2023  ⚪  (score=0)
```python
def p_assert_statement(s: PyrexScanner):
```
L2024  ⚪  (score=0)
```python
    # s.sy == 'assert'
```
L2025  ⚪  (score=0)
```python
    pos = s.position()
```
L2026  ⚪  (score=0)
```python
    s.next()
```
L2027  ⚪  (score=0)
```python
    cond = p_test(s)
```
L2028  ⚪  (score=0)
```python
    if s.sy == ',':
```
L2029  ⚪  (score=0)
```python
        s.next()
```
L2030  ⚪  (score=0)
```python
        value = p_test(s)
```
L2031  ⚪  (score=0)
```python
    else:
```
L2032  ⚪  (score=0)
```python
        value = None
```
L2033  ⚪  (score=0)
```python
    return Nodes.AssertStatNode(pos, condition=cond, value=value)
```
L2034  ⚪  (score=0)
```python
```
L2035  ⚪  (score=0)
```python
```
L2036  ⚪  (score=0)
```python
@cython.cfunc
```
L2037  ⚪  (score=0)
```python
def p_if_statement(s: PyrexScanner):
```
L2038  ⚪  (score=0)
```python
    # s.sy == 'if'
```
L2039  ⚪  (score=0)
```python
    pos = s.position()
```
L2040  ⚪  (score=0)
```python
    s.next()
```
L2041  ⚪  (score=0)
```python
    if_clauses = [p_if_clause(s)]
```
L2042  ⚪  (score=0)
```python
    while s.sy == 'elif':
```
L2043  ⚪  (score=0)
```python
        s.next()
```
L2044  ⚪  (score=0)
```python
        if_clauses.append(p_if_clause(s))
```
L2045  ⚪  (score=0)
```python
    else_clause = p_else_clause(s)
```
L2046  ⚪  (score=0)
```python
    return Nodes.IfStatNode(pos,
```
L2047  ⚪  (score=0)
```python
        if_clauses = if_clauses, else_clause = else_clause)
```
L2048  ⚪  (score=0)
```python
```
L2049  ⚪  (score=0)
```python
```
L2050  ⚪  (score=0)
```python
@cython.cfunc
```
L2051  ⚪  (score=0)
```python
def p_if_clause(s: PyrexScanner):
```
L2052  ⚪  (score=0)
```python
    pos = s.position()
```
L2053  ⚪  (score=0)
```python
    test = p_namedexpr_test(s)
```
L2054  ⚪  (score=0)
```python
    body = p_suite(s)
```
L2055  ⚪  (score=0)
```python
    return Nodes.IfClauseNode(pos,
```
L2056  ⚪  (score=0)
```python
        condition = test, body = body)
```
L2057  ⚪  (score=0)
```python
```
L2058  ⚪  (score=0)
```python
```
L2059  ⚪  (score=0)
```python
@cython.cfunc
```
L2060  ⚪  (score=0)
```python
def p_else_clause(s: PyrexScanner):
```
L2061  ⚪  (score=0)
```python
    if s.sy == 'else':
```
L2062  ⚪  (score=0)
```python
        s.next()
```
L2063  ⚪  (score=0)
```python
        return p_suite(s)
```
L2064  ⚪  (score=0)
```python
    else:
```
L2065  ⚪  (score=0)
```python
        return None
```
L2066  ⚪  (score=0)
```python
```
L2067  ⚪  (score=0)
```python
```
L2068  ⚪  (score=0)
```python
@cython.cfunc
```
L2069  ⚪  (score=0)
```python
def p_while_statement(s: PyrexScanner):
```
L2070  ⚪  (score=0)
```python
    # s.sy == 'while'
```
L2071  ⚪  (score=0)
```python
    pos = s.position()
```
L2072  ⚪  (score=0)
```python
    s.next()
```
L2073  ⚪  (score=0)
```python
    test = p_namedexpr_test(s)
```
L2074  ⚪  (score=0)
```python
    body = p_suite(s)
```
L2075  ⚪  (score=0)
```python
    else_clause = p_else_clause(s)
```
L2076  ⚪  (score=0)
```python
    return Nodes.WhileStatNode(pos,
```
L2077  ⚪  (score=0)
```python
        condition = test, body = body,
```
L2078  ⚪  (score=0)
```python
        else_clause = else_clause)
```
L2079  ⚪  (score=0)
```python
```
L2080  ⚪  (score=0)
```python
```
L2081  ⚪  (score=0)
```python
@cython.cfunc
```
L2082  ⚪  (score=0)
```python
def p_for_statement(s: PyrexScanner, is_async: cython.bint = False):
```
L2083  ⚪  (score=0)
```python
    # s.sy == 'for'
```
L2084  ⚪  (score=0)
```python
    pos = s.position()
```
L2085  ⚪  (score=0)
```python
    s.next()
```
L2086  ⚪  (score=0)
```python
    kw = p_for_bounds(s, allow_testlist=True, is_async=is_async)
```
L2087  ⚪  (score=0)
```python
    body = p_suite(s)
```
L2088  ⚪  (score=0)
```python
    else_clause = p_else_clause(s)
```
L2089  ⚪  (score=0)
```python
    kw.update(body=body, else_clause=else_clause, is_async=is_async)
```
L2090  ⚪  (score=0)
```python
    return Nodes.ForStatNode(pos, **kw)
```
L2091  ⚪  (score=0)
```python
```
L2092  ⚪  (score=0)
```python
```
L2093  ⚪  (score=0)
```python
@cython.cfunc
```
L2094  ⚪  (score=0)
```python
def p_for_bounds(s: PyrexScanner, allow_testlist: cython.bint = True, is_async: cython.bint = False) -> dict:
```
L2095  ⚪  (score=0)
```python
    target = p_for_target(s)
```
L2096  ⚪  (score=0)
```python
    if s.sy == 'in':
```
L2097  ⚪  (score=0)
```python
        s.next()
```
L2098  ⚪  (score=0)
```python
        iterator = p_for_iterator(s, allow_testlist, is_async=is_async)
```
L2099  ⚪  (score=0)
```python
        return dict(target=target, iterator=iterator)
```
L2100  ⚪  (score=0)
```python
    elif not s.in_python_file and not is_async:
```
L2101  ⚪  (score=0)
```python
        if s.sy == 'from':
```
L2102  ⚪  (score=0)
```python
            s.next()
```
L2103  ⚪  (score=0)
```python
            bound1 = p_bit_expr(s)
```
L2104  ⚪  (score=0)
```python
        else:
```
L2105  ⚪  (score=0)
```python
            # Support shorter "for a <= x < b" syntax
```
L2106  ⚪  (score=0)
```python
            bound1, target = target, None
```
L2107  ⚪  (score=0)
```python
        rel1 = p_for_from_relation(s)
```
L2108  ⚪  (score=0)
```python
        name2_pos = s.position()
```
L2109  ⚪  (score=0)
```python
        name2 = p_ident(s)
```
L2110  ⚪  (score=0)
```python
        rel2_pos = s.position()
```
L2111  ⚪  (score=0)
```python
        rel2 = p_for_from_relation(s)
```
L2112  ⚪  (score=0)
```python
        bound2 = p_bit_expr(s)
```
L2113  ⚪  (score=0)
```python
        step = p_for_from_step(s)
```
L2114  ⚪  (score=0)
```python
        if target is None:
```
L2115  ⚪  (score=0)
```python
            target = ExprNodes.NameNode(name2_pos, name = name2)
```
L2116  ⚪  (score=0)
```python
        else:
```
L2117  ⚪  (score=0)
```python
            if not target.is_name:
```
L2118  ⚪  (score=0)
```python
                error(target.pos,
```
L2119  ⚪  (score=0)
```python
                    "Target of for-from statement must be a variable name")
```
L2120  ⚪  (score=0)
```python
            elif name2 != target.name:
```
L2121  ⚪  (score=0)
```python
                error(name2_pos,
```
L2122  ⚪  (score=0)
```python
                    "Variable name in for-from range does not match target")
```
L2123  ⚪  (score=0)
```python
        if rel1[0] != rel2[0]:
```
L2124  ⚪  (score=0)
```python
            error(rel2_pos,
```
L2125  ⚪  (score=0)
```python
                "Relation directions in for-from do not match")
```
L2126  ⚪  (score=0)
```python
        return dict(target = target,
```
L2127  ⚪  (score=0)
```python
                    bound1 = bound1,
```
L2128  ⚪  (score=0)
```python
                    relation1 = rel1,
```
L2129  ⚪  (score=0)
```python
                    relation2 = rel2,
```
L2130  ⚪  (score=0)
```python
                    bound2 = bound2,
```
L2131  ⚪  (score=0)
```python
                    step = step,
```
L2132  ⚪  (score=0)
```python
                    )
```
L2133  ⚪  (score=0)
```python
    else:
```
L2134  ⚪  (score=0)
```python
        s.expect('in')
```
L2135  ⚪  (score=0)
```python
        return {}
```
L2136  ⚪  (score=0)
```python
```
L2137  ⚪  (score=0)
```python
```
L2138  ⚪  (score=0)
```python
@cython.cfunc
```
L2139  ⚪  (score=0)
```python
def p_for_from_relation(s: PyrexScanner):
```
L2140  ⚪  (score=0)
```python
    if s.sy in inequality_relations:
```
L2141  ⚪  (score=0)
```python
        op = s.sy
```
L2142  ⚪  (score=0)
```python
        s.next()
```
L2143  ⚪  (score=0)
```python
        return op
```
L2144  ⚪  (score=0)
```python
    else:
```
L2145  ⚪  (score=0)
```python
        s.error("Expected one of '<', '<=', '>' '>='")
```
L2146  ⚪  (score=0)
```python
```
L2147  ⚪  (score=0)
```python
```
L2148  ⚪  (score=0)
```python
@cython.cfunc
```
L2149  ⚪  (score=0)
```python
def p_for_from_step(s: PyrexScanner):
```
L2150  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == 'by':
```
L2151  ⚪  (score=0)
```python
        s.next()
```
L2152  ⚪  (score=0)
```python
        step = p_bit_expr(s)
```
L2153  ⚪  (score=0)
```python
        return step
```
L2154  ⚪  (score=0)
```python
    else:
```
L2155  ⚪  (score=0)
```python
        return None
```
L2156  ⚪  (score=0)
```python
```
L2157  ⚪  (score=0)
```python
```
L2158  ⚪  (score=0)
```python
inequality_relations = cython.declare(frozenset, frozenset((
```
L2159  ⚪  (score=0)
```python
    '<', '<=', '>', '>=')))
```
L2160  ⚪  (score=0)
```python
```
L2161  ⚪  (score=0)
```python
```
L2162  ⚪  (score=0)
```python
@cython.cfunc
```
L2163  ⚪  (score=0)
```python
def p_target(s: PyrexScanner, terminator: str):
```
L2164  ⚪  (score=0)
```python
    pos = s.position()
```
L2165  ⚪  (score=0)
```python
    expr = p_starred_expr(s)
```
L2166  ⚪  (score=0)
```python
    if s.sy == ',':
```
L2167  ⚪  (score=0)
```python
        s.next()
```
L2168  ⚪  (score=0)
```python
        exprs = [expr]
```
L2169  ⚪  (score=0)
```python
        while s.sy != terminator:
```
L2170  ⚪  (score=0)
```python
            exprs.append(p_starred_expr(s))
```
L2171  ⚪  (score=0)
```python
            if s.sy != ',':
```
L2172  ⚪  (score=0)
```python
                break
```
L2173  ⚪  (score=0)
```python
            s.next()
```
L2174  ⚪  (score=0)
```python
        return ExprNodes.TupleNode(pos, args = exprs)
```
L2175  ⚪  (score=0)
```python
    else:
```
L2176  ⚪  (score=0)
```python
        return expr
```
L2177  ⚪  (score=0)
```python
```
L2178  ⚪  (score=0)
```python
```
L2179  ⚪  (score=0)
```python
@cython.cfunc
```
L2180  ⚪  (score=0)
```python
def p_for_target(s: PyrexScanner):
```
L2181  ⚪  (score=0)
```python
    return p_target(s, 'in')
```
L2182  ⚪  (score=0)
```python
```
L2183  ⚪  (score=0)
```python
```
L2184  ⚪  (score=0)
```python
@cython.cfunc
```
L2185  ⚪  (score=0)
```python
def p_for_iterator(s: PyrexScanner, allow_testlist: cython.bint = True, is_async: cython.bint = False):
```
L2186  ⚪  (score=0)
```python
    pos = s.position()
```
L2187  ⚪  (score=0)
```python
    if allow_testlist:
```
L2188  ⚪  (score=0)
```python
        expr = p_testlist(s)
```
L2189  ⚪  (score=0)
```python
    else:
```
L2190  ⚪  (score=0)
```python
        expr = p_or_test(s)
```
L2191  ⚪  (score=0)
```python
    return (ExprNodes.AsyncIteratorNode if is_async else ExprNodes.IteratorNode)(pos, sequence=expr)
```
L2192  ⚪  (score=0)
```python
```
L2193  ⚪  (score=0)
```python
```
L2194  ⚪  (score=0)
```python
@cython.cfunc
```
L2195  ⚪  (score=0)
```python
def p_try_statement(s: PyrexScanner):
```
L2196  ⚪  (score=0)
```python
    # s.sy == 'try'
```
L2197  ⚪  (score=0)
```python
    pos = s.position()
```
L2198  ⚪  (score=0)
```python
    s.next()
```
L2199  ⚪  (score=0)
```python
    body = p_suite(s)
```
L2200  ⚪  (score=0)
```python
    except_clauses = []
```
L2201  ⚪  (score=0)
```python
    else_clause = None
```
L2202  ⚪  (score=0)
```python
    if s.sy in ('except', 'else'):
```
L2203  ⚪  (score=0)
```python
        while s.sy == 'except':
```
L2204  ⚪  (score=0)
```python
            except_clauses.append(p_except_clause(s))
```
L2205  ⚪  (score=0)
```python
        if s.sy == 'else':
```
L2206  ⚪  (score=0)
```python
            s.next()
```
L2207  ⚪  (score=0)
```python
            else_clause = p_suite(s)
```
L2208  ⚪  (score=0)
```python
        body = Nodes.TryExceptStatNode(pos,
```
L2209  ⚪  (score=0)
```python
            body = body, except_clauses = except_clauses,
```
L2210  ⚪  (score=0)
```python
            else_clause = else_clause)
```
L2211  ⚪  (score=0)
```python
        if s.sy != 'finally':
```
L2212  ⚪  (score=0)
```python
            return body
```
L2213  ⚪  (score=0)
```python
        # try-except-finally is equivalent to nested try-except/try-finally
```
L2214  ⚪  (score=0)
```python
    if s.sy == 'finally':
```
L2215  ⚪  (score=0)
```python
        s.next()
```
L2216  ⚪  (score=0)
```python
        finally_clause = p_suite(s)
```
L2217  ⚪  (score=0)
```python
        return Nodes.TryFinallyStatNode(pos,
```
L2218  ⚪  (score=0)
```python
            body = body, finally_clause = finally_clause)
```
L2219  ⚪  (score=0)
```python
    else:
```
L2220  ⚪  (score=0)
```python
        s.error("Expected 'except' or 'finally'")
```
L2221  ⚪  (score=0)
```python
```
L2222  ⚪  (score=0)
```python
```
L2223  ⚪  (score=0)
```python
@cython.cfunc
```
L2224  ⚪  (score=0)
```python
def p_except_clause(s: PyrexScanner):
```
L2225  ⚪  (score=0)
```python
    # s.sy == 'except'
```
L2226  ⚪  (score=0)
```python
    pos = s.position()
```
L2227  ⚪  (score=0)
```python
    s.next()
```
L2228  ⚪  (score=0)
```python
    exc_type = None
```
L2229  ⚪  (score=0)
```python
    exc_value = None
```
L2230  ⚪  (score=0)
```python
    is_except_as = False
```
L2231  ⚪  (score=0)
```python
    if s.sy != ':':
```
L2232  ⚪  (score=0)
```python
        exc_type = p_test(s)
```
L2233  ⚪  (score=0)
```python
        # normalise into list of single exception tests
```
L2234  ⚪  (score=0)
```python
        if isinstance(exc_type, ExprNodes.TupleNode):
```
L2235  ⚪  (score=0)
```python
            exc_type = exc_type.args
```
L2236  ⚪  (score=0)
```python
        else:
```
L2237  ⚪  (score=0)
```python
            exc_type = [exc_type]
```
L2238  ⚪  (score=0)
```python
        if s.sy == ',' or (s.sy == 'IDENT' and s.systring == 'as'
```
L2239  ⚪  (score=0)
```python
                           and s.context.language_level == 2):
```
L2240  ⚪  (score=0)
```python
            s.next()
```
L2241  ⚪  (score=0)
```python
            exc_value = p_test(s)
```
L2242  ⚪  (score=0)
```python
        elif s.sy == 'IDENT' and s.systring == 'as':
```
L2243  ⚪  (score=0)
```python
            # Py3 syntax requires a name here
```
L2244  ⚪  (score=0)
```python
            s.next()
```
L2245  ⚪  (score=0)
```python
            pos2 = s.position()
```
L2246  ⚪  (score=0)
```python
            name = p_ident(s)
```
L2247  ⚪  (score=0)
```python
            exc_value = ExprNodes.NameNode(pos2, name = name)
```
L2248  ⚪  (score=0)
```python
            is_except_as = True
```
L2249  ⚪  (score=0)
```python
    body = p_suite(s)
```
L2250  ⚪  (score=0)
```python
    return Nodes.ExceptClauseNode(pos,
```
L2251  ⚪  (score=0)
```python
        pattern = exc_type, target = exc_value,
```
L2252  ⚪  (score=0)
```python
        body = body, is_except_as=is_except_as)
```
L2253  ⚪  (score=0)
```python
```
L2254  ⚪  (score=0)
```python
```
L2255  ⚪  (score=0)
```python
@cython.cfunc
```
L2256  ⚪  (score=0)
```python
def p_include_statement(s: PyrexScanner, ctx):
```
L2257  ⚪  (score=0)
```python
    pos = s.position()
```
L2258  ⚪  (score=0)
```python
    s.next()  # 'include'
```
L2259  ⚪  (score=0)
```python
    unicode_include_file_name = p_string_literal(s, 'u')[2]
```
L2260  ⚪  (score=0)
```python
    s.expect_newline("Syntax error in include statement")
```
L2261  ⚪  (score=0)
```python
    if s.compile_time_eval:
```
L2262  ⚪  (score=0)
```python
        include_file_name = unicode_include_file_name
```
L2263  ⚪  (score=0)
```python
        include_file_path = s.context.find_include_file(include_file_name, pos)
```
L2264  ⚪  (score=0)
```python
        if include_file_path:
```
L2265  ⚪  (score=0)
```python
            s.included_files.append(include_file_name)
```
L2266  ⚪  (score=0)
```python
            source_desc = FileSourceDescriptor(include_file_path)
```
L2267  ⚪  (score=0)
```python
            with source_desc.get_file_object() as f:
```
L2268  ⚪  (score=0)
```python
                s2 = PyrexScanner(f, source_desc, s, source_encoding=f.encoding, parse_comments=s.parse_comments)
```
L2269  ⚪  (score=0)
```python
                tree = p_statement_list(s2, ctx)
```
L2270  ⚪  (score=0)
```python
            return tree
```
L2271  ⚪  (score=0)
```python
        else:
```
L2272  ⚪  (score=0)
```python
            return None
```
L2273  ⚪  (score=0)
```python
    else:
```
L2274  ⚪  (score=0)
```python
        return Nodes.PassStatNode(pos)
```
L2275  ⚪  (score=0)
```python
```
L2276  ⚪  (score=0)
```python
```
L2277  ⚪  (score=0)
```python
@cython.cfunc
```
L2278  ⚪  (score=0)
```python
def p_with_statement(s: PyrexScanner):
```
L2279  ⚪  (score=0)
```python
    s.next()  # 'with'
```
L2280  ⚪  (score=0)
```python
    if s.systring == 'template' and not s.in_python_file:
```
L2281  ⚪  (score=0)
```python
        node = p_with_template(s)
```
L2282  ⚪  (score=0)
```python
    else:
```
L2283  ⚪  (score=0)
```python
        node = p_with_items(s)
```
L2284  ⚪  (score=0)
```python
    return node
```
L2285  ⚪  (score=0)
```python
```
L2286  ⚪  (score=0)
```python
```
L2287  ⚪  (score=0)
```python
@cython.cfunc
```
L2288  ⚪  (score=0)
```python
def p_with_items(s: PyrexScanner, is_async: cython.bint = False):
```
L2289  ⚪  (score=0)
```python
    """
```
L2290  ⚪  (score=0)
```python
    Copied from CPython:
```
L2291  ⚪  (score=0)
```python
    | 'with' '(' a[asdl_withitem_seq*]=','.with_item+ ','? ')' ':' b=block {
```
L2292  ⚪  (score=0)
```python
        _PyAST_With(a, b, NULL, EXTRA) }
```
L2293  ⚪  (score=0)
```python
    | 'with' a[asdl_withitem_seq*]=','.with_item+ ':' tc=[TYPE_COMMENT] b=block {
```
L2294  ⚪  (score=0)
```python
        _PyAST_With(a, b, NEW_TYPE_COMMENT(p, tc), EXTRA) }
```
L2295  ⚪  (score=0)
```python
    Therefore the first thing to try is the bracket-enclosed
```
L2296  ⚪  (score=0)
```python
    version and if that fails try the regular version
```
L2297  ⚪  (score=0)
```python
    """
```
L2298  ⚪  (score=0)
```python
    brackets_succeeded = False
```
L2299  ⚪  (score=0)
```python
    items = ()  # unused, but static analysis fails to track that below
```
L2300  ⚪  (score=0)
```python
    if s.sy == '(':
```
L2301  ⚪  (score=0)
```python
        with tentatively_scan(s) as errors:
```
L2302  ⚪  (score=0)
```python
            s.next()
```
L2303  ⚪  (score=0)
```python
            items = p_with_items_list(s, is_async)
```
L2304  ⚪  (score=0)
```python
            s.expect(")")
```
L2305  ⚪  (score=0)
```python
            if s.sy != ":":
```
L2306  ⚪  (score=0)
```python
                # Fail - the message doesn't matter because we'll try the
```
L2307  ⚪  (score=0)
```python
                # non-bracket version so it'll never be shown
```
L2308  ⚪  (score=0)
```python
                s.error("")
```
L2309  ⚪  (score=0)
```python
        brackets_succeeded = not errors
```
L2310  ⚪  (score=0)
```python
    if not brackets_succeeded:
```
L2311  ⚪  (score=0)
```python
        # try the non-bracket version
```
L2312  ⚪  (score=0)
```python
        items = p_with_items_list(s, is_async)
```
L2313  ⚪  (score=0)
```python
    body = p_suite(s)
```
L2314  ⚪  (score=0)
```python
    for cls, pos, kwds in reversed(items):
```
L2315  ⚪  (score=0)
```python
        # construct the actual nodes now that we know what the body is
```
L2316  ⚪  (score=0)
```python
        body = cls(pos, body=body, **kwds)
```
L2317  ⚪  (score=0)
```python
    return body
```
L2318  ⚪  (score=0)
```python
```
L2319  ⚪  (score=0)
```python
```
L2320  ⚪  (score=0)
```python
@cython.cfunc
```
L2321  ⚪  (score=0)
```python
def p_with_items_list(s: PyrexScanner, is_async: cython.bint) -> list:
```
L2322  ⚪  (score=0)
```python
    items = []
```
L2323  ⚪  (score=0)
```python
    while True:
```
L2324  ⚪  (score=0)
```python
        items.append(p_with_item(s, is_async))
```
L2325  ⚪  (score=0)
```python
        if s.sy != ",":
```
L2326  ⚪  (score=0)
```python
            break
```
L2327  ⚪  (score=0)
```python
        s.next()
```
L2328  ⚪  (score=0)
```python
        if s.sy == ")":
```
L2329  ⚪  (score=0)
```python
            # trailing commas allowed
```
L2330  ⚪  (score=0)
```python
            break
```
L2331  ⚪  (score=0)
```python
    return items
```
L2332  ⚪  (score=0)
```python
```
L2333  ⚪  (score=0)
```python
```
L2334  ⚪  (score=0)
```python
@cython.cfunc
```
L2335  ⚪  (score=0)
```python
def p_with_item(s: PyrexScanner, is_async: cython.bint) -> tuple:
```
L2336  ⚪  (score=0)
```python
    # In contrast to most parsing functions, this returns a tuple of
```
L2337  ⚪  (score=0)
```python
    #  class, pos, kwd_dict
```
L2338  ⚪  (score=0)
```python
    # This is because GILStatNode does a reasonable amount of initialization in its
```
L2339  ⚪  (score=0)
```python
    # constructor, and requires "body" to be set, which we don't currently have
```
L2340  ⚪  (score=0)
```python
    pos = s.position()
```
L2341  ⚪  (score=0)
```python
    if not s.in_python_file and s.sy == 'IDENT' and s.systring in ('nogil', 'gil'):
```
L2342  ⚪  (score=0)
```python
        if is_async:
```
L2343  ⚪  (score=0)
```python
            s.error("with gil/nogil cannot be async")
```
L2344  ⚪  (score=0)
```python
        state = s.systring
```
L2345  ⚪  (score=0)
```python
        s.next()
```
L2346  ⚪  (score=0)
```python
```
L2347  ⚪  (score=0)
```python
        # support conditional gil/nogil
```
L2348  ⚪  (score=0)
```python
        condition = None
```
L2349  ⚪  (score=0)
```python
        if s.sy == '(':
```
L2350  ⚪  (score=0)
```python
            s.next()
```
L2351  ⚪  (score=0)
```python
            condition = p_test(s)
```
L2352  ⚪  (score=0)
```python
            s.expect(')')
```
L2353  ⚪  (score=0)
```python
```
L2354  ⚪  (score=0)
```python
        return Nodes.GILStatNode, pos, {"state": state, "condition": condition}
```
L2355  ⚪  (score=0)
```python
    else:
```
L2356  ⚪  (score=0)
```python
        manager = p_test(s)
```
L2357  ⚪  (score=0)
```python
        target = None
```
L2358  ⚪  (score=0)
```python
        if s.sy == 'IDENT' and s.systring == 'as':
```
L2359  ⚪  (score=0)
```python
            s.next()
```
L2360  ⚪  (score=0)
```python
            target = p_starred_expr(s)
```
L2361  ⚪  (score=0)
```python
        return Nodes.WithStatNode, pos, {"manager": manager, "target": target, "is_async": is_async}
```
L2362  ⚪  (score=0)
```python
```
L2363  ⚪  (score=0)
```python
```
L2364  ⚪  (score=0)
```python
@cython.cfunc
```
L2365  ⚪  (score=0)
```python
def p_with_template(s: PyrexScanner):
```
L2366  ⚪  (score=0)
```python
    pos = s.position()
```
L2367  ⚪  (score=0)
```python
    templates = []
```
L2368  ⚪  (score=0)
```python
    s.next()
```
L2369  ⚪  (score=0)
```python
    s.expect('[')
```
L2370  ⚪  (score=0)
```python
    templates.append(s.systring)
```
L2371  ⚪  (score=0)
```python
    s.next()
```
L2372  ⚪  (score=0)
```python
    while s.systring == ',':
```
L2373  ⚪  (score=0)
```python
        s.next()
```
L2374  ⚪  (score=0)
```python
        templates.append(s.systring)
```
L2375  ⚪  (score=0)
```python
        s.next()
```
L2376  ⚪  (score=0)
```python
    s.expect(']')
```
L2377  ⚪  (score=0)
```python
    if s.sy == ':':
```
L2378  ⚪  (score=0)
```python
        s.next()
```
L2379  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in template function declaration")
```
L2380  ⚪  (score=0)
```python
        s.expect_indent()
```
L2381  ⚪  (score=0)
```python
        body_ctx = Ctx()
```
L2382  ⚪  (score=0)
```python
        body_ctx.templates = templates
```
L2383  ⚪  (score=0)
```python
        func_or_var = p_c_func_or_var_declaration(s, pos, body_ctx)
```
L2384  ⚪  (score=0)
```python
        s.expect_dedent()
```
L2385  ⚪  (score=0)
```python
        return func_or_var
```
L2386  ⚪  (score=0)
```python
    else:
```
L2387  ⚪  (score=0)
```python
        error(pos, "Syntax error in template function declaration")
```
L2388  ⚪  (score=0)
```python
```
L2389  ⚪  (score=0)
```python
```
L2390  ⚪  (score=0)
```python
@cython.cfunc
```
L2391  ⚪  (score=0)
```python
def p_simple_statement(s: PyrexScanner, first_statement: cython.bint = 0):
```
L2392  ⚪  (score=0)
```python
    #print "p_simple_statement:", s.sy, s.systring ###
```
L2393  ⚪  (score=0)
```python
    if s.sy == 'global':
```
L2394  ⚪  (score=0)
```python
        node = p_global_statement(s)
```
L2395  ⚪  (score=0)
```python
    elif s.sy == 'nonlocal':
```
L2396  ⚪  (score=0)
```python
        node = p_nonlocal_statement(s)
```
L2397  ⚪  (score=0)
```python
    elif s.sy == 'print':
```
L2398  ⚪  (score=0)
```python
        node = p_print_statement(s)
```
L2399  ⚪  (score=0)
```python
    elif s.sy == 'exec':
```
L2400  ⚪  (score=0)
```python
        node = p_exec_statement(s)
```
L2401  ⚪  (score=0)
```python
    elif s.sy == 'del':
```
L2402  ⚪  (score=0)
```python
        node = p_del_statement(s)
```
L2403  ⚪  (score=0)
```python
    elif s.sy == 'break':
```
L2404  ⚪  (score=0)
```python
        node = p_break_statement(s)
```
L2405  ⚪  (score=0)
```python
    elif s.sy == 'continue':
```
L2406  ⚪  (score=0)
```python
        node = p_continue_statement(s)
```
L2407  ⚪  (score=0)
```python
    elif s.sy == 'return':
```
L2408  ⚪  (score=0)
```python
        node = p_return_statement(s)
```
L2409  ⚪  (score=0)
```python
    elif s.sy == 'raise':
```
L2410  ⚪  (score=0)
```python
        node = p_raise_statement(s)
```
L2411  ⚪  (score=0)
```python
    elif s.sy in ('import', 'cimport'):
```
L2412  ⚪  (score=0)
```python
        node = p_import_statement(s)
```
L2413  ⚪  (score=0)
```python
    elif s.sy == 'from':
```
L2414  ⚪  (score=0)
```python
        node = p_from_import_statement(s, first_statement = first_statement)
```
L2415  ⚪  (score=0)
```python
    elif s.sy == 'yield':
```
L2416  ⚪  (score=0)
```python
        node = p_yield_statement(s)
```
L2417  ⚪  (score=0)
```python
    elif s.sy == 'assert':
```
L2418  ⚪  (score=0)
```python
        node = p_assert_statement(s)
```
L2419  ⚪  (score=0)
```python
    elif s.sy == 'pass':
```
L2420  ⚪  (score=0)
```python
        node = p_pass_statement(s)
```
L2421  ⚪  (score=0)
```python
    else:
```
L2422  ⚪  (score=0)
```python
        node = p_expression_or_assignment(s)
```
L2423  ⚪  (score=0)
```python
    return node
```
L2424  ⚪  (score=0)
```python
```
L2425  ⚪  (score=0)
```python
```
L2426  ⚪  (score=0)
```python
@cython.cfunc
```
L2427  ⚪  (score=0)
```python
def p_simple_statement_list(s: PyrexScanner, ctx, first_statement: cython.bint = 0):
```
L2428  ⚪  (score=0)
```python
    # Parse a series of simple statements on one line
```
L2429  ⚪  (score=0)
```python
    # separated by semicolons.
```
L2430  ⚪  (score=0)
```python
    stat = p_simple_statement(s, first_statement = first_statement)
```
L2431  ⚪  (score=0)
```python
    pos = stat.pos
```
L2432  ⚪  (score=0)
```python
    stats = []
```
L2433  ⚪  (score=0)
```python
    if not isinstance(stat, Nodes.PassStatNode):
```
L2434  ⚪  (score=0)
```python
        stats.append(stat)
```
L2435  ⚪  (score=0)
```python
    while s.sy == ';':
```
L2436  ⚪  (score=0)
```python
        #print "p_simple_statement_list: maybe more to follow" ###
```
L2437  ⚪  (score=0)
```python
        s.next()
```
L2438  ⚪  (score=0)
```python
        if s.sy in ('NEWLINE', 'EOF'):
```
L2439  ⚪  (score=0)
```python
            break
```
L2440  ⚪  (score=0)
```python
        stat = p_simple_statement(s, first_statement = first_statement)
```
L2441  ⚪  (score=0)
```python
        if isinstance(stat, Nodes.PassStatNode):
```
L2442  ⚪  (score=0)
```python
            continue
```
L2443  ⚪  (score=0)
```python
        stats.append(stat)
```
L2444  ⚪  (score=0)
```python
        first_statement = False
```
L2445  ⚪  (score=0)
```python
```
L2446  ⚪  (score=0)
```python
    if not stats:
```
L2447  ⚪  (score=0)
```python
        stat = Nodes.PassStatNode(pos)
```
L2448  ⚪  (score=0)
```python
    elif len(stats) == 1:
```
L2449  ⚪  (score=0)
```python
        stat = stats[0]
```
L2450  ⚪  (score=0)
```python
    else:
```
L2451  ⚪  (score=0)
```python
        stat = Nodes.StatListNode(pos, stats = stats)
```
L2452  ⚪  (score=0)
```python
```
L2453  ⚪  (score=0)
```python
    if s.sy not in ('NEWLINE', 'EOF'):
```
L2454  ⚪  (score=0)
```python
        # provide a better error message for users who accidentally write Cython code in .py files
```
L2455  ⚪  (score=0)
```python
        if isinstance(stat, Nodes.ExprStatNode):
```
L2456  ⚪  (score=0)
```python
            if stat.expr.is_name and stat.expr.name == 'cdef':
```
L2457  ⚪  (score=0)
```python
                s.error("The 'cdef' keyword is only allowed in Cython files (pyx/pxi/pxd)", pos)
```
L2458  ⚪  (score=0)
```python
    s.expect_newline("Syntax error in simple statement list")
```
L2459  ⚪  (score=0)
```python
```
L2460  ⚪  (score=0)
```python
    return stat
```
L2461  ⚪  (score=0)
```python
```
L2462  ⚪  (score=0)
```python
```
L2463  ⚪  (score=0)
```python
@cython.cfunc
```
L2464  ⚪  (score=0)
```python
def p_compile_time_expr(s: PyrexScanner):
```
L2465  ⚪  (score=0)
```python
    old = s.compile_time_expr
```
L2466  ⚪  (score=0)
```python
    s.compile_time_expr = 1
```
L2467  ⚪  (score=0)
```python
    expr = p_testlist(s)
```
L2468  ⚪  (score=0)
```python
    s.compile_time_expr = old
```
L2469  ⚪  (score=0)
```python
    return expr
```
L2470  ⚪  (score=0)
```python
```
L2471  ⚪  (score=0)
```python
```
L2472  ⚪  (score=0)
```python
@cython.cfunc
```
L2473  ⚪  (score=0)
```python
def p_DEF_statement(s: PyrexScanner):
```
L2474  ⚪  (score=0)
```python
    pos = s.position()
```
L2475  ⚪  (score=0)
```python
    denv = s.compile_time_env
```
L2476  ⚪  (score=0)
```python
    s.next()  # 'DEF'
```
L2477  ⚪  (score=0)
```python
    name = p_ident(s)
```
L2478  ⚪  (score=0)
```python
    s.expect('=')
```
L2479  ⚪  (score=0)
```python
    expr = p_compile_time_expr(s)
```
L2480  ⚪  (score=0)
```python
    if s.compile_time_eval:
```
L2481  ⚪  (score=0)
```python
        value = expr.compile_time_value(denv)
```
L2482  ⚪  (score=0)
```python
        #print "p_DEF_statement: %s = %r" % (name, value) ###
```
L2483  ⚪  (score=0)
```python
        denv.declare(name, value)
```
L2484  ⚪  (score=0)
```python
    s.expect_newline("Expected a newline", ignore_semicolon=True)
```
L2485  ⚪  (score=0)
```python
    return Nodes.PassStatNode(pos)
```
L2486  ⚪  (score=0)
```python
```
L2487  ⚪  (score=0)
```python
```
L2488  ⚪  (score=0)
```python
@cython.cfunc
```
L2489  ⚪  (score=0)
```python
def p_IF_statement(s: PyrexScanner, ctx):
```
L2490  ⚪  (score=0)
```python
    pos = s.position()
```
L2491  ⚪  (score=0)
```python
    saved_eval = s.compile_time_eval
```
L2492  ⚪  (score=0)
```python
    current_eval = saved_eval
```
L2493  ⚪  (score=0)
```python
    denv = s.compile_time_env
```
L2494  ⚪  (score=0)
```python
    result = None
```
L2495  ⚪  (score=0)
```python
    while 1:
```
L2496  ⚪  (score=0)
```python
        s.next()  # 'IF' or 'ELIF'
```
L2497  ⚪  (score=0)
```python
        expr = p_compile_time_expr(s)
```
L2498  ⚪  (score=0)
```python
        s.compile_time_eval = current_eval and bool(expr.compile_time_value(denv))
```
L2499  ⚪  (score=0)
```python
        body = p_suite(s, ctx)
```
L2500  ⚪  (score=0)
```python
        if s.compile_time_eval:
```
L2501  ⚪  (score=0)
```python
            result = body
```
L2502  ⚪  (score=0)
```python
            current_eval = 0
```
L2503  ⚪  (score=0)
```python
        if s.sy != 'ELIF':
```
L2504  ⚪  (score=0)
```python
            break
```
L2505  ⚪  (score=0)
```python
    if s.sy == 'ELSE':
```
L2506  ⚪  (score=0)
```python
        s.next()
```
L2507  ⚪  (score=0)
```python
        s.compile_time_eval = current_eval
```
L2508  ⚪  (score=0)
```python
        body = p_suite(s, ctx)
```
L2509  ⚪  (score=0)
```python
        if current_eval:
```
L2510  ⚪  (score=0)
```python
            result = body
```
L2511  ⚪  (score=0)
```python
    if not result:
```
L2512  ⚪  (score=0)
```python
        result = Nodes.PassStatNode(pos)
```
L2513  ⚪  (score=0)
```python
    s.compile_time_eval = saved_eval
```
L2514  ⚪  (score=0)
```python
    return result
```
L2515  ⚪  (score=0)
```python
```
L2516  ⚪  (score=0)
```python
```
L2517  ⚪  (score=0)
```python
@cython.cfunc
```
L2518  ⚪  (score=0)
```python
def p_statement(s: PyrexScanner, ctx, first_statement: cython.bint = False):
```
L2519  ⚪  (score=0)
```python
    cdef_flag: cython.bint = ctx.cdef_flag
```
L2520  ⚪  (score=0)
```python
    pos = s.position()
```
L2521  ⚪  (score=0)
```python
    decorators = None
```
L2522  ⚪  (score=0)
```python
    if s.sy == 'ctypedef':
```
L2523  ⚪  (score=0)
```python
        if ctx.level not in ('module', 'module_pxd'):
```
L2524  ⚪  (score=0)
```python
            s.error("ctypedef statement not allowed here")
```
L2525  ⚪  (score=0)
```python
        #if ctx.api:
```
L2526  ⚪  (score=0)
```python
        #    error(pos, "'api' not allowed with 'ctypedef'")
```
L2527  ⚪  (score=0)
```python
        return p_ctypedef_statement(s, ctx)
```
L2528  ⚪  (score=0)
```python
    elif s.sy == 'DEF':
```
L2529  ⚪  (score=0)
```python
        # We used to dep-warn about this but removed the warning again since
```
L2530  ⚪  (score=0)
```python
        # we don't have a good answer yet for all use cases.
```
L2531  ⚪  (score=0)
```python
        if s.context.compiler_directives.get("warn.deprecated.DEF", False):
```
L2532  ⚪  (score=0)
```python
            warning(pos,
```
L2533  ⚪  (score=0)
```python
                    "The 'DEF' statement  will be removed in a future Cython version. "
```
L2534  ⚪  (score=0)
```python
                    "Consider using global variables, constants, and in-place literals instead. "
```
L2535  ⚪  (score=0)
```python
                    "See https://github.com/cython/cython/issues/4310", level=1)
```
L2536  ⚪  (score=0)
```python
        return p_DEF_statement(s)
```
L2537  ⚪  (score=0)
```python
    elif s.sy == 'IF':
```
L2538  ⚪  (score=0)
```python
        if s.context.compiler_directives.get("warn.deprecated.IF", True):
```
L2539  ⚪  (score=0)
```python
            warning(pos,
```
L2540  ⚪  (score=0)
```python
                    "The 'IF' statement is deprecated and will be removed in a future Cython version. "
```
L2541  ⚪  (score=0)
```python
                    "Consider using runtime conditions or C macros instead. "
```
L2542  ⚪  (score=0)
```python
                    "See https://github.com/cython/cython/issues/4310", level=1)
```
L2543  ⚪  (score=0)
```python
        return p_IF_statement(s, ctx)
```
L2544  ⚪  (score=0)
```python
    elif s.sy == '@':
```
L2545  ⚪  (score=0)
```python
        if ctx.level not in ('module', 'class', 'c_class', 'function', 'property', 'module_pxd', 'c_class_pxd', 'other'):
```
L2546  ⚪  (score=0)
```python
            s.error('decorator not allowed here')
```
L2547  ⚪  (score=0)
```python
        s.level = ctx.level
```
L2548  ⚪  (score=0)
```python
        decorators = p_decorators(s)
```
L2549  ⚪  (score=0)
```python
        if not ctx.allow_struct_enum_decorator and s.sy not in ('def', 'cdef', 'cpdef', 'class', 'async'):
```
L2550  ⚪  (score=0)
```python
            if s.sy == 'IDENT' and s.systring == 'async':
```
L2551  ⚪  (score=0)
```python
                pass  # handled below
```
L2552  ⚪  (score=0)
```python
            else:
```
L2553  ⚪  (score=0)
```python
                s.error("Decorators can only be followed by functions or classes")
```
L2554  ⚪  (score=0)
```python
    elif s.sy == 'pass' and cdef_flag:
```
L2555  ⚪  (score=0)
```python
        # empty cdef block
```
L2556  ⚪  (score=0)
```python
        return p_pass_statement(s, with_newline=True)
```
L2557  ⚪  (score=0)
```python
```
L2558  ⚪  (score=0)
```python
    overridable = False
```
L2559  ⚪  (score=0)
```python
    if s.sy == 'cdef':
```
L2560  ⚪  (score=0)
```python
        cdef_flag = True
```
L2561  ⚪  (score=0)
```python
        s.next()
```
L2562  ⚪  (score=0)
```python
    elif s.sy == 'cpdef':
```
L2563  ⚪  (score=0)
```python
        cdef_flag = True
```
L2564  ⚪  (score=0)
```python
        overridable = True
```
L2565  ⚪  (score=0)
```python
        s.next()
```
L2566  ⚪  (score=0)
```python
    if cdef_flag:
```
L2567  ⚪  (score=0)
```python
        if ctx.level not in ('module', 'module_pxd', 'function', 'c_class', 'c_class_pxd'):
```
L2568  ⚪  (score=0)
```python
            s.error('cdef statement not allowed here')
```
L2569  ⚪  (score=0)
```python
        s.level = ctx.level
```
L2570  ⚪  (score=0)
```python
        node = p_cdef_statement(s, pos, ctx(overridable=overridable))
```
L2571  ⚪  (score=0)
```python
        if decorators is not None:
```
L2572  ⚪  (score=0)
```python
            tup = (Nodes.CFuncDefNode, Nodes.CVarDefNode, Nodes.CClassDefNode)
```
L2573  ⚪  (score=0)
```python
            if ctx.allow_struct_enum_decorator:
```
L2574  ⚪  (score=0)
```python
                tup += (Nodes.CStructOrUnionDefNode, Nodes.CEnumDefNode)
```
L2575  ⚪  (score=0)
```python
            if not isinstance(node, tup):
```
L2576  ⚪  (score=0)
```python
                s.error("Decorators can only be followed by functions or classes")
```
L2577  ⚪  (score=0)
```python
            node.decorators = decorators
```
L2578  ⚪  (score=0)
```python
        return node
```
L2579  ⚪  (score=0)
```python
    else:
```
L2580  ⚪  (score=0)
```python
        if ctx.api:
```
L2581  ⚪  (score=0)
```python
            s.error("'api' not allowed with this statement", fatal=False)
```
L2582  ⚪  (score=0)
```python
        elif s.sy == 'def':
```
L2583  ⚪  (score=0)
```python
            # def statements aren't allowed in pxd files, except
```
L2584  ⚪  (score=0)
```python
            # as part of a cdef class
```
L2585  ⚪  (score=0)
```python
            if ('pxd' in ctx.level) and (ctx.level != 'c_class_pxd'):
```
L2586  ⚪  (score=0)
```python
                s.error('def statement not allowed here')
```
L2587  ⚪  (score=0)
```python
            s.level = ctx.level
```
L2588  ⚪  (score=0)
```python
            return p_def_statement(s, decorators)
```
L2589  ⚪  (score=0)
```python
        elif s.sy == 'class':
```
L2590  ⚪  (score=0)
```python
            if ctx.level not in ('module', 'function', 'class', 'other'):
```
L2591  ⚪  (score=0)
```python
                s.error("class definition not allowed here")
```
L2592  ⚪  (score=0)
```python
            return p_class_statement(s, decorators)
```
L2593  ⚪  (score=0)
```python
        elif s.sy == 'include':
```
L2594  ⚪  (score=0)
```python
            if ctx.level not in ('module', 'module_pxd'):
```
L2595  ⚪  (score=0)
```python
                s.error("include statement not allowed here")
```
L2596  ⚪  (score=0)
```python
            return p_include_statement(s, ctx)
```
L2597  ⚪  (score=0)
```python
        elif ctx.level == 'c_class' and s.sy == 'IDENT' and s.systring == 'property':
```
L2598  ⚪  (score=0)
```python
            return p_property_decl(s)
```
L2599  ⚪  (score=0)
```python
        elif s.sy == 'pass' and ctx.level != 'property':
```
L2600  ⚪  (score=0)
```python
            return p_pass_statement(s, with_newline=True)
```
L2601  ⚪  (score=0)
```python
        else:
```
L2602  ⚪  (score=0)
```python
            if ctx.level in ('c_class_pxd', 'property'):
```
L2603  ⚪  (score=0)
```python
                node = p_ignorable_statement(s)
```
L2604  ⚪  (score=0)
```python
                if node is not None:
```
L2605  ⚪  (score=0)
```python
                    return node
```
L2606  ⚪  (score=0)
```python
                s.error("Executable statement not allowed here")
```
L2607  ⚪  (score=0)
```python
            if s.sy == 'if':
```
L2608  ⚪  (score=0)
```python
                return p_if_statement(s)
```
L2609  ⚪  (score=0)
```python
            elif s.sy == 'while':
```
L2610  ⚪  (score=0)
```python
                return p_while_statement(s)
```
L2611  ⚪  (score=0)
```python
            elif s.sy == 'for':
```
L2612  ⚪  (score=0)
```python
                return p_for_statement(s)
```
L2613  ⚪  (score=0)
```python
            elif s.sy == 'try':
```
L2614  ⚪  (score=0)
```python
                return p_try_statement(s)
```
L2615  ⚪  (score=0)
```python
            elif s.sy == 'with':
```
L2616  ⚪  (score=0)
```python
                return p_with_statement(s)
```
L2617  ⚪  (score=0)
```python
            elif s.sy == 'async':
```
L2618  ⚪  (score=0)
```python
                s.next()
```
L2619  ⚪  (score=0)
```python
                return p_async_statement(s, ctx, decorators)
```
L2620  ⚪  (score=0)
```python
            else:
```
L2621  ⚪  (score=0)
```python
                if s.sy == 'IDENT' and s.systring == 'async':
```
L2622  ⚪  (score=0)
```python
                    ident_name = s.systring
```
L2623  ⚪  (score=0)
```python
                    ident_pos = s.position()
```
L2624  ⚪  (score=0)
```python
                    # PEP 492 enables the async/await keywords when it spots "async def ..."
```
L2625  ⚪  (score=0)
```python
                    s.next()
```
L2626  ⚪  (score=0)
```python
                    if s.sy == 'def':
```
L2627  ⚪  (score=0)
```python
                        return p_async_statement(s, ctx, decorators)
```
L2628  ⚪  (score=0)
```python
                    elif decorators:
```
L2629  ⚪  (score=0)
```python
                        s.error("Decorators can only be followed by functions or classes")
```
L2630  ⚪  (score=0)
```python
                    s.put_back('IDENT', ident_name, ident_pos)  # re-insert original token
```
L2631  ⚪  (score=0)
```python
                if s.sy == 'IDENT' and s.systring == 'match':
```
L2632  ⚪  (score=0)
```python
                    # p_match_statement returns None on a "soft" initial failure
```
L2633  ⚪  (score=0)
```python
                    match_statement = p_match_statement(s, ctx)
```
L2634  ⚪  (score=0)
```python
                    if match_statement is not None:
```
L2635  ⚪  (score=0)
```python
                        return match_statement
```
L2636  ⚪  (score=0)
```python
                return p_simple_statement_list(s, ctx, first_statement=first_statement)
```
L2637  ⚪  (score=0)
```python
```
L2638  ⚪  (score=0)
```python
```
L2639  ⚪  (score=0)
```python
@cython.cfunc
```
L2640  ⚪  (score=0)
```python
def p_statement_list(s: PyrexScanner, ctx, first_statement: cython.bint = 0):
```
L2641  ⚪  (score=0)
```python
    # Parse a series of statements separated by newlines.
```
L2642  ⚪  (score=0)
```python
    pos = s.position()
```
L2643  ⚪  (score=0)
```python
    stats = []
```
L2644  ⚪  (score=0)
```python
    while s.sy not in ('DEDENT', 'EOF'):
```
L2645  ⚪  (score=0)
```python
        stat = p_statement(s, ctx, first_statement = first_statement)
```
L2646  ⚪  (score=0)
```python
        if isinstance(stat, Nodes.PassStatNode):
```
L2647  ⚪  (score=0)
```python
            continue
```
L2648  ⚪  (score=0)
```python
        stats.append(stat)
```
L2649  ⚪  (score=0)
```python
        first_statement = False
```
L2650  ⚪  (score=0)
```python
    if not stats:
```
L2651  ⚪  (score=0)
```python
        return Nodes.PassStatNode(pos)
```
L2652  ⚪  (score=0)
```python
    elif len(stats) == 1:
```
L2653  ⚪  (score=0)
```python
        return stats[0]
```
L2654  ⚪  (score=0)
```python
    else:
```
L2655  ⚪  (score=0)
```python
        return Nodes.StatListNode(pos, stats = stats)
```
L2656  ⚪  (score=0)
```python
```
L2657  ⚪  (score=0)
```python
```
L2658  ⚪  (score=0)
```python
@cython.cfunc
```
L2659  ⚪  (score=0)
```python
def p_suite(s: PyrexScanner, ctx=Ctx()):
```
L2660  ⚪  (score=0)
```python
    return p_suite_with_docstring(s, ctx, with_doc_only=False)[1]
```
L2661  ⚪  (score=0)
```python
```
L2662  ⚪  (score=0)
```python
```
L2663  ⚪  (score=0)
```python
@cython.cfunc
```
L2664  ⚪  (score=0)
```python
def p_suite_with_docstring(s: PyrexScanner, ctx, with_doc_only: cython.bint = False) -> tuple:
```
L2665  ⚪  (score=0)
```python
    s.expect(':')
```
L2666  ⚪  (score=0)
```python
    doc = None
```
L2667  ⚪  (score=0)
```python
    if s.sy == 'NEWLINE':
```
L2668  ⚪  (score=0)
```python
        s.next()
```
L2669  ⚪  (score=0)
```python
        s.expect_indent()
```
L2670  ⚪  (score=0)
```python
        if with_doc_only:
```
L2671  ⚪  (score=0)
```python
            doc = p_doc_string(s)
```
L2672  ⚪  (score=0)
```python
        body = p_statement_list(s, ctx)
```
L2673  ⚪  (score=0)
```python
        s.expect_dedent()
```
L2674  ⚪  (score=0)
```python
    else:
```
L2675  ⚪  (score=0)
```python
        if ctx.api:
```
L2676  ⚪  (score=0)
```python
            s.error("'api' not allowed with this statement", fatal=False)
```
L2677  ⚪  (score=0)
```python
        if ctx.level in ('module', 'class', 'function', 'other'):
```
L2678  ⚪  (score=0)
```python
            body = p_simple_statement_list(s, ctx)
```
L2679  ⚪  (score=0)
```python
        else:
```
L2680  ⚪  (score=0)
```python
            body = p_pass_statement(s)
```
L2681  ⚪  (score=0)
```python
            s.expect_newline("Syntax error in declarations", ignore_semicolon=True)
```
L2682  ⚪  (score=0)
```python
    if not with_doc_only:
```
L2683  ⚪  (score=0)
```python
        doc, body = _extract_docstring(body)
```
L2684  ⚪  (score=0)
```python
    return doc, body
```
L2685  ⚪  (score=0)
```python
```
L2686  ⚪  (score=0)
```python
```
L2687  ⚪  (score=0)
```python
@cython.cfunc
```
L2688  ⚪  (score=0)
```python
def p_positional_and_keyword_args(s: PyrexScanner, end_sy_set, templates = None):
```
L2689  ⚪  (score=0)
```python
    """
```
L2690  ⚪  (score=0)
```python
    Parses positional and keyword arguments. end_sy_set
```
L2691  ⚪  (score=0)
```python
    should contain any s.sy that terminate the argument list.
```
L2692  ⚪  (score=0)
```python
    Argument expansion (* and **) are not allowed.
```
L2693  ⚪  (score=0)
```python
```
L2694  ⚪  (score=0)
```python
    Returns: (positional_args, keyword_args)
```
L2695  ⚪  (score=0)
```python
    """
```
L2696  ⚪  (score=0)
```python
    positional_args = []
```
L2697  ⚪  (score=0)
```python
    keyword_args = []
```
L2698  ⚪  (score=0)
```python
    pos_idx = 0
```
L2699  ⚪  (score=0)
```python
```
L2700  ⚪  (score=0)
```python
    while s.sy not in end_sy_set:
```
L2701  ⚪  (score=0)
```python
        if s.sy == '*' or s.sy == '**':
```
L2702  ⚪  (score=0)
```python
            s.error('Argument expansion not allowed here.', fatal=False)
```
L2703  ⚪  (score=0)
```python
```
L2704  ⚪  (score=0)
```python
        parsed_type = False
```
L2705  ⚪  (score=0)
```python
        if s.sy == 'IDENT' and s.peek()[0] == '=':
```
L2706  ⚪  (score=0)
```python
            ident = s.systring
```
L2707  ⚪  (score=0)
```python
            s.next()  # s.sy is '='
```
L2708  ⚪  (score=0)
```python
            s.next()
```
L2709  ⚪  (score=0)
```python
            if looking_at_expr(s):
```
L2710  ⚪  (score=0)
```python
                arg = p_test(s)
```
L2711  ⚪  (score=0)
```python
            else:
```
L2712  ⚪  (score=0)
```python
                base_type = p_c_base_type(s, templates = templates)
```
L2713  ⚪  (score=0)
```python
                declarator = p_c_declarator(s, empty=True)
```
L2714  ⚪  (score=0)
```python
                arg = Nodes.CComplexBaseTypeNode(base_type.pos,
```
L2715  ⚪  (score=0)
```python
                    base_type = base_type, declarator = declarator)
```
L2716  ⚪  (score=0)
```python
                parsed_type = True
```
L2717  ⚪  (score=0)
```python
            keyword_node = ExprNodes.IdentifierStringNode(arg.pos, value=ident)
```
L2718  ⚪  (score=0)
```python
            keyword_args.append((keyword_node, arg))
```
L2719  ⚪  (score=0)
```python
```
L2720  ⚪  (score=0)
```python
        else:
```
L2721  ⚪  (score=0)
```python
            if looking_at_expr(s):
```
L2722  ⚪  (score=0)
```python
                arg = p_test(s)
```
L2723  ⚪  (score=0)
```python
            else:
```
L2724  ⚪  (score=0)
```python
                base_type = p_c_base_type(s, templates = templates)
```
L2725  ⚪  (score=0)
```python
                declarator = p_c_declarator(s, empty=True)
```
L2726  ⚪  (score=0)
```python
                arg = Nodes.CComplexBaseTypeNode(base_type.pos,
```
L2727  ⚪  (score=0)
```python
                    base_type = base_type, declarator = declarator)
```
L2728  ⚪  (score=0)
```python
                parsed_type = True
```
L2729  ⚪  (score=0)
```python
            positional_args.append(arg)
```
L2730  ⚪  (score=0)
```python
            pos_idx += 1
```
L2731  ⚪  (score=0)
```python
            if len(keyword_args) > 0:
```
L2732  ⚪  (score=0)
```python
                s.error("Non-keyword arg following keyword arg",
```
L2733  ⚪  (score=0)
```python
                        pos=arg.pos)
```
L2734  ⚪  (score=0)
```python
```
L2735  ⚪  (score=0)
```python
        if s.sy != ',':
```
L2736  ⚪  (score=0)
```python
            if s.sy not in end_sy_set:
```
L2737  ⚪  (score=0)
```python
                if parsed_type:
```
L2738  ⚪  (score=0)
```python
                    s.error("Unmatched %s" % " or ".join(end_sy_set))
```
L2739  ⚪  (score=0)
```python
            break
```
L2740  ⚪  (score=0)
```python
        s.next()
```
L2741  ⚪  (score=0)
```python
    return positional_args, keyword_args
```
L2742  ⚪  (score=0)
```python
```
L2743  ⚪  (score=0)
```python
```
L2744  ⚪  (score=0)
```python
@cython.ccall
```
L2745  ⚪  (score=0)
```python
def p_c_base_type(s: PyrexScanner, nonempty: cython.bint = False, templates=None):
```
L2746  ⚪  (score=0)
```python
    if s.sy == '(':
```
L2747  ⚪  (score=0)
```python
        return p_c_complex_base_type(s, templates = templates)
```
L2748  ⚪  (score=0)
```python
    else:
```
L2749  ⚪  (score=0)
```python
        return p_c_simple_base_type(s, nonempty=nonempty, templates=templates)
```
L2750  ⚪  (score=0)
```python
```
L2751  ⚪  (score=0)
```python
```
L2752  ⚪  (score=0)
```python
@cython.cfunc
```
L2753  ⚪  (score=0)
```python
def p_calling_convention(s: PyrexScanner):
```
L2754  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring in calling_convention_words:
```
L2755  ⚪  (score=0)
```python
        result = s.systring
```
L2756  ⚪  (score=0)
```python
        s.next()
```
L2757  ⚪  (score=0)
```python
        return result
```
L2758  ⚪  (score=0)
```python
    else:
```
L2759  ⚪  (score=0)
```python
        return EncodedString("")
```
L2760  ⚪  (score=0)
```python
```
L2761  ⚪  (score=0)
```python
```
L2762  ⚪  (score=0)
```python
calling_convention_words = cython.declare(frozenset, frozenset((
```
L2763  ⚪  (score=0)
```python
    "__stdcall", "__cdecl", "__fastcall")))
```
L2764  ⚪  (score=0)
```python
```
L2765  ⚪  (score=0)
```python
```
L2766  ⚪  (score=0)
```python
@cython.cfunc
```
L2767  ⚪  (score=0)
```python
def p_c_complex_base_type(s: PyrexScanner, templates = None):
```
L2768  ⚪  (score=0)
```python
    # s.sy == '('
```
L2769  ⚪  (score=0)
```python
    pos = s.position()
```
L2770  ⚪  (score=0)
```python
    s.next()
```
L2771  ⚪  (score=0)
```python
    base_type = p_c_base_type(s, templates=templates)
```
L2772  ⚪  (score=0)
```python
    declarator = p_c_declarator(s, empty=True)
```
L2773  ⚪  (score=0)
```python
    type_node = Nodes.CComplexBaseTypeNode(
```
L2774  ⚪  (score=0)
```python
        pos, base_type=base_type, declarator=declarator)
```
L2775  ⚪  (score=0)
```python
    if s.sy == ',':
```
L2776  ⚪  (score=0)
```python
        components = [type_node]
```
L2777  ⚪  (score=0)
```python
        while s.sy == ',':
```
L2778  ⚪  (score=0)
```python
            s.next()
```
L2779  ⚪  (score=0)
```python
            if s.sy == ')':
```
L2780  ⚪  (score=0)
```python
                break
```
L2781  ⚪  (score=0)
```python
            base_type = p_c_base_type(s, templates=templates)
```
L2782  ⚪  (score=0)
```python
            declarator = p_c_declarator(s, empty=True)
```
L2783  ⚪  (score=0)
```python
            components.append(Nodes.CComplexBaseTypeNode(
```
L2784  ⚪  (score=0)
```python
                pos, base_type=base_type, declarator=declarator))
```
L2785  ⚪  (score=0)
```python
        type_node = Nodes.CTupleBaseTypeNode(pos, components = components)
```
L2786  ⚪  (score=0)
```python
```
L2787  ⚪  (score=0)
```python
    s.expect(')')
```
L2788  ⚪  (score=0)
```python
    if s.sy == '[':
```
L2789  ⚪  (score=0)
```python
        if is_memoryviewslice_access(s):
```
L2790  ⚪  (score=0)
```python
            type_node = p_memoryviewslice_access(s, type_node)
```
L2791  ⚪  (score=0)
```python
        else:
```
L2792  ⚪  (score=0)
```python
            type_node = p_buffer_or_template(s, type_node, templates)
```
L2793  ⚪  (score=0)
```python
    return type_node
```
L2794  ⚪  (score=0)
```python
```
L2795  ⚪  (score=0)
```python
```
L2796  ⚪  (score=0)
```python
@cython.cfunc
```
L2797  ⚪  (score=0)
```python
def p_c_simple_base_type(s: PyrexScanner, nonempty: cython.bint, templates=None):
```
L2798  ⚪  (score=0)
```python
    is_basic = False
```
L2799  ⚪  (score=0)
```python
    signed = 1
```
L2800  ⚪  (score=0)
```python
    longness = 0
```
L2801  ⚪  (score=0)
```python
    complex = False
```
L2802  ⚪  (score=0)
```python
    module_path = []
```
L2803  ⚪  (score=0)
```python
    pos = s.position()
```
L2804  ⚪  (score=0)
```python
```
L2805  ⚪  (score=0)
```python
    # Handle const/volatile
```
L2806  ⚪  (score=0)
```python
    is_const = is_volatile = False
```
L2807  ⚪  (score=0)
```python
    while s.sy == 'IDENT':
```
L2808  ⚪  (score=0)
```python
        if s.systring == 'const':
```
L2809  ⚪  (score=0)
```python
            if is_const: error(pos, "Duplicate 'const'")
```
L2810  ⚪  (score=0)
```python
            is_const = True
```
L2811  ⚪  (score=0)
```python
        elif s.systring == 'volatile':
```
L2812  ⚪  (score=0)
```python
            if is_volatile: error(pos, "Duplicate 'volatile'")
```
L2813  ⚪  (score=0)
```python
            is_volatile = True
```
L2814  ⚪  (score=0)
```python
        else:
```
L2815  ⚪  (score=0)
```python
            break
```
L2816  ⚪  (score=0)
```python
        s.next()
```
L2817  ⚪  (score=0)
```python
    if is_const or is_volatile:
```
L2818  ⚪  (score=0)
```python
        base_type = p_c_base_type(s, nonempty=nonempty, templates=templates)
```
L2819  ⚪  (score=0)
```python
        if isinstance(base_type, Nodes.MemoryViewSliceTypeNode):
```
L2820  ⚪  (score=0)
```python
            # reverse order to avoid having to write "(const int)[:]"
```
L2821  ⚪  (score=0)
```python
            base_type.base_type_node = Nodes.CConstOrVolatileTypeNode(pos,
```
L2822  ⚪  (score=0)
```python
                base_type=base_type.base_type_node, is_const=is_const, is_volatile=is_volatile)
```
L2823  ⚪  (score=0)
```python
            return base_type
```
L2824  ⚪  (score=0)
```python
        return Nodes.CConstOrVolatileTypeNode(pos,
```
L2825  ⚪  (score=0)
```python
            base_type=base_type, is_const=is_const, is_volatile=is_volatile)
```
L2826  ⚪  (score=0)
```python
```
L2827  ⚪  (score=0)
```python
    if s.sy != 'IDENT':
```
L2828  ⚪  (score=0)
```python
        error(pos, "Expected an identifier, found '%s'" % s.sy)
```
L2829  ⚪  (score=0)
```python
    if looking_at_base_type(s):
```
L2830  ⚪  (score=0)
```python
        #print "p_c_simple_base_type: looking_at_base_type at", s.position()
```
L2831  ⚪  (score=0)
```python
        is_basic = True
```
L2832  ⚪  (score=0)
```python
        if s.sy == 'IDENT' and s.systring in special_basic_c_types:
```
L2833  ⚪  (score=0)
```python
            signed, longness = special_basic_c_types[s.systring]
```
L2834  ⚪  (score=0)
```python
            name = s.systring
```
L2835  ⚪  (score=0)
```python
            s.next()
```
L2836  ⚪  (score=0)
```python
        else:
```
L2837  ⚪  (score=0)
```python
            signed, longness = p_sign_and_longness(s)
```
L2838  ⚪  (score=0)
```python
            if s.sy == 'IDENT' and s.systring in basic_c_type_names:
```
L2839  ⚪  (score=0)
```python
                name = s.systring
```
L2840  ⚪  (score=0)
```python
                s.next()
```
L2841  ⚪  (score=0)
```python
            else:
```
L2842  ⚪  (score=0)
```python
                name = 'int'  # long [int], short [int], long [int] complex, etc.
```
L2843  ⚪  (score=0)
```python
        if s.sy == 'IDENT' and s.systring == 'complex':
```
L2844  ⚪  (score=0)
```python
            complex = True
```
L2845  ⚪  (score=0)
```python
            s.next()
```
L2846  ⚪  (score=0)
```python
    elif looking_at_dotted_name(s):
```
L2847  ⚪  (score=0)
```python
        #print "p_c_simple_base_type: looking_at_type_name at", s.position()
```
L2848  ⚪  (score=0)
```python
        name = s.systring
```
L2849  ⚪  (score=0)
```python
        s.next()
```
L2850  ⚪  (score=0)
```python
        while s.sy == '.':
```
L2851  ⚪  (score=0)
```python
            module_path.append(name)
```
L2852  ⚪  (score=0)
```python
            s.next()
```
L2853  ⚪  (score=0)
```python
            name = p_ident(s)
```
L2854  ⚪  (score=0)
```python
    else:
```
L2855  ⚪  (score=0)
```python
        name = s.systring
```
L2856  ⚪  (score=0)
```python
        name_pos = s.position()
```
L2857  ⚪  (score=0)
```python
        s.next()
```
L2858  ⚪  (score=0)
```python
        if nonempty and s.sy != 'IDENT':
```
L2859  ⚪  (score=0)
```python
            # Make sure this is not a declaration of a variable or function.
```
L2860  ⚪  (score=0)
```python
            if s.sy == '(':
```
L2861  ⚪  (score=0)
```python
                old_pos = s.position()
```
L2862  ⚪  (score=0)
```python
                s.next()
```
L2863  ⚪  (score=0)
```python
                if (s.sy == '*' or s.sy == '**' or s.sy == '&'
```
L2864  ⚪  (score=0)
```python
                        or (s.sy == 'IDENT' and s.systring in calling_convention_words)):
```
L2865  ⚪  (score=0)
```python
                    s.put_back('(', '(', old_pos)
```
L2866  ⚪  (score=0)
```python
                else:
```
L2867  ⚪  (score=0)
```python
                    s.put_back('(', '(', old_pos)
```
L2868  ⚪  (score=0)
```python
                    s.put_back('IDENT', name, name_pos)
```
L2869  ⚪  (score=0)
```python
                    name = None
```
L2870  ⚪  (score=0)
```python
            elif s.sy not in ('*', '**', '[', '&'):
```
L2871  ⚪  (score=0)
```python
                s.put_back('IDENT', name, name_pos)
```
L2872  ⚪  (score=0)
```python
                name = None
```
L2873  ⚪  (score=0)
```python
```
L2874  ⚪  (score=0)
```python
    type_node = Nodes.CSimpleBaseTypeNode(pos,
```
L2875  ⚪  (score=0)
```python
        name = name, module_path = module_path,
```
L2876  ⚪  (score=0)
```python
        is_basic_c_type = is_basic, signed = signed,
```
L2877  ⚪  (score=0)
```python
        complex = complex, longness = longness,
```
L2878  ⚪  (score=0)
```python
        templates = templates)
```
L2879  ⚪  (score=0)
```python
```
L2880  ⚪  (score=0)
```python
    #    declarations here.
```
L2881  ⚪  (score=0)
```python
    if s.sy == '[':
```
L2882  ⚪  (score=0)
```python
        if is_memoryviewslice_access(s):
```
L2883  ⚪  (score=0)
```python
            type_node = p_memoryviewslice_access(s, type_node)
```
L2884  ⚪  (score=0)
```python
        else:
```
L2885  ⚪  (score=0)
```python
            type_node = p_buffer_or_template(s, type_node, templates)
```
L2886  ⚪  (score=0)
```python
```
L2887  ⚪  (score=0)
```python
    if s.sy == '.':
```
L2888  ⚪  (score=0)
```python
        s.next()
```
L2889  ⚪  (score=0)
```python
        name = p_ident(s)
```
L2890  ⚪  (score=0)
```python
        type_node = Nodes.CNestedBaseTypeNode(pos, base_type = type_node, name = name)
```
L2891  ⚪  (score=0)
```python
```
L2892  ⚪  (score=0)
```python
    return type_node
```
L2893  ⚪  (score=0)
```python
```
L2894  ⚪  (score=0)
```python
```
L2895  ⚪  (score=0)
```python
@cython.cfunc
```
L2896  ⚪  (score=0)
```python
def p_buffer_or_template(s: PyrexScanner, base_type_node, templates):
```
L2897  ⚪  (score=0)
```python
    # s.sy == '['
```
L2898  ⚪  (score=0)
```python
    pos = s.position()
```
L2899  ⚪  (score=0)
```python
    s.next()
```
L2900  ⚪  (score=0)
```python
    # Note that buffer_positional_options_count=1, so the only positional argument is dtype.
```
L2901  ⚪  (score=0)
```python
    # For templated types, all parameters are types.
```
L2902  ⚪  (score=0)
```python
    positional_args, keyword_args = (
```
L2903  ⚪  (score=0)
```python
        p_positional_and_keyword_args(s, (']',), templates)
```
L2904  ⚪  (score=0)
```python
    )
```
L2905  ⚪  (score=0)
```python
    s.expect(']')
```
L2906  ⚪  (score=0)
```python
```
L2907  ⚪  (score=0)
```python
    if s.sy == '[':
```
L2908  ⚪  (score=0)
```python
        base_type_node = p_buffer_or_template(s, base_type_node, templates)
```
L2909  ⚪  (score=0)
```python
```
L2910  ⚪  (score=0)
```python
    keyword_dict = ExprNodes.DictNode(pos,
```
L2911  ⚪  (score=0)
```python
        key_value_pairs = [
```
L2912  ⚪  (score=0)
```python
            ExprNodes.DictItemNode(pos=key.pos, key=key, value=value)
```
L2913  ⚪  (score=0)
```python
            for key, value in keyword_args
```
L2914  ⚪  (score=0)
```python
        ])
```
L2915  ⚪  (score=0)
```python
    result = Nodes.TemplatedTypeNode(pos,
```
L2916  ⚪  (score=0)
```python
        positional_args = positional_args,
```
L2917  ⚪  (score=0)
```python
        keyword_args = keyword_dict,
```
L2918  ⚪  (score=0)
```python
        base_type_node = base_type_node)
```
L2919  ⚪  (score=0)
```python
    return result
```
L2920  ⚪  (score=0)
```python
```
L2921  ⚪  (score=0)
```python
```
L2922  ⚪  (score=0)
```python
@cython.cfunc
```
L2923  ⚪  (score=0)
```python
def is_memoryviewslice_access(s: PyrexScanner) -> cython.bint:
```
L2924  ⚪  (score=0)
```python
    # s.sy == '['
```
L2925  ⚪  (score=0)
```python
    # a memoryview slice declaration is distinguishable from a buffer access
```
L2926  ⚪  (score=0)
```python
    # declaration by the first entry in the bracketed list.  The buffer will
```
L2927  ⚪  (score=0)
```python
    # not have an unnested colon in the first entry; the memoryview slice will.
```
L2928  ⚪  (score=0)
```python
    saved = [(s.sy, s.systring, s.position())]
```
L2929  ⚪  (score=0)
```python
    s.next()
```
L2930  ⚪  (score=0)
```python
    retval = False
```
L2931  ⚪  (score=0)
```python
    if s.systring == ':':
```
L2932  ⚪  (score=0)
```python
        retval = True
```
L2933  ⚪  (score=0)
```python
    elif s.sy == 'INT':
```
L2934  ⚪  (score=0)
```python
        saved.append((s.sy, s.systring, s.position()))
```
L2935  ⚪  (score=0)
```python
        s.next()
```
L2936  ⚪  (score=0)
```python
        if s.sy == ':':
```
L2937  ⚪  (score=0)
```python
            retval = True
```
L2938  ⚪  (score=0)
```python
```
L2939  ⚪  (score=0)
```python
    for sv in reversed(saved):
```
L2940  ⚪  (score=0)
```python
        s.put_back(*sv)
```
L2941  ⚪  (score=0)
```python
```
L2942  ⚪  (score=0)
```python
    return retval
```
L2943  ⚪  (score=0)
```python
```
L2944  ⚪  (score=0)
```python
```
L2945  ⚪  (score=0)
```python
@cython.cfunc
```
L2946  ⚪  (score=0)
```python
def p_memoryviewslice_access(s: PyrexScanner, base_type_node):
```
L2947  ⚪  (score=0)
```python
    # s.sy == '['
```
L2948  ⚪  (score=0)
```python
    pos = s.position()
```
L2949  ⚪  (score=0)
```python
    s.next()
```
L2950  ⚪  (score=0)
```python
    subscripts, _ = p_subscript_list(s)
```
L2951  ⚪  (score=0)
```python
    # make sure each entry in subscripts is a slice
```
L2952  ⚪  (score=0)
```python
    for subscript in subscripts:
```
L2953  ⚪  (score=0)
```python
        if len(subscript) < 2:
```
L2954  ⚪  (score=0)
```python
            s.error("An axis specification in memoryview declaration does not have a ':'.")
```
L2955  ⚪  (score=0)
```python
    s.expect(']')
```
L2956  ⚪  (score=0)
```python
    indexes = make_slice_nodes(pos, subscripts)
```
L2957  ⚪  (score=0)
```python
    result = Nodes.MemoryViewSliceTypeNode(pos,
```
L2958  ⚪  (score=0)
```python
            base_type_node = base_type_node,
```
L2959  ⚪  (score=0)
```python
            axes = indexes)
```
L2960  ⚪  (score=0)
```python
    return result
```
L2961  ⚪  (score=0)
```python
```
L2962  ⚪  (score=0)
```python
```
L2963  ⚪  (score=0)
```python
@cython.cfunc
```
L2964  ⚪  (score=0)
```python
def looking_at_name(s: PyrexScanner) -> cython.bint:
```
L2965  ⚪  (score=0)
```python
    return s.sy == 'IDENT' and s.systring not in calling_convention_words
```
L2966  ⚪  (score=0)
```python
```
L2967  ⚪  (score=0)
```python
```
L2968  ⚪  (score=0)
```python
@cython.cfunc
```
L2969  ⚪  (score=0)
```python
def looking_at_expr(s: PyrexScanner) -> cython.bint:
```
L2970  ⚪  (score=0)
```python
    if s.systring in base_type_start_words:
```
L2971  ⚪  (score=0)
```python
        return False
```
L2972  ⚪  (score=0)
```python
    elif s.sy == 'IDENT':
```
L2973  ⚪  (score=0)
```python
        is_type = False
```
L2974  ⚪  (score=0)
```python
        name = s.systring
```
L2975  ⚪  (score=0)
```python
        name_pos = s.position()
```
L2976  ⚪  (score=0)
```python
        dotted_path = []
```
L2977  ⚪  (score=0)
```python
        s.next()
```
L2978  ⚪  (score=0)
```python
```
L2979  ⚪  (score=0)
```python
        while s.sy == '.':
```
L2980  ⚪  (score=0)
```python
            s.next()
```
L2981  ⚪  (score=0)
```python
            dotted_path.append((s.systring, s.position()))
```
L2982  ⚪  (score=0)
```python
            s.expect('IDENT')
```
L2983  ⚪  (score=0)
```python
```
L2984  ⚪  (score=0)
```python
        saved = s.sy, s.systring, s.position()
```
L2985  ⚪  (score=0)
```python
        if s.sy == 'IDENT':
```
L2986  ⚪  (score=0)
```python
            is_type = True
```
L2987  ⚪  (score=0)
```python
        elif s.sy == '*' or s.sy == '**':
```
L2988  ⚪  (score=0)
```python
            s.next()
```
L2989  ⚪  (score=0)
```python
            is_type = s.sy in (')', ']')
```
L2990  ⚪  (score=0)
```python
            s.put_back(*saved)
```
L2991  ⚪  (score=0)
```python
        elif s.sy == '(':
```
L2992  ⚪  (score=0)
```python
            s.next()
```
L2993  ⚪  (score=0)
```python
            is_type = s.sy == '*'
```
L2994  ⚪  (score=0)
```python
            s.put_back(*saved)
```
L2995  ⚪  (score=0)
```python
        elif s.sy == '[':
```
L2996  ⚪  (score=0)
```python
            s.next()
```
L2997  ⚪  (score=0)
```python
            is_type = s.sy == ']' or not looking_at_expr(s)  # could be a nested template type
```
L2998  ⚪  (score=0)
```python
            s.put_back(*saved)
```
L2999  ⚪  (score=0)
```python
```
L3000  ⚪  (score=0)
```python
        dotted_path.reverse()
```
L3001  ⚪  (score=0)
```python
        for p in dotted_path:
```
L3002  ⚪  (score=0)
```python
            s.put_back('IDENT', *p)
```
L3003  ⚪  (score=0)
```python
            s.put_back('.', '.', p[1])  # gets the position slightly wrong
```
L3004  ⚪  (score=0)
```python
```
L3005  ⚪  (score=0)
```python
        s.put_back('IDENT', name, name_pos)
```
L3006  ⚪  (score=0)
```python
        return not is_type and saved[0]
```
L3007  ⚪  (score=0)
```python
    else:
```
L3008  ⚪  (score=0)
```python
        return True
```
L3009  ⚪  (score=0)
```python
```
L3010  ⚪  (score=0)
```python
```
L3011  ⚪  (score=0)
```python
@cython.cfunc
```
L3012  ⚪  (score=0)
```python
def looking_at_base_type(s: PyrexScanner) -> cython.bint:
```
L3013  ⚪  (score=0)
```python
    #print "looking_at_base_type?", s.sy, s.systring, s.position()
```
L3014  ⚪  (score=0)
```python
    return s.sy == 'IDENT' and s.systring in base_type_start_words
```
L3015  ⚪  (score=0)
```python
```
L3016  ⚪  (score=0)
```python
```
L3017  ⚪  (score=0)
```python
@cython.cfunc
```
L3018  ⚪  (score=0)
```python
def looking_at_dotted_name(s: PyrexScanner) -> cython.bint:
```
L3019  ⚪  (score=0)
```python
    if s.sy == 'IDENT':
```
L3020  ⚪  (score=0)
```python
        name = s.systring
```
L3021  ⚪  (score=0)
```python
        name_pos = s.position()
```
L3022  ⚪  (score=0)
```python
        s.next()
```
L3023  ⚪  (score=0)
```python
        result: cython.bint = s.sy == '.'
```
L3024  ⚪  (score=0)
```python
        s.put_back('IDENT', name, name_pos)
```
L3025  ⚪  (score=0)
```python
        return result
```
L3026  ⚪  (score=0)
```python
    else:
```
L3027  ⚪  (score=0)
```python
        return False
```
L3028  ⚪  (score=0)
```python
```
L3029  ⚪  (score=0)
```python
```
L3030  ⚪  (score=0)
```python
basic_c_type_names = cython.declare(frozenset, frozenset((
```
L3031  ⚪  (score=0)
```python
    "void", "char", "int", "float", "double", "bint")))
```
L3032  ⚪  (score=0)
```python
```
L3033  ⚪  (score=0)
```python
special_basic_c_types = cython.declare(dict, {
```
L3034  ⚪  (score=0)
```python
    # name : (signed, longness)
```
L3035  ⚪  (score=0)
```python
    "Py_UNICODE" : (0, 0),
```
L3036  ⚪  (score=0)
```python
    "Py_UCS4"    : (0, 0),
```
L3037  ⚪  (score=0)
```python
    "Py_hash_t"  : (2, 0),
```
L3038  ⚪  (score=0)
```python
    "Py_ssize_t" : (2, 0),
```
L3039  ⚪  (score=0)
```python
    "ssize_t"    : (2, 0),
```
L3040  ⚪  (score=0)
```python
    "size_t"     : (0, 0),
```
L3041  ⚪  (score=0)
```python
    "ptrdiff_t"  : (2, 0),
```
L3042  ⚪  (score=0)
```python
    "Py_tss_t"   : (1, 0),
```
L3043  ⚪  (score=0)
```python
})
```
L3044  ⚪  (score=0)
```python
```
L3045  ⚪  (score=0)
```python
sign_and_longness_words = cython.declare(frozenset, frozenset((
```
L3046  ⚪  (score=0)
```python
    "short", "long", "signed", "unsigned")))
```
L3047  ⚪  (score=0)
```python
```
L3048  ⚪  (score=0)
```python
base_type_start_words = cython.declare(
```
L3049  ⚪  (score=0)
```python
    frozenset,
```
L3050  ⚪  (score=0)
```python
    basic_c_type_names
```
L3051  ⚪  (score=0)
```python
    | sign_and_longness_words
```
L3052  ⚪  (score=0)
```python
    | frozenset(special_basic_c_types))
```
L3053  ⚪  (score=0)
```python
```
L3054  ⚪  (score=0)
```python
struct_enum_union = cython.declare(frozenset, frozenset((
```
L3055  ⚪  (score=0)
```python
    "struct", "union", "enum", "packed")))
```
L3056  ⚪  (score=0)
```python
```
L3057  ⚪  (score=0)
```python
```
L3058  ⚪  (score=0)
```python
@cython.cfunc
```
L3059  ⚪  (score=0)
```python
def p_sign_and_longness(s: PyrexScanner) -> tuple:
```
L3060  ⚪  (score=0)
```python
    signed = 1
```
L3061  ⚪  (score=0)
```python
    longness = 0
```
L3062  ⚪  (score=0)
```python
    while s.sy == 'IDENT' and s.systring in sign_and_longness_words:
```
L3063  ⚪  (score=0)
```python
        if s.systring == 'unsigned':
```
L3064  ⚪  (score=0)
```python
            signed = 0
```
L3065  ⚪  (score=0)
```python
        elif s.systring == 'signed':
```
L3066  ⚪  (score=0)
```python
            signed = 2
```
L3067  ⚪  (score=0)
```python
        elif s.systring == 'short':
```
L3068  ⚪  (score=0)
```python
            longness = -1
```
L3069  ⚪  (score=0)
```python
        elif s.systring == 'long':
```
L3070  ⚪  (score=0)
```python
            longness += 1
```
L3071  ⚪  (score=0)
```python
        s.next()
```
L3072  ⚪  (score=0)
```python
    return signed, longness
```
L3073  ⚪  (score=0)
```python
```
L3074  ⚪  (score=0)
```python
```
L3075  ⚪  (score=0)
```python
@cython.cfunc
```
L3076  ⚪  (score=0)
```python
def p_opt_cname(s: PyrexScanner):
```
L3077  ⚪  (score=0)
```python
    literal = p_opt_string_literal(s, 'u')
```
L3078  ⚪  (score=0)
```python
    if literal is not None:
```
L3079  ⚪  (score=0)
```python
        cname = EncodedString(literal)
```
L3080  ⚪  (score=0)
```python
        cname.encoding = s.source_encoding
```
L3081  ⚪  (score=0)
```python
    else:
```
L3082  ⚪  (score=0)
```python
        cname = None
```
L3083  ⚪  (score=0)
```python
    return cname
```
L3084  ⚪  (score=0)
```python
```
L3085  ⚪  (score=0)
```python
```
L3086  ⚪  (score=0)
```python
@cython.ccall
```
L3087  ⚪  (score=0)
```python
def p_c_declarator(s: PyrexScanner, ctx = Ctx(),
```
L3088  ⚪  (score=0)
```python
                   empty: cython.bint = False, is_type: cython.bint = False, cmethod_flag: cython.bint = False,
```
L3089  ⚪  (score=0)
```python
                   assignable: cython.bint = False, nonempty: cython.bint = False,
```
L3090  ⚪  (score=0)
```python
                   calling_convention_allowed: cython.bint = False):
```
L3091  ⚪  (score=0)
```python
    # If empty is true, the declarator must be empty. If nonempty is true,
```
L3092  ⚪  (score=0)
```python
    # the declarator must be nonempty. Otherwise we don't care.
```
L3093  ⚪  (score=0)
```python
    # If cmethod_flag is true, then if this declarator declares
```
L3094  ⚪  (score=0)
```python
    # a function, it's a C method of an extension type.
```
L3095  ⚪  (score=0)
```python
    pos = s.position()
```
L3096  ⚪  (score=0)
```python
    if s.sy == '(':
```
L3097  ⚪  (score=0)
```python
        s.next()
```
L3098  ⚪  (score=0)
```python
        if s.sy == ')' or looking_at_name(s):
```
L3099  ⚪  (score=0)
```python
            base = Nodes.CNameDeclaratorNode(pos, name=s.context.intern_ustring(""), cname=None)
```
L3100  ⚪  (score=0)
```python
            result = p_c_func_declarator(s, pos, ctx, base, cmethod_flag)
```
L3101  ⚪  (score=0)
```python
        else:
```
L3102  ⚪  (score=0)
```python
            result = p_c_declarator(s, ctx, empty = empty, is_type = is_type,
```
L3103  ⚪  (score=0)
```python
                                    cmethod_flag = cmethod_flag,
```
L3104  ⚪  (score=0)
```python
                                    nonempty = nonempty,
```
L3105  ⚪  (score=0)
```python
                                    calling_convention_allowed = True)
```
L3106  ⚪  (score=0)
```python
            s.expect(')')
```
L3107  ⚪  (score=0)
```python
    else:
```
L3108  ⚪  (score=0)
```python
        result = p_c_simple_declarator(s, ctx, empty, is_type, cmethod_flag,
```
L3109  ⚪  (score=0)
```python
                                       assignable, nonempty)
```
L3110  ⚪  (score=0)
```python
    if not calling_convention_allowed and result.calling_convention and s.sy != '(':
```
L3111  ⚪  (score=0)
```python
        error(s.position(), "%s on something that is not a function"
```
L3112  ⚪  (score=0)
```python
            % result.calling_convention)
```
L3113  ⚪  (score=0)
```python
    while s.sy in ('[', '('):
```
L3114  ⚪  (score=0)
```python
        pos = s.position()
```
L3115  ⚪  (score=0)
```python
        if s.sy == '[':
```
L3116  ⚪  (score=0)
```python
            result = p_c_array_declarator(s, result)
```
L3117  ⚪  (score=0)
```python
        else:  # sy == '('
```
L3118  ⚪  (score=0)
```python
            s.next()
```
L3119  ⚪  (score=0)
```python
            result = p_c_func_declarator(s, pos, ctx, result, cmethod_flag)
```
L3120  ⚪  (score=0)
```python
        cmethod_flag = 0
```
L3121  ⚪  (score=0)
```python
    return result
```
L3122  ⚪  (score=0)
```python
```
L3123  ⚪  (score=0)
```python
```
L3124  ⚪  (score=0)
```python
@cython.cfunc
```
L3125  ⚪  (score=0)
```python
def p_c_array_declarator(s: PyrexScanner, base):
```
L3126  ⚪  (score=0)
```python
    pos = s.position()
```
L3127  ⚪  (score=0)
```python
    s.next()  # '['
```
L3128  ⚪  (score=0)
```python
    if s.sy != ']':
```
L3129  ⚪  (score=0)
```python
        dim = p_testlist(s)
```
L3130  ⚪  (score=0)
```python
    else:
```
L3131  ⚪  (score=0)
```python
        dim = None
```
L3132  ⚪  (score=0)
```python
    s.expect(']')
```
L3133  ⚪  (score=0)
```python
    return Nodes.CArrayDeclaratorNode(pos, base = base, dimension = dim)
```
L3134  ⚪  (score=0)
```python
```
L3135  ⚪  (score=0)
```python
```
L3136  ⚪  (score=0)
```python
@cython.cfunc
```
L3137  ⚪  (score=0)
```python
def p_c_func_declarator(s: PyrexScanner, pos, ctx, base, cmethod_flag: cython.bint):
```
L3138  ⚪  (score=0)
```python
    # Opening paren has already been skipped
```
L3139  ⚪  (score=0)
```python
    args = p_c_arg_list(s, ctx, cmethod_flag = cmethod_flag,
```
L3140  ⚪  (score=0)
```python
                        nonempty_declarators = 0)
```
L3141  ⚪  (score=0)
```python
    ellipsis = p_optional_ellipsis(s)
```
L3142  ⚪  (score=0)
```python
    s.expect(')')
```
L3143  ⚪  (score=0)
```python
    nogil = p_nogil(s)
```
L3144  ⚪  (score=0)
```python
    exc_val, exc_check, exc_clause = p_exception_value_clause(s, ctx.visibility == 'extern')
```
L3145  ⚪  (score=0)
```python
    if nogil and exc_clause:
```
L3146  ⚪  (score=0)
```python
        warning(
```
L3147  ⚪  (score=0)
```python
            s.position(),
```
L3148  ⚪  (score=0)
```python
            "The keyword 'nogil' should appear at the end of the "
```
L3149  ⚪  (score=0)
```python
            "function signature line. Placing it before 'except' "
```
L3150  ⚪  (score=0)
```python
            "or 'noexcept' will be disallowed in a future version "
```
L3151  ⚪  (score=0)
```python
            "of Cython.",
```
L3152  ⚪  (score=0)
```python
            level=2
```
L3153  ⚪  (score=0)
```python
        )
```
L3154  ⚪  (score=0)
```python
    nogil = nogil or p_nogil(s)
```
L3155  ⚪  (score=0)
```python
    with_gil = p_with_gil(s)
```
L3156  ⚪  (score=0)
```python
    return Nodes.CFuncDeclaratorNode(pos,
```
L3157  ⚪  (score=0)
```python
        base = base, args = args, has_varargs = ellipsis,
```
L3158  ⚪  (score=0)
```python
        exception_value = exc_val, exception_check = exc_check,
```
L3159  ⚪  (score=0)
```python
        nogil = nogil or ctx.nogil or with_gil, with_gil = with_gil, has_explicit_exc_clause=exc_clause)
```
L3160  ⚪  (score=0)
```python
```
L3161  ⚪  (score=0)
```python
```
L3162  ⚪  (score=0)
```python
supported_overloaded_operators = cython.declare(frozenset, frozenset((
```
L3163  ⚪  (score=0)
```python
    '+', '-', '*', '/', '%',
```
L3164  ⚪  (score=0)
```python
    '++', '--', '~', '|', '&', '^', '<<', '>>', ',',
```
L3165  ⚪  (score=0)
```python
    '==', '!=', '>=', '>', '<=', '<',
```
L3166  ⚪  (score=0)
```python
    '[]', '()', '!', '=',
```
L3167  ⚪  (score=0)
```python
    'bool',
```
L3168  ⚪  (score=0)
```python
)))
```
L3169  ⚪  (score=0)
```python
```
L3170  ⚪  (score=0)
```python
```
L3171  ⚪  (score=0)
```python
@cython.cfunc
```
L3172  ⚪  (score=0)
```python
def p_c_simple_declarator(s: PyrexScanner, ctx,
```
L3173  ⚪  (score=0)
```python
                          empty: cython.bint, is_type: cython.bint, cmethod_flag: cython.bint,
```
L3174  ⚪  (score=0)
```python
                          assignable: cython.bint, nonempty: cython.bint):
```
L3175  ⚪  (score=0)
```python
    pos = s.position()
```
L3176  ⚪  (score=0)
```python
    calling_convention = p_calling_convention(s)
```
L3177  ⚪  (score=0)
```python
    if s.sy in ('*', '**'):
```
L3178  ⚪  (score=0)
```python
        # scanner returns '**' as a single token
```
L3179  ⚪  (score=0)
```python
        is_ptrptr = s.sy == '**'
```
L3180  ⚪  (score=0)
```python
        s.next()
```
L3181  ⚪  (score=0)
```python
```
L3182  ⚪  (score=0)
```python
        const_pos = s.position()
```
L3183  ⚪  (score=0)
```python
        is_const = s.systring == 'const' and s.sy == 'IDENT'
```
L3184  ⚪  (score=0)
```python
        if is_const:
```
L3185  ⚪  (score=0)
```python
            s.next()
```
L3186  ⚪  (score=0)
```python
```
L3187  ⚪  (score=0)
```python
        base = p_c_declarator(s, ctx, empty=empty, is_type=is_type,
```
L3188  ⚪  (score=0)
```python
                              cmethod_flag=cmethod_flag,
```
L3189  ⚪  (score=0)
```python
                              assignable=assignable, nonempty=nonempty)
```
L3190  ⚪  (score=0)
```python
        if is_const:
```
L3191  ⚪  (score=0)
```python
            base = Nodes.CConstDeclaratorNode(const_pos, base=base)
```
L3192  ⚪  (score=0)
```python
        if is_ptrptr:
```
L3193  ⚪  (score=0)
```python
            base = Nodes.CPtrDeclaratorNode(pos, base=base)
```
L3194  ⚪  (score=0)
```python
        result = Nodes.CPtrDeclaratorNode(pos, base=base)
```
L3195  ⚪  (score=0)
```python
    elif s.sy == '&' or (s.sy == '&&' and s.context.cpp):
```
L3196  ⚪  (score=0)
```python
        node_class = Nodes.CppRvalueReferenceDeclaratorNode if s.sy == '&&' else Nodes.CReferenceDeclaratorNode
```
L3197  ⚪  (score=0)
```python
        s.next()
```
L3198  ⚪  (score=0)
```python
        base = p_c_declarator(s, ctx, empty=empty, is_type=is_type,
```
L3199  ⚪  (score=0)
```python
                              cmethod_flag=cmethod_flag,
```
L3200  ⚪  (score=0)
```python
                              assignable=assignable, nonempty=nonempty)
```
L3201  ⚪  (score=0)
```python
        result = node_class(pos, base=base)
```
L3202  ⚪  (score=0)
```python
    else:
```
L3203  ⚪  (score=0)
```python
        rhs = None
```
L3204  ⚪  (score=0)
```python
        if s.sy == 'IDENT':
```
L3205  ⚪  (score=0)
```python
            name = s.systring
```
L3206  ⚪  (score=0)
```python
            if empty:
```
L3207  ⚪  (score=0)
```python
                error(s.position(), "Declarator should be empty")
```
L3208  ⚪  (score=0)
```python
            s.next()
```
L3209  ⚪  (score=0)
```python
            cname = p_opt_cname(s)
```
L3210  ⚪  (score=0)
```python
            if name != 'operator' and s.sy == '=' and assignable:
```
L3211  ⚪  (score=0)
```python
                s.next()
```
L3212  ⚪  (score=0)
```python
                rhs = p_test(s)
```
L3213  ⚪  (score=0)
```python
        else:
```
L3214  ⚪  (score=0)
```python
            if nonempty:
```
L3215  ⚪  (score=0)
```python
                error(s.position(), "Empty declarator")
```
L3216  ⚪  (score=0)
```python
            name = ""
```
L3217  ⚪  (score=0)
```python
            cname = None
```
L3218  ⚪  (score=0)
```python
        if cname is None and ctx.namespace is not None and nonempty:
```
L3219  ⚪  (score=0)
```python
            cname = ctx.namespace + "::" + name
```
L3220  ⚪  (score=0)
```python
        if name == 'operator' and ctx.visibility == 'extern' and nonempty:
```
L3221  ⚪  (score=0)
```python
            op = s.sy
```
L3222  ⚪  (score=0)
```python
            if [1 for c in op if c in '+-*/<=>!%&|([^~,']:
```
L3223  ⚪  (score=0)
```python
                s.next()
```
L3224  ⚪  (score=0)
```python
                # Handle diphthong operators.
```
L3225  ⚪  (score=0)
```python
                if op == '(':
```
L3226  ⚪  (score=0)
```python
                    s.expect(')')
```
L3227  ⚪  (score=0)
```python
                    op = '()'
```
L3228  ⚪  (score=0)
```python
                elif op == '[':
```
L3229  ⚪  (score=0)
```python
                    s.expect(']')
```
L3230  ⚪  (score=0)
```python
                    op = '[]'
```
L3231  ⚪  (score=0)
```python
                elif op in ('-', '+', '|', '&') and s.sy == op:
```
L3232  ⚪  (score=0)
```python
                    op *= 2       # ++, --, ...
```
L3233  ⚪  (score=0)
```python
                    s.next()
```
L3234  ⚪  (score=0)
```python
                elif s.sy == '=':
```
L3235  ⚪  (score=0)
```python
                    op += s.sy    # +=, -=, ...
```
L3236  ⚪  (score=0)
```python
                    s.next()
```
L3237  ⚪  (score=0)
```python
                if op not in supported_overloaded_operators:
```
L3238  ⚪  (score=0)
```python
                    s.error("Overloading operator '%s' not yet supported." % op,
```
L3239  ⚪  (score=0)
```python
                            fatal=False)
```
L3240  ⚪  (score=0)
```python
                name += op
```
L3241  ⚪  (score=0)
```python
            elif op == 'IDENT':
```
L3242  ⚪  (score=0)
```python
                op = s.systring
```
L3243  ⚪  (score=0)
```python
                if op not in supported_overloaded_operators:
```
L3244  ⚪  (score=0)
```python
                    s.error("Overloading operator '%s' not yet supported." % op,
```
L3245  ⚪  (score=0)
```python
                            fatal=False)
```
L3246  ⚪  (score=0)
```python
                name = name + ' ' + op
```
L3247  ⚪  (score=0)
```python
                s.next()
```
L3248  ⚪  (score=0)
```python
        result = Nodes.CNameDeclaratorNode(pos,
```
L3249  ⚪  (score=0)
```python
            name = name, cname = cname, default = rhs)
```
L3250  ⚪  (score=0)
```python
    result.calling_convention = calling_convention
```
L3251  ⚪  (score=0)
```python
    return result
```
L3252  ⚪  (score=0)
```python
```
L3253  ⚪  (score=0)
```python
```
L3254  ⚪  (score=0)
```python
@cython.cfunc
```
L3255  ⚪  (score=0)
```python
def p_nogil(s: PyrexScanner) -> cython.bint:
```
L3256  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == 'nogil':
```
L3257  ⚪  (score=0)
```python
        s.next()
```
L3258  ⚪  (score=0)
```python
        return True
```
L3259  ⚪  (score=0)
```python
    else:
```
L3260  ⚪  (score=0)
```python
        return False
```
L3261  ⚪  (score=0)
```python
```
L3262  ⚪  (score=0)
```python
```
L3263  ⚪  (score=0)
```python
@cython.cfunc
```
L3264  ⚪  (score=0)
```python
def p_with_gil(s: PyrexScanner) -> cython.bint:
```
L3265  ⚪  (score=0)
```python
    if s.sy == 'with':
```
L3266  ⚪  (score=0)
```python
        s.next()
```
L3267  ⚪  (score=0)
```python
        s.expect_keyword('gil')
```
L3268  ⚪  (score=0)
```python
        return True
```
L3269  ⚪  (score=0)
```python
    else:
```
L3270  ⚪  (score=0)
```python
        return False
```
L3271  ⚪  (score=0)
```python
```
L3272  ⚪  (score=0)
```python
```
L3273  ⚪  (score=0)
```python
@cython.cfunc
```
L3274  ⚪  (score=0)
```python
def p_exception_value_clause(s: PyrexScanner, is_extern: cython.bint) -> tuple:
```
L3275  ⚪  (score=0)
```python
    """
```
L3276  ⚪  (score=0)
```python
    Parse exception value clause.
```
L3277  ⚪  (score=0)
```python
```
L3278  ⚪  (score=0)
```python
    Maps clauses to exc_check / exc_value / exc_clause as follows:
```
L3279  ⚪  (score=0)
```python
     ______________________________________________________________________
```
L3280  ⚪  (score=0)
```python
    |                             |             |             |            |
```
L3281  ⚪  (score=0)
```python
    | Clause                      | exc_check   | exc_value   | exc_clause |
```
L3282  ⚪  (score=0)
```python
    | ___________________________ | ___________ | ___________ | __________ |
```
L3283  ⚪  (score=0)
```python
    |                             |             |             |            |
```
L3284  ⚪  (score=0)
```python
    | <nothing> (default func.)   | True        | None        | False      |
```
L3285  ⚪  (score=0)
```python
    | <nothing> (cdef extern)     | False       | None        | False      |
```
L3286  ⚪  (score=0)
```python
    | noexcept                    | False       | None        | True       |
```
L3287  ⚪  (score=0)
```python
    | except <val>                | False       | <val>       | True       |
```
L3288  ⚪  (score=0)
```python
    | except? <val>               | True        | <val>       | True       |
```
L3289  ⚪  (score=0)
```python
    | except *                    | True        | None        | True       |
```
L3290  ⚪  (score=0)
```python
    | except +                    | '+'         | None        | True       |
```
L3291  ⚪  (score=0)
```python
    | except +*                   | '+'         | '*'         | True       |
```
L3292  ⚪  (score=0)
```python
    | except +<PyErr>             | '+'         | <PyErr>     | True       |
```
L3293  ⚪  (score=0)
```python
    | ___________________________ | ___________ | ___________ | __________ |
```
L3294  ⚪  (score=0)
```python
```
L3295  ⚪  (score=0)
```python
    Note that the only reason we need `exc_clause` is to raise a
```
L3296  ⚪  (score=0)
```python
    warning when `'except'` or `'noexcept'` is placed after the
```
L3297  ⚪  (score=0)
```python
    `'nogil'` keyword.
```
L3298  ⚪  (score=0)
```python
    """
```
L3299  ⚪  (score=0)
```python
    exc_clause: cython.bint = False
```
L3300  ⚪  (score=0)
```python
    exc_val = None
```
L3301  ⚪  (score=0)
```python
    exc_check = False if is_extern else True
```
L3302  ⚪  (score=0)
```python
```
L3303  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == 'noexcept':
```
L3304  ⚪  (score=0)
```python
        exc_clause = True
```
L3305  ⚪  (score=0)
```python
        s.next()
```
L3306  ⚪  (score=0)
```python
        exc_check = False
```
L3307  ⚪  (score=0)
```python
    elif s.sy == 'except':
```
L3308  ⚪  (score=0)
```python
        exc_clause = True
```
L3309  ⚪  (score=0)
```python
        s.next()
```
L3310  ⚪  (score=0)
```python
        if s.sy == '*':
```
L3311  ⚪  (score=0)
```python
            exc_check = True
```
L3312  ⚪  (score=0)
```python
            s.next()
```
L3313  ⚪  (score=0)
```python
        elif s.sy == '+':
```
L3314  ⚪  (score=0)
```python
            exc_check = '+'
```
L3315  ⚪  (score=0)
```python
            plus_char_pos = s.position()[2]
```
L3316  ⚪  (score=0)
```python
            s.next()
```
L3317  ⚪  (score=0)
```python
            if s.sy == 'IDENT':
```
L3318  ⚪  (score=0)
```python
                name = s.systring
```
L3319  ⚪  (score=0)
```python
                if name == 'nogil':
```
L3320  ⚪  (score=0)
```python
                    if s.position()[2] == plus_char_pos + 1:
```
L3321  ⚪  (score=0)
```python
                        error(s.position(),
```
L3322  ⚪  (score=0)
```python
                              "'except +nogil' defines an exception handling function. Use 'except + nogil' for the 'nogil' modifier.")
```
L3323  ⚪  (score=0)
```python
                    # 'except + nogil' is parsed outside
```
L3324  ⚪  (score=0)
```python
                else:
```
L3325  ⚪  (score=0)
```python
                    exc_val = p_name(s, name)
```
L3326  ⚪  (score=0)
```python
                    s.next()
```
L3327  ⚪  (score=0)
```python
            elif s.sy == '*':
```
L3328  ⚪  (score=0)
```python
                exc_val = ExprNodes.CharNode(s.position(), value='*')
```
L3329  ⚪  (score=0)
```python
                s.next()
```
L3330  ⚪  (score=0)
```python
        else:
```
L3331  ⚪  (score=0)
```python
            if s.sy == '?':
```
L3332  ⚪  (score=0)
```python
                exc_check = True
```
L3333  ⚪  (score=0)
```python
                s.next()
```
L3334  ⚪  (score=0)
```python
            else:
```
L3335  ⚪  (score=0)
```python
                exc_check = False
```
L3336  ⚪  (score=0)
```python
            # exc_val can be non-None even if exc_check is False, c.f. "except -1"
```
L3337  ⚪  (score=0)
```python
            exc_val = p_test(s)
```
L3338  ⚪  (score=0)
```python
```
L3339  ⚪  (score=0)
```python
    return exc_val, exc_check, exc_clause
```
L3340  ⚪  (score=0)
```python
```
L3341  ⚪  (score=0)
```python
```
L3342  ⚪  (score=0)
```python
c_arg_list_terminators = cython.declare(frozenset, frozenset((
```
L3343  ⚪  (score=0)
```python
    '*', '**', '...', ')', ':', '/')))
```
L3344  ⚪  (score=0)
```python
```
L3345  ⚪  (score=0)
```python
```
L3346  ⚪  (score=0)
```python
@cython.ccall
```
L3347  ⚪  (score=0)
```python
def p_c_arg_list(s: PyrexScanner, ctx = Ctx(),
```
L3348  ⚪  (score=0)
```python
                 in_pyfunc: cython.bint = False, cmethod_flag: cython.bint = False,
```
L3349  ⚪  (score=0)
```python
                 nonempty_declarators: cython.bint = False, kw_only: cython.bint = False,
```
L3350  ⚪  (score=0)
```python
                 annotated: cython.bint = True) -> list:
```
L3351  ⚪  (score=0)
```python
    #  Comma-separated list of C argument declarations, possibly empty.
```
L3352  ⚪  (score=0)
```python
    #  May have a trailing comma.
```
L3353  ⚪  (score=0)
```python
    args = []
```
L3354  ⚪  (score=0)
```python
    is_self_arg = cmethod_flag
```
L3355  ⚪  (score=0)
```python
    while s.sy not in c_arg_list_terminators:
```
L3356  ⚪  (score=0)
```python
        args.append(p_c_arg_decl(s, ctx, in_pyfunc, is_self_arg,
```
L3357  ⚪  (score=0)
```python
            nonempty = nonempty_declarators, kw_only = kw_only,
```
L3358  ⚪  (score=0)
```python
            annotated = annotated))
```
L3359  ⚪  (score=0)
```python
        if s.sy != ',':
```
L3360  ⚪  (score=0)
```python
            break
```
L3361  ⚪  (score=0)
```python
        s.next()
```
L3362  ⚪  (score=0)
```python
        is_self_arg = 0
```
L3363  ⚪  (score=0)
```python
    return args
```
L3364  ⚪  (score=0)
```python
```
L3365  ⚪  (score=0)
```python
```
L3366  ⚪  (score=0)
```python
@cython.cfunc
```
L3367  ⚪  (score=0)
```python
def p_optional_ellipsis(s: PyrexScanner) -> cython.bint:
```
L3368  ⚪  (score=0)
```python
    if s.sy == '...':
```
L3369  ⚪  (score=0)
```python
        expect_ellipsis(s)
```
L3370  ⚪  (score=0)
```python
        return True
```
L3371  ⚪  (score=0)
```python
    else:
```
L3372  ⚪  (score=0)
```python
        return False
```
L3373  ⚪  (score=0)
```python
```
L3374  ⚪  (score=0)
```python
```
L3375  ⚪  (score=0)
```python
@cython.cfunc
```
L3376  ⚪  (score=0)
```python
def p_c_arg_decl(s: PyrexScanner, ctx, in_pyfunc: cython.bint, cmethod_flag: cython.bint = False,
```
L3377  ⚪  (score=0)
```python
                 nonempty: cython.bint = False,
```
L3378  ⚪  (score=0)
```python
                 kw_only: cython.bint = False, annotated: cython.bint = True):
```
L3379  ⚪  (score=0)
```python
    pos = s.position()
```
L3380  ⚪  (score=0)
```python
    not_none = or_none = False
```
L3381  ⚪  (score=0)
```python
    default = None
```
L3382  ⚪  (score=0)
```python
    annotation = None
```
L3383  ⚪  (score=0)
```python
    if s.in_python_file:
```
L3384  ⚪  (score=0)
```python
        # empty type declaration
```
L3385  ⚪  (score=0)
```python
        base_type = Nodes.CSimpleBaseTypeNode(pos,
```
L3386  ⚪  (score=0)
```python
            name = None, module_path = [],
```
L3387  ⚪  (score=0)
```python
            is_basic_c_type = False, signed = 0,
```
L3388  ⚪  (score=0)
```python
            complex = False, longness = 0,
```
L3389  ⚪  (score=0)
```python
            is_self_arg = cmethod_flag, templates = None)
```
L3390  ⚪  (score=0)
```python
    else:
```
L3391  ⚪  (score=0)
```python
        base_type = p_c_base_type(s, nonempty=nonempty)
```
L3392  ⚪  (score=0)
```python
    declarator = p_c_declarator(s, ctx, nonempty = nonempty)
```
L3393  ⚪  (score=0)
```python
    if s.sy in ('not', 'or') and not s.in_python_file:
```
L3394  ⚪  (score=0)
```python
        kind = s.sy
```
L3395  ⚪  (score=0)
```python
        s.next()
```
L3396  ⚪  (score=0)
```python
        if s.sy == 'IDENT' and s.systring == 'None':
```
L3397  ⚪  (score=0)
```python
            s.next()
```
L3398  ⚪  (score=0)
```python
        else:
```
L3399  ⚪  (score=0)
```python
            s.error("Expected 'None'")
```
L3400  ⚪  (score=0)
```python
        if not in_pyfunc:
```
L3401  ⚪  (score=0)
```python
            error(pos, "'%s None' only allowed in Python functions" % kind)
```
L3402  ⚪  (score=0)
```python
        or_none = kind == 'or'
```
L3403  ⚪  (score=0)
```python
        not_none = kind == 'not'
```
L3404  ⚪  (score=0)
```python
    if annotated and s.sy == ':':
```
L3405  ⚪  (score=0)
```python
        s.next()
```
L3406  ⚪  (score=0)
```python
        annotation = p_annotation(s)
```
L3407  ⚪  (score=0)
```python
    if s.sy == '=':
```
L3408  ⚪  (score=0)
```python
        s.next()
```
L3409  ⚪  (score=0)
```python
        if 'pxd' in ctx.level:
```
L3410  ⚪  (score=0)
```python
            if s.sy in ['*', '?']:
```
L3411  ⚪  (score=0)
```python
                # TODO(github/1736): Make this an error for inline declarations.
```
L3412  ⚪  (score=0)
```python
                default = ExprNodes.NoneNode(pos)
```
L3413  ⚪  (score=0)
```python
                s.next()
```
L3414  ⚪  (score=0)
```python
            elif 'inline' in ctx.modifiers:
```
L3415  ⚪  (score=0)
```python
                default = p_test(s)
```
L3416  ⚪  (score=0)
```python
            else:
```
L3417  ⚪  (score=0)
```python
                error(pos, "default values cannot be specified in pxd files, use ? or *")
```
L3418  ⚪  (score=0)
```python
        else:
```
L3419  ⚪  (score=0)
```python
            default = p_test(s)
```
L3420  ⚪  (score=0)
```python
    return Nodes.CArgDeclNode(pos,
```
L3421  ⚪  (score=0)
```python
        base_type = base_type,
```
L3422  ⚪  (score=0)
```python
        declarator = declarator,
```
L3423  ⚪  (score=0)
```python
        not_none = not_none,
```
L3424  ⚪  (score=0)
```python
        or_none = or_none,
```
L3425  ⚪  (score=0)
```python
        default = default,
```
L3426  ⚪  (score=0)
```python
        annotation = annotation,
```
L3427  ⚪  (score=0)
```python
        kw_only = kw_only)
```
L3428  ⚪  (score=0)
```python
```
L3429  ⚪  (score=0)
```python
```
L3430  ⚪  (score=0)
```python
@cython.cfunc
```
L3431  ⚪  (score=0)
```python
def p_annotation(s: PyrexScanner):
```
L3432  ⚪  (score=0)
```python
    """An annotation just has the "test" syntax, but also stores the string it came from
```
L3433  ⚪  (score=0)
```python
```
L3434  ⚪  (score=0)
```python
    Note that the string is *allowed* to be changed/processed (although isn't here)
```
L3435  ⚪  (score=0)
```python
    so may not exactly match the string generated by Python, and if it doesn't
```
L3436  ⚪  (score=0)
```python
    then it is not a bug.
```
L3437  ⚪  (score=0)
```python
    """
```
L3438  ⚪  (score=0)
```python
    pos = s.position()
```
L3439  ⚪  (score=0)
```python
    expr = p_test(s)
```
L3440  ⚪  (score=0)
```python
    return ExprNodes.AnnotationNode(pos, expr=expr)
```
L3441  ⚪  (score=0)
```python
```
L3442  ⚪  (score=0)
```python
```
L3443  ⚪  (score=0)
```python
@cython.cfunc
```
L3444  ⚪  (score=0)
```python
def p_api(s: PyrexScanner) -> cython.bint:
```
L3445  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == 'api':
```
L3446  ⚪  (score=0)
```python
        s.next()
```
L3447  ⚪  (score=0)
```python
        return True
```
L3448  ⚪  (score=0)
```python
    else:
```
L3449  ⚪  (score=0)
```python
        return False
```
L3450  ⚪  (score=0)
```python
```
L3451  ⚪  (score=0)
```python
```
L3452  ⚪  (score=0)
```python
@cython.cfunc
```
L3453  ⚪  (score=0)
```python
def p_cdef_statement(s: PyrexScanner, pos, ctx):
```
L3454  ⚪  (score=0)
```python
    ctx.visibility = p_visibility(s, ctx.visibility)
```
L3455  ⚪  (score=0)
```python
    ctx.api = ctx.api or p_api(s)
```
L3456  ⚪  (score=0)
```python
    if ctx.api:
```
L3457  ⚪  (score=0)
```python
        if ctx.visibility not in ('private', 'public'):
```
L3458  ⚪  (score=0)
```python
            error(pos, "Cannot combine 'api' with '%s'" % ctx.visibility)
```
L3459  ⚪  (score=0)
```python
    if (ctx.visibility == 'extern') and s.sy == 'from':
```
L3460  ⚪  (score=0)
```python
        return p_cdef_extern_block(s, pos, ctx)
```
L3461  ⚪  (score=0)
```python
    elif s.sy == 'import':
```
L3462  ⚪  (score=0)
```python
        s.next()
```
L3463  ⚪  (score=0)
```python
        return p_cdef_extern_block(s, pos, ctx)
```
L3464  ⚪  (score=0)
```python
    elif p_nogil(s):
```
L3465  ⚪  (score=0)
```python
        ctx.nogil = True
```
L3466  ⚪  (score=0)
```python
        if ctx.overridable:
```
L3467  ⚪  (score=0)
```python
            error(pos, "cdef blocks cannot be declared cpdef")
```
L3468  ⚪  (score=0)
```python
        return p_cdef_block(s, ctx)
```
L3469  ⚪  (score=0)
```python
    elif s.sy == ':':
```
L3470  ⚪  (score=0)
```python
        if ctx.overridable:
```
L3471  ⚪  (score=0)
```python
            error(pos, "cdef blocks cannot be declared cpdef")
```
L3472  ⚪  (score=0)
```python
        return p_cdef_block(s, ctx)
```
L3473  ⚪  (score=0)
```python
    elif s.sy == 'class':
```
L3474  ⚪  (score=0)
```python
        if ctx.level not in ('module', 'module_pxd'):
```
L3475  ⚪  (score=0)
```python
            error(pos, "Extension type definition not allowed here")
```
L3476  ⚪  (score=0)
```python
        if ctx.overridable:
```
L3477  ⚪  (score=0)
```python
            error(pos, "Extension types cannot be declared cpdef")
```
L3478  ⚪  (score=0)
```python
        return p_c_class_definition(s, pos, ctx)
```
L3479  ⚪  (score=0)
```python
    elif s.sy == 'IDENT' and s.systring == 'cppclass':
```
L3480  ⚪  (score=0)
```python
        return p_cpp_class_definition(s, pos, ctx)
```
L3481  ⚪  (score=0)
```python
    elif s.sy == 'IDENT' and s.systring in struct_enum_union:
```
L3482  ⚪  (score=0)
```python
        if ctx.level not in ('module', 'module_pxd'):
```
L3483  ⚪  (score=0)
```python
            error(pos, "C struct/union/enum definition not allowed here")
```
L3484  ⚪  (score=0)
```python
        if ctx.overridable:
```
L3485  ⚪  (score=0)
```python
            if s.systring != 'enum':
```
L3486  ⚪  (score=0)
```python
                error(pos, "C struct/union cannot be declared cpdef")
```
L3487  ⚪  (score=0)
```python
        return p_struct_enum(s, pos, ctx)
```
L3488  ⚪  (score=0)
```python
    elif s.sy == 'IDENT' and s.systring == 'fused':
```
L3489  ⚪  (score=0)
```python
        return p_fused_definition(s, pos, ctx)
```
L3490  ⚪  (score=0)
```python
    else:
```
L3491  ⚪  (score=0)
```python
        return p_c_func_or_var_declaration(s, pos, ctx)
```
L3492  ⚪  (score=0)
```python
```
L3493  ⚪  (score=0)
```python
```
L3494  ⚪  (score=0)
```python
@cython.cfunc
```
L3495  ⚪  (score=0)
```python
def p_cdef_block(s: PyrexScanner, ctx):
```
L3496  ⚪  (score=0)
```python
    return p_suite(s, ctx(cdef_flag = True))
```
L3497  ⚪  (score=0)
```python
```
L3498  ⚪  (score=0)
```python
```
L3499  ⚪  (score=0)
```python
@cython.cfunc
```
L3500  ⚪  (score=0)
```python
def p_cdef_extern_block(s: PyrexScanner, pos, ctx):
```
L3501  ⚪  (score=0)
```python
    if ctx.overridable:
```
L3502  ⚪  (score=0)
```python
        error(pos, "cdef extern blocks cannot be declared cpdef")
```
L3503  ⚪  (score=0)
```python
    include_file = None
```
L3504  ⚪  (score=0)
```python
    s.expect('from')
```
L3505  ⚪  (score=0)
```python
    if s.sy == '*':
```
L3506  ⚪  (score=0)
```python
        s.next()
```
L3507  ⚪  (score=0)
```python
    else:
```
L3508  ⚪  (score=0)
```python
        include_file = p_string_literal(s, 'u')[2]
```
L3509  ⚪  (score=0)
```python
    ctx = ctx(cdef_flag = True, visibility = 'extern')
```
L3510  ⚪  (score=0)
```python
    if s.systring == "namespace":
```
L3511  ⚪  (score=0)
```python
        s.next()
```
L3512  ⚪  (score=0)
```python
        ctx.namespace = p_string_literal(s, 'u')[2]
```
L3513  ⚪  (score=0)
```python
    if p_nogil(s):
```
L3514  ⚪  (score=0)
```python
        ctx.nogil = True
```
L3515  ⚪  (score=0)
```python
```
L3516  ⚪  (score=0)
```python
    # Use "docstring" as verbatim string to include
```
L3517  ⚪  (score=0)
```python
    verbatim_include, body = p_suite_with_docstring(s, ctx, True)
```
L3518  ⚪  (score=0)
```python
```
L3519  ⚪  (score=0)
```python
    return Nodes.CDefExternNode(pos,
```
L3520  ⚪  (score=0)
```python
        include_file = include_file,
```
L3521  ⚪  (score=0)
```python
        verbatim_include = verbatim_include,
```
L3522  ⚪  (score=0)
```python
        body = body,
```
L3523  ⚪  (score=0)
```python
        namespace = ctx.namespace)
```
L3524  ⚪  (score=0)
```python
```
L3525  ⚪  (score=0)
```python
```
L3526  ⚪  (score=0)
```python
@cython.cfunc
```
L3527  ⚪  (score=0)
```python
def p_c_enum_definition(s: PyrexScanner, pos, ctx):
```
L3528  ⚪  (score=0)
```python
    # s.sy == ident 'enum'
```
L3529  ⚪  (score=0)
```python
    s.next()
```
L3530  ⚪  (score=0)
```python
```
L3531  ⚪  (score=0)
```python
    scoped = False
```
L3532  ⚪  (score=0)
```python
    if s.context.cpp and (s.sy == 'class' or (s.sy == 'IDENT' and s.systring == 'struct')):
```
L3533  ⚪  (score=0)
```python
        scoped = True
```
L3534  ⚪  (score=0)
```python
        s.next()
```
L3535  ⚪  (score=0)
```python
```
L3536  ⚪  (score=0)
```python
    if s.sy == 'IDENT':
```
L3537  ⚪  (score=0)
```python
        name = s.systring
```
L3538  ⚪  (score=0)
```python
        s.next()
```
L3539  ⚪  (score=0)
```python
        cname = p_opt_cname(s)
```
L3540  ⚪  (score=0)
```python
        if cname is None and ctx.namespace is not None:
```
L3541  ⚪  (score=0)
```python
            cname = ctx.namespace + "::" + name
```
L3542  ⚪  (score=0)
```python
    else:
```
L3543  ⚪  (score=0)
```python
        name = cname = None
```
L3544  ⚪  (score=0)
```python
        if scoped:
```
L3545  ⚪  (score=0)
```python
            s.error("Unnamed scoped enum not allowed")
```
L3546  ⚪  (score=0)
```python
```
L3547  ⚪  (score=0)
```python
    if scoped and s.sy == '(':
```
L3548  ⚪  (score=0)
```python
        s.next()
```
L3549  ⚪  (score=0)
```python
        underlying_type = p_c_base_type(s)
```
L3550  ⚪  (score=0)
```python
        s.expect(')')
```
L3551  ⚪  (score=0)
```python
    else:
```
L3552  ⚪  (score=0)
```python
        underlying_type = Nodes.CSimpleBaseTypeNode(
```
L3553  ⚪  (score=0)
```python
            pos,
```
L3554  ⚪  (score=0)
```python
            name="int",
```
L3555  ⚪  (score=0)
```python
            module_path = [],
```
L3556  ⚪  (score=0)
```python
            is_basic_c_type = True,
```
L3557  ⚪  (score=0)
```python
            signed = 1,
```
L3558  ⚪  (score=0)
```python
            complex = False,
```
L3559  ⚪  (score=0)
```python
            longness = 0
```
L3560  ⚪  (score=0)
```python
        )
```
L3561  ⚪  (score=0)
```python
```
L3562  ⚪  (score=0)
```python
    s.expect(':')
```
L3563  ⚪  (score=0)
```python
    items = []
```
L3564  ⚪  (score=0)
```python
```
L3565  ⚪  (score=0)
```python
    doc = None
```
L3566  ⚪  (score=0)
```python
    if s.sy != 'NEWLINE':
```
L3567  ⚪  (score=0)
```python
        p_c_enum_line(s, ctx, items)
```
L3568  ⚪  (score=0)
```python
    else:
```
L3569  ⚪  (score=0)
```python
        s.next()  # 'NEWLINE'
```
L3570  ⚪  (score=0)
```python
        s.expect_indent()
```
L3571  ⚪  (score=0)
```python
        doc = p_doc_string(s)
```
L3572  ⚪  (score=0)
```python
```
L3573  ⚪  (score=0)
```python
        while s.sy not in ('DEDENT', 'EOF'):
```
L3574  ⚪  (score=0)
```python
            p_c_enum_line(s, ctx, items)
```
L3575  ⚪  (score=0)
```python
```
L3576  ⚪  (score=0)
```python
        s.expect_dedent()
```
L3577  ⚪  (score=0)
```python
```
L3578  ⚪  (score=0)
```python
    if not items and ctx.visibility != "extern":
```
L3579  ⚪  (score=0)
```python
        error(pos, "Empty enum definition not allowed outside a 'cdef extern from' block")
```
L3580  ⚪  (score=0)
```python
```
L3581  ⚪  (score=0)
```python
    return Nodes.CEnumDefNode(
```
L3582  ⚪  (score=0)
```python
        pos, name=name, cname=cname,
```
L3583  ⚪  (score=0)
```python
        scoped=scoped, items=items,
```
L3584  ⚪  (score=0)
```python
        underlying_type=underlying_type,
```
L3585  ⚪  (score=0)
```python
        typedef_flag=ctx.typedef_flag, visibility=ctx.visibility,
```
L3586  ⚪  (score=0)
```python
        create_wrapper=ctx.overridable,
```
L3587  ⚪  (score=0)
```python
        api=ctx.api, in_pxd=ctx.level == 'module_pxd', doc=doc)
```
L3588  ⚪  (score=0)
```python
```
L3589  ⚪  (score=0)
```python
```
L3590  ⚪  (score=0)
```python
@cython.cfunc
```
L3591  ⚪  (score=0)
```python
def p_c_enum_line(s: PyrexScanner, ctx, items: list):
```
L3592  ⚪  (score=0)
```python
    if s.sy != 'pass':
```
L3593  ⚪  (score=0)
```python
        p_c_enum_item(s, ctx, items)
```
L3594  ⚪  (score=0)
```python
        while s.sy == ',':
```
L3595  ⚪  (score=0)
```python
            s.next()
```
L3596  ⚪  (score=0)
```python
            if s.sy in ('NEWLINE', 'EOF'):
```
L3597  ⚪  (score=0)
```python
                break
```
L3598  ⚪  (score=0)
```python
            p_c_enum_item(s, ctx, items)
```
L3599  ⚪  (score=0)
```python
    else:
```
L3600  ⚪  (score=0)
```python
        s.next()
```
L3601  ⚪  (score=0)
```python
    s.expect_newline("Syntax error in enum item list")
```
L3602  ⚪  (score=0)
```python
```
L3603  ⚪  (score=0)
```python
```
L3604  ⚪  (score=0)
```python
@cython.cfunc
```
L3605  ⚪  (score=0)
```python
def p_c_enum_item(s: PyrexScanner, ctx, items: list):
```
L3606  ⚪  (score=0)
```python
    pos = s.position()
```
L3607  ⚪  (score=0)
```python
    name = p_ident(s)
```
L3608  ⚪  (score=0)
```python
    cname = p_opt_cname(s)
```
L3609  ⚪  (score=0)
```python
    if cname is None and ctx.namespace is not None:
```
L3610  ⚪  (score=0)
```python
        cname = ctx.namespace + "::" + name
```
L3611  ⚪  (score=0)
```python
    value = None
```
L3612  ⚪  (score=0)
```python
    if s.sy == '=':
```
L3613  ⚪  (score=0)
```python
        s.next()
```
L3614  ⚪  (score=0)
```python
        value = p_test(s)
```
L3615  ⚪  (score=0)
```python
    items.append(Nodes.CEnumDefItemNode(pos,
```
L3616  ⚪  (score=0)
```python
        name = name, cname = cname, value = value))
```
L3617  ⚪  (score=0)
```python
```
L3618  ⚪  (score=0)
```python
```
L3619  ⚪  (score=0)
```python
@cython.cfunc
```
L3620  ⚪  (score=0)
```python
def p_c_struct_or_union_definition(s: PyrexScanner, pos, ctx):
```
L3621  ⚪  (score=0)
```python
    packed = False
```
L3622  ⚪  (score=0)
```python
    if s.systring == 'packed':
```
L3623  ⚪  (score=0)
```python
        packed = True
```
L3624  ⚪  (score=0)
```python
        s.next()
```
L3625  ⚪  (score=0)
```python
        if s.sy != 'IDENT' or s.systring != 'struct':
```
L3626  ⚪  (score=0)
```python
            s.expected('struct')
```
L3627  ⚪  (score=0)
```python
    # s.sy == ident 'struct' or 'union'
```
L3628  ⚪  (score=0)
```python
    kind = s.systring
```
L3629  ⚪  (score=0)
```python
    s.next()
```
L3630  ⚪  (score=0)
```python
    name = p_ident(s)
```
L3631  ⚪  (score=0)
```python
    cname = p_opt_cname(s)
```
L3632  ⚪  (score=0)
```python
    if cname is None and ctx.namespace is not None:
```
L3633  ⚪  (score=0)
```python
        cname = ctx.namespace + "::" + name
```
L3634  ⚪  (score=0)
```python
    attributes = None
```
L3635  ⚪  (score=0)
```python
    if s.sy == ':':
```
L3636  ⚪  (score=0)
```python
        s.next()
```
L3637  ⚪  (score=0)
```python
        attributes = []
```
L3638  ⚪  (score=0)
```python
        if s.sy == 'pass':
```
L3639  ⚪  (score=0)
```python
            s.next()
```
L3640  ⚪  (score=0)
```python
            s.expect_newline("Expected a newline", ignore_semicolon=True)
```
L3641  ⚪  (score=0)
```python
        else:
```
L3642  ⚪  (score=0)
```python
            s.expect('NEWLINE')
```
L3643  ⚪  (score=0)
```python
            s.expect_indent()
```
L3644  ⚪  (score=0)
```python
            body_ctx = Ctx(visibility=ctx.visibility)
```
L3645  ⚪  (score=0)
```python
            while s.sy != 'DEDENT':
```
L3646  ⚪  (score=0)
```python
                if s.sy != 'pass':
```
L3647  ⚪  (score=0)
```python
                    attributes.append(
```
L3648  ⚪  (score=0)
```python
                        p_c_func_or_var_declaration(s, s.position(), body_ctx))
```
L3649  ⚪  (score=0)
```python
                else:
```
L3650  ⚪  (score=0)
```python
                    s.next()
```
L3651  ⚪  (score=0)
```python
                    s.expect_newline("Expected a newline")
```
L3652  ⚪  (score=0)
```python
            s.expect_dedent()
```
L3653  ⚪  (score=0)
```python
```
L3654  ⚪  (score=0)
```python
        if not attributes and ctx.visibility != "extern":
```
L3655  ⚪  (score=0)
```python
            error(pos, "Empty struct or union definition not allowed outside a 'cdef extern from' block")
```
L3656  ⚪  (score=0)
```python
    else:
```
L3657  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in struct or union definition")
```
L3658  ⚪  (score=0)
```python
```
L3659  ⚪  (score=0)
```python
    return Nodes.CStructOrUnionDefNode(pos,
```
L3660  ⚪  (score=0)
```python
        name = name, cname = cname, kind = kind, attributes = attributes,
```
L3661  ⚪  (score=0)
```python
        typedef_flag = ctx.typedef_flag, visibility = ctx.visibility,
```
L3662  ⚪  (score=0)
```python
        api = ctx.api, in_pxd = ctx.level == 'module_pxd', packed = packed)
```
L3663  ⚪  (score=0)
```python
```
L3664  ⚪  (score=0)
```python
```
L3665  ⚪  (score=0)
```python
@cython.cfunc
```
L3666  ⚪  (score=0)
```python
def p_fused_definition(s: PyrexScanner, pos, ctx):
```
L3667  ⚪  (score=0)
```python
    """
```
L3668  ⚪  (score=0)
```python
    c(type)def fused my_fused_type:
```
L3669  ⚪  (score=0)
```python
        ...
```
L3670  ⚪  (score=0)
```python
    """
```
L3671  ⚪  (score=0)
```python
    # s.systring == 'fused'
```
L3672  ⚪  (score=0)
```python
```
L3673  ⚪  (score=0)
```python
    if ctx.level not in ('module', 'module_pxd'):
```
L3674  ⚪  (score=0)
```python
        error(pos, "Fused type definition not allowed here")
```
L3675  ⚪  (score=0)
```python
```
L3676  ⚪  (score=0)
```python
    s.next()
```
L3677  ⚪  (score=0)
```python
    name = p_ident(s)
```
L3678  ⚪  (score=0)
```python
```
L3679  ⚪  (score=0)
```python
    s.expect(":")
```
L3680  ⚪  (score=0)
```python
    s.expect_newline()
```
L3681  ⚪  (score=0)
```python
    s.expect_indent()
```
L3682  ⚪  (score=0)
```python
```
L3683  ⚪  (score=0)
```python
    types = []
```
L3684  ⚪  (score=0)
```python
    while s.sy != 'DEDENT':
```
L3685  ⚪  (score=0)
```python
        if s.sy != 'pass':
```
L3686  ⚪  (score=0)
```python
            #types.append(p_c_declarator(s))
```
L3687  ⚪  (score=0)
```python
            types.append(p_c_base_type(s))  #, nonempty=1))
```
L3688  ⚪  (score=0)
```python
        else:
```
L3689  ⚪  (score=0)
```python
            s.next()
```
L3690  ⚪  (score=0)
```python
```
L3691  ⚪  (score=0)
```python
        s.expect_newline()
```
L3692  ⚪  (score=0)
```python
```
L3693  ⚪  (score=0)
```python
    s.expect_dedent()
```
L3694  ⚪  (score=0)
```python
```
L3695  ⚪  (score=0)
```python
    if not types:
```
L3696  ⚪  (score=0)
```python
        error(pos, "Need at least one type")
```
L3697  ⚪  (score=0)
```python
```
L3698  ⚪  (score=0)
```python
    return Nodes.FusedTypeNode(pos, name=name, types=types)
```
L3699  ⚪  (score=0)
```python
```
L3700  ⚪  (score=0)
```python
```
L3701  ⚪  (score=0)
```python
@cython.cfunc
```
L3702  ⚪  (score=0)
```python
def p_struct_enum(s: PyrexScanner, pos, ctx):
```
L3703  ⚪  (score=0)
```python
    if s.systring == 'enum':
```
L3704  ⚪  (score=0)
```python
        return p_c_enum_definition(s, pos, ctx)
```
L3705  ⚪  (score=0)
```python
    else:
```
L3706  ⚪  (score=0)
```python
        return p_c_struct_or_union_definition(s, pos, ctx)
```
L3707  ⚪  (score=0)
```python
```
L3708  ⚪  (score=0)
```python
```
L3709  ⚪  (score=0)
```python
@cython.cfunc
```
L3710  ⚪  (score=0)
```python
def p_visibility(s: PyrexScanner, prev_visibility):
```
L3711  ⚪  (score=0)
```python
    visibility = prev_visibility
```
L3712  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring in ('extern', 'public', 'readonly'):
```
L3713  ⚪  (score=0)
```python
        visibility = s.systring
```
L3714  ⚪  (score=0)
```python
        if prev_visibility != 'private' and visibility != prev_visibility:
```
L3715  ⚪  (score=0)
```python
            s.error("Conflicting visibility options '%s' and '%s'"
```
L3716  ⚪  (score=0)
```python
                % (prev_visibility, visibility), fatal=False)
```
L3717  ⚪  (score=0)
```python
        s.next()
```
L3718  ⚪  (score=0)
```python
    return visibility
```
L3719  ⚪  (score=0)
```python
```
L3720  ⚪  (score=0)
```python
```
L3721  ⚪  (score=0)
```python
@cython.cfunc
```
L3722  ⚪  (score=0)
```python
def p_c_modifiers(s: PyrexScanner) -> list:
```
L3723  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring in ('inline',):
```
L3724  ⚪  (score=0)
```python
        modifier = s.systring
```
L3725  ⚪  (score=0)
```python
        s.next()
```
L3726  ⚪  (score=0)
```python
        return [modifier] + p_c_modifiers(s)
```
L3727  ⚪  (score=0)
```python
    return []
```
L3728  ⚪  (score=0)
```python
```
L3729  ⚪  (score=0)
```python
```
L3730  ⚪  (score=0)
```python
@cython.cfunc
```
L3731  ⚪  (score=0)
```python
def p_c_func_or_var_declaration(s: PyrexScanner, pos, ctx):
```
L3732  ⚪  (score=0)
```python
    cmethod_flag: cython.bint = ctx.level in ('c_class', 'c_class_pxd')
```
L3733  ⚪  (score=0)
```python
    modifiers = p_c_modifiers(s)
```
L3734  ⚪  (score=0)
```python
    base_type = p_c_base_type(s, nonempty=True, templates = ctx.templates)
```
L3735  ⚪  (score=0)
```python
    declarator = p_c_declarator(s, ctx(modifiers=modifiers), cmethod_flag = cmethod_flag,
```
L3736  ⚪  (score=0)
```python
                                assignable=True, nonempty =True)
```
L3737  ⚪  (score=0)
```python
    declarator.overridable = ctx.overridable
```
L3738  ⚪  (score=0)
```python
```
L3739  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == 'const' and ctx.level == 'cpp_class':
```
L3740  ⚪  (score=0)
```python
        s.next()
```
L3741  ⚪  (score=0)
```python
        is_const_method = True
```
L3742  ⚪  (score=0)
```python
    else:
```
L3743  ⚪  (score=0)
```python
        is_const_method = False
```
L3744  ⚪  (score=0)
```python
```
L3745  ⚪  (score=0)
```python
    if s.sy == '->':
```
L3746  ⚪  (score=0)
```python
        # Special enough to give a better error message and keep going.
```
L3747  ⚪  (score=0)
```python
        s.error(
```
L3748  ⚪  (score=0)
```python
            "Return type annotation is not allowed in cdef/cpdef signatures. "
```
L3749  ⚪  (score=0)
```python
            "Please define it before the function name, as in C signatures.",
```
L3750  ⚪  (score=0)
```python
            fatal=False)
```
L3751  ⚪  (score=0)
```python
        s.next()
```
L3752  ⚪  (score=0)
```python
        p_test(s)  # Keep going, but ignore result.
```
L3753  ⚪  (score=0)
```python
```
L3754  ⚪  (score=0)
```python
    if s.sy == ':':
```
L3755  ⚪  (score=0)
```python
        if ctx.level not in ('module', 'c_class', 'module_pxd', 'c_class_pxd', 'cpp_class') and not ctx.templates:
```
L3756  ⚪  (score=0)
```python
            s.error("C function definition not allowed here")
```
L3757  ⚪  (score=0)
```python
        doc, suite = p_suite_with_docstring(s, Ctx(level='function'))
```
L3758  ⚪  (score=0)
```python
        result = Nodes.CFuncDefNode(pos,
```
L3759  ⚪  (score=0)
```python
            visibility = ctx.visibility,
```
L3760  ⚪  (score=0)
```python
            base_type = base_type,
```
L3761  ⚪  (score=0)
```python
            declarator = declarator,
```
L3762  ⚪  (score=0)
```python
            body = suite,
```
L3763  ⚪  (score=0)
```python
            doc = doc,
```
L3764  ⚪  (score=0)
```python
            modifiers = modifiers,
```
L3765  ⚪  (score=0)
```python
            api = ctx.api,
```
L3766  ⚪  (score=0)
```python
            overridable = ctx.overridable,
```
L3767  ⚪  (score=0)
```python
            is_const_method = is_const_method)
```
L3768  ⚪  (score=0)
```python
    else:
```
L3769  ⚪  (score=0)
```python
        #if api:
```
L3770  ⚪  (score=0)
```python
        #    s.error("'api' not allowed with variable declaration")
```
L3771  ⚪  (score=0)
```python
        if is_const_method:
```
L3772  ⚪  (score=0)
```python
            declarator.is_const_method = is_const_method
```
L3773  ⚪  (score=0)
```python
        declarators = [declarator]
```
L3774  ⚪  (score=0)
```python
        while s.sy == ',':
```
L3775  ⚪  (score=0)
```python
            s.next()
```
L3776  ⚪  (score=0)
```python
            if s.sy == 'NEWLINE':
```
L3777  ⚪  (score=0)
```python
                break
```
L3778  ⚪  (score=0)
```python
            declarator = p_c_declarator(s, ctx, cmethod_flag = cmethod_flag,
```
L3779  ⚪  (score=0)
```python
                                        assignable=True, nonempty=True)
```
L3780  ⚪  (score=0)
```python
            declarators.append(declarator)
```
L3781  ⚪  (score=0)
```python
        doc_line = s.start_line + 1
```
L3782  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in C variable declaration", ignore_semicolon=True)
```
L3783  ⚪  (score=0)
```python
        if ctx.level in ('c_class', 'c_class_pxd') and s.start_line == doc_line:
```
L3784  ⚪  (score=0)
```python
            doc = p_doc_string(s)
```
L3785  ⚪  (score=0)
```python
        else:
```
L3786  ⚪  (score=0)
```python
            doc = None
```
L3787  ⚪  (score=0)
```python
        result = Nodes.CVarDefNode(pos,
```
L3788  ⚪  (score=0)
```python
            visibility = ctx.visibility,
```
L3789  ⚪  (score=0)
```python
            base_type = base_type,
```
L3790  ⚪  (score=0)
```python
            declarators = declarators,
```
L3791  ⚪  (score=0)
```python
            in_pxd = ctx.level in ('module_pxd', 'c_class_pxd'),
```
L3792  ⚪  (score=0)
```python
            doc = doc,
```
L3793  ⚪  (score=0)
```python
            api = ctx.api,
```
L3794  ⚪  (score=0)
```python
            modifiers = modifiers,
```
L3795  ⚪  (score=0)
```python
            overridable = ctx.overridable)
```
L3796  ⚪  (score=0)
```python
    return result
```
L3797  ⚪  (score=0)
```python
```
L3798  ⚪  (score=0)
```python
```
L3799  ⚪  (score=0)
```python
@cython.cfunc
```
L3800  ⚪  (score=0)
```python
def p_ctypedef_statement(s: PyrexScanner, ctx):
```
L3801  ⚪  (score=0)
```python
    # s.sy == 'ctypedef'
```
L3802  ⚪  (score=0)
```python
    pos = s.position()
```
L3803  ⚪  (score=0)
```python
    s.next()
```
L3804  ⚪  (score=0)
```python
    visibility = p_visibility(s, ctx.visibility)
```
L3805  ⚪  (score=0)
```python
    api = p_api(s)
```
L3806  ⚪  (score=0)
```python
    ctx = ctx(typedef_flag=True, visibility = visibility)
```
L3807  ⚪  (score=0)
```python
    if api:
```
L3808  ⚪  (score=0)
```python
        ctx.api = True
```
L3809  ⚪  (score=0)
```python
    if s.sy == 'class':
```
L3810  ⚪  (score=0)
```python
        return p_c_class_definition(s, pos, ctx)
```
L3811  ⚪  (score=0)
```python
    elif s.sy == 'IDENT' and s.systring in struct_enum_union:
```
L3812  ⚪  (score=0)
```python
        return p_struct_enum(s, pos, ctx)
```
L3813  ⚪  (score=0)
```python
    elif s.sy == 'IDENT' and s.systring == 'fused':
```
L3814  ⚪  (score=0)
```python
        return p_fused_definition(s, pos, ctx)
```
L3815  ⚪  (score=0)
```python
    else:
```
L3816  ⚪  (score=0)
```python
        base_type = p_c_base_type(s, nonempty=True)
```
L3817  ⚪  (score=0)
```python
        declarator = p_c_declarator(s, ctx, is_type=True, nonempty=True)
```
L3818  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in ctypedef statement", ignore_semicolon=True)
```
L3819  ⚪  (score=0)
```python
        return Nodes.CTypeDefNode(
```
L3820  ⚪  (score=0)
```python
            pos, base_type = base_type,
```
L3821  ⚪  (score=0)
```python
            declarator = declarator,
```
L3822  ⚪  (score=0)
```python
            visibility = visibility, api = api,
```
L3823  ⚪  (score=0)
```python
            in_pxd = ctx.level == 'module_pxd')
```
L3824  ⚪  (score=0)
```python
```
L3825  ⚪  (score=0)
```python
```
L3826  ⚪  (score=0)
```python
@cython.cfunc
```
L3827  ⚪  (score=0)
```python
def p_decorators(s: PyrexScanner) -> list:
```
L3828  ⚪  (score=0)
```python
    decorators = []
```
L3829  ⚪  (score=0)
```python
    while s.sy == '@':
```
L3830  ⚪  (score=0)
```python
        pos = s.position()
```
L3831  ⚪  (score=0)
```python
        s.next()
```
L3832  ⚪  (score=0)
```python
        decorator = p_namedexpr_test(s)
```
L3833  ⚪  (score=0)
```python
        decorators.append(Nodes.DecoratorNode(pos, decorator=decorator))
```
L3834  ⚪  (score=0)
```python
        s.expect_newline("Expected a newline after decorator")
```
L3835  ⚪  (score=0)
```python
    return decorators
```
L3836  ⚪  (score=0)
```python
```
L3837  ⚪  (score=0)
```python
```
L3838  ⚪  (score=0)
```python
@cython.cfunc
```
L3839  ⚪  (score=0)
```python
def _reject_cdef_modifier_in_py(s: PyrexScanner, name):
```
L3840  ⚪  (score=0)
```python
    """Step over incorrectly placed cdef modifiers (@see _CDEF_MODIFIERS) to provide a good error message for them.
```
L3841  ⚪  (score=0)
```python
    """
```
L3842  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and name in _CDEF_MODIFIERS:
```
L3843  ⚪  (score=0)
```python
        # Special enough to provide a good error message.
```
L3844  ⚪  (score=0)
```python
        s.error("Cannot use cdef modifier '%s' in Python function signature. Use a decorator instead." % name, fatal=False)
```
L3845  ⚪  (score=0)
```python
        return p_ident(s)  # Keep going, in case there are other errors.
```
L3846  ⚪  (score=0)
```python
    return name
```
L3847  ⚪  (score=0)
```python
```
L3848  ⚪  (score=0)
```python
```
L3849  ⚪  (score=0)
```python
@cython.cfunc
```
L3850  ⚪  (score=0)
```python
def p_def_statement(s: PyrexScanner, decorators: list = None, is_async_def: cython.bint = False):
```
L3851  ⚪  (score=0)
```python
    # s.sy == 'def'
```
L3852  ⚪  (score=0)
```python
    pos = decorators[0].pos if decorators else s.position()
```
L3853  ⚪  (score=0)
```python
    # PEP 492 switches the async/await keywords on in "async def" functions
```
L3854  ⚪  (score=0)
```python
    if is_async_def:
```
L3855  ⚪  (score=0)
```python
        s.enter_async()
```
L3856  ⚪  (score=0)
```python
    s.next()
```
L3857  ⚪  (score=0)
```python
    name = _reject_cdef_modifier_in_py(s, p_ident(s))
```
L3858  ⚪  (score=0)
```python
    s.expect(
```
L3859  ⚪  (score=0)
```python
        '(',
```
L3860  ⚪  (score=0)
```python
        "Expected '(', found '%s'. Did you use cdef syntax in a Python declaration? "
```
L3861  ⚪  (score=0)
```python
        "Use decorators and Python type annotations instead." % (
```
L3862  ⚪  (score=0)
```python
            s.systring if s.sy == 'IDENT' else s.sy))
```
L3863  ⚪  (score=0)
```python
    args, star_arg, starstar_arg = p_varargslist(s, terminator=')')
```
L3864  ⚪  (score=0)
```python
    s.expect(')')
```
L3865  ⚪  (score=0)
```python
    _reject_cdef_modifier_in_py(s, s.systring)
```
L3866  ⚪  (score=0)
```python
    return_type_annotation = None
```
L3867  ⚪  (score=0)
```python
    if s.sy == '->':
```
L3868  ⚪  (score=0)
```python
        s.next()
```
L3869  ⚪  (score=0)
```python
        return_type_annotation = p_annotation(s)
```
L3870  ⚪  (score=0)
```python
        _reject_cdef_modifier_in_py(s, s.systring)
```
L3871  ⚪  (score=0)
```python
```
L3872  ⚪  (score=0)
```python
    doc, body = p_suite_with_docstring(s, Ctx(level='function'))
```
L3873  ⚪  (score=0)
```python
    if is_async_def:
```
L3874  ⚪  (score=0)
```python
        s.exit_async()
```
L3875  ⚪  (score=0)
```python
```
L3876  ⚪  (score=0)
```python
    return Nodes.DefNode(
```
L3877  ⚪  (score=0)
```python
        pos, name=name, args=args, star_arg=star_arg, starstar_arg=starstar_arg,
```
L3878  ⚪  (score=0)
```python
        doc=doc, body=body, decorators=decorators, is_async_def=is_async_def,
```
L3879  ⚪  (score=0)
```python
        return_type_annotation=return_type_annotation)
```
L3880  ⚪  (score=0)
```python
```
L3881  ⚪  (score=0)
```python
```
L3882  ⚪  (score=0)
```python
@cython.cfunc
```
L3883  ⚪  (score=0)
```python
def p_varargslist(s: PyrexScanner, terminator: cython.Py_UCS4 = ')', annotated: cython.bint = True) -> tuple:
```
L3884  ⚪  (score=0)
```python
    args = p_c_arg_list(s, in_pyfunc=True, nonempty_declarators=True,
```
L3885  ⚪  (score=0)
```python
                        annotated = annotated)
```
L3886  ⚪  (score=0)
```python
    star_arg = None
```
L3887  ⚪  (score=0)
```python
    starstar_arg = None
```
L3888  ⚪  (score=0)
```python
    if s.sy == '/':
```
L3889  ⚪  (score=0)
```python
        if len(args) == 0:
```
L3890  ⚪  (score=0)
```python
            s.error("Got zero positional-only arguments despite presence of "
```
L3891  ⚪  (score=0)
```python
                    "positional-only specifier '/'")
```
L3892  ⚪  (score=0)
```python
        s.next()
```
L3893  ⚪  (score=0)
```python
        # Mark all args to the left as pos only
```
L3894  ⚪  (score=0)
```python
        for arg in args:
```
L3895  ⚪  (score=0)
```python
            arg.pos_only = 1
```
L3896  ⚪  (score=0)
```python
        if s.sy == ',':
```
L3897  ⚪  (score=0)
```python
            s.next()
```
L3898  ⚪  (score=0)
```python
            args.extend(p_c_arg_list(
```
L3899  ⚪  (score=0)
```python
                s, in_pyfunc=True, nonempty_declarators=True, annotated = annotated))
```
L3900  ⚪  (score=0)
```python
        elif s.sy != terminator:
```
L3901  ⚪  (score=0)
```python
            s.error("Syntax error in Python function argument list")
```
L3902  ⚪  (score=0)
```python
    if s.sy == '*':
```
L3903  ⚪  (score=0)
```python
        s.next()
```
L3904  ⚪  (score=0)
```python
        if s.sy == 'IDENT':
```
L3905  ⚪  (score=0)
```python
            star_arg = p_py_arg_decl(s, annotated=annotated)
```
L3906  ⚪  (score=0)
```python
        if s.sy == ',':
```
L3907  ⚪  (score=0)
```python
            s.next()
```
L3908  ⚪  (score=0)
```python
            args.extend(p_c_arg_list(
```
L3909  ⚪  (score=0)
```python
                s, in_pyfunc =True, nonempty_declarators=True, kw_only=True, annotated = annotated))
```
L3910  ⚪  (score=0)
```python
        elif s.sy != terminator:
```
L3911  ⚪  (score=0)
```python
            s.error("Syntax error in Python function argument list")
```
L3912  ⚪  (score=0)
```python
    if s.sy == '**':
```
L3913  ⚪  (score=0)
```python
        s.next()
```
L3914  ⚪  (score=0)
```python
        starstar_arg = p_py_arg_decl(s, annotated=annotated)
```
L3915  ⚪  (score=0)
```python
    if s.sy == ',':
```
L3916  ⚪  (score=0)
```python
        s.next()
```
L3917  ⚪  (score=0)
```python
    return (args, star_arg, starstar_arg)
```
L3918  ⚪  (score=0)
```python
```
L3919  ⚪  (score=0)
```python
```
L3920  ⚪  (score=0)
```python
@cython.cfunc
```
L3921  ⚪  (score=0)
```python
def p_py_arg_decl(s: PyrexScanner, annotated: cython.bint = True):
```
L3922  ⚪  (score=0)
```python
    pos = s.position()
```
L3923  ⚪  (score=0)
```python
    name = p_ident(s)
```
L3924  ⚪  (score=0)
```python
    annotation = None
```
L3925  ⚪  (score=0)
```python
    if annotated and s.sy == ':':
```
L3926  ⚪  (score=0)
```python
        s.next()
```
L3927  ⚪  (score=0)
```python
        annotation = p_annotation(s)
```
L3928  ⚪  (score=0)
```python
    return Nodes.PyArgDeclNode(pos, name = name, annotation = annotation)
```
L3929  ⚪  (score=0)
```python
```
L3930  ⚪  (score=0)
```python
```
L3931  ⚪  (score=0)
```python
@cython.cfunc
```
L3932  ⚪  (score=0)
```python
def p_class_statement(s: PyrexScanner, decorators):
```
L3933  ⚪  (score=0)
```python
    # s.sy == 'class'
```
L3934  ⚪  (score=0)
```python
    pos = s.position()
```
L3935  ⚪  (score=0)
```python
    s.next()
```
L3936  ⚪  (score=0)
```python
    class_name = EncodedString(p_ident(s))
```
L3937  ⚪  (score=0)
```python
    class_name.encoding = s.source_encoding  # FIXME: why is this needed?
```
L3938  ⚪  (score=0)
```python
    arg_tuple = None
```
L3939  ⚪  (score=0)
```python
    keyword_dict = None
```
L3940  ⚪  (score=0)
```python
    if s.sy == '(':
```
L3941  ⚪  (score=0)
```python
        positional_args, keyword_args = p_call_parse_args(s, allow_genexp=False)
```
L3942  ⚪  (score=0)
```python
        arg_tuple, keyword_dict = p_call_build_packed_args(pos, positional_args, keyword_args)
```
L3943  ⚪  (score=0)
```python
    if arg_tuple is None:
```
L3944  ⚪  (score=0)
```python
        # XXX: empty arg_tuple
```
L3945  ⚪  (score=0)
```python
        arg_tuple = ExprNodes.TupleNode(pos, args=[])
```
L3946  ⚪  (score=0)
```python
    doc, body = p_suite_with_docstring(s, Ctx(level='class'))
```
L3947  ⚪  (score=0)
```python
    return Nodes.PyClassDefNode(
```
L3948  ⚪  (score=0)
```python
        pos, name=class_name,
```
L3949  ⚪  (score=0)
```python
        bases=arg_tuple,
```
L3950  ⚪  (score=0)
```python
        keyword_args=keyword_dict,
```
L3951  ⚪  (score=0)
```python
        doc=doc, body=body, decorators=decorators,
```
L3952  ⚪  (score=0)
```python
        force_py3_semantics=s.context.language_level >= 3)
```
L3953  ⚪  (score=0)
```python
```
L3954  ⚪  (score=0)
```python
```
L3955  ⚪  (score=0)
```python
@cython.cfunc
```
L3956  ⚪  (score=0)
```python
def p_c_class_definition(s: PyrexScanner, pos,  ctx):
```
L3957  ⚪  (score=0)
```python
    # s.sy == 'class'
```
L3958  ⚪  (score=0)
```python
    s.next()
```
L3959  ⚪  (score=0)
```python
    module_path = []
```
L3960  ⚪  (score=0)
```python
    class_name = p_ident(s)
```
L3961  ⚪  (score=0)
```python
    while s.sy == '.':
```
L3962  ⚪  (score=0)
```python
        s.next()
```
L3963  ⚪  (score=0)
```python
        module_path.append(class_name)
```
L3964  ⚪  (score=0)
```python
        class_name = p_ident(s)
```
L3965  ⚪  (score=0)
```python
    if module_path and ctx.visibility != 'extern':
```
L3966  ⚪  (score=0)
```python
        error(pos, "Qualified class name only allowed for 'extern' C class")
```
L3967  ⚪  (score=0)
```python
    if module_path and s.sy == 'IDENT' and s.systring == 'as':
```
L3968  ⚪  (score=0)
```python
        s.next()
```
L3969  ⚪  (score=0)
```python
        as_name = p_ident(s)
```
L3970  ⚪  (score=0)
```python
    else:
```
L3971  ⚪  (score=0)
```python
        as_name = class_name
```
L3972  ⚪  (score=0)
```python
    objstruct_name = None
```
L3973  ⚪  (score=0)
```python
    typeobj_name = None
```
L3974  ⚪  (score=0)
```python
    bases = None
```
L3975  ⚪  (score=0)
```python
    check_size = None
```
L3976  ⚪  (score=0)
```python
    if s.sy == '(':
```
L3977  ⚪  (score=0)
```python
        positional_args, keyword_args = p_call_parse_args(s, allow_genexp=False)
```
L3978  ⚪  (score=0)
```python
        if keyword_args:
```
L3979  ⚪  (score=0)
```python
            s.error("C classes cannot take keyword bases.")
```
L3980  ⚪  (score=0)
```python
        bases, _ = p_call_build_packed_args(pos, positional_args, keyword_args)
```
L3981  ⚪  (score=0)
```python
    if bases is None:
```
L3982  ⚪  (score=0)
```python
        bases = ExprNodes.TupleNode(pos, args=[])
```
L3983  ⚪  (score=0)
```python
```
L3984  ⚪  (score=0)
```python
    if s.sy == '[':
```
L3985  ⚪  (score=0)
```python
        if ctx.visibility not in ('public', 'extern') and not ctx.api:
```
L3986  ⚪  (score=0)
```python
            error(s.position(), "Name options only allowed for 'public', 'api', or 'extern' C class")
```
L3987  ⚪  (score=0)
```python
        objstruct_name, typeobj_name, check_size = p_c_class_options(s)
```
L3988  ⚪  (score=0)
```python
    if s.sy == ':':
```
L3989  ⚪  (score=0)
```python
        if ctx.level == 'module_pxd':
```
L3990  ⚪  (score=0)
```python
            body_level = 'c_class_pxd'
```
L3991  ⚪  (score=0)
```python
        else:
```
L3992  ⚪  (score=0)
```python
            body_level = 'c_class'
```
L3993  ⚪  (score=0)
```python
        doc, body = p_suite_with_docstring(s, Ctx(level=body_level))
```
L3994  ⚪  (score=0)
```python
    else:
```
L3995  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in C class definition")
```
L3996  ⚪  (score=0)
```python
        doc = None
```
L3997  ⚪  (score=0)
```python
        body = None
```
L3998  ⚪  (score=0)
```python
    if ctx.visibility == 'extern':
```
L3999  ⚪  (score=0)
```python
        if not module_path:
```
L4000  ⚪  (score=0)
```python
            error(pos, "Module name required for 'extern' C class")
```
L4001  ⚪  (score=0)
```python
        if typeobj_name:
```
L4002  ⚪  (score=0)
```python
            error(pos, "Type object name specification not allowed for 'extern' C class")
```
L4003  ⚪  (score=0)
```python
    elif ctx.visibility == 'public':
```
L4004  ⚪  (score=0)
```python
        if not objstruct_name:
```
L4005  ⚪  (score=0)
```python
            error(pos, "Object struct name specification required for 'public' C class")
```
L4006  ⚪  (score=0)
```python
        if not typeobj_name:
```
L4007  ⚪  (score=0)
```python
            error(pos, "Type object name specification required for 'public' C class")
```
L4008  ⚪  (score=0)
```python
    elif ctx.visibility == 'private':
```
L4009  ⚪  (score=0)
```python
        if ctx.api:
```
L4010  ⚪  (score=0)
```python
            if not objstruct_name:
```
L4011  ⚪  (score=0)
```python
                error(pos, "Object struct name specification required for 'api' C class")
```
L4012  ⚪  (score=0)
```python
            if not typeobj_name:
```
L4013  ⚪  (score=0)
```python
                error(pos, "Type object name specification required for 'api' C class")
```
L4014  ⚪  (score=0)
```python
    else:
```
L4015  ⚪  (score=0)
```python
        error(pos, "Invalid class visibility '%s'" % ctx.visibility)
```
L4016  ⚪  (score=0)
```python
    return Nodes.CClassDefNode(pos,
```
L4017  ⚪  (score=0)
```python
        visibility = ctx.visibility,
```
L4018  ⚪  (score=0)
```python
        typedef_flag = ctx.typedef_flag,
```
L4019  ⚪  (score=0)
```python
        api = ctx.api,
```
L4020  ⚪  (score=0)
```python
        module_name = ".".join(module_path),
```
L4021  ⚪  (score=0)
```python
        class_name = class_name,
```
L4022  ⚪  (score=0)
```python
        as_name = as_name,
```
L4023  ⚪  (score=0)
```python
        bases = bases,
```
L4024  ⚪  (score=0)
```python
        objstruct_name = objstruct_name,
```
L4025  ⚪  (score=0)
```python
        typeobj_name = typeobj_name,
```
L4026  ⚪  (score=0)
```python
        check_size = check_size,
```
L4027  ⚪  (score=0)
```python
        in_pxd = ctx.level == 'module_pxd',
```
L4028  ⚪  (score=0)
```python
        doc = doc,
```
L4029  ⚪  (score=0)
```python
        body = body)
```
L4030  ⚪  (score=0)
```python
```
L4031  ⚪  (score=0)
```python
```
L4032  ⚪  (score=0)
```python
@cython.cfunc
```
L4033  ⚪  (score=0)
```python
def p_c_class_options(s: PyrexScanner) -> tuple:
```
L4034  ⚪  (score=0)
```python
    objstruct_name = None
```
L4035  ⚪  (score=0)
```python
    typeobj_name = None
```
L4036  ⚪  (score=0)
```python
    check_size = None
```
L4037  ⚪  (score=0)
```python
    s.expect('[')
```
L4038  ⚪  (score=0)
```python
    while 1:
```
L4039  ⚪  (score=0)
```python
        if s.sy != 'IDENT':
```
L4040  ⚪  (score=0)
```python
            break
```
L4041  ⚪  (score=0)
```python
        if s.systring == 'object':
```
L4042  ⚪  (score=0)
```python
            s.next()
```
L4043  ⚪  (score=0)
```python
            objstruct_name = p_ident(s)
```
L4044  ⚪  (score=0)
```python
        elif s.systring == 'type':
```
L4045  ⚪  (score=0)
```python
            s.next()
```
L4046  ⚪  (score=0)
```python
            typeobj_name = p_ident(s)
```
L4047  ⚪  (score=0)
```python
        elif s.systring == 'check_size':
```
L4048  ⚪  (score=0)
```python
            s.next()
```
L4049  ⚪  (score=0)
```python
            check_size = p_ident(s)
```
L4050  ⚪  (score=0)
```python
            if check_size not in ('ignore', 'warn', 'error'):
```
L4051  ⚪  (score=0)
```python
                s.error("Expected one of ignore, warn or error, found %r" % check_size)
```
L4052  ⚪  (score=0)
```python
        if s.sy != ',':
```
L4053  ⚪  (score=0)
```python
            break
```
L4054  ⚪  (score=0)
```python
        s.next()
```
L4055  ⚪  (score=0)
```python
    s.expect(']', "Expected 'object', 'type' or 'check_size'")
```
L4056  ⚪  (score=0)
```python
    return objstruct_name, typeobj_name, check_size
```
L4057  ⚪  (score=0)
```python
```
L4058  ⚪  (score=0)
```python
```
L4059  ⚪  (score=0)
```python
@cython.cfunc
```
L4060  ⚪  (score=0)
```python
def p_property_decl(s: PyrexScanner):
```
L4061  ⚪  (score=0)
```python
    pos = s.position()
```
L4062  ⚪  (score=0)
```python
    s.next()  # 'property'
```
L4063  ⚪  (score=0)
```python
    name = p_ident(s)
```
L4064  ⚪  (score=0)
```python
    doc, body = p_suite_with_docstring(
```
L4065  ⚪  (score=0)
```python
        s, Ctx(level='property'), with_doc_only=True)
```
L4066  ⚪  (score=0)
```python
    return Nodes.PropertyNode(pos, name=name, doc=doc, body=body)
```
L4067  ⚪  (score=0)
```python
```
L4068  ⚪  (score=0)
```python
```
L4069  ⚪  (score=0)
```python
@cython.cfunc
```
L4070  ⚪  (score=0)
```python
def p_ignorable_statement(s: PyrexScanner):
```
L4071  ⚪  (score=0)
```python
    """
```
L4072  ⚪  (score=0)
```python
    Parses any kind of ignorable statement that is allowed in .pxd files.
```
L4073  ⚪  (score=0)
```python
    """
```
L4074  ⚪  (score=0)
```python
    if s.sy == 'BEGIN_STRING':
```
L4075  ⚪  (score=0)
```python
        pos = s.position()
```
L4076  ⚪  (score=0)
```python
        string_node = p_atom(s)
```
L4077  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in string", ignore_semicolon=True)
```
L4078  ⚪  (score=0)
```python
        return Nodes.ExprStatNode(pos, expr=string_node)
```
L4079  ⚪  (score=0)
```python
    return None
```
L4080  ⚪  (score=0)
```python
```
L4081  ⚪  (score=0)
```python
```
L4082  ⚪  (score=0)
```python
@cython.cfunc
```
L4083  ⚪  (score=0)
```python
def p_doc_string(s: PyrexScanner):
```
L4084  ⚪  (score=0)
```python
    if s.sy == 'BEGIN_STRING':
```
L4085  ⚪  (score=0)
```python
        pos = s.position()
```
L4086  ⚪  (score=0)
```python
        kind, bytes_result, unicode_result = p_cat_string_literal(s)
```
L4087  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in doc string", ignore_semicolon=True)
```
L4088  ⚪  (score=0)
```python
        if kind in ('u', ''):
```
L4089  ⚪  (score=0)
```python
            return unicode_result
```
L4090  ⚪  (score=0)
```python
        warning(pos, "Python 3 requires docstrings to be unicode strings")
```
L4091  ⚪  (score=0)
```python
        return bytes_result
```
L4092  ⚪  (score=0)
```python
    else:
```
L4093  ⚪  (score=0)
```python
        return None
```
L4094  ⚪  (score=0)
```python
```
L4095  ⚪  (score=0)
```python
```
L4096  ⚪  (score=0)
```python
@cython.cfunc
```
L4097  ⚪  (score=0)
```python
def _extract_docstring(node) -> tuple:
```
L4098  ⚪  (score=0)
```python
    """
```
L4099  ⚪  (score=0)
```python
    Extract a docstring from a statement or from the first statement
```
L4100  ⚪  (score=0)
```python
    in a list.  Remove the statement if found.  Return a tuple
```
L4101  ⚪  (score=0)
```python
    (plain-docstring or None, node).
```
L4102  ⚪  (score=0)
```python
    """
```
L4103  ⚪  (score=0)
```python
    doc_node = None
```
L4104  ⚪  (score=0)
```python
    if node is None:
```
L4105  ⚪  (score=0)
```python
        pass
```
L4106  ⚪  (score=0)
```python
    elif isinstance(node, Nodes.ExprStatNode):
```
L4107  ⚪  (score=0)
```python
        if node.expr.is_string_literal:
```
L4108  ⚪  (score=0)
```python
            doc_node = node.expr
```
L4109  ⚪  (score=0)
```python
            node = Nodes.StatListNode(node.pos, stats=[])
```
L4110  ⚪  (score=0)
```python
    elif isinstance(node, Nodes.StatListNode) and node.stats:
```
L4111  ⚪  (score=0)
```python
        stats = node.stats
```
L4112  ⚪  (score=0)
```python
        if isinstance(stats[0], Nodes.ExprStatNode):
```
L4113  ⚪  (score=0)
```python
            if stats[0].expr.is_string_literal:
```
L4114  ⚪  (score=0)
```python
                doc_node = stats[0].expr
```
L4115  ⚪  (score=0)
```python
                del stats[0]
```
L4116  ⚪  (score=0)
```python
```
L4117  ⚪  (score=0)
```python
    if doc_node is None:
```
L4118  ⚪  (score=0)
```python
        doc = None
```
L4119  ⚪  (score=0)
```python
    elif isinstance(doc_node, ExprNodes.BytesNode):
```
L4120  ⚪  (score=0)
```python
        warning(node.pos,
```
L4121  ⚪  (score=0)
```python
                "Python 3 requires docstrings to be unicode strings")
```
L4122  ⚪  (score=0)
```python
        doc = doc_node.value
```
L4123  ⚪  (score=0)
```python
    else:
```
L4124  ⚪  (score=0)
```python
        doc = doc_node.value
```
L4125  ⚪  (score=0)
```python
    return doc, node
```
L4126  ⚪  (score=0)
```python
```
L4127  ⚪  (score=0)
```python
```
L4128  ⚪  (score=0)
```python
@cython.ccall
```
L4129  ⚪  (score=0)
```python
def p_code(s: PyrexScanner, level=None, ctx=Ctx):
```
L4130  ⚪  (score=0)
```python
    body = p_statement_list(s, ctx(level = level), first_statement=True)
```
L4131  ⚪  (score=0)
```python
    if s.sy != 'EOF':
```
L4132  ⚪  (score=0)
```python
        s.error("Syntax error in statement [%s,%s]" % (
```
L4133  ⚪  (score=0)
```python
            repr(s.sy), repr(s.systring)))
```
L4134  ⚪  (score=0)
```python
    return body
```
L4135  ⚪  (score=0)
```python
```
L4136  ⚪  (score=0)
```python
```
L4137  ⚪  (score=0)
```python
_match_compiler_directive_comment = cython.declare(object, re.compile(
```
L4138  ⚪  (score=0)
```python
    r"^#\s*cython\s*:\s*((\w|[.])+\s*=.*)$").match)
```
L4139  ⚪  (score=0)
```python
```
L4140  ⚪  (score=0)
```python
```
L4141  ⚪  (score=0)
```python
def _parse_directive_assignments(
```
L4142  ⚪  (score=0)
```python
    spec: str,
```
L4143  ⚪  (score=0)
```python
    *,
```
L4144  ⚪  (score=0)
```python
    relaxed_bool: bool = False,
```
L4145  ⚪  (score=0)
```python
    ignore_unknown: bool = False,
```
L4146  ⚪  (score=0)
```python
    current_settings: Optional[dict] = None,
```
L4147  ⚪  (score=0)
```python
) -> dict:
```
L4148  ⚪  (score=0)
```python
    directives = Directives.Directives()
```
L4149  ⚪  (score=0)
```python
    result: dict = dict(current_settings or {})
```
L4150  ⚪  (score=0)
```python
    def _coerce_value(name: str, raw_value: str, relaxed: bool) -> Any:
```
L4151  ⚪  (score=0)
```python
        type_info = Directives.directive_types.get(name)
```
L4152  ⚪  (score=0)
```python
        if type_info is bool:
```
L4153  ⚪  (score=0)
```python
            text = raw_value if not relaxed else raw_value.lower()
```
L4154  ⚪  (score=0)
```python
            truthy = {"true", "yes", "1"} if relaxed else {"True"}
```
L4155  ⚪  (score=0)
```python
            falsy = {"false", "no", "0"} if relaxed else {"False"}
```
L4156  ⚪  (score=0)
```python
            if text in truthy:
```
L4157  ⚪  (score=0)
```python
                return True
```
L4158  ⚪  (score=0)
```python
            if text in falsy:
```
L4159  ⚪  (score=0)
```python
                return False
```
L4160  ⚪  (score=0)
```python
            raise ValueError(
```
L4161  ⚪  (score=0)
```python
                f"{name} directive must be set to True or False, got '{raw_value}'"
```
L4162  ⚪  (score=0)
```python
            )
```
L4163  ⚪  (score=0)
```python
        if type_info is int:
```
L4164  ⚪  (score=0)
```python
            try:
```
L4165  ⚪  (score=0)
```python
                return int(raw_value)
```
L4166  ⚪  (score=0)
```python
            except ValueError:
```
L4167  ⚪  (score=0)
```python
                raise ValueError(
```
L4168  ⚪  (score=0)
```python
                    f"{name} directive must be set to an integer, got '{raw_value}'"
```
L4169  ⚪  (score=0)
```python
                ) from None
```
L4170  ⚪  (score=0)
```python
        if type_info is str:
```
L4171  ⚪  (score=0)
```python
            return raw_value
```
L4172  ⚪  (score=0)
```python
        if callable(type_info):
```
L4173  ⚪  (score=0)
```python
            return type_info(name, raw_value)
```
L4174  ⚪  (score=0)
```python
        return raw_value
```
L4175  ⚪  (score=0)
```python
    for item in spec.split(","):
```
L4176  ⚪  (score=0)
```python
        item = item.strip()
```
L4177  ⚪  (score=0)
```python
        if not item:
```
L4178  ⚪  (score=0)
```python
            continue
```
L4179  ⚪  (score=0)
```python
        if "=" not in item:
```
L4180  ⚪  (score=0)
```python
            raise ValueError(f'Expected "=" in option "{item}"')
```
L4181  ⚪  (score=0)
```python
        name, raw_value = [s.strip() for s in item.split("=", 1)]
```
L4182  ⚪  (score=0)
```python
        if name.endswith(".all"):
```
L4183  ⚪  (score=0)
```python
            prefix = name[:len(name) - 3]
```
L4184  ⚪  (score=0)
```python
            found_any = False
```
L4185  ⚪  (score=0)
```python
            for directive in directives:
```
L4186  ⚪  (score=0)
```python
                if directive.startswith(prefix):
```
L4187  ⚪  (score=0)
```python
                    found_any = True
```
L4188  ⚪  (score=0)
```python
                    result[directive] = _coerce_value(directive, raw_value, relaxed_bool)
```
L4189  ⚪  (score=0)
```python
            if not found_any and not ignore_unknown:
```
L4190  ⚪  (score=0)
```python
                raise ValueError(f'Unknown option: "{name}"')
```
L4191  ⚪  (score=0)
```python
            continue
```
L4192  ⚪  (score=0)
```python
```
L4193  ⚪  (score=0)
```python
        if name not in directives:
```
L4194  ⚪  (score=0)
```python
            if not ignore_unknown:
```
L4195  ⚪  (score=0)
```python
                raise ValueError(f'Unknown option: "{name}"')
```
L4196  ⚪  (score=0)
```python
            continue
```
L4197  ⚪  (score=0)
```python
```
L4198  ⚪  (score=0)
```python
        dtype = Directives.directive_types.get(name)
```
L4199  ⚪  (score=0)
```python
        if dtype is list:
```
L4200  ⚪  (score=0)
```python
            if name in result and isinstance(result[name], list):
```
L4201  ⚪  (score=0)
```python
                result[name].append(raw_value)
```
L4202  ⚪  (score=0)
```python
            else:
```
L4203  ⚪  (score=0)
```python
                result[name] = [raw_value]
```
L4204  ⚪  (score=0)
```python
        else:
```
L4205  ⚪  (score=0)
```python
            result[name] = _coerce_value(name, raw_value, relaxed_bool)
```
L4206  ⚪  (score=0)
```python
    return result
```
L4207  ⚪  (score=0)
```python
```
L4208  ⚪  (score=0)
```python
```
L4209  ⚪  (score=0)
```python
@cython.cfunc
```
L4210  ⚪  (score=0)
```python
def p_compiler_directive_comments(s: PyrexScanner) -> dict:
```
L4211  ⚪  (score=0)
```python
    result = {}
```
L4212  ⚪  (score=0)
```python
    while s.sy == 'commentline':
```
L4213  ⚪  (score=0)
```python
        pos = s.position()
```
L4214  ⚪  (score=0)
```python
        m = _match_compiler_directive_comment(s.systring)
```
L4215  ⚪  (score=0)
```python
        if m:
```
L4216  ⚪  (score=0)
```python
            directives_string = m.group(1).strip()
```
L4217  ⚪  (score=0)
```python
            try:
```
L4218  ⚪  (score=0)
```python
                new_directives = _parse_directive_assignments(
```
L4219  ⚪  (score=0)
```python
                    directives_string, ignore_unknown=True
```
L4220  ⚪  (score=0)
```python
                )
```
L4221  ⚪  (score=0)
```python
            except ValueError as e:
```
L4222  ⚪  (score=0)
```python
                s.error(e.args[0], fatal=False)
```
L4223  ⚪  (score=0)
```python
                s.next()
```
L4224  ⚪  (score=0)
```python
                continue
```
L4225  ⚪  (score=0)
```python
```
L4226  ⚪  (score=0)
```python
            for name in new_directives:
```
L4227  ⚪  (score=0)
```python
                if name not in result:
```
L4228  ⚪  (score=0)
```python
                    pass
```
L4229  ⚪  (score=0)
```python
                elif Directives.GLOBAL_DIRECTIVES.directive_types.get(name) is list:
```
L4230  ⚪  (score=0)
```python
                    result[name] += new_directives[name]
```
L4231  ⚪  (score=0)
```python
                    new_directives[name] = result[name]
```
L4232  ⚪  (score=0)
```python
                elif new_directives[name] == result[name]:
```
L4233  ⚪  (score=0)
```python
                    warning(pos, "Duplicate directive found: %s" % (name,))
```
L4234  ⚪  (score=0)
```python
                else:
```
L4235  ⚪  (score=0)
```python
                    s.error("Conflicting settings found for top-level directive %s: %r and %r" % (
```
L4236  ⚪  (score=0)
```python
                        name, result[name], new_directives[name]), pos=pos)
```
L4237  ⚪  (score=0)
```python
```
L4238  ⚪  (score=0)
```python
            if 'language_level' in new_directives:
```
L4239  ⚪  (score=0)
```python
                # Make sure we apply the language level already to the first token that follows the comments.
```
L4240  ⚪  (score=0)
```python
                s.context.set_language_level(new_directives['language_level'])
```
L4241  ⚪  (score=0)
```python
            if 'legacy_implicit_noexcept' in new_directives:
```
L4242  ⚪  (score=0)
```python
                s.context.legacy_implicit_noexcept = new_directives['legacy_implicit_noexcept']
```
L4243  ⚪  (score=0)
```python
```
L4244  ⚪  (score=0)
```python
```
L4245  ⚪  (score=0)
```python
            result.update(new_directives)
```
L4246  ⚪  (score=0)
```python
```
L4247  ⚪  (score=0)
```python
        s.next()
```
L4248  ⚪  (score=0)
```python
    return result
```
L4249  ⚪  (score=0)
```python
```
L4250  ⚪  (score=0)
```python
```
L4251  ⚪  (score=0)
```python
@cython.ccall
```
L4252  ⚪  (score=0)
```python
def p_module(s: PyrexScanner, pxd, full_module_name, ctx=Ctx):
```
L4253  ⚪  (score=0)
```python
    pos = s.position()
```
L4254  ⚪  (score=0)
```python
```
L4255  ⚪  (score=0)
```python
    directive_comments = p_compiler_directive_comments(s)
```
L4256  ⚪  (score=0)
```python
    s.parse_comments = False
```
L4257  ⚪  (score=0)
```python
```
L4258  ⚪  (score=0)
```python
    if s.context.language_level is None:
```
L4259  ⚪  (score=0)
```python
        s.context.set_language_level('3')
```
L4260  ⚪  (score=0)
```python
```
L4261  ⚪  (score=0)
```python
    level = 'module_pxd' if pxd else 'module'
```
L4262  ⚪  (score=0)
```python
    doc = p_doc_string(s)
```
L4263  ⚪  (score=0)
```python
    body = p_statement_list(s, ctx(level=level), first_statement=True)
```
L4264  ⚪  (score=0)
```python
    if s.sy != 'EOF':
```
L4265  ⚪  (score=0)
```python
        s.error("Syntax error in statement [%s,%s]" % (
```
L4266  ⚪  (score=0)
```python
            repr(s.sy), repr(s.systring)))
```
L4267  ⚪  (score=0)
```python
    return ModuleNode(
```
L4268  ⚪  (score=0)
```python
        pos,
```
L4269  ⚪  (score=0)
```python
        doc = doc,
```
L4270  ⚪  (score=0)
```python
        body = body,
```
L4271  ⚪  (score=0)
```python
        full_module_name = full_module_name,
```
L4272  ⚪  (score=0)
```python
        directive_comments = directive_comments,
```
L4273  ⚪  (score=0)
```python
        directives = Directives.DIRECTIVE_DEFAULTS,
```
L4274  ⚪  (score=0)
```python
    )
```
L4275  ⚪  (score=0)
```python
```
L4276  ⚪  (score=0)
```python
```
L4277  ⚪  (score=0)
```python
@cython.cfunc
```
L4278  ⚪  (score=0)
```python
def p_template_definition(s: PyrexScanner) -> tuple:
```
L4279  ⚪  (score=0)
```python
    name = p_ident(s)
```
L4280  ⚪  (score=0)
```python
    if s.sy == '=':
```
L4281  ⚪  (score=0)
```python
        s.expect('=')
```
L4282  ⚪  (score=0)
```python
        s.expect('*')
```
L4283  ⚪  (score=0)
```python
        required = False
```
L4284  ⚪  (score=0)
```python
    else:
```
L4285  ⚪  (score=0)
```python
        required = True
```
L4286  ⚪  (score=0)
```python
    return name, required
```
L4287  ⚪  (score=0)
```python
```
L4288  ⚪  (score=0)
```python
```
L4289  ⚪  (score=0)
```python
@cython.cfunc
```
L4290  ⚪  (score=0)
```python
def p_cpp_class_definition(s: PyrexScanner, pos,  ctx):
```
L4291  ⚪  (score=0)
```python
    # s.sy == 'cppclass'
```
L4292  ⚪  (score=0)
```python
    s.next()
```
L4293  ⚪  (score=0)
```python
    class_name = p_ident(s)
```
L4294  ⚪  (score=0)
```python
    cname = p_opt_cname(s)
```
L4295  ⚪  (score=0)
```python
    if cname is None and ctx.namespace is not None:
```
L4296  ⚪  (score=0)
```python
        cname = ctx.namespace + "::" + class_name
```
L4297  ⚪  (score=0)
```python
    if s.sy == '.':
```
L4298  ⚪  (score=0)
```python
        error(pos, "Qualified class name not allowed C++ class")
```
L4299  ⚪  (score=0)
```python
    if s.sy == '[':
```
L4300  ⚪  (score=0)
```python
        s.next()
```
L4301  ⚪  (score=0)
```python
        templates = [p_template_definition(s)]
```
L4302  ⚪  (score=0)
```python
        while s.sy == ',':
```
L4303  ⚪  (score=0)
```python
            s.next()
```
L4304  ⚪  (score=0)
```python
            templates.append(p_template_definition(s))
```
L4305  ⚪  (score=0)
```python
        s.expect(']')
```
L4306  ⚪  (score=0)
```python
        template_names = [name for name, required in templates]
```
L4307  ⚪  (score=0)
```python
    else:
```
L4308  ⚪  (score=0)
```python
        templates = None
```
L4309  ⚪  (score=0)
```python
        template_names = None
```
L4310  ⚪  (score=0)
```python
    if s.sy == '(':
```
L4311  ⚪  (score=0)
```python
        s.next()
```
L4312  ⚪  (score=0)
```python
        base_classes = [p_c_base_type(s, templates = template_names)]
```
L4313  ⚪  (score=0)
```python
        while s.sy == ',':
```
L4314  ⚪  (score=0)
```python
            s.next()
```
L4315  ⚪  (score=0)
```python
            base_classes.append(p_c_base_type(s, templates = template_names))
```
L4316  ⚪  (score=0)
```python
        s.expect(')')
```
L4317  ⚪  (score=0)
```python
    else:
```
L4318  ⚪  (score=0)
```python
        base_classes = []
```
L4319  ⚪  (score=0)
```python
    if s.sy == '[':
```
L4320  ⚪  (score=0)
```python
        error(s.position(), "Name options not allowed for C++ class")
```
L4321  ⚪  (score=0)
```python
    nogil = p_nogil(s)
```
L4322  ⚪  (score=0)
```python
    if s.sy == ':':
```
L4323  ⚪  (score=0)
```python
        s.next()
```
L4324  ⚪  (score=0)
```python
        s.expect('NEWLINE')
```
L4325  ⚪  (score=0)
```python
        s.expect_indent()
```
L4326  ⚪  (score=0)
```python
        # Allow a cppclass to have docstrings. It will be discarded as comment.
```
L4327  ⚪  (score=0)
```python
        # The goal of this is consistency: we can make docstrings inside cppclass methods,
```
L4328  ⚪  (score=0)
```python
        # so why not on the cppclass itself ?
```
L4329  ⚪  (score=0)
```python
        p_doc_string(s)
```
L4330  ⚪  (score=0)
```python
        attributes = []
```
L4331  ⚪  (score=0)
```python
        body_ctx = Ctx(visibility = ctx.visibility, level='cpp_class', nogil=nogil or ctx.nogil)
```
L4332  ⚪  (score=0)
```python
        body_ctx.templates = template_names
```
L4333  ⚪  (score=0)
```python
        while s.sy != 'DEDENT':
```
L4334  ⚪  (score=0)
```python
            if s.sy != 'pass':
```
L4335  ⚪  (score=0)
```python
                attributes.append(p_cpp_class_attribute(s, body_ctx))
```
L4336  ⚪  (score=0)
```python
            else:
```
L4337  ⚪  (score=0)
```python
                s.next()
```
L4338  ⚪  (score=0)
```python
                s.expect_newline("Expected a newline")
```
L4339  ⚪  (score=0)
```python
        s.expect_dedent()
```
L4340  ⚪  (score=0)
```python
    else:
```
L4341  ⚪  (score=0)
```python
        attributes = None
```
L4342  ⚪  (score=0)
```python
        s.expect_newline("Syntax error in C++ class definition")
```
L4343  ⚪  (score=0)
```python
    return Nodes.CppClassNode(pos,
```
L4344  ⚪  (score=0)
```python
        name = class_name,
```
L4345  ⚪  (score=0)
```python
        cname = cname,
```
L4346  ⚪  (score=0)
```python
        base_classes = base_classes,
```
L4347  ⚪  (score=0)
```python
        visibility = ctx.visibility,
```
L4348  ⚪  (score=0)
```python
        in_pxd = ctx.level == 'module_pxd',
```
L4349  ⚪  (score=0)
```python
        attributes = attributes,
```
L4350  ⚪  (score=0)
```python
        templates = templates)
```
L4351  ⚪  (score=0)
```python
```
L4352  ⚪  (score=0)
```python
```
L4353  ⚪  (score=0)
```python
@cython.cfunc
```
L4354  ⚪  (score=0)
```python
def p_cpp_class_attribute(s: PyrexScanner, ctx):
```
L4355  ⚪  (score=0)
```python
    pos = s.position()
```
L4356  ⚪  (score=0)
```python
    decorators = None
```
L4357  ⚪  (score=0)
```python
    if s.sy == '@':
```
L4358  ⚪  (score=0)
```python
        decorators = p_decorators(s)
```
L4359  ⚪  (score=0)
```python
    if s.systring == 'cppclass':
```
L4360  ⚪  (score=0)
```python
        return p_cpp_class_definition(s, pos, ctx)
```
L4361  ⚪  (score=0)
```python
    elif s.systring == 'ctypedef':
```
L4362  ⚪  (score=0)
```python
        return p_ctypedef_statement(s, ctx)
```
L4363  ⚪  (score=0)
```python
    elif s.sy == 'IDENT' and s.systring in struct_enum_union:
```
L4364  ⚪  (score=0)
```python
        if s.systring != 'enum':
```
L4365  ⚪  (score=0)
```python
            return p_cpp_class_definition(s, pos, ctx)
```
L4366  ⚪  (score=0)
```python
        else:
```
L4367  ⚪  (score=0)
```python
            return p_struct_enum(s, pos, ctx)
```
L4368  ⚪  (score=0)
```python
    else:
```
L4369  ⚪  (score=0)
```python
        node = p_c_func_or_var_declaration(s, pos, ctx)
```
L4370  ⚪  (score=0)
```python
        if decorators is not None:
```
L4371  ⚪  (score=0)
```python
            tup = Nodes.CFuncDefNode, Nodes.CVarDefNode, Nodes.CClassDefNode
```
L4372  ⚪  (score=0)
```python
            if ctx.allow_struct_enum_decorator:
```
L4373  ⚪  (score=0)
```python
                tup += Nodes.CStructOrUnionDefNode, Nodes.CEnumDefNode
```
L4374  ⚪  (score=0)
```python
            if not isinstance(node, tup):
```
L4375  ⚪  (score=0)
```python
                s.error("Decorators can only be followed by functions or classes")
```
L4376  ⚪  (score=0)
```python
            node.decorators = decorators
```
L4377  ⚪  (score=0)
```python
        return node
```
L4378  ⚪  (score=0)
```python
```
L4379  ⚪  (score=0)
```python
```
L4380  ⚪  (score=0)
```python
@cython.cfunc
```
L4381  ⚪  (score=0)
```python
def p_match_statement(s: PyrexScanner, ctx):
```
L4382  ⚪  (score=0)
```python
    assert s.sy == "IDENT" and s.systring == "match"
```
L4383  ⚪  (score=0)
```python
    pos = s.position()
```
L4384  ⚪  (score=0)
```python
    with tentatively_scan(s) as errors:
```
L4385  ⚪  (score=0)
```python
        s.next()
```
L4386  ⚪  (score=0)
```python
        subject = p_namedexpr_test(s)
```
L4387  ⚪  (score=0)
```python
        subjects = None
```
L4388  ⚪  (score=0)
```python
        if s.sy == ",":
```
L4389  ⚪  (score=0)
```python
            subjects = [subject]
```
L4390  ⚪  (score=0)
```python
        while s.sy == ",":
```
L4391  ⚪  (score=0)
```python
            s.next()
```
L4392  ⚪  (score=0)
```python
            if s.sy == ":":
```
L4393  ⚪  (score=0)
```python
                break
```
L4394  ⚪  (score=0)
```python
            subjects.append(p_test(s))
```
L4395  ⚪  (score=0)
```python
        if subjects is not None:
```
L4396  ⚪  (score=0)
```python
            subject = ExprNodes.TupleNode(pos, args=subjects)
```
L4397  ⚪  (score=0)
```python
        s.expect(":")
```
L4398  ⚪  (score=0)
```python
    if errors:
```
L4399  ⚪  (score=0)
```python
        return None
```
L4400  ⚪  (score=0)
```python
```
L4401  ⚪  (score=0)
```python
    # at this stage we are committed to it being a match block so continue
```
L4402  ⚪  (score=0)
```python
    # outside "with tentatively_scan"
```
L4403  ⚪  (score=0)
```python
    # (I think this deviates from the PEG parser slightly, and it'd
```
L4404  ⚪  (score=0)
```python
    # backtrack on the whole thing)
```
L4405  ⚪  (score=0)
```python
    s.expect_newline()
```
L4406  ⚪  (score=0)
```python
    s.expect_indent()
```
L4407  ⚪  (score=0)
```python
    cases = []
```
L4408  ⚪  (score=0)
```python
    while s.sy != "DEDENT":
```
L4409  ⚪  (score=0)
```python
        cases.append(p_case_block(s, ctx))
```
L4410  ⚪  (score=0)
```python
    s.expect_dedent()
```
L4411  ⚪  (score=0)
```python
    return MatchCaseNodes.MatchNode(pos, subject=subject, cases=cases)
```
L4412  ⚪  (score=0)
```python
```
L4413  ⚪  (score=0)
```python
```
L4414  ⚪  (score=0)
```python
@cython.cfunc
```
L4415  ⚪  (score=0)
```python
def p_case_block(s: PyrexScanner, ctx):
```
L4416  ⚪  (score=0)
```python
    if not (s.sy == "IDENT" and s.systring == "case"):
```
L4417  ⚪  (score=0)
```python
        s.expected("case")
```
L4418  ⚪  (score=0)
```python
    s.next()
```
L4419  ⚪  (score=0)
```python
    pos = s.position()
```
L4420  ⚪  (score=0)
```python
    pattern = p_patterns(s)
```
L4421  ⚪  (score=0)
```python
    guard = None
```
L4422  ⚪  (score=0)
```python
    if s.sy == 'if':
```
L4423  ⚪  (score=0)
```python
        s.next()
```
L4424  ⚪  (score=0)
```python
        guard = p_test(s)
```
L4425  ⚪  (score=0)
```python
    body = p_suite(s, ctx)
```
L4426  ⚪  (score=0)
```python
```
L4427  ⚪  (score=0)
```python
    return MatchCaseNodes.MatchCaseNode(pos, pattern=pattern, body=body, guard=guard)
```
L4428  ⚪  (score=0)
```python
```
L4429  ⚪  (score=0)
```python
```
L4430  ⚪  (score=0)
```python
@cython.cfunc
```
L4431  ⚪  (score=0)
```python
def p_patterns(s: PyrexScanner):
```
L4432  ⚪  (score=0)
```python
    # note - in slight contrast to the name (which comes from the Python grammar),
```
L4433  ⚪  (score=0)
```python
    # returns a single pattern
```
L4434  ⚪  (score=0)
```python
    patterns = []
```
L4435  ⚪  (score=0)
```python
    seq = False
```
L4436  ⚪  (score=0)
```python
    pos = s.position()
```
L4437  ⚪  (score=0)
```python
    while True:
```
L4438  ⚪  (score=0)
```python
        with tentatively_scan(s) as errors:
```
L4439  ⚪  (score=0)
```python
            pattern = p_maybe_star_pattern(s)
```
L4440  ⚪  (score=0)
```python
        if errors:
```
L4441  ⚪  (score=0)
```python
            if patterns:
```
L4442  ⚪  (score=0)
```python
                break  # all is good provided we have at least 1 pattern
```
L4443  ⚪  (score=0)
```python
            else:
```
L4444  ⚪  (score=0)
```python
                e = errors[0]
```
L4445  ⚪  (score=0)
```python
                s.error(e.args[1], pos=e.args[0])
```
L4446  ⚪  (score=0)
```python
        patterns.append(pattern)
```
L4447  ⚪  (score=0)
```python
```
L4448  ⚪  (score=0)
```python
        if s.sy == ",":
```
L4449  ⚪  (score=0)
```python
            seq = True
```
L4450  ⚪  (score=0)
```python
            s.next()
```
L4451  ⚪  (score=0)
```python
            if s.sy in [":", "if"]:
```
L4452  ⚪  (score=0)
```python
                break  # common reasons to break
```
L4453  ⚪  (score=0)
```python
        else:
```
L4454  ⚪  (score=0)
```python
            break
```
L4455  ⚪  (score=0)
```python
```
L4456  ⚪  (score=0)
```python
    if seq:
```
L4457  ⚪  (score=0)
```python
        return MatchCaseNodes.MatchSequencePatternNode(pos, patterns=patterns)
```
L4458  ⚪  (score=0)
```python
    else:
```
L4459  ⚪  (score=0)
```python
        return patterns[0]
```
L4460  ⚪  (score=0)
```python
```
L4461  ⚪  (score=0)
```python
```
L4462  ⚪  (score=0)
```python
@cython.cfunc
```
L4463  ⚪  (score=0)
```python
def p_maybe_star_pattern(s: PyrexScanner):
```
L4464  ⚪  (score=0)
```python
    # For match case. Either star_pattern or pattern
```
L4465  ⚪  (score=0)
```python
    if s.sy == "*":
```
L4466  ⚪  (score=0)
```python
        # star pattern
```
L4467  ⚪  (score=0)
```python
        s.next()
```
L4468  ⚪  (score=0)
```python
        target = None
```
L4469  ⚪  (score=0)
```python
        if s.systring != "_":  # for match-case '_' is treated as a special wildcard
```
L4470  ⚪  (score=0)
```python
            target = p_pattern_capture_target(s)
```
L4471  ⚪  (score=0)
```python
        else:
```
L4472  ⚪  (score=0)
```python
            s.next()
```
L4473  ⚪  (score=0)
```python
        pattern = MatchCaseNodes.MatchAndAssignPatternNode(
```
L4474  ⚪  (score=0)
```python
            s.position(), target=target, is_star=True
```
L4475  ⚪  (score=0)
```python
        )
```
L4476  ⚪  (score=0)
```python
        return pattern
```
L4477  ⚪  (score=0)
```python
    else:
```
L4478  ⚪  (score=0)
```python
        pattern = p_pattern(s)
```
L4479  ⚪  (score=0)
```python
        return pattern
```
L4480  ⚪  (score=0)
```python
```
L4481  ⚪  (score=0)
```python
```
L4482  ⚪  (score=0)
```python
@cython.cfunc
```
L4483  ⚪  (score=0)
```python
def p_pattern(s: PyrexScanner):
```
L4484  ⚪  (score=0)
```python
    # try "as_pattern" then "or_pattern"
```
L4485  ⚪  (score=0)
```python
    # (but practically "as_pattern" starts with "or_pattern" too)
```
L4486  ⚪  (score=0)
```python
    patterns = []
```
L4487  ⚪  (score=0)
```python
    pos = s.position()
```
L4488  ⚪  (score=0)
```python
    while True:
```
L4489  ⚪  (score=0)
```python
        patterns.append(p_closed_pattern(s))
```
L4490  ⚪  (score=0)
```python
        if s.sy != "|":
```
L4491  ⚪  (score=0)
```python
            break
```
L4492  ⚪  (score=0)
```python
        s.next()
```
L4493  ⚪  (score=0)
```python
```
L4494  ⚪  (score=0)
```python
    if len(patterns) > 1:
```
L4495  ⚪  (score=0)
```python
        pattern = MatchCaseNodes.OrPatternNode(
```
L4496  ⚪  (score=0)
```python
            pos,
```
L4497  ⚪  (score=0)
```python
            alternatives=patterns
```
L4498  ⚪  (score=0)
```python
        )
```
L4499  ⚪  (score=0)
```python
    else:
```
L4500  ⚪  (score=0)
```python
        pattern = patterns[0]
```
L4501  ⚪  (score=0)
```python
```
L4502  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == 'as':
```
L4503  ⚪  (score=0)
```python
        s.next()
```
L4504  ⚪  (score=0)
```python
        with tentatively_scan(s) as errors:
```
L4505  ⚪  (score=0)
```python
            pattern.as_targets.append(p_pattern_capture_target(s))
```
L4506  ⚪  (score=0)
```python
        if errors and s.sy == "_":
```
L4507  ⚪  (score=0)
```python
            s.next()
```
L4508  ⚪  (score=0)
```python
            # make this a specific error
```
L4509  ⚪  (score=0)
```python
            return Nodes.ErrorNode(errors[0].args[0], what=errors[0].args[1])
```
L4510  ⚪  (score=0)
```python
        elif errors:
```
L4511  ⚪  (score=0)
```python
            with tentatively_scan(s):
```
L4512  ⚪  (score=0)
```python
                expr = p_test(s)
```
L4513  ⚪  (score=0)
```python
                return Nodes.ErrorNode(expr.pos, what="Invalid pattern target")
```
L4514  ⚪  (score=0)
```python
            s.error(errors[0])
```
L4515  ⚪  (score=0)
```python
    return pattern
```
L4516  ⚪  (score=0)
```python
```
L4517  ⚪  (score=0)
```python
```
L4518  ⚪  (score=0)
```python
@cython.cfunc
```
L4519  ⚪  (score=0)
```python
def p_closed_pattern(s: PyrexScanner):
```
L4520  ⚪  (score=0)
```python
    """
```
L4521  ⚪  (score=0)
```python
    The PEG parser specifies it as
```
L4522  ⚪  (score=0)
```python
    | literal_pattern
```
L4523  ⚪  (score=0)
```python
    | capture_pattern
```
L4524  ⚪  (score=0)
```python
    | wildcard_pattern
```
L4525  ⚪  (score=0)
```python
    | value_pattern
```
L4526  ⚪  (score=0)
```python
    | group_pattern
```
L4527  ⚪  (score=0)
```python
    | sequence_pattern
```
L4528  ⚪  (score=0)
```python
    | mapping_pattern
```
L4529  ⚪  (score=0)
```python
    | class_pattern
```
L4530  ⚪  (score=0)
```python
```
L4531  ⚪  (score=0)
```python
    For the sake avoiding too much backtracking, we know:
```
L4532  ⚪  (score=0)
```python
    * starts with "{" is a sequence_pattern
```
L4533  ⚪  (score=0)
```python
    * starts with "[" is a mapping_pattern
```
L4534  ⚪  (score=0)
```python
    * starts with "(" is a group_pattern or sequence_pattern
```
L4535  ⚪  (score=0)
```python
    * wildcard pattern is just identifier=='_'
```
L4536  ⚪  (score=0)
```python
    The rest are then tried in order with backtracking
```
L4537  ⚪  (score=0)
```python
    """
```
L4538  ⚪  (score=0)
```python
    if s.sy == 'IDENT' and s.systring == '_':
```
L4539  ⚪  (score=0)
```python
        pos = s.position()
```
L4540  ⚪  (score=0)
```python
        s.next()
```
L4541  ⚪  (score=0)
```python
        return MatchCaseNodes.MatchAndAssignPatternNode(pos)
```
L4542  ⚪  (score=0)
```python
    elif s.sy == '{':
```
L4543  ⚪  (score=0)
```python
        return p_mapping_pattern(s)
```
L4544  ⚪  (score=0)
```python
    elif s.sy == '[':
```
L4545  ⚪  (score=0)
```python
        return p_sequence_pattern(s)
```
L4546  ⚪  (score=0)
```python
    elif s.sy == '(':
```
L4547  ⚪  (score=0)
```python
        with tentatively_scan(s) as errors:
```
L4548  ⚪  (score=0)
```python
            result = p_group_pattern(s)
```
L4549  ⚪  (score=0)
```python
            if not errors:
```
L4550  ⚪  (score=0)
```python
                return result
```
L4551  ⚪  (score=0)
```python
        return p_sequence_pattern(s)
```
L4552  ⚪  (score=0)
```python
```
L4553  ⚪  (score=0)
```python
    with tentatively_scan(s) as errors:
```
L4554  ⚪  (score=0)
```python
        result = p_literal_pattern(s)
```
L4555  ⚪  (score=0)
```python
        if not errors:
```
L4556  ⚪  (score=0)
```python
            return result
```
L4557  ⚪  (score=0)
```python
    with tentatively_scan(s) as errors:
```
L4558  ⚪  (score=0)
```python
        result = p_capture_pattern(s)
```
L4559  ⚪  (score=0)
```python
        if not errors:
```
L4560  ⚪  (score=0)
```python
            return result
```
L4561  ⚪  (score=0)
```python
    with tentatively_scan(s) as errors:
```
L4562  ⚪  (score=0)
```python
        result = p_value_pattern(s)
```
L4563  ⚪  (score=0)
```python
        if not errors:
```
L4564  ⚪  (score=0)
```python
            return result
```
L4565  ⚪  (score=0)
```python
    return p_class_pattern(s)
```
L4566  ⚪  (score=0)
```python
```
L4567  ⚪  (score=0)
```python
```
L4568  ⚪  (score=0)
```python
@cython.cfunc
```
L4569  ⚪  (score=0)
```python
def p_literal_pattern(s: PyrexScanner):
```
L4570  ⚪  (score=0)
```python
    # a lot of duplication in this function with "p_atom"
```
L4571  ⚪  (score=0)
```python
    next_must_be_a_number = False
```
L4572  ⚪  (score=0)
```python
    sign = ''
```
L4573  ⚪  (score=0)
```python
    if s.sy == '-':
```
L4574  ⚪  (score=0)
```python
        sign = s.sy
```
L4575  ⚪  (score=0)
```python
        sign_pos = s.position()
```
L4576  ⚪  (score=0)
```python
        s.next()
```
L4577  ⚪  (score=0)
```python
        next_must_be_a_number = True
```
L4578  ⚪  (score=0)
```python
```
L4579  ⚪  (score=0)
```python
    sy = s.sy
```
L4580  ⚪  (score=0)
```python
    pos = s.position()
```
L4581  ⚪  (score=0)
```python
```
L4582  ⚪  (score=0)
```python
    res = None
```
L4583  ⚪  (score=0)
```python
    if sy == 'INT':
```
L4584  ⚪  (score=0)
```python
        res = p_int_literal(s)
```
L4585  ⚪  (score=0)
```python
    elif sy == 'FLOAT':
```
L4586  ⚪  (score=0)
```python
        value = s.systring
```
L4587  ⚪  (score=0)
```python
        s.next()
```
L4588  ⚪  (score=0)
```python
        res = ExprNodes.FloatNode(pos, value=value)
```
L4589  ⚪  (score=0)
```python
```
L4590  ⚪  (score=0)
```python
    if res is not None and sign == "-":
```
L4591  ⚪  (score=0)
```python
        res = ExprNodes.UnaryMinusNode(sign_pos, operand=res)
```
L4592  ⚪  (score=0)
```python
```
L4593  ⚪  (score=0)
```python
    if res is not None and s.sy in ['+', '-']:
```
L4594  ⚪  (score=0)
```python
        sign = s.sy
```
L4595  ⚪  (score=0)
```python
        s.next()
```
L4596  ⚪  (score=0)
```python
        if s.sy != 'IMAG':
```
L4597  ⚪  (score=0)
```python
            s.error("Expected imaginary number")
```
L4598  ⚪  (score=0)
```python
        else:
```
L4599  ⚪  (score=0)
```python
            add_pos = s.position()
```
L4600  ⚪  (score=0)
```python
            imag_text = s.systring
```
L4601  ⚪  (score=0)
```python
            value = imag_text[:len(imag_text) - 1]
```
L4602  ⚪  (score=0)
```python
            s.next()
```
L4603  ⚪  (score=0)
```python
            res = ExprNodes.binop_node(
```
L4604  ⚪  (score=0)
```python
                add_pos,
```
L4605  ⚪  (score=0)
```python
                sign,
```
L4606  ⚪  (score=0)
```python
                operand1=res,
```
L4607  ⚪  (score=0)
```python
                operand2=ExprNodes.ImagNode(s.position(), value=value)
```
L4608  ⚪  (score=0)
```python
            )
```
L4609  ⚪  (score=0)
```python
```
L4610  ⚪  (score=0)
```python
    if res is None and sy == 'IMAG':
```
L4611  ⚪  (score=0)
```python
        imag_text = s.systring
```
L4612  ⚪  (score=0)
```python
        value = imag_text[:len(imag_text) - 1]
```
L4613  ⚪  (score=0)
```python
        s.next()
```
L4614  ⚪  (score=0)
```python
        res = ExprNodes.ImagNode(pos, value=sign+value)
```
L4615  ⚪  (score=0)
```python
        if sign == "-":
```
L4616  ⚪  (score=0)
```python
            res = ExprNodes.UnaryMinusNode(sign_pos, operand=res)
```
L4617  ⚪  (score=0)
```python
```
L4618  ⚪  (score=0)
```python
    if res is not None:
```
L4619  ⚪  (score=0)
```python
        return MatchCaseNodes.MatchValuePatternNode(pos, value=res)
```
L4620  ⚪  (score=0)
```python
```
L4621  ⚪  (score=0)
```python
    if next_must_be_a_number:
```
L4622  ⚪  (score=0)
```python
        s.error("Expected a number")
```
L4623  ⚪  (score=0)
```python
    if sy == 'BEGIN_STRING':
```
L4624  ⚪  (score=0)
```python
        res = p_atom_string(s)
```
L4625  ⚪  (score=0)
```python
        # Whether f-strings are suitable is validated in PostParse.
```
L4626  ⚪  (score=0)
```python
        return MatchCaseNodes.MatchValuePatternNode(pos, value=res)
```
L4627  ⚪  (score=0)
```python
    elif sy == 'IDENT':
```
L4628  ⚪  (score=0)
```python
        # Note that p_atom_ident_constants includes NULL.
```
L4629  ⚪  (score=0)
```python
        # This is a deliberate Cython addition to the pattern matching specification
```
L4630  ⚪  (score=0)
```python
        result = p_atom_ident_constants(s)
```
L4631  ⚪  (score=0)
```python
        if result:
```
L4632  ⚪  (score=0)
```python
            return MatchCaseNodes.MatchValuePatternNode(pos, value=result, is_is_check=True)
```
L4633  ⚪  (score=0)
```python
```
L4634  ⚪  (score=0)
```python
    s.error("Failed to match literal")
```
L4635  ⚪  (score=0)
```python
```
L4636  ⚪  (score=0)
```python
```
L4637  ⚪  (score=0)
```python
@cython.cfunc
```
L4638  ⚪  (score=0)
```python
def p_capture_pattern(s: PyrexScanner):
```
L4639  ⚪  (score=0)
```python
    return MatchCaseNodes.MatchAndAssignPatternNode(
```
L4640  ⚪  (score=0)
```python
        s.position(),
```
L4641  ⚪  (score=0)
```python
        target=p_pattern_capture_target(s)
```
L4642  ⚪  (score=0)
```python
    )
```
L4643  ⚪  (score=0)
```python
```
L4644  ⚪  (score=0)
```python
```
L4645  ⚪  (score=0)
```python
@cython.cfunc
```
L4646  ⚪  (score=0)
```python
def p_value_pattern(s: PyrexScanner):
```
L4647  ⚪  (score=0)
```python
    if s.sy != "IDENT":
```
L4648  ⚪  (score=0)
```python
        s.error("Expected identifier")
```
L4649  ⚪  (score=0)
```python
    pos = s.position()
```
L4650  ⚪  (score=0)
```python
    res = p_name(s, s.systring)
```
L4651  ⚪  (score=0)
```python
    s.next()
```
L4652  ⚪  (score=0)
```python
    if s.sy != '.':
```
L4653  ⚪  (score=0)
```python
        s.error(".")
```
L4654  ⚪  (score=0)
```python
    while s.sy == '.':
```
L4655  ⚪  (score=0)
```python
        attr_pos = s.position()
```
L4656  ⚪  (score=0)
```python
        s.next()
```
L4657  ⚪  (score=0)
```python
        attr = p_ident(s)
```
L4658  ⚪  (score=0)
```python
        res = ExprNodes.AttributeNode(attr_pos, obj=res, attribute=attr)
```
L4659  ⚪  (score=0)
```python
    if s.sy in ['(', '=']:
```
L4660  ⚪  (score=0)
```python
        s.error("Unexpected symbol '%s'" % s.sy)
```
L4661  ⚪  (score=0)
```python
    return MatchCaseNodes.MatchValuePatternNode(pos, value=res)
```
L4662  ⚪  (score=0)
```python
```
L4663  ⚪  (score=0)
```python
```
L4664  ⚪  (score=0)
```python
@cython.cfunc
```
L4665  ⚪  (score=0)
```python
def p_group_pattern(s: PyrexScanner):
```
L4666  ⚪  (score=0)
```python
    s.expect("(")
```
L4667  ⚪  (score=0)
```python
    pattern = p_pattern(s)
```
L4668  ⚪  (score=0)
```python
    s.expect(")")
```
L4669  ⚪  (score=0)
```python
    return pattern
```
L4670  ⚪  (score=0)
```python
```
L4671  ⚪  (score=0)
```python
```
L4672  ⚪  (score=0)
```python
@cython.cfunc
```
L4673  ⚪  (score=0)
```python
def p_sequence_pattern(s: PyrexScanner):
```
L4674  ⚪  (score=0)
```python
    opener = s.sy
```
L4675  ⚪  (score=0)
```python
    pos = s.position()
```
L4676  ⚪  (score=0)
```python
    if opener in ['[', '(']:
```
L4677  ⚪  (score=0)
```python
        closer = ']' if opener == '[' else ')'
```
L4678  ⚪  (score=0)
```python
        s.next()
```
L4679  ⚪  (score=0)
```python
        # maybe_sequence_pattern and open_sequence_pattern
```
L4680  ⚪  (score=0)
```python
        patterns = []
```
L4681  ⚪  (score=0)
```python
        while s.sy != closer:
```
L4682  ⚪  (score=0)
```python
            patterns.append(p_maybe_star_pattern(s))
```
L4683  ⚪  (score=0)
```python
            if s.sy == ",":
```
L4684  ⚪  (score=0)
```python
                s.next()
```
L4685  ⚪  (score=0)
```python
            else:
```
L4686  ⚪  (score=0)
```python
                if opener == '(' and len(patterns) == 1:
```
L4687  ⚪  (score=0)
```python
                    s.error("tuple-like pattern of length 1 must finish with ','")
```
L4688  ⚪  (score=0)
```python
                break
```
L4689  ⚪  (score=0)
```python
        s.expect(closer)
```
L4690  ⚪  (score=0)
```python
        return MatchCaseNodes.MatchSequencePatternNode(pos, patterns=patterns)
```
L4691  ⚪  (score=0)
```python
    else:
```
L4692  ⚪  (score=0)
```python
        s.error("Expected '[' or '('")
```
L4693  ⚪  (score=0)
```python
```
L4694  ⚪  (score=0)
```python
```
L4695  ⚪  (score=0)
```python
@cython.cfunc
```
L4696  ⚪  (score=0)
```python
def p_mapping_pattern(s: PyrexScanner):
```
L4697  ⚪  (score=0)
```python
    pos = s.position()
```
L4698  ⚪  (score=0)
```python
    s.expect('{')
```
L4699  ⚪  (score=0)
```python
    if s.sy == '}':
```
L4700  ⚪  (score=0)
```python
        # trivial empty mapping
```
L4701  ⚪  (score=0)
```python
        s.next()
```
L4702  ⚪  (score=0)
```python
        return MatchCaseNodes.MatchMappingPatternNode(pos)
```
L4703  ⚪  (score=0)
```python
```
L4704  ⚪  (score=0)
```python
    double_star_capture_target = None
```
L4705  ⚪  (score=0)
```python
    items_patterns = []
```
L4706  ⚪  (score=0)
```python
    star_star_arg_pos = None
```
L4707  ⚪  (score=0)
```python
    while s.sy != '}':
```
L4708  ⚪  (score=0)
```python
        if double_star_capture_target and not star_star_arg_pos:
```
L4709  ⚪  (score=0)
```python
            star_star_arg_pos = s.position()
```
L4710  ⚪  (score=0)
```python
        if s.sy == '**':
```
L4711  ⚪  (score=0)
```python
            s.next()
```
L4712  ⚪  (score=0)
```python
            double_star_capture_target = p_pattern_capture_target(s)
```
L4713  ⚪  (score=0)
```python
        else:
```
L4714  ⚪  (score=0)
```python
            # key=(literal_expr | attr)
```
L4715  ⚪  (score=0)
```python
            with tentatively_scan(s) as errors:
```
L4716  ⚪  (score=0)
```python
                pattern = p_literal_pattern(s)
```
L4717  ⚪  (score=0)
```python
                key = pattern.value
```
L4718  ⚪  (score=0)
```python
            if errors:
```
L4719  ⚪  (score=0)
```python
                pattern = p_value_pattern(s)
```
L4720  ⚪  (score=0)
```python
                key = pattern.value
```
L4721  ⚪  (score=0)
```python
            s.expect(':')
```
L4722  ⚪  (score=0)
```python
            value = p_pattern(s)
```
L4723  ⚪  (score=0)
```python
            items_patterns.append((key, value))
```
L4724  ⚪  (score=0)
```python
        if s.sy != ',':
```
L4725  ⚪  (score=0)
```python
            break
```
L4726  ⚪  (score=0)
```python
        s.next()
```
L4727  ⚪  (score=0)
```python
    s.expect('}')
```
L4728  ⚪  (score=0)
```python
```
L4729  ⚪  (score=0)
```python
    if star_star_arg_pos is not None:
```
L4730  ⚪  (score=0)
```python
        return Nodes.ErrorNode(
```
L4731  ⚪  (score=0)
```python
            star_star_arg_pos,
```
L4732  ⚪  (score=0)
```python
            what = "** pattern must be the final part of a mapping pattern."
```
L4733  ⚪  (score=0)
```python
        )
```
L4734  ⚪  (score=0)
```python
    return MatchCaseNodes.MatchMappingPatternNode(
```
L4735  ⚪  (score=0)
```python
        pos,
```
L4736  ⚪  (score=0)
```python
        keys = [kv[0] for kv in items_patterns],
```
L4737  ⚪  (score=0)
```python
        value_patterns = [kv[1] for kv in items_patterns],
```
L4738  ⚪  (score=0)
```python
        double_star_capture_target = double_star_capture_target
```
L4739  ⚪  (score=0)
```python
    )
```
L4740  ⚪  (score=0)
```python
```
L4741  ⚪  (score=0)
```python
```
L4742  ⚪  (score=0)
```python
@cython.cfunc
```
L4743  ⚪  (score=0)
```python
def p_class_pattern(s: PyrexScanner):
```
L4744  ⚪  (score=0)
```python
    # start by parsing the class as name_or_attr
```
L4745  ⚪  (score=0)
```python
    pos = s.position()
```
L4746  ⚪  (score=0)
```python
    res = p_name(s, s.systring)
```
L4747  ⚪  (score=0)
```python
    s.next()
```
L4748  ⚪  (score=0)
```python
    while s.sy == '.':
```
L4749  ⚪  (score=0)
```python
        attr_pos = s.position()
```
L4750  ⚪  (score=0)
```python
        s.next()
```
L4751  ⚪  (score=0)
```python
        attr = p_ident(s)
```
L4752  ⚪  (score=0)
```python
        res = ExprNodes.AttributeNode(attr_pos, obj=res, attribute=attr)
```
L4753  ⚪  (score=0)
```python
    class_ = res
```
L4754  ⚪  (score=0)
```python
```
L4755  ⚪  (score=0)
```python
    s.expect("(")
```
L4756  ⚪  (score=0)
```python
    if s.sy == ")":
```
L4757  ⚪  (score=0)
```python
        # trivial case with no arguments matched
```
L4758  ⚪  (score=0)
```python
        s.next()
```
L4759  ⚪  (score=0)
```python
        return MatchCaseNodes.ClassPatternNode(pos, class_=class_)
```
L4760  ⚪  (score=0)
```python
```
L4761  ⚪  (score=0)
```python
    # parse the arguments
```
L4762  ⚪  (score=0)
```python
    positional_patterns = []
```
L4763  ⚪  (score=0)
```python
    keyword_patterns = []
```
L4764  ⚪  (score=0)
```python
    keyword_patterns_error = None
```
L4765  ⚪  (score=0)
```python
    while s.sy != ')':
```
L4766  ⚪  (score=0)
```python
        with tentatively_scan(s) as errors:
```
L4767  ⚪  (score=0)
```python
            positional_patterns.append(p_pattern(s))
```
L4768  ⚪  (score=0)
```python
        if not errors:
```
L4769  ⚪  (score=0)
```python
            if keyword_patterns:
```
L4770  ⚪  (score=0)
```python
                keyword_patterns_error = s.position()
```
L4771  ⚪  (score=0)
```python
        else:
```
L4772  ⚪  (score=0)
```python
            with tentatively_scan(s) as errors:
```
L4773  ⚪  (score=0)
```python
                keyword_patterns.append(p_keyword_pattern(s))
```
L4774  ⚪  (score=0)
```python
        if s.sy != ",":
```
L4775  ⚪  (score=0)
```python
            break
```
L4776  ⚪  (score=0)
```python
        s.next()
```
L4777  ⚪  (score=0)
```python
    s.expect(")")
```
L4778  ⚪  (score=0)
```python
```
L4779  ⚪  (score=0)
```python
    if keyword_patterns_error is not None:
```
L4780  ⚪  (score=0)
```python
        return Nodes.ErrorNode(
```
L4781  ⚪  (score=0)
```python
            keyword_patterns_error,
```
L4782  ⚪  (score=0)
```python
            what="Positional patterns follow keyword patterns"
```
L4783  ⚪  (score=0)
```python
        )
```
L4784  ⚪  (score=0)
```python
    return MatchCaseNodes.ClassPatternNode(
```
L4785  ⚪  (score=0)
```python
        pos, class_ = class_,
```
L4786  ⚪  (score=0)
```python
        positional_patterns = positional_patterns,
```
L4787  ⚪  (score=0)
```python
        keyword_pattern_names = [kv[0] for kv in keyword_patterns],
```
L4788  ⚪  (score=0)
```python
        keyword_pattern_patterns = [kv[1] for kv in keyword_patterns],
```
L4789  ⚪  (score=0)
```python
    )
```
L4790  ⚪  (score=0)
```python
```
L4791  ⚪  (score=0)
```python
```
L4792  ⚪  (score=0)
```python
@cython.cfunc
```
L4793  ⚪  (score=0)
```python
def p_keyword_pattern(s: PyrexScanner):
```
L4794  ⚪  (score=0)
```python
    if s.sy != "IDENT":
```
L4795  ⚪  (score=0)
```python
        s.error("Expected identifier")
```
L4796  ⚪  (score=0)
```python
    arg = p_name(s, s.systring)
```
L4797  ⚪  (score=0)
```python
    s.next()
```
L4798  ⚪  (score=0)
```python
    s.expect("=")
```
L4799  ⚪  (score=0)
```python
    value = p_pattern(s)
```
L4800  ⚪  (score=0)
```python
    return arg, value
```
L4801  ⚪  (score=0)
```python
```
L4802  ⚪  (score=0)
```python
```
L4803  ⚪  (score=0)
```python
@cython.cfunc
```
L4804  ⚪  (score=0)
```python
def p_pattern_capture_target(s: PyrexScanner):
```
L4805  ⚪  (score=0)
```python
    # any name but '_', and with some constraints on what follows
```
L4806  ⚪  (score=0)
```python
    if s.sy != 'IDENT':
```
L4807  ⚪  (score=0)
```python
        s.error("Expected identifier")
```
L4808  ⚪  (score=0)
```python
    if s.systring == '_':
```
L4809  ⚪  (score=0)
```python
        s.error("Pattern capture target cannot be '_'")
```
L4810  ⚪  (score=0)
```python
    target = p_name(s, s.systring)
```
L4811  ⚪  (score=0)
```python
    s.next()
```
L4812  ⚪  (score=0)
```python
    if s.sy in ['.', '(', '=']:
```
L4813  ⚪  (score=0)
```python
        s.error("Illegal next symbol '%s'" % s.sy)
```
L4814  ⚪  (score=0)
```python
    return target
```
L4815  ⚪  (score=0)
```python
```
L4816  ⚪  (score=0)
```python
```
L4817  ⚪  (score=0)
```python
```
L4818  ⚪  (score=0)
```python
#----------------------------------------------
```
L4819  ⚪  (score=0)
```python
#
```
L4820  ⚪  (score=0)
```python
#   Debugging
```
L4821  ⚪  (score=0)
```python
#
```
L4822  ⚪  (score=0)
```python
#----------------------------------------------
```
L4823  ⚪  (score=0)
```python
```
L4824  ⚪  (score=0)
```python
@cython.ccall
```
L4825  ⚪  (score=0)
```python
def print_parse_tree(f, node, level: cython.long, key = None):
```
L4826  ⚪  (score=0)
```python
    ind: str = "  " * level
```
L4827  ⚪  (score=0)
```python
    f.write(ind)
```
L4828  ⚪  (score=0)
```python
    if key:
```
L4829  ⚪  (score=0)
```python
        f.write(f"{key}: ")
```
L4830  ⚪  (score=0)
```python
    if not node:
```
L4831  ⚪  (score=0)
```python
        f.write("None\n")
```
L4832  ⚪  (score=0)
```python
    elif type(node) is tuple:
```
L4833  ⚪  (score=0)
```python
        f.write(f"({node[0]} @ {node[1]}\n")
```
L4834  ⚪  (score=0)
```python
        for item in node[2:]:
```
L4835  ⚪  (score=0)
```python
            print_parse_tree(f, item, level+1)
```
L4836  ⚪  (score=0)
```python
        f.write(f"{ind})\n")
```
L4837  ⚪  (score=0)
```python
    elif isinstance(node, Nodes.Node):
```
L4838  ⚪  (score=0)
```python
        try:
```
L4839  ⚪  (score=0)
```python
            tag = node.tag
```
L4840  ⚪  (score=0)
```python
        except AttributeError:
```
L4841  ⚪  (score=0)
```python
            tag = node.__class__.__name__
```
L4842  ⚪  (score=0)
```python
        f.write(f"{tag} @ {node.pos}\n")
```
L4843  ⚪  (score=0)
```python
        for name, value in sorted(node.__dict__.items()):
```
L4844  ⚪  (score=0)
```python
            if name != 'tag' and name != 'pos':
```
L4845  ⚪  (score=0)
```python
                print_parse_tree(f, value, level+1, name)
```
L4846  ⚪  (score=0)
```python
    elif type(node) is list:
```
L4847  ⚪  (score=0)
```python
        f.write("[\n")
```
L4848  ⚪  (score=0)
```python
        for item in node:
```
L4849  ⚪  (score=0)
```python
            print_parse_tree(f, item, level+1)
```
L4850  ⚪  (score=0)
```python
        f.write(f"{ind}]\n")
```
L4851  ⚪  (score=0)
```python
    else:
```
L4852  ⚪  (score=0)
```python
        f.write(f"{ind}{node}\n")
```
