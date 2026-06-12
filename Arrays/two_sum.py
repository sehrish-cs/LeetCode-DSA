class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
          
#optimal 

class Solution(object):
     def twoSum(self,nums, target):
            iterated = {}
            
            for i in range(len(nums)):
                num = nums[i]
                complement = target - num

                if complement in iterated:
                    return [iterated[complement], i]

                iterated[num] = i
            
            return []

    


