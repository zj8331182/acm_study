class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        first = 0
        second = 1
        index = 0
        while index < n:
            if index % 2 == 1:
                first += second
            else:
                second += first
            index += 1
        if n % 2 == 0:
            return second
        else:
            return first


if __name__ == '__main__':
    s = Solution()
    print(s.fibonacci(10))
