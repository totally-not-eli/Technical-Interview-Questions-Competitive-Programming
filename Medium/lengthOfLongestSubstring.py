class Solution:
    def lengthOfLongestSubstring(self,string):
        # the idea here is similar to the problem with 2 sums. We can use a hashmap to check for the elements if it has already been seen or not.
        # or maybe we can just use a sliding window approach :p
        i = j = 0
        max_length = 0
        dict_ = {}
        
        while j < len(string):
            #traverse through all the string while the j pointer is not at the last element.
            #its a sliding window so j would reach the last value before i.
            if string[j] not in dict_:
                # if the element in the string is a new element
                dict_[string[j]] = j
                # add the element in the dictionary with the j pointer.
                # e.g
                # string -> "abcbca"
                # is a in dict_? no, we add it there with the index. {"a":0}
                j += 1
                # increment j
                # add a new value to the max_length : of whoever is longer, if the previous or the new length :p
                max_length = max(len(dict_),max_length)
                
            else: #if element is not a new string
                dict_.pop(string[i])
                # remove the element that has been seen, but! the preceding not the new one.
                i += 1
                # increment i since it's a new sliding window
                
        return max_length

if __name__ == "__main__":
    x = Solution()
    string = input("Please enter a string: ")
    print(x.lengthOfLongestSubstring(string))                
                