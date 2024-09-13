class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        #Seems like you can just keep a rolling time counter as you iterate through
        #the list, its already sorted for you so I think thats it 
        
        time,summ=0,0
        for customer in customers: 
            if time<customer[0]: 
                summ+=customer[1]
                time=customer[0]+customer[1]
            else: 
                time+=customer[1]
                summ=summ+time-customer[0]
        return summ/float(len(customers))

        #Yeah so you just need a rolling time and each customer you add the new
        #time minus the customers arrival time because they were never waiting 
        #before their arrival time. You just need to think: for a customers waiting
        #time, only two things matter: time their food is done and time they got 
        #there, the diff is the waiting time 
        
        #But theres also the case where the rolling time resets and thats when 
        #there is no more overlap with the next customers arrival time, in that 
        #case, that customers waiting time is just the [1] value and rolling time
        #resets to that customers [0]+[1]. At the end, average is just summ /
        #len of array 

