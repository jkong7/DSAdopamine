class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter 
        def freq_smallest(word): 
            counter=Counter(word)
            minn='z'
            for char in word: 
                minn=min(char, minn)
            return counter[minn]

        words_freq=[]
        for w in words: 
            words_freq.append(freq_smallest(w))
        words_freq.sort()

        def bs(num): 
            def condition(targetindex): 
                return words_freq[targetindex]>num
            left,right=0, len(words_freq)-1 
            while left<right: 
                mid=left+(right-left)//2
                if condition(mid): 
                    right=mid 
                else: 
                    left=mid+1 
            return left if condition(left) else -1 

        answer=[0]*len(queries)
        for i,w in enumerate(queries): 
            num=freq_smallest(w)
            answer[i]=0 if bs(num)==-1 else len(words_freq)-bs(num)
        return answer 
