# Cython annotation for Machines.py

Raw output: Machines.c

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
Classes for building NFAs and DFAs
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
import cython
```
L8  ⚪  (score=0)
```python
from .Transitions import TransitionMap
```
L9  ⚪  (score=0)
```python
```
L10  ⚪  (score=0)
```python
maxint = 2**31-1  # sentinel value
```
L11  ⚪  (score=0)
```python
```
L12  ⚪  (score=0)
```python
LOWEST_PRIORITY = -maxint
```
L13  ⚪  (score=0)
```python
```
L14  ⚪  (score=0)
```python
```
L15  ⚪  (score=0)
```python
class Machine:
```
L16  ⚪  (score=0)
```python
    """A collection of Nodes representing an NFA or DFA."""
```
L17  ⚪  (score=0)
```python
    def __init__(self):
```
L18  ⚪  (score=0)
```python
        self.states = []  # [Node]
```
L19  ⚪  (score=0)
```python
        self.initial_states = {}  # {(name, bol): Node}
```
L20  ⚪  (score=0)
```python
        self.next_state_number = 1
```
L21  ⚪  (score=0)
```python
```
L22  ⚪  (score=0)
```python
    def __del__(self):
```
L23  ⚪  (score=0)
```python
        for state in self.states:
```
L24  ⚪  (score=0)
```python
            state.destroy()
```
L25  ⚪  (score=0)
```python
```
L26  ⚪  (score=0)
```python
    def new_state(self):
```
L27  ⚪  (score=0)
```python
        """Add a new state to the machine and return it."""
```
L28  ⚪  (score=0)
```python
        s = Node()
```
L29  ⚪  (score=0)
```python
        n: cython.Py_ssize_t = self.next_state_number
```
L30  ⚪  (score=0)
```python
        self.next_state_number = n + 1
```
L31  ⚪  (score=0)
```python
        s.number = n
```
L32  ⚪  (score=0)
```python
        self.states.append(s)
```
L33  ⚪  (score=0)
```python
        return s
```
L34  ⚪  (score=0)
```python
```
L35  ⚪  (score=0)
```python
    def new_initial_state(self, name):
```
L36  ⚪  (score=0)
```python
        state = self.new_state()
```
L37  ⚪  (score=0)
```python
        self.make_initial_state(name, state)
```
L38  ⚪  (score=0)
```python
        return state
```
L39  ⚪  (score=0)
```python
```
L40  ⚪  (score=0)
```python
    def make_initial_state(self, name, state):
```
L41  ⚪  (score=0)
```python
        self.initial_states[name] = state
```
L42  ⚪  (score=0)
```python
```
L43  ⚪  (score=0)
```python
    def get_initial_state(self, name):
```
L44  ⚪  (score=0)
```python
        return self.initial_states[name]
```
L45  ⚪  (score=0)
```python
```
L46  ⚪  (score=0)
```python
    def dump(self, file):
```
L47  ⚪  (score=0)
```python
        file.write("Plex.Machine:\n")
```
L48  ⚪  (score=0)
```python
        if self.initial_states is not None:
```
L49  ⚪  (score=0)
```python
            file.write("   Initial states:\n")
```
L50  ⚪  (score=0)
```python
            for (name, state) in sorted(self.initial_states.items()):
```
L51  ⚪  (score=0)
```python
                file.write("      '%s': %d\n" % (name, state.number))
```
L52  ⚪  (score=0)
```python
        for s in self.states:
```
L53  ⚪  (score=0)
```python
            s.dump(file)
```
L54  ⚪  (score=0)
```python
```
L55  ⚪  (score=0)
```python
```
L56  ⚪  (score=0)
```python
class Node:
```
L57  ⚪  (score=0)
```python
    """A state of an NFA or DFA."""
```
L58  ⚪  (score=0)
```python
```
L59  ⚪  (score=0)
```python
    def __init__(self):
```
L60  ⚪  (score=0)
```python
        # Preinitialise the list of empty transitions, because
```
L61  ⚪  (score=0)
```python
        # the nfa-to-dfa algorithm needs it
```
L62  ⚪  (score=0)
```python
        self.transitions = TransitionMap()      # TransitionMap
```
L63  ⚪  (score=0)
```python
        self.action_priority = LOWEST_PRIORITY  # integer
```
L64  ⚪  (score=0)
```python
        self.action = None  # Action
```
L65  ⚪  (score=0)
```python
        self.number = 0     # for debug output
```
L66  ⚪  (score=0)
```python
        self.epsilon_closure = None  # used by nfa_to_dfa()
```
L67  ⚪  (score=0)
```python
```
L68  ⚪  (score=0)
```python
    def destroy(self):
```
L69  ⚪  (score=0)
```python
        self.transitions = None
```
L70  ⚪  (score=0)
```python
        self.action = None
```
L71  ⚪  (score=0)
```python
        self.epsilon_closure = None
```
L72  ⚪  (score=0)
```python
```
L73  ⚪  (score=0)
```python
    def add_transition(self, event, new_state):
```
L74  ⚪  (score=0)
```python
        self.transitions.add(event, new_state)
```
L75  ⚪  (score=0)
```python
```
L76  ⚪  (score=0)
```python
    def link_to(self, state):
```
L77  ⚪  (score=0)
```python
        """Add an epsilon-move from this state to another state."""
```
L78  ⚪  (score=0)
```python
        self.add_transition('', state)
```
L79  ⚪  (score=0)
```python
```
L80  ⚪  (score=0)
```python
    def set_action(self, action, priority):
```
L81  ⚪  (score=0)
```python
        """Make this an accepting state with the given action. If
```
L82  ⚪  (score=0)
```python
        there is already an action, choose the action with highest
```
L83  ⚪  (score=0)
```python
        priority."""
```
L84  ⚪  (score=0)
```python
        if priority > self.action_priority:
```
L85  ⚪  (score=0)
```python
            self.action = action
```
L86  ⚪  (score=0)
```python
            self.action_priority = priority
```
L87  ⚪  (score=0)
```python
```
L88  ⚪  (score=0)
```python
    def get_action(self):
```
L89  ⚪  (score=0)
```python
        return self.action
```
L90  ⚪  (score=0)
```python
```
L91  ⚪  (score=0)
```python
    def get_action_priority(self):
```
L92  ⚪  (score=0)
```python
        return self.action_priority
```
L93  ⚪  (score=0)
```python
```
L94  ⚪  (score=0)
```python
    def is_accepting(self):
```
L95  ⚪  (score=0)
```python
        return self.action is not None
```
L96  ⚪  (score=0)
```python
```
L97  ⚪  (score=0)
```python
    def __str__(self):
```
L98  ⚪  (score=0)
```python
        return "State %d" % self.number
```
L99  ⚪  (score=0)
```python
```
L100  ⚪  (score=0)
```python
    def dump(self, file):
```
L101  ⚪  (score=0)
```python
        # Header
```
L102  ⚪  (score=0)
```python
        file.write("   State %d:\n" % self.number)
```
L103  ⚪  (score=0)
```python
        # Transitions
```
L104  ⚪  (score=0)
```python
        #        self.dump_transitions(file)
```
L105  ⚪  (score=0)
```python
        self.transitions.dump(file)
```
L106  ⚪  (score=0)
```python
        # Action
```
L107  ⚪  (score=0)
```python
        action = self.action
```
L108  ⚪  (score=0)
```python
        priority = self.action_priority
```
L109  ⚪  (score=0)
```python
        if action is not None:
```
L110  ⚪  (score=0)
```python
            file.write("      %s [priority %d]\n" % (action, priority))
```
L111  ⚪  (score=0)
```python
```
L112  ⚪  (score=0)
```python
    def __lt__(self, other):
```
L113  ⚪  (score=0)
```python
        return self.number < other.number
```
L114  ⚪  (score=0)
```python
```
L115  ⚪  (score=0)
```python
    def __hash__(self):
```
L116  ⚪  (score=0)
```python
        # Prevent overflowing hash values due to arbitrarily large unsigned addresses.
```
L117  ⚪  (score=0)
```python
        return id(self) & maxint
```
L118  ⚪  (score=0)
```python
```
L119  ⚪  (score=0)
```python
```
L120  ⚪  (score=0)
```python
class FastMachine:
```
L121  ⚪  (score=0)
```python
    """
```
L122  ⚪  (score=0)
```python
    FastMachine is a deterministic machine represented in a way that
```
L123  ⚪  (score=0)
```python
    allows fast scanning.
```
L124  ⚪  (score=0)
```python
    """
```
L125  ⚪  (score=0)
```python
    def __init__(self):
```
L126  ⚪  (score=0)
```python
        self.initial_states = {}  # {state_name:state}
```
L127  ⚪  (score=0)
```python
        self.states = []          # [state]  where state = {event:state, 'else':state, 'action':Action}
```
L128  ⚪  (score=0)
```python
        self.next_number = 1      # for debugging
```
L129  ⚪  (score=0)
```python
        self.new_state_template = {
```
L130  ⚪  (score=0)
```python
            '': None, 'bol': None, 'eol': None, 'eof': None, 'else': None
```
L131  ⚪  (score=0)
```python
        }
```
L132  ⚪  (score=0)
```python
```
L133  ⚪  (score=0)
```python
    def __del__(self):
```
L134  ⚪  (score=0)
```python
        for state in self.states:
```
L135  ⚪  (score=0)
```python
            state.clear()
```
L136  ⚪  (score=0)
```python
```
L137  ⚪  (score=0)
```python
    def new_state(self, action=None):
```
L138  ⚪  (score=0)
```python
        number: cython.Py_ssize_t = self.next_number
```
L139  ⚪  (score=0)
```python
        self.next_number = number + 1
```
L140  ⚪  (score=0)
```python
        result = self.new_state_template.copy()
```
L141  ⚪  (score=0)
```python
        result['number'] = number
```
L142  ⚪  (score=0)
```python
        result['action'] = action
```
L143  ⚪  (score=0)
```python
        self.states.append(result)
```
L144  ⚪  (score=0)
```python
        return result
```
L145  ⚪  (score=0)
```python
```
L146  ⚪  (score=0)
```python
    def make_initial_state(self, name, state):
```
L147  ⚪  (score=0)
```python
        self.initial_states[name] = state
```
L148  ⚪  (score=0)
```python
```
L149  ⚪  (score=0)
```python
    def add_transitions(self, state: dict, event, new_state, maxint: cython.int = maxint):
```
L150  ⚪  (score=0)
```python
        code:  cython.int
```
L151  ⚪  (score=0)
```python
        code0: cython.int
```
L152  ⚪  (score=0)
```python
        code1: cython.int
```
L153  ⚪  (score=0)
```python
```
L154  ⚪  (score=0)
```python
        if type(event) is tuple:
```
L155  ⚪  (score=0)
```python
            code0, code1 = event
```
L156  ⚪  (score=0)
```python
            if code0 == -maxint:
```
L157  ⚪  (score=0)
```python
                state['else'] = new_state
```
L158  ⚪  (score=0)
```python
            elif code1 != maxint:
```
L159  ⚪  (score=0)
```python
                for code in range(code0, code1):
```
L160  ⚪  (score=0)
```python
                    state[chr(code)] = new_state
```
L161  ⚪  (score=0)
```python
        else:
```
L162  ⚪  (score=0)
```python
            state[event] = new_state
```
L163  ⚪  (score=0)
```python
```
L164  ⚪  (score=0)
```python
    def get_initial_state(self, name):
```
L165  ⚪  (score=0)
```python
        return self.initial_states[name]
```
L166  ⚪  (score=0)
```python
```
L167  ⚪  (score=0)
```python
    def dump(self, file):
```
L168  ⚪  (score=0)
```python
        file.write("Plex.FastMachine:\n")
```
L169  ⚪  (score=0)
```python
        file.write("   Initial states:\n")
```
L170  ⚪  (score=0)
```python
        for name, state in sorted(self.initial_states.items()):
```
L171  ⚪  (score=0)
```python
            file.write("      %s: %s\n" % (repr(name), state['number']))
```
L172  ⚪  (score=0)
```python
        for state in self.states:
```
L173  ⚪  (score=0)
```python
            self.dump_state(state, file)
```
L174  ⚪  (score=0)
```python
```
L175  ⚪  (score=0)
```python
    def dump_state(self, state, file):
```
L176  ⚪  (score=0)
```python
        # Header
```
L177  ⚪  (score=0)
```python
        file.write("   State %d:\n" % state['number'])
```
L178  ⚪  (score=0)
```python
        # Transitions
```
L179  ⚪  (score=0)
```python
        self.dump_transitions(state, file)
```
L180  ⚪  (score=0)
```python
        # Action
```
L181  ⚪  (score=0)
```python
        action = state['action']
```
L182  ⚪  (score=0)
```python
        if action is not None:
```
L183  ⚪  (score=0)
```python
            file.write("      %s\n" % action)
```
L184  ⚪  (score=0)
```python
```
L185  ⚪  (score=0)
```python
    def dump_transitions(self, state, file):
```
L186  ⚪  (score=0)
```python
        chars_leading_to_state = {}
```
L187  ⚪  (score=0)
```python
        special_to_state = {}
```
L188  ⚪  (score=0)
```python
        for (c, s) in state.items():
```
L189  ⚪  (score=0)
```python
            if len(c) == 1:
```
L190  ⚪  (score=0)
```python
                chars = chars_leading_to_state.get(id(s))
```
L191  ⚪  (score=0)
```python
                if chars is None:
```
L192  ⚪  (score=0)
```python
                    chars = []
```
L193  ⚪  (score=0)
```python
                    chars_leading_to_state[id(s)] = chars
```
L194  ⚪  (score=0)
```python
                chars.append(c)
```
L195  ⚪  (score=0)
```python
            elif len(c) <= 4:
```
L196  ⚪  (score=0)
```python
                special_to_state[c] = s
```
L197  ⚪  (score=0)
```python
        ranges_to_state = {}
```
L198  ⚪  (score=0)
```python
        for state in self.states:
```
L199  ⚪  (score=0)
```python
            char_list = chars_leading_to_state.get(id(state))
```
L200  ⚪  (score=0)
```python
            if char_list:
```
L201  ⚪  (score=0)
```python
                ranges = self.chars_to_ranges(char_list)
```
L202  ⚪  (score=0)
```python
                ranges_to_state[ranges] = state
```
L203  ⚪  (score=0)
```python
        for ranges in sorted(ranges_to_state):
```
L204  ⚪  (score=0)
```python
            key = self.ranges_to_string(ranges)
```
L205  ⚪  (score=0)
```python
            state = ranges_to_state[ranges]
```
L206  ⚪  (score=0)
```python
            file.write("      %s --> State %d\n" % (key, state['number']))
```
L207  ⚪  (score=0)
```python
        for key in ('bol', 'eol', 'eof', 'else'):
```
L208  ⚪  (score=0)
```python
            state = special_to_state.get(key)
```
L209  ⚪  (score=0)
```python
            if state:
```
L210  ⚪  (score=0)
```python
                file.write("      %s --> State %d\n" % (key, state['number']))
```
L211  ⚪  (score=0)
```python
```
L212  ⚪  (score=0)
```python
    def chars_to_ranges(self, char_list: list) -> tuple:
```
L213  ⚪  (score=0)
```python
        char_list.sort()
```
L214  ⚪  (score=0)
```python
```
L215  ⚪  (score=0)
```python
        c1: cython.Py_UCS4
```
L216  ⚪  (score=0)
```python
        c2: cython.Py_UCS4
```
L217  ⚪  (score=0)
```python
        i: cython.Py_ssize_t = 0
```
L218  ⚪  (score=0)
```python
        n: cython.Py_ssize_t = len(char_list)
```
L219  ⚪  (score=0)
```python
        result = []
```
L220  ⚪  (score=0)
```python
        while i < n:
```
L221  ⚪  (score=0)
```python
            c1 = ord(char_list[i])
```
L222  ⚪  (score=0)
```python
            c2 = c1
```
L223  ⚪  (score=0)
```python
            i += 1
```
L224  ⚪  (score=0)
```python
            while i < n and ord(char_list[i]) == c2 + 1:
```
L225  ⚪  (score=0)
```python
                i += 1
```
L226  ⚪  (score=0)
```python
                c2 += 1
```
L227  ⚪  (score=0)
```python
            result.append((chr(c1), chr(c2)))
```
L228  ⚪  (score=0)
```python
        return tuple(result)
```
L229  ⚪  (score=0)
```python
```
L230  ⚪  (score=0)
```python
    def ranges_to_string(self, range_list) -> str:
```
L231  ⚪  (score=0)
```python
        return ','.join(map(self.range_to_string, range_list))
```
L232  ⚪  (score=0)
```python
```
L233  ⚪  (score=0)
```python
    def range_to_string(self, range_tuple: tuple):
```
L234  ⚪  (score=0)
```python
        (c1, c2) = range_tuple
```
L235  ⚪  (score=0)
```python
        if c1 == c2:
```
L236  ⚪  (score=0)
```python
            return repr(c1)
```
L237  ⚪  (score=0)
```python
        else:
```
L238  ⚪  (score=0)
```python
            return f"{c1!r}..{c2!r}"
```
