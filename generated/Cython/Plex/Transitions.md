# Cython annotation for Transitions.py

Raw output: Transitions.c

L1  ⚪  (score=0)
```python
"""
```
L2  ⚪  (score=0)
```python
Plex - Transition Maps
```
L3  ⚪  (score=0)
```python
```
L4  ⚪  (score=0)
```python
This version represents state sets directly as dicts for speed.
```
L5  ⚪  (score=0)
```python
"""
```
L6  ⚪  (score=0)
```python
import cython
```
L7  ⚪  (score=0)
```python
```
L8  ⚪  (score=0)
```python
maxint = 2**31-1  # sentinel value
```
L9  ⚪  (score=0)
```python
```
L10  ⚪  (score=0)
```python
```
L11  ⚪  (score=0)
```python
class TransitionMap:
```
L12  ⚪  (score=0)
```python
    """
```
L13  ⚪  (score=0)
```python
    A TransitionMap maps an input event to a set of states.
```
L14  ⚪  (score=0)
```python
    An input event is one of: a range of character codes,
```
L15  ⚪  (score=0)
```python
    the empty string (representing an epsilon move), or one
```
L16  ⚪  (score=0)
```python
    of the special symbols BOL, EOL, EOF.
```
L17  ⚪  (score=0)
```python
```
L18  ⚪  (score=0)
```python
    For characters, this implementation compactly represents
```
L19  ⚪  (score=0)
```python
    the map by means of a list:
```
L20  ⚪  (score=0)
```python
```
L21  ⚪  (score=0)
```python
      [code_0, states_0, code_1, states_1, code_2, states_2,
```
L22  ⚪  (score=0)
```python
        ..., code_n-1, states_n-1, code_n]
```
L23  ⚪  (score=0)
```python
```
L24  ⚪  (score=0)
```python
    where |code_i| is a character code, and |states_i| is a
```
L25  ⚪  (score=0)
```python
    set of states corresponding to characters with codes |c|
```
L26  ⚪  (score=0)
```python
    in the range |code_i| <= |c| <= |code_i+1|.
```
L27  ⚪  (score=0)
```python
```
L28  ⚪  (score=0)
```python
    The following invariants hold:
```
L29  ⚪  (score=0)
```python
      n >= 1
```
L30  ⚪  (score=0)
```python
      code_0 == -maxint
```
L31  ⚪  (score=0)
```python
      code_n == maxint
```
L32  ⚪  (score=0)
```python
      code_i < code_i+1 for i in 0..n-1
```
L33  ⚪  (score=0)
```python
      states_0 == states_n-1
```
L34  ⚪  (score=0)
```python
```
L35  ⚪  (score=0)
```python
    Mappings for the special events '', BOL, EOL, EOF are
```
L36  ⚪  (score=0)
```python
    kept separately in a dictionary.
```
L37  ⚪  (score=0)
```python
    """
```
L38  ⚪  (score=0)
```python
```
L39  ⚪  (score=0)
```python
    def __init__(self, map=None, special=None):
```
L40  ⚪  (score=0)
```python
        if not map:
```
L41  ⚪  (score=0)
```python
            map = [-maxint, set(), maxint]
```
L42  ⚪  (score=0)
```python
        if not special:
```
L43  ⚪  (score=0)
```python
            special = {}
```
L44  ⚪  (score=0)
```python
        self.map = map          # The list of codes and states
```
L45  ⚪  (score=0)
```python
        self.special = special  # Mapping for special events
```
L46  ⚪  (score=0)
```python
```
L47  ⚪  (score=0)
```python
    def add(self, event, new_state):
```
L48  ⚪  (score=0)
```python
        """
```
L49  ⚪  (score=0)
```python
        Add transition to |new_state| on |event|.
```
L50  ⚪  (score=0)
```python
        """
```
L51  ⚪  (score=0)
```python
        i: cython.Py_ssize_t
```
L52  ⚪  (score=0)
```python
        j: cython.Py_ssize_t
```
L53  ⚪  (score=0)
```python
        if type(event) is tuple:
```
L54  ⚪  (score=0)
```python
            code0, code1 = event
```
L55  ⚪  (score=0)
```python
            i = self.split(code0)
```
L56  ⚪  (score=0)
```python
            j = self.split(code1)
```
L57  ⚪  (score=0)
```python
            map = self.map
```
L58  ⚪  (score=0)
```python
            while i < j:
```
L59  ⚪  (score=0)
```python
                map[i + 1].add(new_state)
```
L60  ⚪  (score=0)
```python
                i += 2
```
L61  ⚪  (score=0)
```python
        else:
```
L62  ⚪  (score=0)
```python
            self.get_special(event).add(new_state)
```
L63  ⚪  (score=0)
```python
```
L64  ⚪  (score=0)
```python
    def add_set(self, event, new_set):
```
L65  ⚪  (score=0)
```python
        """
```
L66  ⚪  (score=0)
```python
        Add transitions to the states in |new_set| on |event|.
```
L67  ⚪  (score=0)
```python
        """
```
L68  ⚪  (score=0)
```python
        i: cython.Py_ssize_t
```
L69  ⚪  (score=0)
```python
        j: cython.Py_ssize_t
```
L70  ⚪  (score=0)
```python
        if type(event) is tuple:
```
L71  ⚪  (score=0)
```python
            code0, code1 = event
```
L72  ⚪  (score=0)
```python
            i = self.split(code0)
```
L73  ⚪  (score=0)
```python
            j = self.split(code1)
```
L74  ⚪  (score=0)
```python
            map = self.map
```
L75  ⚪  (score=0)
```python
            while i < j:
```
L76  ⚪  (score=0)
```python
                map[i + 1].update(new_set)
```
L77  ⚪  (score=0)
```python
                i += 2
```
L78  ⚪  (score=0)
```python
        else:
```
L79  ⚪  (score=0)
```python
            self.get_special(event).update(new_set)
```
L80  ⚪  (score=0)
```python
```
L81  ⚪  (score=0)
```python
    def get_epsilon(self):
```
L82  ⚪  (score=0)
```python
        """
```
L83  ⚪  (score=0)
```python
        Return the mapping for epsilon, or None.
```
L84  ⚪  (score=0)
```python
        """
```
L85  ⚪  (score=0)
```python
        return self.special.get('')
```
L86  ⚪  (score=0)
```python
```
L87  ⚪  (score=0)
```python
    def iteritems(self):
```
L88  ⚪  (score=0)
```python
        """
```
L89  ⚪  (score=0)
```python
        Return the mapping as an iterable of ((code1, code2), state_set) and
```
L90  ⚪  (score=0)
```python
        (special_event, state_set) pairs.
```
L91  ⚪  (score=0)
```python
        """
```
L92  ⚪  (score=0)
```python
        result = []
```
L93  ⚪  (score=0)
```python
        map = self.map
```
L94  ⚪  (score=0)
```python
        else_set: cython.bint = map[1]
```
L95  ⚪  (score=0)
```python
        i: cython.Py_ssize_t = 0
```
L96  ⚪  (score=0)
```python
        n: cython.Py_ssize_t = len(map) - 1
```
L97  ⚪  (score=0)
```python
        code0 = map[0]
```
L98  ⚪  (score=0)
```python
        while i < n:
```
L99  ⚪  (score=0)
```python
            state_set = map[i + 1]
```
L100  ⚪  (score=0)
```python
            code1 = map[i + 2]
```
L101  ⚪  (score=0)
```python
            if state_set or else_set:
```
L102  ⚪  (score=0)
```python
                result.append(((code0, code1), state_set))
```
L103  ⚪  (score=0)
```python
            code0 = code1
```
L104  ⚪  (score=0)
```python
            i += 2
```
L105  ⚪  (score=0)
```python
        for event, state_set in self.special.items():
```
L106  ⚪  (score=0)
```python
            if state_set:
```
L107  ⚪  (score=0)
```python
                result.append((event, state_set))
```
L108  ⚪  (score=0)
```python
        return iter(result)
```
L109  ⚪  (score=0)
```python
```
L110  ⚪  (score=0)
```python
    items = iteritems
```
L111  ⚪  (score=0)
```python
```
L112  ⚪  (score=0)
```python
    # ------------------- Private methods --------------------
```
L113  ⚪  (score=0)
```python
```
L114  ⚪  (score=0)
```python
    def split(self, code: cython.long):
```
L115  ⚪  (score=0)
```python
        """
```
L116  ⚪  (score=0)
```python
        Search the list for the position of the split point for |code|,
```
L117  ⚪  (score=0)
```python
        inserting a new split point if necessary. Returns index |i| such
```
L118  ⚪  (score=0)
```python
        that |code| == |map[i]|.
```
L119  ⚪  (score=0)
```python
        """
```
L120  ⚪  (score=0)
```python
        # We use a funky variation on binary search.
```
L121  ⚪  (score=0)
```python
        map = self.map
```
L122  ⚪  (score=0)
```python
        hi: cython.Py_ssize_t = len(map) - 1
```
L123  ⚪  (score=0)
```python
        # Special case: code == map[-1]
```
L124  ⚪  (score=0)
```python
        if code == maxint:
```
L125  ⚪  (score=0)
```python
            return hi
```
L126  ⚪  (score=0)
```python
```
L127  ⚪  (score=0)
```python
        # General case
```
L128  ⚪  (score=0)
```python
        lo: cython.Py_ssize_t = 0
```
L129  ⚪  (score=0)
```python
        mid: cython.Py_ssize_t
```
L130  ⚪  (score=0)
```python
        # loop invariant: map[lo] <= code < map[hi] and hi - lo >= 2
```
L131  ⚪  (score=0)
```python
        while hi - lo >= 4:
```
L132  ⚪  (score=0)
```python
            # Find midpoint truncated to even index
```
L133  ⚪  (score=0)
```python
            mid = ((lo + hi) // 2) & ~1
```
L134  ⚪  (score=0)
```python
            if code < map[mid]:
```
L135  ⚪  (score=0)
```python
                hi = mid
```
L136  ⚪  (score=0)
```python
            else:
```
L137  ⚪  (score=0)
```python
                lo = mid
```
L138  ⚪  (score=0)
```python
        # map[lo] <= code < map[hi] and hi - lo == 2
```
L139  ⚪  (score=0)
```python
        if map[lo] == code:
```
L140  ⚪  (score=0)
```python
            return lo
```
L141  ⚪  (score=0)
```python
        else:
```
L142  ⚪  (score=0)
```python
            map[hi:hi] = [code, map[hi - 1].copy()]
```
L143  ⚪  (score=0)
```python
            return hi
```
L144  ⚪  (score=0)
```python
```
L145  ⚪  (score=0)
```python
    def get_special(self, event) -> set:
```
L146  ⚪  (score=0)
```python
        """
```
L147  ⚪  (score=0)
```python
        Get state set for special event, adding a new entry if necessary.
```
L148  ⚪  (score=0)
```python
        """
```
L149  ⚪  (score=0)
```python
        special = self.special
```
L150  ⚪  (score=0)
```python
        state_set = special.get(event)
```
L151  ⚪  (score=0)
```python
        if state_set is None:
```
L152  ⚪  (score=0)
```python
            state_set = set()
```
L153  ⚪  (score=0)
```python
            special[event] = state_set
```
L154  ⚪  (score=0)
```python
        return state_set
```
L155  ⚪  (score=0)
```python
```
L156  ⚪  (score=0)
```python
    # --------------------- Conversion methods -----------------------
```
L157  ⚪  (score=0)
```python
```
L158  ⚪  (score=0)
```python
    def __str__(self):
```
L159  ⚪  (score=0)
```python
        map_strs = []
```
L160  ⚪  (score=0)
```python
        map = self.map
```
L161  ⚪  (score=0)
```python
        n: cython.Py_ssize_t = len(map)
```
L162  ⚪  (score=0)
```python
        i: cython.Py_ssize_t = 0
```
L163  ⚪  (score=0)
```python
        while i < n:
```
L164  ⚪  (score=0)
```python
            code = map[i]
```
L165  ⚪  (score=0)
```python
            if code == -maxint:
```
L166  ⚪  (score=0)
```python
                code_str = "-inf"
```
L167  ⚪  (score=0)
```python
            elif code == maxint:
```
L168  ⚪  (score=0)
```python
                code_str = "inf"
```
L169  ⚪  (score=0)
```python
            else:
```
L170  ⚪  (score=0)
```python
                code_str = str(code)
```
L171  ⚪  (score=0)
```python
            map_strs.append(code_str)
```
L172  ⚪  (score=0)
```python
            i += 1
```
L173  ⚪  (score=0)
```python
            if i < n:
```
L174  ⚪  (score=0)
```python
                map_strs.append(state_set_str(map[i]))
```
L175  ⚪  (score=0)
```python
            i += 1
```
L176  ⚪  (score=0)
```python
        special_strs = {}
```
L177  ⚪  (score=0)
```python
        for event, set in self.special.items():
```
L178  ⚪  (score=0)
```python
            special_strs[event] = state_set_str(set)
```
L179  ⚪  (score=0)
```python
        return "[%s]+%s" % (
```
L180  ⚪  (score=0)
```python
            ','.join(map_strs),
```
L181  ⚪  (score=0)
```python
            special_strs
```
L182  ⚪  (score=0)
```python
        )
```
L183  ⚪  (score=0)
```python
```
L184  ⚪  (score=0)
```python
    # --------------------- Debugging methods -----------------------
```
L185  ⚪  (score=0)
```python
```
L186  ⚪  (score=0)
```python
    def check(self):
```
L187  ⚪  (score=0)
```python
        """Check data structure integrity."""
```
L188  ⚪  (score=0)
```python
        if not self.map[-3] < self.map[-1]:
```
L189  ⚪  (score=0)
```python
            print(self)
```
L190  ⚪  (score=0)
```python
            assert 0
```
L191  ⚪  (score=0)
```python
```
L192  ⚪  (score=0)
```python
    def dump(self, file):
```
L193  ⚪  (score=0)
```python
        map = self.map
```
L194  ⚪  (score=0)
```python
        i: cython.Py_ssize_t = 0
```
L195  ⚪  (score=0)
```python
        n: cython.Py_ssize_t = len(map) - 1
```
L196  ⚪  (score=0)
```python
        while i < n:
```
L197  ⚪  (score=0)
```python
            self.dump_range(map[i], map[i + 2], map[i + 1], file)
```
L198  ⚪  (score=0)
```python
            i += 2
```
L199  ⚪  (score=0)
```python
        for event, set in self.special.items():
```
L200  ⚪  (score=0)
```python
            if set:
```
L201  ⚪  (score=0)
```python
                if not event:
```
L202  ⚪  (score=0)
```python
                    event = 'empty'
```
L203  ⚪  (score=0)
```python
                self.dump_trans(event, set, file)
```
L204  ⚪  (score=0)
```python
```
L205  ⚪  (score=0)
```python
    def dump_range(self, code0, code1, set, file):
```
L206  ⚪  (score=0)
```python
        if set:
```
L207  ⚪  (score=0)
```python
            if code0 == -maxint:
```
L208  ⚪  (score=0)
```python
                if code1 == maxint:
```
L209  ⚪  (score=0)
```python
                    k = "any"
```
L210  ⚪  (score=0)
```python
                else:
```
L211  ⚪  (score=0)
```python
                    k = "< %s" % self.dump_char(code1)
```
L212  ⚪  (score=0)
```python
            elif code1 == maxint:
```
L213  ⚪  (score=0)
```python
                k = "> %s" % self.dump_char(code0 - 1)
```
L214  ⚪  (score=0)
```python
            elif code0 == code1 - 1:
```
L215  ⚪  (score=0)
```python
                k = self.dump_char(code0)
```
L216  ⚪  (score=0)
```python
            else:
```
L217  ⚪  (score=0)
```python
                k = "%s..%s" % (self.dump_char(code0),
```
L218  ⚪  (score=0)
```python
                                self.dump_char(code1 - 1))
```
L219  ⚪  (score=0)
```python
            self.dump_trans(k, set, file)
```
L220  ⚪  (score=0)
```python
```
L221  ⚪  (score=0)
```python
    def dump_char(self, code):
```
L222  ⚪  (score=0)
```python
        if 0 <= code <= 255:
```
L223  ⚪  (score=0)
```python
            return repr(chr(code))
```
L224  ⚪  (score=0)
```python
        else:
```
L225  ⚪  (score=0)
```python
            return "chr(%d)" % code
```
L226  ⚪  (score=0)
```python
```
L227  ⚪  (score=0)
```python
    def dump_trans(self, key, set, file):
```
L228  ⚪  (score=0)
```python
        file.write("      %s --> %s\n" % (key, self.dump_set(set)))
```
L229  ⚪  (score=0)
```python
```
L230  ⚪  (score=0)
```python
    def dump_set(self, set):
```
L231  ⚪  (score=0)
```python
        return state_set_str(set)
```
L232  ⚪  (score=0)
```python
```
L233  ⚪  (score=0)
```python
```
L234  ⚪  (score=0)
```python
#
```
L235  ⚪  (score=0)
```python
#   State set manipulation functions
```
L236  ⚪  (score=0)
```python
#
```
L237  ⚪  (score=0)
```python
```
L238  ⚪  (score=0)
```python
def state_set_str(set):
```
L239  ⚪  (score=0)
```python
    return "[%s]" % ','.join(["S%d" % state.number for state in set])
```
