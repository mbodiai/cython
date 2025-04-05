"""
Inject Cython type declarations into a .py file using parso static analysis.
"""
from __future__ import absolute_import
import sys
from io import open
from collections import defaultdict
from typing import cast
import parso
from parso.python import tree

from Cython.Utils import open_source_file

CYTHON_TYPE_MAP = {
    'int': 'long',
    'float': 'double',
    'str': 'str',
    'bool': 'bint',
    'bytes': 'bytes',
    'list': 'list',
    'dict': 'dict',
    'set': 'set',
    'tuple': 'tuple',
    'Any': 'object',
    'Optional': 'object',
    'Union': 'object',
    'None': 'void',
    'complex': 'double complex',
}

# Add debug flag
VERBOSE = False

def get_type_annotation(node: tree.Node):
    """Extract type annotation from a node."""
    if not hasattr(node, 'annotation') or not node.annotation:
        return None
    
    annotation = node.annotation.get_code().strip()
    if VERBOSE:
        print(f"Processing annotation: {annotation}")
        
    # Handle tuple types like Tuple[int, str]
    if annotation.startswith('Tuple['):
        return 'tuple' # For now treat as simple tuple
        
    # Handle Optional[Type] -> Type
    if annotation.startswith('Optional['):
        inner_type = annotation[9:-1]
        return CYTHON_TYPE_MAP.get(inner_type, 'object')
        
    # Handle Union[Type1, Type2] -> object
    if annotation.startswith('Union['):
        return 'object'
        
    # Handle List[Type] -> list
    if annotation.startswith('List['):
        return 'list'
        
    # Handle Dict[K, V] -> dict
    if annotation.startswith('Dict['):
        return 'dict'
        
    result = CYTHON_TYPE_MAP.get(annotation, 'object')
    if VERBOSE:
        print(f"Mapped {annotation} to {result}")
    return result

def traverse_node(node: tree.Node):
    """Helper to recursively traverse a parso node tree."""
    yield node
    if hasattr(node, 'children'):
        for child in node.children:
            yield from traverse_node(child)

def _parse_annotation(node: tree.Node):
    """Extract type annotation from a node's string representation."""
    code = node.get_code().strip()
    if ':' in code:
        _, annotation = code.split(':')
        annotation = annotation.strip()
        # Handle arrow for return types
        if '->' in annotation:
            annotation = annotation.split('->')[1].strip()
        return CYTHON_TYPE_MAP.get(annotation.strip(), 'object')
    return None

def analyse(source_path: str, code=None) -> dict[str, dict[str, set[str]]]:
    """Analyse a Python source file using parso to find type annotations."""
    if not source_path and code is None:
        raise ValueError("Either 'source_path' or 'code' is required.")
    
    scoped_names = defaultdict(lambda: defaultdict(set))
    if code is None:
        with open(source_path, encoding='utf-8') as f:
            code = f.read()
            
    try:
        grammar = parso.load_grammar()
        module: tree.Module = grammar.parse(code)
        
        def extract_function_types(node: tree.BaseNode):
            if node.type != 'funcdef':
                return
            
            scope_key = ('function', node.start_pos)
            
            # Get parameter types by checking children
            params: list[tree.Param] = [c for c in node.children if getattr(c, 'type', None) == 'parameters']
            if params:
                for param in params[0].children:
                    if hasattr(param, 'annotation'):
                        param_name = param.name.value
                        type_hint = get_type_annotation(param)
                        if type_hint:
                            scoped_names[scope_key][param_name].add(type_hint)
            
            # Get return type 
            for child in node.children:
                if hasattr(child, 'type') and child.type == 'operator' and child.value == '->':
                    next_child = node.children[node.children.index(child) + 1]
                    return_type = get_type_annotation(next_child)
                    if return_type:
                        scoped_names[scope_key]['return'].add(return_type)

        # Walk through all nodes using traverse_node instead of walk()
        for node in traverse_node(module):
            if getattr(node, 'type', None) == 'funcdef':
                extract_function_types(node)
            elif getattr(node, 'type', None) == 'annassign':
                target = node.children[0].get_code()
                type_hint = get_type_annotation(node)
                if type_hint:
                    scoped_names[('global', node.start_pos)][target].add(type_hint)

    except Exception as e:
        print(f"Error parsing file: {e}")
        import traceback
        traceback.print_exc()
        return {}

    return dict(scoped_names)

def inject_types(source_path, types) -> list[str]:
    """Inject Cython type declarations into source."""
    lines = ['import cython\n']
    
    with open_source_file(source_path) as f:
        for line_no, line in enumerate(f, 1):
            for (scope_name, pos), type_info in types.items():
                if pos[0] == line_no:
                    if scope_name == 'function':
                        type_decls = [
                            f"{name}='{typ}'"
                            for name, typs in type_info.items()
                            for typ in typs if name != 'return'
                        ]
                        if type_decls:
                            lines.append(f"{' ' * pos[1]}@cython.locals({', '.join(type_decls)})\n")
                            
                        if 'return' in type_info:
                            ret_type = next(iter(type_info['return']))
                            lines.append(f"{' ' * pos[1]}@cython.returns({ret_type})\n")
                    else:
                        type_decls = [
                            f"{name}='{next(iter(typs))}'"
                            for name, typs in type_info.items()
                        ]
                        if type_decls:
                            lines.append(f"{' ' * pos[1]}cython.declare({', '.join(type_decls)})\n")
            lines.append(line)
    return lines

def main(file_paths=None, overwrite=False, verbose=False):
    """Process .py files and inject type declarations."""
    global VERBOSE
    VERBOSE = verbose
    
    if file_paths is None:
        file_paths = sys.argv[1:]
        # Check for -v/--verbose flag
        if '-v' in file_paths or '--verbose' in file_paths:
            VERBOSE = True
            file_paths = [f for f in file_paths if f not in ('-v', '--verbose')]
            
    for source_path in file_paths:
        types = analyse(source_path)
        lines = inject_types(source_path, types)
        target_path = source_path + ('' if overwrite else '_typed.py')
        with open(target_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line)

if __name__ == '__main__':
    main()
