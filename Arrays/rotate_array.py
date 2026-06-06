class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        temp = nums[n-k:]
        del nums[n-k:]
        nums[:0] = temp
        return nums
        
            
