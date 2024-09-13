class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        #Okay, SORT positions first, thats what I thought, otherwise u can't do this

        #Because sorting doesn't mess anything up, the same collisions and relations
        #will be true 

        #Create mapping first 
        pos_map={}
        for i in range(len(positions)): 
            pos_map[positions[i]]=[healths[i], directions[i]]
        unsorted=list(positions)
        positions.sort()

        rightconverter={}
        leftconverter={}

        stack=[]
        result=[]
        for pos in positions: 
            if pos_map[pos][1]=='R': 
                stack.append([pos, pos_map[pos][0]]) 
                continue 
            lefthealth=pos_map[pos][0]
            while stack and lefthealth>stack[-1][1]: 
                stack.pop()
                lefthealth-=1 #Left is running through right, decrease left by 1 
            if stack and lefthealth==stack[-1][1]: #If got stopped by same health-pop
                stack.pop()
                continue 
            if stack: 
                stack[-1][1]-=1 #Left got stopped by right, decrease right by 1
            if not stack: 
                leftconverter[pos]=lefthealth 
        for pos, health in stack: 
            rightconverter[pos]=health 
        for pos in unsorted: 
            if pos in leftconverter: 
                result.append(leftconverter[pos])
            elif pos in rightconverter: 
                result.append(rightconverter[pos])
        return result