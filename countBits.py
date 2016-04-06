class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l=[0]
        n=1
        while n<=num:
            for i in xrange(n):
                if len(l)<=num:
                    l.append(l[i]+1)
                else:
                    break
            n*=2
        return l