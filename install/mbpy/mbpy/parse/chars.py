from enum import Enum, auto


class CharClass(Enum):
    # Structural
    ENCLOSER_OPEN = auto()  # ({[<
    ENCLOSER_CLOSE = auto()  # )}]>
    QUOTE = auto()  # "'`
    OPERATOR = auto()  # + - * / % = < > !
    SEPARATOR = auto()  # , ; :

    # Identifiers
    ALPHA_UPPER = auto()  # A-Z
    ALPHA_LOWER = auto()  # a-z
    NUMERIC = auto()  # 0-9
    UNDERSCORE = auto()  # _

    # Special
    PERIOD = auto()  # .
    HASH = auto()  # #
    BULLET = auto()  # - * •

    # Whitespace
    INDENT = auto()  # space/tab at start
    WHITESPACE = auto()  # other whitespace

    # Other
    SYMBOL = auto()  # Any other symbol
    UNKNOWN = auto()  # Unclassified


def get_char_class(_char: str) -> CharClass:
    """Classify a single character into its CharClass."""
    if not _char:
        return CharClass.UNKNOWN

    if _char in "({[<":
        return CharClass.ENCLOSER_OPEN
    if _char in ")}]>":
        return CharClass.ENCLOSER_CLOSE
    if _char in "'\"`":
        return CharClass.QUOTE
    if _char in "+-*/%=<>!":
        return CharClass.OPERATOR
    if _char in ",:;":
        return CharClass.SEPARATOR
    if _char.isupper():
        return CharClass.ALPHA_UPPER
    if _char.islower():
        return CharClass.ALPHA_LOWER
    if _char.isdigit():
        return CharClass.NUMERIC
    if _char == "_":
        return CharClass.UNDERSCORE
    if _char == ".":
        return CharClass.PERIOD
    if _char == "#":
        return CharClass.HASH
    if _char in "-*•●○◆■":
        return CharClass.BULLET
    if _char.isspace():
        return CharClass.WHITESPACE

    return CharClass.SYMBOL
