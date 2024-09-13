class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path, options): 
            if len(path)==len(nums): 
                output.append(path)
            for i in range(len(options)): 
                newpath=path+[options[i]]
                backtrack(newpath, options[:i]+options[i+1:])
        output=[]
        backtrack([], nums)
        return output
        #Did it over fast for clarity. Same templates, validation for appending 
        #path to output. immutable use of newpath, and then recursive call to 
        #backtrack with 1. newpath and 2. reduced options space (in this case
        #everything in options EXCEPT for index i)


        def backtrack(path, options): 
            if len(path)==len(nums): 
                output.append(path[:])
            for i in range(len(options)): 
                path.append(options[i]) #Path with +1 number
                backtrack(path, options[:i]+options[i+1:]) #Go deeper with that +1 path and new options
                path.pop() #Once that recursion returns^, pop to backtrack 
        output=[]
        backtrack([], nums)
        return output 
        #O(n*n!) n! permutations and n time to copy/listify tuple path to output


# Two Return Scenarios:
# Explicit Return: When len(path) == len(nums), we have a complete permutation.
# The current path is added to the output, and the function returns explicitly.
# Implicit Return: When the for loop completes, it implicitly returns, causing the function to backtrack.

# Backtracking Mechanism:
# After Recursive Call: Since path.pop() comes after the recursive call to backtrack,
# it ensures that once a recursive exploration completes (either by reaching a full permutation or finishing the for loop),
# the last added element is removed.
# Floating Back Up: Both return scenarios (explicit and implicit) cause the function to float back up to the previous call
# in the recursion stack, where path.pop() will execute.

# Filtering with options[:i] + options[i+1:]:
# This operation generates a new list of options excluding the current element.
# It ensures that each permutation is built with the remaining numbers, filtering out the current element to avoid repetition.

#Validation: Current path forms a valid solution? len path==len nums
#Exploration: For loop through available candidates, recursively explore further 
#by making a recursive call with the updated path and reduced set of options 
#Backtracking: Undo the last choice by popping last added candidate from path 

#NOTe: The reason we use pop is bc path is mutable (array). We can also do similar
#to path sum 2 for BT where we use path as an immutable (tuple), then the backtrackin
#is inherently taken care of and we don't have to do any pops: 

