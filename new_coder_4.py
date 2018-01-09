def compute(stumps):
    nodes = {0: 1}
    for index in range(len(stumps)):
        if index in nodes.keys():
            for i in range(index, index + int(stumps[index]) + 1):
                if i >= len(stumps):
                    return nodes.get(index)
                if i not in nodes.keys() or nodes.get(i) > (nodes.get(index) + 1):
                    nodes[i] = (nodes.get(index) + 1)
    return -1


def test():
    print(compute(str("3 6 6 6 3 8 9 8 5 2 9 7 3 6 5 4 2 3 6 9 9 8 6 4 1 0 4 4 8 9 3 6 0 7 8 1 1 8 4").strip()
                  .split()))

    print(compute(str("2 0 1 1 1").strip()
                  .split()))


def main():
    len_ = int(input())
    print(compute(str(input()).strip().split()))


if __name__ == '__main__':
    # test()
    main()
