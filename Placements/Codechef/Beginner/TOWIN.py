for j in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        l.sort(reverse=True)      # Sort the array in reverse order
        ans1=0
        ans2=0
        for i in range(n):
            if(i==0):             
                ans1+=l[i]
            elif (i==1) or (i==2):
                ans2+=l[i]
            elif(i%2==1):
                ans1+=l[i]
            else:
                ans2+=l[i]
        if ans1>ans2:print("first")
        elif ans2>ans1:print("second")
        else:print("draw")
        
"""
Explanation

1. Make sum of the numbers alternately and check which one is highest at the end.

2. If first one is higher then print "first". 

3. If second one is higher then print "second".
"""