# mode: run


def zip_index_fastpath(seq):
    total = 0
    for i, value in zip(range(len(seq)), seq):
        total += i + value
    return total


def pow_square_fastpath(int x):
    cdef int y = x
    return y ** 2


def run():
    data = [1, 3, 5, 7]
    print(zip_index_fastpath(data))
    print(pow_square_fastpath(6))


if __name__ == "__main__":
    run()