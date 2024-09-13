class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        #Just need to keep track of stuff using ht nicely 

        #Need to keep track of highest view count video of each creator and total 
        #view count, also case where same view count video, track the id as the smallest
        #that can be bypassed by only doing a > check 

        ht={}

        maxx=0 

        for i, name in enumerate(creators): 
            if name not in ht: 
                ht[name]=(views[i], views[i], ids[i])
                maxx=max(maxx, views[i])
            else: 
                cur_summ, cur_views, cur_ids=ht[name][0], ht[name][1], ht[name][2]
                cur_summ+=views[i]
                if views[i]>cur_views: 
                    cur_views, cur_ids=views[i], ids[i]
                elif views[i]==cur_views: 
                    if ids[i]<cur_ids: 
                        cur_ids=ids[i]
                ht[name]=(cur_summ, cur_views, cur_ids)
                maxx=max(maxx, cur_summ)
        
        result=[]
        for name, key in ht.items(): 
            if key[0]==maxx: 
                result.append([name, key[2]])
        return result 



        #Just one ht which stores name:(sum, highest views, smallest id with that views)
        #along with keeping track of the max sum so that you can retrive those with that
        #sum at the end with another pass 