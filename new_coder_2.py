# number_dic = {"1": 1, "2": 8, "3": 27, "4": 64, "5": 125, "6": 216, "7": 343, "8": 512, "9": 729}
number_map = [153, 370, 371, 407]


# def compute(start, end):
#     result = []
#     for num in range(start, end):
#         num_temp = 0
#         for s in str(num):
#             num_add = number_dic.get(s)
#             if num_add is None:
#                 continue
#             elif num_add > num:
#                 num_temp = 0
#                 break
#             else:
#                 num_temp += num_add
#         if num_temp == num:
#             result.append(str(num_temp))
#     if len(result) > 0:
#         return " ".join(result)
#     else:
#         return "no"
#
#
# def test():
#     return compute(100, 999)


def main():
    line = input()
    str_line = line.split(" ")
    start = int(str_line[0])
    end = int(str_line[1])
    result = ""
    for n in number_map:
        if start <= n <= end:
            result += str(n) if result == "" else " " + str(n)
    if result != "":
        return result
    else:
        return "no"


if __name__ == '__main__':
    # print(test())
    print(main())
