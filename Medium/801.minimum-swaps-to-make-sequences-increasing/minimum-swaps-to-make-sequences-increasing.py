class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        keep = [len(A)]*len(A)
        swap = [len(A)]*len(A)

        keep[0] = 0
        swap[0] = 1

        for i in range(1,len(A)):

            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1

            if A[i] > B[i-1] and B[i] > A[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1]+1)

        return min(keep[-1],swap[-1])
