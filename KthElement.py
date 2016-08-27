class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        kth=[nums[0]]
        m=1
        if k>n:
            k=n
        if n>=k*2:

            for i in nums[1:]:
                if i>kth[0]:
                    j=1
                    while j<m:
                        if i<kth[j]:
                            break
                        j+=1
                    # print j,i
                    kth.insert(j,i)
                    # print kth
                    m+=1
                    if m>k:
                        kth.pop(0)
                        m-=1
                elif m<k:
                    kth.insert(0,i)
                    m+=1

            # print kth
            return kth[0]
        else:
            k=n-k+1
            print k
            for i in nums[1:]:
                # print kth
                if i<kth[0]:
                    j=1
                    while j<m:
                        # print i,kth[j]
                        if i>kth[j]:

                            break
                        j+=1
                    # print j,i
                    kth.insert(j,i)
                    m+=1
                    if m>k:
                        m-=1
                        kth.pop(0)
                elif m<k:
                    kth.insert(0,i)
                    m+=1
                    # print kth
            # print kth
            return kth[0]