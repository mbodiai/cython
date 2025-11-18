# Cython annotation for Scanners.py

Raw output: Scanners.c

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
Scanning an input stream
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
from typing import TYPE_CHECKING, Any
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
```
L11  ⚪  (score=0)
```python
cython.declare(BOL=object, EOL=object, EOF=object, NOT_FOUND=object)  # noqa:E402
```
L12  ⚪  (score=0)
```python
```
L13  ⚪  (score=0)
```python
from . import Errors
```
L14  ⚪  (score=0)
```python
from .Regexps import BOL, EOF, EOL
```
L15  ⚪  (score=0)
```python
```
L16  ⚪  (score=0)
```python
if TYPE_CHECKING:
```
L17  ⚪  (score=0)
```python
    from .Lexicons import Lexicon
```
L18  ⚪  (score=0)
```python
    from typing import IO
```
L19  ⚪  (score=0)
```python
    from Cython.Compiler.Scanning import SourceDescriptor
```
L20  ⚪  (score=0)
```python
else:
```
L21  ⚪  (score=0)
```python
    Lexicon = object
```
L22  ⚪  (score=0)
```python
    IO = object
```
L23  ⚪  (score=0)
```python
    SourceDescriptor = object
```
L24  ⚪  (score=0)
```python
NOT_FOUND = object()
```
L25  ⚪  (score=0)
```python
```
L26  ⚪  (score=0)
```python
```
L27  ⚪  (score=0)
```python
class Scanner:
```
L28  ⚪  (score=0)
```python
    """A Scanner is used to read tokens from a stream of characters using the token set specified by a Plex.Lexicon.
```
L29  ⚪  (score=0)
```python
```
L30  ⚪  (score=0)
```python
    Constructor:
```
L31  ⚪  (score=0)
```python
```
L32  ⚪  (score=0)
```python
      Scanner(lexicon, stream, name = '')
```
L33  ⚪  (score=0)
```python
```
L34  ⚪  (score=0)
```python
        See the docstring of the __init__ method for details.
```
L35  ⚪  (score=0)
```python
```
L36  ⚪  (score=0)
```python
    Methods:
```
L37  ⚪  (score=0)
```python
      See the docstrings of the individual methods for more
```
L38  ⚪  (score=0)
```python
      information.
```
L39  ⚪  (score=0)
```python
```
L40  ⚪  (score=0)
```python
      read() --> (value, text)
```
L41  ⚪  (score=0)
```python
        Reads the next lexical token from the stream.
```
L42  ⚪  (score=0)
```python
```
L43  ⚪  (score=0)
```python
      position() --> (name, line, col)
```
L44  ⚪  (score=0)
```python
        Returns the position of the last token read using the
```
L45  ⚪  (score=0)
```python
        read() method.
```
L46  ⚪  (score=0)
```python
```
L47  ⚪  (score=0)
```python
      begin(state_name)
```
L48  ⚪  (score=0)
```python
        Causes scanner to change state.
```
L49  ⚪  (score=0)
```python
```
L50  ⚪  (score=0)
```python
      produce(value [, text])
```
L51  ⚪  (score=0)
```python
        Causes return of a token value to the caller of the
```
L52  ⚪  (score=0)
```python
        Scanner.
```
L53  ⚪  (score=0)
```python
```
L54  ⚪  (score=0)
```python
    """
```
L55  ⚪  (score=0)
```python
```
L56  ⚪  (score=0)
```python
    #  lexicon = None        # Lexicon
```
L57  ⚪  (score=0)
```python
    #  stream = None         # file-like object
```
L58  ⚪  (score=0)
```python
    #  name = ''
```
L59  ⚪  (score=0)
```python
    #  buffer = ''
```
L60  ⚪  (score=0)
```python
    #
```
L61  ⚪  (score=0)
```python
    #  These positions are used by the scanner to track its internal state:
```
L62  ⚪  (score=0)
```python
    #  buf_start_pos = 0     # position in input of start of buffer
```
L63  ⚪  (score=0)
```python
    #  next_pos = 0          # position in input of next char to read
```
L64  ⚪  (score=0)
```python
    #  cur_pos = 0           # position in input of current char
```
L65  ⚪  (score=0)
```python
    #  cur_line = 1          # line number of current char
```
L66  ⚪  (score=0)
```python
    #  cur_line_start = 0    # position in input of start of current line
```
L67  ⚪  (score=0)
```python
    #  start_pos = 0         # position in input of start of token
```
L68  ⚪  (score=0)
```python
    #  current_scanner_position_tuple = ("", 0, 0)
```
L69  ⚪  (score=0)
```python
    #        tuple of filename, line number and position in line, really mainly for error reporting
```
L70  ⚪  (score=0)
```python
    #
```
L71  ⚪  (score=0)
```python
    #  These positions are used to track what was read from the queue
```
L72  ⚪  (score=0)
```python
    #   (which may differ from the internal state when tokens are replaced onto the queue)
```
L73  ⚪  (score=0)
```python
    #  last_token_position_tuple = ("", 0, 0)  # tuple of filename, line number and position in line
```
L74  ⚪  (score=0)
```python
```
L75  ⚪  (score=0)
```python
    #  text = None           # text of last token read
```
L76  ⚪  (score=0)
```python
    #  initial_state = None  # Node
```
L77  ⚪  (score=0)
```python
    #  state_name = ''       # Name of initial state
```
L78  ⚪  (score=0)
```python
    #  queue = None          # list of tokens and positions to be returned
```
L79  ⚪  (score=0)
```python
    #  trace = 0
```
L80  ⚪  (score=0)
```python
    lexicon:"Lexicon"
```
L81  ⚪  (score=0)
```python
    stream:"IO"
```
L82  ⚪  (score=0)
```python
    name:"str|SourceDescriptor"
```
L83  ⚪  (score=0)
```python
    initial_pos:tuple[int, int, int]|None
```
L84  ⚪  (score=0)
```python
    trace:int
```
L85  ⚪  (score=0)
```python
    buffer:str
```
L86  ⚪  (score=0)
```python
    buf_start_pos:int
```
L87  ⚪  (score=0)
```python
    next_pos:int
```
L88  ⚪  (score=0)
```python
    cur_pos:int
```
L89  ⚪  (score=0)
```python
    cur_line:int
```
L90  ⚪  (score=0)
```python
    start_pos:int
```
L91  ⚪  (score=0)
```python
    current_scanner_position_tuple:tuple[str, int, int]
```
L92  ⚪  (score=0)
```python
    last_token_position_tuple:tuple[str, int, int]
```
L93  ⚪  (score=0)
```python
    text:str|None
```
L94  ⚪  (score=0)
```python
    initial_state:dict|None
```
L95  ⚪  (score=0)
```python
    state_name:str|None
```
L96  ⚪  (score=0)
```python
    queue:list[tuple[tuple[Any, str], tuple[str, int, int]]]
```
L97  ⚪  (score=0)
```python
    input_state:int
```
L98  ⚪  (score=0)
```python
    cur_char:str
```
L99  ⚪  (score=0)
```python
    cur_line_start:int
```
L100  ⚪  (score=0)
```python
    def __init__(self, lexicon:"Lexicon", stream:"IO", name:"str|SourceDescriptor"='', initial_pos:tuple[int, int, int]=None):
```
L101  ⚪  (score=0)
```python
        """Scanner constructor.
```
L102  ⚪  (score=0)
```python
```
L103  ⚪  (score=0)
```python
          |lexicon| is a Plex.Lexicon instance specifying the lexical tokens
```
L104  ⚪  (score=0)
```python
          to be recognised.
```
L105  ⚪  (score=0)
```python
```
L106  ⚪  (score=0)
```python
          |stream| can be a file object or anything which implements a
```
L107  ⚪  (score=0)
```python
          compatible read() method.
```
L108  ⚪  (score=0)
```python
```
L109  ⚪  (score=0)
```python
          |name| is optional, and may be the name of the file being
```
L110  ⚪  (score=0)
```python
          scanned or any other identifying string.
```
L111  ⚪  (score=0)
```python
        """
```
L112  ⚪  (score=0)
```python
        self.trace = 0
```
L113  ⚪  (score=0)
```python
```
L114  ⚪  (score=0)
```python
        self.buffer = ''
```
L115  ⚪  (score=0)
```python
        self.buf_start_pos = 0
```
L116  ⚪  (score=0)
```python
        self.next_pos = 0
```
L117  ⚪  (score=0)
```python
        self.cur_pos = 0
```
L118  ⚪  (score=0)
```python
        self.cur_line = 1
```
L119  ⚪  (score=0)
```python
        self.start_pos = 0
```
L120  ⚪  (score=0)
```python
        self.current_scanner_position_tuple = ("", 0, 0)
```
L121  ⚪  (score=0)
```python
        self.last_token_position_tuple = ("", 0, 0)
```
L122  ⚪  (score=0)
```python
        self.text = None
```
L123  ⚪  (score=0)
```python
        self.state_name = None
```
L124  ⚪  (score=0)
```python
```
L125  ⚪  (score=0)
```python
        self.lexicon = lexicon
```
L126  ⚪  (score=0)
```python
        self.stream = stream
```
L127  ⚪  (score=0)
```python
        self.name = name
```
L128  ⚪  (score=0)
```python
        self.queue = []
```
L129  ⚪  (score=0)
```python
        self.initial_state= None
```
L130  ⚪  (score=0)
```python
        self.begin('')
```
L131  ⚪  (score=0)
```python
        self.next_pos = 0
```
L132  ⚪  (score=0)
```python
        self.cur_pos = 0
```
L133  ⚪  (score=0)
```python
        self.cur_line_start = 0
```
L134  ⚪  (score=0)
```python
        self.cur_char = BOL
```
L135  ⚪  (score=0)
```python
        self.input_state = 1
```
L136  ⚪  (score=0)
```python
        if initial_pos is not None:
```
L137  ⚪  (score=0)
```python
            self.cur_line, self.cur_line_start = initial_pos[1], -initial_pos[2]
```
L138  ⚪  (score=0)
```python
```
L139  ⚪  (score=0)
```python
    def read(self):
```
L140  ⚪  (score=0)
```python
        """Read the next lexical token from the stream and return a
```
L141  ⚪  (score=0)
```python
        tuple (value, text), where |value| is the value associated with
```
L142  ⚪  (score=0)
```python
        the token as specified by the Lexicon, and |text| is the actual
```
L143  ⚪  (score=0)
```python
        string read from the stream. Returns (None, '') on end of file.
```
L144  ⚪  (score=0)
```python
        """  # noqa: D205
```
L145  ⚪  (score=0)
```python
        queue = self.queue
```
L146  ⚪  (score=0)
```python
        while not queue:
```
L147  ⚪  (score=0)
```python
            self.text, action = self.scan_a_token()
```
L148  ⚪  (score=0)
```python
            if action is None:
```
L149  ⚪  (score=0)
```python
                self.produce(None)
```
L150  ⚪  (score=0)
```python
                self.eof()
```
L151  ⚪  (score=0)
```python
            else:
```
L152  ⚪  (score=0)
```python
                value = action.perform(self, self.text)
```
L153  ⚪  (score=0)
```python
                if value is not None:
```
L154  ⚪  (score=0)
```python
                    self.produce(value)
```
L155  ⚪  (score=0)
```python
        result, self.last_token_position_tuple = queue[0]
```
L156  ⚪  (score=0)
```python
        del queue[0]
```
L157  ⚪  (score=0)
```python
        return result
```
L158  ⚪  (score=0)
```python
```
L159  ⚪  (score=0)
```python
    def unread(self, token, value, position):
```
L160  ⚪  (score=0)
```python
        self.queue.insert(0, ((token, value), position))
```
L161  ⚪  (score=0)
```python
```
L162  ⚪  (score=0)
```python
    def get_current_scan_pos(self):
```
L163  ⚪  (score=0)
```python
        # distinct from the position of the last token due to the queue
```
L164  ⚪  (score=0)
```python
        return self.current_scanner_position_tuple
```
L165  ⚪  (score=0)
```python
```
L166  ⚪  (score=0)
```python
    def scan_a_token(self):
```
L167  ⚪  (score=0)
```python
        """
```
L168  ⚪  (score=0)
```python
        Read the next input sequence recognised by the machine
```
L169  ⚪  (score=0)
```python
        and return (text, action). Returns ('', None) on end of
```
L170  ⚪  (score=0)
```python
        file.
```
L171  ⚪  (score=0)
```python
        """
```
L172  ⚪  (score=0)
```python
        self.start_pos = self.cur_pos
```
L173  ⚪  (score=0)
```python
        self.current_scanner_position_tuple = (
```
L174  ⚪  (score=0)
```python
            self.name, self.cur_line, self.cur_pos - self.cur_line_start
```
L175  ⚪  (score=0)
```python
        )
```
L176  ⚪  (score=0)
```python
        action = self.run_machine_inlined()
```
L177  ⚪  (score=0)
```python
        if action is not None:
```
L178  ⚪  (score=0)
```python
            if self.trace:
```
L179  ⚪  (score=0)
```python
                print("Scanner: read: Performing %s %d:%d" % (
```
L180  ⚪  (score=0)
```python
                    action, self.start_pos, self.cur_pos))
```
L181  ⚪  (score=0)
```python
            text = self.buffer[
```
L182  ⚪  (score=0)
```python
                self.start_pos - self.buf_start_pos:
```
L183  ⚪  (score=0)
```python
                self.cur_pos - self.buf_start_pos]
```
L184  ⚪  (score=0)
```python
            return (text, action)
```
L185  ⚪  (score=0)
```python
```
L186  ⚪  (score=0)
```python
        if self.cur_pos == self.start_pos and (self.cur_char is None or self.cur_char is EOF):
```
L187  ⚪  (score=0)
```python
            return ('', None)
```
L188  ⚪  (score=0)
```python
        raise Errors.UnrecognizedInput(self, self.state_name)
```
L189  ⚪  (score=0)
```python
```
L190  ⚪  (score=0)
```python
    @cython.final
```
L191  ⚪  (score=0)
```python
    def run_machine_inlined(self):
```
L192  ⚪  (score=0)
```python
        """
```
L193  ⚪  (score=0)
```python
        Inlined version of run_machine for speed.
```
L194  ⚪  (score=0)
```python
        """
```
L195  ⚪  (score=0)
```python
        state: dict = self.initial_state
```
L196  ⚪  (score=0)
```python
        cur_pos: cython.Py_ssize_t = self.cur_pos
```
L197  ⚪  (score=0)
```python
        cur_line: cython.Py_ssize_t = self.cur_line
```
L198  ⚪  (score=0)
```python
        cur_line_start: cython.Py_ssize_t = self.cur_line_start
```
L199  ⚪  (score=0)
```python
        cur_char = self.cur_char
```
L200  ⚪  (score=0)
```python
        input_state: cython.long = self.input_state
```
L201  ⚪  (score=0)
```python
        next_pos: cython.Py_ssize_t = self.next_pos
```
L202  ⚪  (score=0)
```python
        data: str
```
L203  ⚪  (score=0)
```python
        buffer: str = self.buffer
```
L204  ⚪  (score=0)
```python
        buf_start_pos: cython.Py_ssize_t = self.buf_start_pos
```
L205  ⚪  (score=0)
```python
        buf_len: cython.Py_ssize_t = len(buffer)
```
L206  ⚪  (score=0)
```python
        buf_index: cython.Py_ssize_t
```
L207  ⚪  (score=0)
```python
        discard: cython.Py_ssize_t
```
L208  ⚪  (score=0)
```python
```
L209  ⚪  (score=0)
```python
        b_action, b_cur_pos, b_cur_line, b_cur_line_start, b_cur_char, b_input_state, b_next_pos = \
```
L210  ⚪  (score=0)
```python
            None, 0, 0, 0, '', 0, 0
```
L211  ⚪  (score=0)
```python
```
L212  ⚪  (score=0)
```python
        trace: cython.bint = self.trace
```
L213  ⚪  (score=0)
```python
        while 1:
```
L214  ⚪  (score=0)
```python
            if trace:
```
L215  ⚪  (score=0)
```python
                print("State %d, %d/%d:%s -->" % (
```
L216  ⚪  (score=0)
```python
                    state['number'], input_state, cur_pos, repr(cur_char)))
```
L217  ⚪  (score=0)
```python
```
L218  ⚪  (score=0)
```python
            # Begin inlined self.save_for_backup()
```
L219  ⚪  (score=0)
```python
            action = state['action']
```
L220  ⚪  (score=0)
```python
            if action is not None:
```
L221  ⚪  (score=0)
```python
                b_action, b_cur_pos, b_cur_line, b_cur_line_start, b_cur_char, b_input_state, b_next_pos = \
```
L222  ⚪  (score=0)
```python
                    action, cur_pos, cur_line, cur_line_start, cur_char, input_state, next_pos
```
L223  ⚪  (score=0)
```python
            # End inlined self.save_for_backup()
```
L224  ⚪  (score=0)
```python
```
L225  ⚪  (score=0)
```python
            c = cur_char
```
L226  ⚪  (score=0)
```python
            new_state = state.get(c, NOT_FOUND)
```
L227  ⚪  (score=0)
```python
            if new_state is NOT_FOUND:
```
L228  ⚪  (score=0)
```python
                new_state = c and state.get('else')
```
L229  ⚪  (score=0)
```python
```
L230  ⚪  (score=0)
```python
            if new_state:
```
L231  ⚪  (score=0)
```python
                if trace:
```
L232  ⚪  (score=0)
```python
                    print("State %d" % new_state['number'])
```
L233  ⚪  (score=0)
```python
                state = new_state
```
L234  ⚪  (score=0)
```python
                # Begin inlined: self.next_char()
```
L235  ⚪  (score=0)
```python
                if input_state == 1:
```
L236  ⚪  (score=0)
```python
                    cur_pos = next_pos
```
L237  ⚪  (score=0)
```python
                    # Begin inlined: c = self.read_char()
```
L238  ⚪  (score=0)
```python
                    buf_index = next_pos - buf_start_pos
```
L239  ⚪  (score=0)
```python
                    if buf_index < buf_len:
```
L240  ⚪  (score=0)
```python
                        c = buffer[buf_index]
```
L241  ⚪  (score=0)
```python
                        next_pos += 1
```
L242  ⚪  (score=0)
```python
                    else:
```
L243  ⚪  (score=0)
```python
                        discard = self.start_pos - buf_start_pos
```
L244  ⚪  (score=0)
```python
                        data = self.stream.read(0x1000)
```
L245  ⚪  (score=0)
```python
                        buffer = self.buffer[discard:] + data
```
L246  ⚪  (score=0)
```python
                        self.buffer = buffer
```
L247  ⚪  (score=0)
```python
                        buf_start_pos += discard
```
L248  ⚪  (score=0)
```python
                        self.buf_start_pos = buf_start_pos
```
L249  ⚪  (score=0)
```python
                        buf_len = len(buffer)
```
L250  ⚪  (score=0)
```python
                        buf_index -= discard
```
L251  ⚪  (score=0)
```python
                        if data:
```
L252  ⚪  (score=0)
```python
                            c = buffer[buf_index]
```
L253  ⚪  (score=0)
```python
                            next_pos += 1
```
L254  ⚪  (score=0)
```python
                        else:
```
L255  ⚪  (score=0)
```python
                            c = ''
```
L256  ⚪  (score=0)
```python
                    # End inlined: c = self.read_char()
```
L257  ⚪  (score=0)
```python
                    if c == '\n':
```
L258  ⚪  (score=0)
```python
                        cur_char = EOL
```
L259  ⚪  (score=0)
```python
                        input_state = 2
```
L260  ⚪  (score=0)
```python
                    elif not c:
```
L261  ⚪  (score=0)
```python
                        cur_char = EOL
```
L262  ⚪  (score=0)
```python
                        input_state = 4
```
L263  ⚪  (score=0)
```python
                    else:
```
L264  ⚪  (score=0)
```python
                        cur_char = c
```
L265  ⚪  (score=0)
```python
                elif input_state == 2:  # after EoL (1) -> BoL (3)
```
L266  ⚪  (score=0)
```python
                    cur_char = '\n'
```
L267  ⚪  (score=0)
```python
                    input_state = 3
```
L268  ⚪  (score=0)
```python
                elif input_state == 3:  # start new code line
```
L269  ⚪  (score=0)
```python
                    cur_line += 1
```
L270  ⚪  (score=0)
```python
                    cur_line_start = cur_pos = next_pos
```
L271  ⚪  (score=0)
```python
                    cur_char = BOL
```
L272  ⚪  (score=0)
```python
                    input_state = 1
```
L273  ⚪  (score=0)
```python
                elif input_state == 4:  # after final line (1) -> EoF (5)
```
L274  ⚪  (score=0)
```python
                    cur_char = EOF
```
L275  ⚪  (score=0)
```python
                    input_state = 5
```
L276  ⚪  (score=0)
```python
                else:  # input_state == 5  (EoF)
```
L277  ⚪  (score=0)
```python
                    cur_char = ''
```
L278  ⚪  (score=0)
```python
                    # End inlined self.next_char()
```
L279  ⚪  (score=0)
```python
            else:  # not new_state
```
L280  ⚪  (score=0)
```python
                if trace:
```
L281  ⚪  (score=0)
```python
                    print("blocked")
```
L282  ⚪  (score=0)
```python
                # Begin inlined: action = self.back_up()
```
L283  ⚪  (score=0)
```python
                if b_action is not None:
```
L284  ⚪  (score=0)
```python
                    (action, cur_pos, cur_line, cur_line_start,
```
L285  ⚪  (score=0)
```python
                     cur_char, input_state, next_pos) = \
```
L286  ⚪  (score=0)
```python
                        (b_action, b_cur_pos, b_cur_line, b_cur_line_start,
```
L287  ⚪  (score=0)
```python
                         b_cur_char, b_input_state, b_next_pos)
```
L288  ⚪  (score=0)
```python
                else:
```
L289  ⚪  (score=0)
```python
                    action = None
```
L290  ⚪  (score=0)
```python
                break  # while 1
```
L291  ⚪  (score=0)
```python
                # End inlined: action = self.back_up()
```
L292  ⚪  (score=0)
```python
```
L293  ⚪  (score=0)
```python
        self.cur_pos = cur_pos
```
L294  ⚪  (score=0)
```python
        self.cur_line = cur_line
```
L295  ⚪  (score=0)
```python
        self.cur_line_start = cur_line_start
```
L296  ⚪  (score=0)
```python
        self.cur_char = cur_char
```
L297  ⚪  (score=0)
```python
        self.input_state = input_state
```
L298  ⚪  (score=0)
```python
        self.next_pos = next_pos
```
L299  ⚪  (score=0)
```python
        if trace:
```
L300  ⚪  (score=0)
```python
            if action is not None:
```
L301  ⚪  (score=0)
```python
                print("Doing %s" % action)
```
L302  ⚪  (score=0)
```python
        return action
```
L303  ⚪  (score=0)
```python
```
L304  ⚪  (score=0)
```python
    def position(self) -> tuple:
```
L305  ⚪  (score=0)
```python
        """
```
L306  ⚪  (score=0)
```python
        Return a tuple (name, line, col) representing the location of
```
L307  ⚪  (score=0)
```python
        the last token read using the read() method. |name| is the
```
L308  ⚪  (score=0)
```python
        name that was provided to the Scanner constructor; |line|
```
L309  ⚪  (score=0)
```python
        is the line number in the stream (1-based); |col| is the
```
L310  ⚪  (score=0)
```python
        position within the line of the first character of the token
```
L311  ⚪  (score=0)
```python
        (0-based).
```
L312  ⚪  (score=0)
```python
        """
```
L313  ⚪  (score=0)
```python
        return self.last_token_position_tuple
```
L314  ⚪  (score=0)
```python
```
L315  ⚪  (score=0)
```python
    def get_position(self):
```
L316  ⚪  (score=0)
```python
        """
```
L317  ⚪  (score=0)
```python
        Python accessible wrapper around position(), only for error reporting.
```
L318  ⚪  (score=0)
```python
        """
```
L319  ⚪  (score=0)
```python
        return self.position()
```
L320  ⚪  (score=0)
```python
```
L321  ⚪  (score=0)
```python
    def begin(self, state_name):
```
L322  ⚪  (score=0)
```python
        """Set the current state of the scanner to the named state."""
```
L323  ⚪  (score=0)
```python
        self.initial_state = (
```
L324  ⚪  (score=0)
```python
            self.lexicon.get_initial_state(state_name))
```
L325  ⚪  (score=0)
```python
        self.state_name = state_name
```
L326  ⚪  (score=0)
```python
```
L327  ⚪  (score=0)
```python
    def produce(self, value, text=None):
```
L328  ⚪  (score=0)
```python
        """
```
L329  ⚪  (score=0)
```python
        Called from an action procedure, causes |value| to be returned
```
L330  ⚪  (score=0)
```python
        as the token value from read(). If |text| is supplied, it is
```
L331  ⚪  (score=0)
```python
        returned in place of the scanned text.
```
L332  ⚪  (score=0)
```python
```
L333  ⚪  (score=0)
```python
        produce() can be called more than once during a single call to an action
```
L334  ⚪  (score=0)
```python
        procedure, in which case the tokens are queued up and returned one
```
L335  ⚪  (score=0)
```python
        at a time by subsequent calls to read(), until the queue is empty,
```
L336  ⚪  (score=0)
```python
        whereupon scanning resumes.
```
L337  ⚪  (score=0)
```python
        """
```
L338  ⚪  (score=0)
```python
        if text is None:
```
L339  ⚪  (score=0)
```python
            text = self.text
```
L340  ⚪  (score=0)
```python
        self.queue.append(((value, text), self.current_scanner_position_tuple))
```
L341  ⚪  (score=0)
```python
```
L342  ⚪  (score=0)
```python
    def eof(self):
```
L343  ⚪  (score=0)
```python
        """
```
L344  ⚪  (score=0)
```python
        Override this method if you want something to be done at
```
L345  ⚪  (score=0)
```python
        end of file.
```
L346  ⚪  (score=0)
```python
        """
```
L347  ⚪  (score=0)
```python
        pass
```
L348  ⚪  (score=0)
```python
```
L349  ⚪  (score=0)
```python
    @property
```
L350  ⚪  (score=0)
```python
    def start_line(self):
```
L351  ⚪  (score=0)
```python
        return self.last_token_position_tuple[1]
```
