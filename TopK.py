class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d=dict()
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        return sorted(d,key=d.get,reverse=True)[:k]