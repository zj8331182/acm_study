def get_number(str_):
    result = []
    str_ = list(str_)
    i = iter(str_)
    print(next(i))
    for s in str_:
        if "Z" == s:
            result.append(2)
            str_.remove("Z")
            str_.remove("E")
            str_.remove("R")
            str_.remove("O")
        elif "W" == s:
            result.append(4)
            str_.remove("T")
            str_.remove("W")
            str_.remove("O")
        elif "U" == s:
            result.append(6)
            str_.remove("F")
            str_.remove("O")
            str_.remove("U")
            str_.remove("R")
        elif "X" == s:
            result.append(8)
            str_.remove("S")
            str_.remove("I")
            str_.remove("X")
        elif "G" == s:
            result.append(0)
            str_.remove("E")
            str_.remove("I")
            str_.remove("G")
            str_.remove("H")
            str_.remove("T")
    print(str_)
    for s in str_:
        if 'O' == s:
            result.append(3)
            str_.remove("O")
            str_.remove("N")
            str_.remove("E")
        elif "T" == s:
            result.append(5)
            str_.remove("T")
            str_.remove("H")
            str_.remove("R")
            str_.remove("E")
            str_.remove("E")
        elif "F" == s:
            result.append(7)
            str_.remove("F")
            str_.remove("I")
            str_.remove("V")
            str_.remove("E")
        elif "S" == s:
            result.append(9)
            str_.remove("S")
            str_.remove("E")
            str_.remove("V")
            str_.remove("N")
            str_.remove("E")
    print(str_)
    c = int(len(str_) / 4)
    for i in range(c):
        result.append(1)
    print(result)
    # return "".join(result)


def main():
    n = int(input())
    inputs = []
    while n > 0:
        inputs.append(input())
        n -= 1
    for inp in inputs:
        print(get_number(inp))


def test():
    print(get_number("OHEWTIEGTHENRTEO"))


if __name__ == '__main__':
    # main()
    test()
