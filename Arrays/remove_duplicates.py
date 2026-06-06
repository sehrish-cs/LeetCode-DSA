class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)-1
        i=0
        while i<n:
            if(nums[i]== nums[i+1]):
                nums.pop(i+1)
                n= len(nums)-1
            else:
                i +=1

        m = len(nums)
        return m
