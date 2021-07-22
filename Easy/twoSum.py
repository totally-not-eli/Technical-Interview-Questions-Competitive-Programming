class Solution:
    def twoSum(self, nums, target):
        # create a hashmap, key = parameter inside a specific list index, value = the index itself.
        hash_ = {k:v for v,k in enumerate(nums)}
        # if we initially have [1,2,3,4,5]
        # the hash/dictionary will become = {1:0, 2:1, 3:2, 4:3, 5:4}
        
        #next step is to iterate through every element at the given list.
        for i in range(len(nums)):
            value_needed = target - nums[i]
            #the idea here is to get the value needed if we have a certain value. 
            #E.g if we have 1 as element and the target if 9, val = target- elem = 8.
            #we will be using this to check in the dictionary if we have the value 8.
            #however, there only exists 1 solution and the value for the respective index must not be repeated, to avoid this failure, we obey the following conditons.
            
            if value_needed in hash_ and i != hash_[value_needed]:
                return [i,hash_[value_needed]]
                #return the indices
                #no need to return an empty if no elements found since it was stated that there exist 1 value!
                #this method is ideal since the list is not sorted.
                #if it was sorted id probably went with binary search lmao.
                
        return "No elements were found, can you buckle up?"
        #for the sake of argument let's do this :p
#try it out!
if __name__ == "__main__":
    x = Solution()
    nums = list(map(int,input("Enter the numbers: ").strip().split()))
    target = int(input("Enter the target: "))
    print(x.twoSum(nums,target))
    

            
    