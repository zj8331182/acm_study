def compute(number, len_):
    result = 0
    while len_:
        result += number
        number **= 0.5
        len_ -= 1
    return "%0.2f" % result


def test():
    print(compute(2, 2))


def main():
    line = input().strip().split()
    print(compute(float(line[0]), int(line[1])))


if __name__ == '__main__':
    # test()
    main()
