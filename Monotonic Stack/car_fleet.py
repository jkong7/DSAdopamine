class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        #Yeah well first try with reg stack and equation solving didn't work


        #Something interesting, if you line the cars up in sorted position order 
        #and calculate the amount of time it takes for the cars to reach the finish 
        #two cars will become a fleet if the time it takes is less than a next cars
        #time it takes. For example: 
        #3 7 (time it takes to reach finish), this means the 3 car will have to 
        #intersect the 7 car. If it was greater like 8 7, it wont intersect, 
        #Also if they are equal, they will intersect at the target!!

        #So as long as a car has a car ahead of it with a greater time it takes to
        #get to the end, they will become a fleet. So this turns into a find 
        #next greater element problem using mono decreasing stack. 
        #If at the end a number DOESNT have a next greater or = element, that 
        #represents one fleet so just return the count of -1s at the end of the res
        #array!!!

        #Even better, just return len of stack at the end right because that 
        #rep number of elements with no next greater element so res array not even
        #needed?

        #The speed of a fleet becomes the min speed of any car in the fleet 
        #so I think this plays perfectly into the next greater property. 
        #For example 25 49 96 51 are the speeds, 25 49 become one, and 49 and 96 
        #become one and that right there counts as one fleet, if it was 
        #25 100 96, 25 and 100 become a fleet with time speed 100 and 100 
        #is less than 96 so it won't ever catch up (two seperate fleets)
        #25 49 96 51 will be two seperate fleets which is rep correctly by 
        #[49, 96, -1, -1] 

        #Yeah res array not even needed, straight stack usage the whole way! 

        #Summary, convert into an array sorted by positions with time it takes 
        #to get to the end. A next greater/= time represents an intersection/fleet
        #formation, the len of the stack at the end of the mono dec stack algo
        #rep # of cars with no next greater, everything else had a next greater 
        #which contributed to one fleet/one of the fleets left in the stack 
        #so len(stack) at the end rep numnber of fleets

        #Each element in the stack at the end rep a fleet that hasn't merged with
        #another car 

        #Like this case: 1.75 1.5 1.25 1 .75 .5 .25, there are NO next greaters
        #so NO fleet formations so len(stack)=6 (6 seperate fleets)

        #So all that to say, hopefully this is correct: 

        array=[]
        for i in range(len(position)): 
            array.append((position[i], (target-position[i])/float(speed[i]))) #Pos, time 
        array.sort(key=lambda x: x[0]) #Sort by position 

        stack=[]
        for i in range(len(array)):
            while stack and array[i][1]>=array[stack[-1]][1]:
                index=stack.pop() #stack will be index only    
            stack.append(i)
        return len(stack)

        #Bro I thought I Was bugging or seeing shit dawg. Same code was giving 
        #different outputs in leetcode vs VS code bro. 
        #In regular python (which is my leetcode), / performs integer division 
        #which means it truncates decimals and returns integer. In python3, / is 
        #always float division which is prob what my VS code is in. Here, I need
        #to explicitly use /float() to specify float division. 
        #OKAY BUT ANYWAYS-THIS PROBLEM IS SICKKKK, I discovered that mono stack 
        #pattern out of thin air bro holy fuck this feels amazing. This problem 
        #is actually sick. ITs all about time to the end and if a time has a 
        #next greater time, thats a fleet creation 
