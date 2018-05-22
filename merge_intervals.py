class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        if len(intervals)<2:
            return intervals
        map={}
        a=[]
        for i in intervals:
            if i.start not in map:
                map[i.start]=[i]
                a.append(i.start)
            else:
                map[i.start].append(i)
        a.sort()
        for i in a:
            max=0
            for j in map[i]:
                if j.end>max:
                    max=j.end
            map[i]=[i,max]
        print(map)
        print(a)
        main=[]
        i=0
        for i in range(1,len(a)):
            a1=map[a[i-1]]
            a2=map[a[i]]
            if a2[0]<=a1[1]:
                if a1[1]>a2[1]:
                    map[a[i]]=[a1[0],a1[1]]
                else:
                    map[a[i]]=[a1[0],a2[1]]
            else:
                main.append(a1)
        if i==len(a)-1:
            main.append(map[a[i]])
        return main

intervals=[]
a=Interval(2,3)
intervals.append(a)
a=Interval(5,5)
intervals.append(a)
a=Interval(2,2)
intervals.append(a)
a=Interval(3,4)
intervals.append(a)
a=Interval(3,4)
intervals.append(a)
b=Solution()
print(b.merge(intervals))



