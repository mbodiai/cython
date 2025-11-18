# Cython annotation for LineTable.py

Raw output: LineTable.c

L1  ⚪  (score=0)
```python
"""
```
L2  ⚪  (score=0)
```python
Build a line table for CodeObjects, according to PEP-626 / Python 3.11.
```
L3  ⚪  (score=0)
```python
```
L4  ⚪  (score=0)
```python
See  https://github.com/python/cpython/blob/1054a755a3016f95fcd24b3ad20e8ed9048b7939/InternalDocs/locations.md
```
L5  ⚪  (score=0)
```python
See  https://github.com/python/cpython/blob/1054a755a3016f95fcd24b3ad20e8ed9048b7939/Python/assemble.c#L192
```
L6  ⚪  (score=0)
```python
"""
```
L7  ⚪  (score=0)
```python
```
L8  ⚪  (score=0)
```python
import cython
```
L9  ⚪  (score=0)
```python
```
L10  ⚪  (score=0)
```python
```
L11  ⚪  (score=0)
```python
def build_line_table(positions: list, firstlineno: cython.int):
```
L12  ⚪  (score=0)
```python
    # positions is a list of four-tuples (start_lineno, end_lineno, start_col_offset, end_col_offset)
```
L13  ⚪  (score=0)
```python
    table_bytes = []
```
L14  ⚪  (score=0)
```python
    last_lineno: cython.int = firstlineno
```
L15  ⚪  (score=0)
```python
    for position_info in positions:
```
L16  ⚪  (score=0)
```python
        last_lineno = encode_single_position(table_bytes, position_info, last_lineno)
```
L17  ⚪  (score=0)
```python
    linetable = ''.join(table_bytes)
```
L18  ⚪  (score=0)
```python
```
L19  ⚪  (score=0)
```python
    """
```
L20  ⚪  (score=0)
```python
    # Hacky debug helper code for the line table generation.
```
L21  ⚪  (score=0)
```python
    code_obj = build_line_table.__code__.replace(co_linetable=linetable.encode('latin1'), co_firstlineno=firstlineno)
```
L22  ⚪  (score=0)
```python
    print()
```
L23  ⚪  (score=0)
```python
    print(repr(linetable))
```
L24  ⚪  (score=0)
```python
    print(positions)
```
L25  ⚪  (score=0)
```python
    print(list(code_obj.co_positions()))
```
L26  ⚪  (score=0)
```python
    """
```
L27  ⚪  (score=0)
```python
```
L28  ⚪  (score=0)
```python
    return linetable
```
L29  ⚪  (score=0)
```python
```
L30  ⚪  (score=0)
```python
```
L31  ⚪  (score=0)
```python
@cython.cfunc
```
L32  ⚪  (score=0)
```python
def encode_single_position(table_bytes: list, position_info: tuple, last_lineno: cython.int) -> cython.int:
```
L33  ⚪  (score=0)
```python
    start_lineno: cython.int
```
L34  ⚪  (score=0)
```python
    end_lineno: cython.int
```
L35  ⚪  (score=0)
```python
    start_column: cython.int
```
L36  ⚪  (score=0)
```python
    end_column: cython.int
```
L37  ⚪  (score=0)
```python
```
L38  ⚪  (score=0)
```python
    start_lineno, end_lineno, start_column, end_column = position_info
```
L39  ⚪  (score=0)
```python
    assert start_lineno >= last_lineno, f"{start_lineno} >= {last_lineno}"  # positions should be sorted
```
L40  ⚪  (score=0)
```python
```
L41  ⚪  (score=0)
```python
    last_lineno_delta: cython.int = start_lineno - last_lineno
```
L42  ⚪  (score=0)
```python
```
L43  ⚪  (score=0)
```python
    if end_lineno == start_lineno:
```
L44  ⚪  (score=0)
```python
        # All in one line, can try short forms.
```
L45  ⚪  (score=0)
```python
        if last_lineno_delta == 0 and start_column < 80 and 0 <= (end_column - start_column) < 16:
```
L46  ⚪  (score=0)
```python
            # Short format (code 0-9): still on same line, small column offset
```
L47  ⚪  (score=0)
```python
            encode_location_short(table_bytes, start_column, end_column)
```
L48  ⚪  (score=0)
```python
            return end_lineno
```
L49  ⚪  (score=0)
```python
        elif 0 <= last_lineno_delta < 3 and start_column < 128 and end_column < 128:
```
L50  ⚪  (score=0)
```python
            # One line format (code 10-12): small line offsets / larger column offsets
```
L51  ⚪  (score=0)
```python
            encode_location_oneline(table_bytes, last_lineno_delta, start_column, end_column)
```
L52  ⚪  (score=0)
```python
            return end_lineno
```
L53  ⚪  (score=0)
```python
```
L54  ⚪  (score=0)
```python
    # Store in long format (code 14)
```
L55  ⚪  (score=0)
```python
    encode_location_start(table_bytes, 14)
```
L56  ⚪  (score=0)
```python
    # Since we sort positions, negative line deltas should never occur ==> inline encode_varint_signed()
```
L57  ⚪  (score=0)
```python
    encode_varint(table_bytes, last_lineno_delta << 1)
```
L58  ⚪  (score=0)
```python
    encode_varint(table_bytes, end_lineno - start_lineno)
```
L59  ⚪  (score=0)
```python
    encode_varint(table_bytes, start_column + 1)
```
L60  ⚪  (score=0)
```python
    encode_varint(table_bytes, end_column + 1)
```
L61  ⚪  (score=0)
```python
    return end_lineno
```
L62  ⚪  (score=0)
```python
```
L63  ⚪  (score=0)
```python
```
L64  ⚪  (score=0)
```python
@cython.exceptval(-1, check=False)
```
L65  ⚪  (score=0)
```python
@cython.cfunc
```
L66  ⚪  (score=0)
```python
def encode_location_start(table_bytes: list, code: cython.int) -> cython.int:
```
L67  ⚪  (score=0)
```python
    # "Instruction" size is always 1
```
L68  ⚪  (score=0)
```python
    # 128 | (code << 3) | (length - 1)
```
L69  ⚪  (score=0)
```python
    table_bytes.append(chr(128 | (code << 3)))
```
L70  ⚪  (score=0)
```python
    return 0
```
L71  ⚪  (score=0)
```python
```
L72  ⚪  (score=0)
```python
```
L73  ⚪  (score=0)
```python
@cython.exceptval(-1, check=False)
```
L74  ⚪  (score=0)
```python
@cython.cfunc
```
L75  ⚪  (score=0)
```python
def encode_location_short(table_bytes: list, start_column: cython.int, end_column: cython.int) -> cython.int:
```
L76  ⚪  (score=0)
```python
    low_bits: cython.int = start_column & 7
```
L77  ⚪  (score=0)
```python
    code: cython.int = start_column >> 3
```
L78  ⚪  (score=0)
```python
    # inlined encode_location_start()
```
L79  ⚪  (score=0)
```python
    table_bytes.append(f"{128 | (code << 3):c}{(low_bits << 4) | (end_column - start_column):c}")
```
L80  ⚪  (score=0)
```python
    return 0
```
L81  ⚪  (score=0)
```python
```
L82  ⚪  (score=0)
```python
```
L83  ⚪  (score=0)
```python
@cython.exceptval(-1, check=False)
```
L84  ⚪  (score=0)
```python
@cython.cfunc
```
L85  ⚪  (score=0)
```python
def encode_location_oneline(table_bytes: list, line_delta: cython.int, start_column: cython.int, end_column: cython.int) -> cython.int:
```
L86  ⚪  (score=0)
```python
    code: cython.int = 10 + line_delta
```
L87  ⚪  (score=0)
```python
    # inlined encode_location_start()
```
L88  ⚪  (score=0)
```python
    table_bytes.append(f"{128 | (code << 3):c}{start_column:c}{end_column:c}")
```
L89  ⚪  (score=0)
```python
    return 0
```
L90  ⚪  (score=0)
```python
```
L91  ⚪  (score=0)
```python
```
L92  ⚪  (score=0)
```python
"""
```
L93  ⚪  (score=0)
```python
# Since we sort positions, negative line deltas should not occur.
```
L94  ⚪  (score=0)
```python
@cython.cfunc
```
L95  ⚪  (score=0)
```python
def encode_varint_signed(table_bytes: list, value: cython.int) -> cython.int:
```
L96  ⚪  (score=0)
```python
    # (unsigned int)(-val) has undefined behavior for INT_MIN
```
L97  ⚪  (score=0)
```python
    uval: cython.uint = cython.cast(cython.uint, value) if cython.compiled else value
```
L98  ⚪  (score=0)
```python
    if value < 0:
```
L99  ⚪  (score=0)
```python
        uval = ((0 - uval) << 1) | 1
```
L100  ⚪  (score=0)
```python
    else:
```
L101  ⚪  (score=0)
```python
        uval = uval << 1
```
L102  ⚪  (score=0)
```python
    encode_varint(table_bytes, uval)
```
L103  ⚪  (score=0)
```python
"""
```
L104  ⚪  (score=0)
```python
```
L105  ⚪  (score=0)
```python
```
L106  ⚪  (score=0)
```python
@cython.exceptval(-1, check=False)
```
L107  ⚪  (score=0)
```python
@cython.cfunc
```
L108  ⚪  (score=0)
```python
def encode_varint(table_bytes: list, value: cython.uint) -> cython.int:
```
L109  ⚪  (score=0)
```python
    assert value > 0 or value == 0
```
L110  ⚪  (score=0)
```python
    while value >= 64:
```
L111  ⚪  (score=0)
```python
        table_bytes.append(chr(64 | (value & 63)))
```
L112  ⚪  (score=0)
```python
        value >>= 6
```
L113  ⚪  (score=0)
```python
    table_bytes.append(chr(value))
```
L114  ⚪  (score=0)
```python
    return 0
```
