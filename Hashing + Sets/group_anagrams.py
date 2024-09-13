class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        worddict={}
        for string in strs: 
            sorted_string = ''.join(sorted(string))
            if sorted_string in worddict:
                worddict[sorted_string].append(string)
            else: 
                worddict[sorted_string]=[string]
        return list(worddict.values())

        #Main insight to solve: anagrams all have the exact same sorted string 
        #so use that to identify and group them in a dict
        #Uses the sorted string as keys and values as the actual words 
        #If the sorted current string is in the dict, append the actual word/string
        #to the value, if its not initialize a sortedstring-word entry and the 
        #value is initialized as an array. At the end, the values of the dict 
        #will contain the grouped anagrams so return it as a list. 

        #Syntax note: sorted(...) returns a list. ''.join will join it back to a str