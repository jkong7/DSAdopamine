class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Length 3, we just require a repeat letter and then ANY letter in between 
        #those two repeats 

        #We want to handle duplicate palindromes which occur with the same 1 and 3
        #I think we can just be greedy and ONLY consider the FIRST a and the LAST a
        #and then build up everything in between that is unique chars 
        #Ex: aabca: only consider first and last a and there are 3 unique chars 
        #between them so +=3

        #input is 10^5, look for O(n)

        #Can prob do a pass to find first and last indexes of each letter (if both
        #exist), in the same passs maintain a uniqur char count, when you get to 
        #a repeat instance of a char, replace/make the dict entry of the char equal
        #to the unique count ONLY IF char has been there before do you append the 
        #unique char count, else you can init as 0 


        def unique(start_index, end_index): 
            substring = s[start_index+1:end_index]
            unique_characters = set(substring)
            return len(unique_characters)

        counts={}
        for i, char in enumerate(s): 
            if char not in counts: 
                counts[char]=(i,i)
            else: 
                counts[char]=(counts[char][0], i)
        total=0 
        for start,end in counts.values(): 
            if end-start>=2: 
                total+=unique(start,end)
        return total 
        #need to find the first and last occurence of each letter and then count 
        #the number of unique chars BETWEEN them (not inclusive) and thats the total
        #number of palindromes with 1st and 3rd letter as that letter. So first 
        #do a pass to populate a dict with start and end values then loop through
        #that dict and if end-start index is >=2 (has to be>=2 or else can't be 3
        #sized palindrome), then calculate unique chars in between which is jsut
        #the len of the set of the substring of start+1:end and increment that 
        #to total 
