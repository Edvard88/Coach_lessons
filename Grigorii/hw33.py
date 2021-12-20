def batch(iterator, backet_size=10, drop_last=False):
    backet = []
    count_elem = len(iterator)

    for elem in iterator:
        count_elem -= 1
        # print("elem", elem)
        backet.append(elem)
        # print("backet append", backet)
        if len(backet) % backet_size == 0:
            print("yeild 1")
            print("count_elem yeild 1", count_elem)
            yield backet
            backet = []
        if count_elem < backet_size - 1:
            # print("drop_last: ")
            print("yeild 2")
            print("count_elem yeild 2", count_elem)
            yield backet


l = [1,2,3,4,5,6,7,8,9,10]
g = batch(l, 3)

for elem in g:
    print(elem)