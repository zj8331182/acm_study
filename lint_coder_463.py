class Solution:
    """
    @param: A: an integer array
    @return:
    """

    def sortIntegers(self, A):
        for i in range(0, len(A)):
            for j in range(i, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        return A


if __name__ == '__main__':
    arr_ = [5, 4, 2, 1, 6]
    s = Solution()
    print(s.sortIntegers(arr_))
