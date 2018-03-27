ans={}

input=input("Please type antyhing:\n")

for a in input:
    if a not in ans:
        ans[a]=1
    else:
        ans[a]=ans[a]+1

for a in ans:
    print("'{}':{}".format(a,ans[a]))