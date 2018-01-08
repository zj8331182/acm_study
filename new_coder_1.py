def get_number(str_):
    result = []
    count_0 = str_.count("Z")
    count_2 = str_.count("W")
    count_4 = str_.count("U")
    count_6 = str_.count("X")
    count_8 = str_.count("G")
    count_1 = str_.count("O") - count_0 - count_2 - count_4
    count_7 = str_.count("S") - count_6
    result += ["0"] * count_8
    result += ["1"] * int((str_.count("N") - count_1 - count_7) / 2)
    result += ["2"] * count_0
    result += ["3"] * count_1
    result += ["4"] * count_2
    result += ["5"] * (str_.count("T") - count_2 - count_8)
    result += ["6"] * count_4
    result += ["7"] * (str_.count("F") - count_4)
    result += ["8"] * count_6
    result += ["9"] * count_7
    return "".join(result)


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
    main()
    # test()
