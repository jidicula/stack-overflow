def slicer(l: list, n: int):
    output = l[n:]
    return output


def del_items(l: list, n: int):
    output = l
    del output[:n]
    return output


list_length = 1000
slice_size = 50


if __name__ == "__main__":
    from timeit import timeit

    print(
        timeit(
            "slicer(list(range(list_length)), slice_size)",
            setup="from __main__ import list_length, slice_size, slicer",
        )
    )
    print(
        timeit(
            "del_items(list(range(list_length)), slice_size)",
            setup="from __main__ import list_length, slice_size, del_items",
        )
    )
