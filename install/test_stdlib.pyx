# cython: language_level=3
from libc.stdlib cimport malloc, free, atoi

def test_malloc(int size):
    """Test malloc and free from stdlib."""
    cdef char *buffer = <char *>malloc(size)
    if buffer == NULL:
        raise MemoryError("Failed to allocate memory")
    
    # Initialize memory with some data
    for i in range(size):
        buffer[i] = i % 256
    
    # Read some values
    result = [buffer[i] for i in range(min(10, size))]
    
    # Free the memory
    free(buffer)
    
    return result

def test_atoi(str s):
    """Test string to integer conversion."""
    cdef bytes bytes_string = s.encode('utf8')
    return atoi(bytes_string) 