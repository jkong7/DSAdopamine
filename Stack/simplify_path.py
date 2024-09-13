class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        #/ divides into paths, this removes empty strings which effectively treats
        #multiple / as just one since the split component between two // is just
        #an empty string 
        components = [component for component in path.split('/') if component]
        #We probably want whats LEFT in the stack after going through everything 
        stack=[]
        # .. = POP THE STACK AND MOVE ON 
        # . =literally just move on 
        #the stack at the end is the return after ''.join 

        for part in components: 
            if part not in ['.', '..']: 
                stack.append(part)
                continue
            if part=='..' and stack: 
                stack.pop()
            elif part=='.' or not stack: 
                continue 
        joined='/'.join(stack)
        return '/'+joined
        #Got it, pretty straighforward stack problem 

#.join notes, IMPORTANT: 

#separator.join(iterable), concatenates elements of an iterable into a single string 
## Example with no separator
array = ['home', 'user', 'usr', 'local', 'bin']
result = ''.join(array)
print(result)  # Output: "homeuserusrlocalbin"

# Example with '/' as a separator
result = '/'.join(array)
print(result)  # Output: "home/user/usr/local/bin"


#.split is the OPPOSITE of .join 
#string.split(separator), splits a string into a list of substrings based on the 
#specified seperator 

# Example with '/' as a separator
path = "home/user/usr/local/bin"
components = path.split('/')
print(components)  # Output: ['home', 'user', 'usr', 'local', 'bin']

# Example with default separator (whitespace)
sentence = "this is a test"
words = sentence.split()
print(words)  # Output: ['this', 'is', 'a', 'test']

#Both are O(n), where n is length of string/list 
