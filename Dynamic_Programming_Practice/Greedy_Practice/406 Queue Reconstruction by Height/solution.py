class Solution(object):


    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return []
        people_obj, height, res ={}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in people_obj:
                people_obj[p[0]]+=(p[1],i),
            else:
                people_obj[p[0]] = [(p[1], i)]
                height += p[0],
        height.sort()

        for i in height[::-1]:
            people_obj[i].sort()
            for p in people_obj[i]:
                res.insert(p[0], people[p[1]])

        return res