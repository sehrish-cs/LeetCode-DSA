class Solution(object):
        def moveZeroes(self, nums):
            countZeroes = 0
            
            i =0
            while i <len(nums):
                if(nums[i]==0):
                    nums.pop(i)
                    countZeroes+=1
                else:
                    i +=1 
            for j in range(countZeroes):
                nums.append(0)
            
            return nums
#----------------------------------------------------------
class OptimalSolution(object):
     def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < len(nums):
            nums[j] = 0       
            j += 1
        return nums
          