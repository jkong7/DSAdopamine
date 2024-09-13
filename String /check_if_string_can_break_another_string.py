class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #[2, 3, 4, 4, 4, 4, 11, 14, 19]
        #[4, 4, 8, 8, 13, 17, 19, 21, 22]   

        #To get the 0-25 number rep of a letter IMPORANT, its just ord(char)-ord('a')
        #ord returns the ASCII key of chars, ord('a) returns 97 so to translate it to 
        #0-25, you do -ord('a). For this problem it prob doesnt matter since all we 
        #care about is the greater than relationships between letters  

        s1nums,s2nums=[], []
        for char in s1: 
            s1nums.append(ord(char)-ord('a'))
        for char in s2: 
            s2nums.append(ord(char)-ord('a'))
        s1nums.sort()
        s2nums.sort()
        
        s1greater=all(s1nums[i]>=s2nums[i] for i in range(len(s1nums)))
        s2greater=all(s2nums[i]>=s1nums[i] for i in range(len(s1nums)))

        return s1greater or s2greater 

        # yeah we just want to know if EVERY char in one of the strings can
        #be mapped to a char greater than or equal to it in another string in a 1-1
        #mapping. So just sort the two numbers corresponding with the letters (0-25) 
        #and there if for each i, theres a >= relationship, return true,, else if even
        #one breaks, we know that less than number will never be greater than another 
        #num so it just doesnt work right there.

        