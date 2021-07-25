class Solution:
    def isomorphicString(self,s,t):
        #s and t are input data of type string
        #easiest way
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

        # second way to do this is by mapping it manually using a dictionary, and whenever the element is not yet found/ unique, we add it in the dictionary
    def isomorphicString_1(self,s,t):
        def convert_str(string):
            i = 0
            map_ , output = {}, []
            for element in string:
                if element not in map_:
                    map_[element] = i
                    i += 1
                output.append(map_[element])
            return output
        return convert_str(s) == convert_str(t)


if __name__ == '__main__':
    x = Solution()
    s = input("Please enter the first string: ")
    t = input("Please enter the seccond string: ")
    print("{}\n\nAbove is first way\nNext is second way\n\n{}".format(x.isomorphicString(s,t),x.isomorphicString_1(s,t)))



